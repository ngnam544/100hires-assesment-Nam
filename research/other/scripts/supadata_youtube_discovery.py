import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


API_BASE_URL = "https://api.supadata.ai/v1/youtube/search"
DEFAULT_OUTPUT_PATH = Path("research") / "_candidate_videos.md"


def parse_args():
    parser = argparse.ArgumentParser(
        description="Discover candidate YouTube videos for experts via Supadata search."
    )
    parser.add_argument(
        "experts",
        nargs="*",
        help='Expert names, e.g. "David Spinks" "Erica Kuhl".',
    )
    parser.add_argument(
        "--experts-file",
        help="Optional text or JSON file containing expert names.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Search results per expert. Supadata allows 1-5000. Default: 10.",
    )
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT_PATH),
        help=f"Markdown output path. Default: {DEFAULT_OUTPUT_PATH}",
    )
    return parser.parse_args()


def load_experts_from_file(path):
    file_path = Path(path)
    raw = file_path.read_text(encoding="utf-8").strip()
    if not raw:
        return []

    if file_path.suffix.lower() == ".json":
        data = json.loads(raw)
        if not isinstance(data, list):
            raise ValueError("--experts-file JSON must be an array of names.")
        return [str(name).strip() for name in data if str(name).strip()]

    return [line.strip() for line in raw.splitlines() if line.strip()]


def collect_experts(args):
    experts = []
    if args.experts_file:
        experts.extend(load_experts_from_file(args.experts_file))
    experts.extend(args.experts)

    deduped = []
    seen = set()
    for expert in experts:
        normalized = expert.strip()
        if normalized and normalized.lower() not in seen:
            seen.add(normalized.lower())
            deduped.append(normalized)
    return deduped


def search_youtube(api_key, expert_name, limit):
    params = {
        "query": f"{expert_name} community",
        "type": "video",
        "limit": str(limit),
    }
    url = f"{API_BASE_URL}?{urlencode(params)}"
    request = Request(
        url,
        headers={
            "x-api-key": api_key,
            "Accept": "application/json",
            "User-Agent": "100hires-supadata-discovery/1.0",
        },
    )

    try:
        with urlopen(request, timeout=45) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Supadata HTTP {e.code}: {body}") from e
    except URLError as e:
        raise RuntimeError(f"Supadata request failed: {e.reason}") from e


def video_url(result):
    if result.get("url"):
        return result["url"]
    video_id = result.get("id")
    if video_id:
        return f"https://www.youtube.com/watch?v={video_id}"
    return ""


def channel_name(result):
    channel = result.get("channel") or {}
    if isinstance(channel, dict):
        return channel.get("name") or ""
    return str(channel)


def publish_date(result):
    return result.get("uploadDate") or result.get("publishDate") or result.get("publishedAt") or ""


def markdown_escape(value):
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def render_markdown(search_results):
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    lines = [
        "# Candidate YouTube Videos",
        "",
        f"Generated: {generated_at}",
        "",
        "Discovery only. Transcripts not pulled.",
        "",
    ]

    for expert_name, payload in search_results:
        lines.extend([f"## {expert_name}", ""])

        results = payload.get("results", [])
        videos = [item for item in results if item.get("type") in (None, "video")]
        if not videos:
            lines.extend(["No video results found.", ""])
            continue

        lines.extend([
            "| Title | Channel | URL | Publish Date |",
            "| --- | --- | --- | --- |",
        ])
        for item in videos:
            lines.append(
                "| {title} | {channel} | {url} | {date} |".format(
                    title=markdown_escape(item.get("title", "")),
                    channel=markdown_escape(channel_name(item)),
                    url=markdown_escape(video_url(item)),
                    date=markdown_escape(publish_date(item)),
                )
            )
        lines.append("")

    return "\n".join(lines)


def main():
    args = parse_args()
    api_key = os.environ.get("SUPADATA_API_KEY")
    if not api_key:
        print("Missing SUPADATA_API_KEY environment variable.", file=sys.stderr)
        return 1
    if args.limit < 1:
        print("--limit must be >= 1.", file=sys.stderr)
        return 1

    experts = collect_experts(args)
    if not experts:
        print("Provide expert names as arguments or via --experts-file.", file=sys.stderr)
        return 1

    search_results = []
    for expert_name in experts:
        print(f'Searching "{expert_name} community"...')
        payload = search_youtube(api_key, expert_name, args.limit)
        search_results.append((expert_name, payload))

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_markdown(search_results), encoding="utf-8")
    print(f"Wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
