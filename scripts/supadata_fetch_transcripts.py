import argparse
import csv
import json
import os
import re
import sys
import time
from io import StringIO
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


TRANSCRIPT_URL = "https://api.supadata.ai/v1/youtube/transcript"
TRANSCRIPT_JOB_URL = "https://api.supadata.ai/v1/transcript/{job_id}"
DEFAULT_INPUT_PATH = Path("research") / "_candidate_videos.md"
DEFAULT_OUTPUT_DIR = Path("research") / "youtube-transcripts"
USER_AGENT = "100hires-supadata-transcript-fetcher/1.0"


def parse_args():
    parser = argparse.ArgumentParser(
        description="Fetch Supadata transcripts for candidate YouTube videos."
    )
    parser.add_argument(
        "--input",
        default=str(DEFAULT_INPUT_PATH),
        help=f"Candidate markdown file. Default: {DEFAULT_INPUT_PATH}",
    )
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT_DIR),
        help=f"Flat transcript output directory. Default: {DEFAULT_OUTPUT_DIR}",
    )
    parser.add_argument(
        "--lang",
        default="en",
        help="Preferred transcript language. Default: en.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite transcript files that already exist.",
    )
    parser.add_argument(
        "--max-videos",
        type=int,
        help="Optional cap for testing a small batch.",
    )
    return parser.parse_args()


def markdown_unescape(value):
    return value.replace("\\|", "|").strip()


def parse_candidates(path):
    candidates = []
    current_expert = None
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            current_expert = line[3:].strip()
            continue
        if not current_expert or not line.startswith("| ") or line.startswith("| ---"):
            continue
        if " Title " in line and " Channel " in line:
            continue

        reader = csv.reader(StringIO(line.strip().strip("|")), delimiter="|", escapechar="\\")
        columns = next(reader, [])
        if len(columns) < 4:
            continue

        title, channel, url, publish_date = [markdown_unescape(col) for col in columns[:4]]
        if url.startswith("http"):
            candidates.append({
                "expert": current_expert,
                "title": title,
                "channel": channel,
                "url": url,
                "publish_date": publish_date,
            })
    return candidates


def safe_filename(value, max_length=120):
    value = re.sub(r"[<>:\"/\\|?*\x00-\x1f]", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    value = value.rstrip(". ")
    return value[:max_length].rstrip(". ") or "untitled"


def output_path_for(output_dir, item):
    expert = safe_filename(item["expert"], 60)
    title = safe_filename(item["title"], 120)
    return Path(output_dir) / f"{expert}_{title}.md"


def output_paths_for(output_dir, candidates):
    counts = {}
    paths = []
    for item in candidates:
        base_path = output_path_for(output_dir, item)
        base_key = str(base_path).lower()
        counts[base_key] = counts.get(base_key, 0) + 1
        if counts[base_key] == 1:
            paths.append(base_path)
            continue

        suffix = counts[base_key]
        paths.append(base_path.with_name(f"{base_path.stem} ({suffix}){base_path.suffix}"))
    return paths


def request_json(url, api_key):
    request = Request(
        url,
        headers={
            "x-api-key": api_key,
            "Accept": "application/json",
            "User-Agent": USER_AGENT,
        },
    )
    try:
        with urlopen(request, timeout=90) as response:
            return response.status, json.loads(response.read().decode("utf-8"))
    except HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {e.code}: {body}") from e
    except URLError as e:
        raise RuntimeError(f"request failed: {e.reason}") from e


def transcript_request(api_key, video_url, lang):
    params = {
        "url": video_url,
        "text": "true",
    }
    if lang:
        params["lang"] = lang
    status, payload = request_json(f"{TRANSCRIPT_URL}?{urlencode(params)}", api_key)

    job_id = payload.get("jobId") or payload.get("job_id") or payload.get("id")
    if job_id and status in (202, 206):
        return poll_transcript_job(api_key, job_id)
    return payload


def poll_transcript_job(api_key, job_id, attempts=30, delay=5):
    for _ in range(attempts):
        _, payload = request_json(TRANSCRIPT_JOB_URL.format(job_id=job_id), api_key)
        status = payload.get("status")
        if status == "completed":
            return payload
        if status == "failed":
            raise RuntimeError(f"transcript job failed: {payload.get('error')}")
        time.sleep(delay)
    raise RuntimeError(f"transcript job timed out: {job_id}")


def transcript_text(payload):
    content = payload.get("content", "")
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        chunks = []
        for item in content:
            if isinstance(item, dict):
                text = item.get("text", "")
            else:
                text = str(item)
            if text:
                chunks.append(text.strip())
        return "\n\n".join(chunks).strip()
    return str(content).strip()


def appearance_note(expert, channel):
    normalized_expert = re.sub(r"[^a-z0-9]+", "", expert.lower())
    normalized_channel = re.sub(r"[^a-z0-9]+", "", channel.lower())
    if normalized_channel and normalized_channel in normalized_expert or normalized_expert and normalized_expert in normalized_channel:
        return "own channel"
    return "guest appearance"


def render_transcript(item, payload):
    text = transcript_text(payload)
    metadata = [
        "---",
        f"expert_name: {item['expert']}",
        f"video_title: {item['title']}",
        f"publish_date: {item['publish_date']}",
        f"source_channel: {item['channel']}",
        f"appearance: {appearance_note(item['expert'], item['channel'])}",
        f"source_url: {item['url']}",
        f"transcript_language: {payload.get('lang', '')}",
        "---",
        "",
        f"# {item['title']}",
        "",
    ]
    return "\n".join(metadata) + text + "\n"


def main():
    args = parse_args()
    api_key = os.environ.get("SUPADATA_API_KEY")
    if not api_key:
        print("Missing SUPADATA_API_KEY environment variable.", file=sys.stderr)
        return 1

    candidates = parse_candidates(args.input)
    if args.max_videos:
        candidates = candidates[:args.max_videos]
    if not candidates:
        print("No candidate URLs found.", file=sys.stderr)
        return 1

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    successes = []
    failures = []
    skipped = []
    target_paths = output_paths_for(output_dir, candidates)
    for index, (item, path) in enumerate(zip(candidates, target_paths), 1):
        if path.exists() and not args.overwrite:
            skipped.append((item, path))
            print(f"[{index}/{len(candidates)}] SKIP exists: {path.name}")
            continue

        print(f"[{index}/{len(candidates)}] Fetching: {item['expert']} - {item['title']}")
        try:
            payload = transcript_request(api_key, item["url"], args.lang)
            text = transcript_text(payload)
            if not text:
                raise RuntimeError("empty transcript")
            path.write_text(render_transcript(item, payload), encoding="utf-8")
            successes.append((item, path))
        except Exception as e:
            failures.append((item, str(e)))
            print(f"  FAILED: {e}")

    print("\nTranscript summary")
    print("=" * 60)
    print(f"Candidates: {len(candidates)}")
    print(f"Successes: {len(successes)}")
    print(f"Skipped existing: {len(skipped)}")
    print(f"Failures: {len(failures)}")
    if failures:
        print("\nFailures:")
        for item, error in failures:
            print(f"- {item['expert']} | {item['title']} | {error}")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
