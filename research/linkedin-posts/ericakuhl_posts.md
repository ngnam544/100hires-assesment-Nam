# Recent Posts for ericakuhl

Product Management Leader | AI, Data & SaaS Platform Products | Driving Digital Growth | PhD

AI-Driven Software Engineer @ Gainsight | UI Specialist | Passionate about Front-End Development & UI Architecture with Product Integrations  | React, Next.js & TypeScript

Backend Developer at CyePro | Java, Spring Boot, MySQL, Python | Generative AI, ML, DL Enthusiast | Turning Ideas into Building Systems | From Scratch to Advanced, Scalable, High-Performance Applications

Senior Software Engineer @Gainsight | Javascript, React

Lead Software Engineer @ Gainsight

Backend Software Engineer (Java | Spring Boot | Microservices | Redis | AWS) | 4 yrs building scalable, high-performance systems at Gainsight

Software Engineer @ Gainsight | CS'23 (Hons) Graduate @ IIIT Kottayam

Senior Product Manager at Gainsight || Author on CommunityFREQ

Software Engineer - Backend | Python • PHP • AWS • Docker | Microservices | REST APIs | Linux+ Certified | AWS Certified

Nutalapati Shiva rama krishna

Working as TechOps NOC Engineer at Gainsight.

Never miss a reaction or comment

LinkedIn is better on the new Windows app

Huy Hoàng (Harry) Phạm posted: Chuyện các thanh niên cái méo gì cũng biết nhưng méo biết gì (như mình) Dạo này lên mạng, nhất là vào cái năm 2026 này, anh em rất dễ gặp một kiểu người. Mấy thanh niên này nạp thông tin khổng lồ mỗi ngày: triết học, tâm lý học, kinh doanh, phát triển bản thân. Cái méo gì cũng biết một tí, chém gió phần phật, nhưng trải nghiệm thực tế thì bằng không. Họ xây dựng bản thân dựa trên việc hiểu lý thuyết chứ không phải sống thực tế. Thay vì tập giao tiếp, họ xem video dạy tự tin. Thay vì rèn kỷ luật, họ đọc sách kỷ luật. Cày video truyền cảm hứng thay vì xắn tay lên làm. Họ thấy mình thông minh vì não liên tục được kích thích. Nhưng anh em ạ, nạp kiến thức không tạo ra sự thay đổi. Thực ra, mớ kiến thức đó chỉ là áo giáp bảo vệ cảm xúc. Thực tế ngoài kia phũ phàng lắm. Ra đời làm thật thì dễ sấp mặt, dễ quê, dễ lộ cái dốt. Còn ngồi đọc sách thì an toàn tuyệt đối. Cứ nấp sau lý thuyết, mấy thanh niên (và cả mình đôi khi) cứ tự huyễn hoặc rằng mình sâu sắc, khác bọt so với đám đông. Thế là họ kẹt mãi ở bước chuẩn bị. Lúc nào cũng tưởng mình sắp thành công đến nơi, trong khi đời thực méo có gì thay đổi. Họ dùng từ ngữ đao to búa lớn để phân tích sự đời, nhưng lại méo biết đối phó với sự từ chối, bấp bênh hay rủi ro. Cuộc sống của họ biến thành sự quan sát thay vì trực tiếp tham gia. Internet lại rất hay tung hô kiểu người này. Nói đạo lý thì dễ kiếm like hơn là làm thật. Lâu dần, họ nhầm lẫn việc tự phân tích với sự trưởng thành, nhầm thông tin với trí tuệ. Nhưng lột bỏ vỏ bọc thông minh ấy đi, bên dưới chỉ có một thứ: nỗi sợ. Sợ thất bại. Sợ nhục. Sợ bị đời tát cho tỉnh. Vì hành động thực tế sẽ đập nát ảo tưởng. Ngay giây phút bạn bắt tay vào làm, bạn không thể nấp sau cái mác tiềm năng được nữa.

Change notification preferences

Thanks. Your feedback helps us improve your notifications.

Follow BIDV (Bank for Investment and Development of Vietnam) to see open roles and company insights.

Huy Hoàng (Harry) Phạm posted: Ở bài viết trước, mình đã giới thiệu sự ra đời của Nhận Diện Idol. Giờ mình sẽ tập trung vào technical, kiến trúc tổng thể và công nghệ sử dụng nhé. Quá trình làm app mất đúng 4 ngày từ khâu lên ý tưởng đến lúc test xong. Bước 1: Thu thập dữ liệu. Đây là bước chua chát nhất vì chả có API nào tổng hợp thông tin idol cả. Mỗi idol cần 20 đến 30 ảnh. API free khá hẻo nên mình tự viết crawler lọc top 2000 idol hot nhất. Bước 2: Train và test. Đẩy data lên Microsoft API để train. Do kẹt limit, mình vứt tool lên VPS cho chạy xuyên đêm 8 tiếng. Mình lấy 90 phần trăm để train, 10 phần trăm để test. Độ chính xác tầm 60 đến 75 phần trăm, khá ổn để mò kim đáy biển. Bước 3: Xây dựng API. Dựng một cái RestfulAPI đơn giản, nhận URL ảnh vào và lòi tên diễn viên ra. Bước 4: Thiết kế UI. Hí hoáy nửa ngày với React và Tailwind CSS là xong giao diện. Gắn thêm Firebase với Google Analytics vào là đẹp. Về kiến trúc, do bản tính lười biếng và sự nghèo khó, mình xài một đống tech stack nghe rất kêu nhưng chủ yếu là để xài chùa: 1. Crawler: Dùng .NET 10 viết crawler chạy trên Mac, sẵn tiện chứng minh .NET năm 2026 chạy bao ngon trên mọi nền tảng. 2. Recognize API: Xài hàng thần thánh Microsoft Cognitive Services để train AI nhận diện. 3. Idol Database: Thông tin idol lưu thành file JSON quăng lên Amazon S3. Đơn giản vì lười viết code insert database, cứ dump ra file cho lẹ. 4. Cache Server: Gọi MS API nhiều sẽ rất viêm màng túi. Mình kẹp thêm Redis Cache trên Amazon EC2 kiểm tra trước cho rẻ, chứ hàng Azure hơi chát. 5. API chính: Nơi xử lý gọi MS API và tra database. Lười quản lý server nên mình xài Azure Functions dạng Serverless. Viết code xong Azure tự lo scale, lại còn cho free mấy triệu request mỗi tháng. 6. Website: Toàn bộ logic nằm ở API nên web chỉ là HTML tĩnh host trên Github Pages. Chấp luôn giang hồ DDoS. 7. Upload: Lười làm API upload nên mình nhét luôn Cloudinary vào xài tạm. Kiến trúc này hơi over-engineering, phần vì thiếu tiền, phần vì thích test công nghệ. Phần sau mình sẽ hướng dẫn chi tiết và vứt bớt vài râu ria cho anh em dễ thở hơn nhé. Có thắc mắc gì anh em cứ bình luận bên dưới.

As cover letters fade away, this CV section matters more than ever.

Learn more about FPT Software and discover other Pages you might be interested in following.

Patrick Phat Nguyen posted: Làm Product, viết spec sao cho đủ technical? Dạo gần đây, mình nhận được khá nhiều câu hỏi: “Không technical thì viết spec như thế nào để Dev hiểu?”, hoặc “Spec đã viết kỹ lắm rồi mà Design vẫn thiếu screen, QA vẫn thiếu case, còn Tech thì bảo chưa đủ technical?” Theo mình, vấn đề không hẳn nằm ở việc PM không biết code. Phần lớn vấn đề do PM chỉ mới mô tả ở tầng UI (màn hình có gì, user bấm vào đâu) nhưng chưa mô tả được hệ thống ở tầng Concept (thực thể gì, thuộc tính nào, và vận hành ra sao) Vấn đề này có 3 triệu chứng sau: (1) Bắt đầu bằng màn hình thay vì đối tượng nghiệp vụ: có flow và UI, nhưng chưa rõ dữ liệu, trạng thái và logic phía sau. (2) Mô tả ở tầng trừu tượng quá thấp (Quá technical) khiến team không hiểu feature sẽ generalize như thế nào, hoặc ở tầng trừu tượng quá cao (Quá high-level), không biết feature sẽ hành xử cụ thể ra sao. (3) Không thể mô tả và tư duy edge case của tính năng mà chỉ mô tả được happy case. Với nhu cầu nâng cấp suất ăn cho độc giả The Poly Manager, mình hi vọng phần nào sẽ giải đáp được vấn đề trong bài hôm nay thông qua việc ứng dụng tư duy Concept. Bài viết ở đây: https://lnkd.in/dERUjgVG

Nghia Dao Chi viewed your profile. See all views.

You're a top applicant for Marketing Executive (Work From Home) at Hire Feed and 80+ other jobs.

Old-school career advice still works. This HR leader explains why.

🥇 Ton coworkers are earning wins in Zip.

Căn bản thiết kế Concept trong xây dựng sản phẩm phần mềm

Product @ Zalo | Ex-Founder

Làm Product, viết spec sao cho đủ technical?

Dạo gần đây, mình nhận được khá nhiều câu hỏi: “Không technical thì viết spec như thế nào để Dev hiểu?”, hoặc “Spec đã viết kỹ lắm rồi mà Design vẫn thiếu screen, QA vẫn thiếu case, còn Tech thì bảo chưa đủ technical?”

Theo mình, vấn đề không hẳn nằm ở việc PM không biết code. Phần lớn vấn đề do PM chỉ mới mô tả ở tầng UI (màn hình có gì, user bấm vào đâu) nhưng chưa mô tả được hệ thống ở tầng Concept (thực thể gì, thuộc tính nào, và vận hành ra sao)

Vấn đề này có 3 triệu chứng sau:
(1) Bắt đầu bằng màn hình thay vì đối tượng nghiệp vụ: có flow và UI, nhưng chưa rõ dữ liệu, trạng thái và logic phía sau.
(2) Mô tả ở tầng trừu tượng quá thấp (Quá technical) khiến team không hiểu feature sẽ generalize như thế nào, hoặc ở tầng trừu tượng quá cao (Quá high-level), không biết feature sẽ hành xử cụ thể ra sao.
(3) Không thể mô tả và tư duy edge case của tính năng mà chỉ mô tả được happy case.

Với nhu cầu nâng cấp suất ăn cho độc giả The Poly Manager, mình hi vọng phần nào sẽ giải đáp được vấn đề trong bài hôm nay thông qua việc ứng dụng tư duy Concept.

Bài viết ở đây: https://lnkd.in/dERUjgVG

Full Stack Engineer. Founder of hoccodeai.com

Nếu bạn biết code, biết viết, biết tiếng Anh… mà làm app dởm, viết content còn dở hơn mấy ông dùng ChatGPT làm, nghĩa là trình độ bạn chả giỏi lắm đâu 🙄

Brand partnership • Brand & Web Designer / Content Creator

Promoted • Partnership with LinkedIn

I think I just found the biggest marketing cheat code: LinkedIn Ads. #LinkedInPartner

Smart ad spend is all about measuring your return on ad spend (ROAS), which boilsdown to reaching the right audience with your message. LinkedIn’s unique targeting tools (filtering by job title, industry, company, and more) helps you reach the exact people who need your product/service.

In fact, LinkedIn Ads generates the highest B2B ROAS of all online ad networks (Source: Dreamdata Benchmarks Report, 2025).

Visit linkedin.com/createads to start advertising with LinkedIn.

EVP & GM at Gainsight | Sharing real lessons across Community, Customer Education, CS & PX

I once ran a brainstorming session I thought was inclusive… until I realized I was only creating space for people who think like me.

I’ve always LOVED a good brainstorm.

Whiteboard. Post-its. Fast ideas flying. Building on each other in real time. That’s my happy place.

Early in my leadership career, I assumed everyone worked that way…

They don’t.

In one session, the energy was high and ideas were flowing. But one teammate sat quietly the whole time – wide-eyed, saying nothing. I called on her, thinking I was helping create space.

It had the opposite effect.

She shook her head no and looked completely deflated.

Later, I asked her manager about it. Her response caught me off guard:
“Not everyone is like you.”

Some people need time. They want to sit with an idea, turn it over, come back with something more thoughtful. Not everyone reacts in the moment.

That was a wake-up call for me because I realized the way I was running brainstorms wasn’t actually designed to get the best ideas. It was designed to get the fastest (and the loudest) ones. 

So I changed how I approached it.

Now I share prompts ahead of time. I still bring people together live, but I build in those quiet moments to think. I make space for different styles to show up.

The ideas got better. And more importantly, more voices showed up in the work.

Turns out, this is harder to get right than you’d think. Especially if you naturally thrive in the chaos of a live brainstorm.

But leadership isn’t about designing environments that work for you.

It’s designing environments where your team can do their best thinking.

I remember sitting on the floor at Dreamforce…surrounded by a pile of stickers…watching a group of grown adults get *very* competitive about who got which one.

And it hit me – this is what people mean when they say a community “feels different.”

For a long time, I didn’t think of “fun” as part of my work. Fun was skiing, hiking, playing cards with my kids. Work was…work.

Then somewhere along the way while building the Trailblazer Community, we started doing things that didn’t look like traditional enterprise tech at all.

– We mailed a community member in Boston a 6 pack of Pliny the Elder because he was answering everything in the forums. 🍻

– We made a custom Salesforce onesie for a top contributor about to become a dad. 👶

– We crowdsourced Salesforce pickup lines for Valentine’s Day (yes, really) and turned them into shareable cards. 💌

– And at events? People sat on the floor trading stickers like it was recess again. 

None of this was in a strategy doc. We were flying the plane while building it. 

But looking back…it wasn’t random.

The community took on a personality. And that personality gave people permission to show up a little more human.

That’s the part I think we underestimate.

Fun isn’t just about being playful for the sake of it. It lowers the stakes. It makes it easier to ask a “dumb” question. It builds trust faster than another perfectly worded FAQ ever will.

But here’s the thing: 
It’s really hard to do this well.

Because “fun” looks different everywhere. It’s not always stickers and characters (although… Chatty and SaaSy did make a strong case). Sometimes it’s just a witty reply, a well-timed emoji, or noticing what someone cares about and surprising them with it.

Here’s what I’ve tried (steal it if it helps):

✅ Pay attention to what your early members love. Then amplify it.

✅ Reward behavior you want more of… even if it’s unconventional.

✅ Don’t take yourself too seriously. Your community won’t either.

We’re living in a pretty heavy moment right now. Work can feel serious. Sometimes too serious. So maybe the question isn’t “should community be fun?”

Maybe it’s… where could you add just a little more of it? 🎈

Last year felt pretty hard to top.

It was my first Pulse at Gainsight - I was on stage for the keynote, I had started a new chapter in my career, and now it's one year later and I'm thinking to myself...how am I supposed to follow that up?

So naturally…the only answer was to build something new.
One thing I knew when I joined Gainsight was that I didn’t want community and education sitting on the sidelines of the bigger customer conversation anymore. I’ve spent too many years in this work to believe these are just add-ons

Turns out - it’s not.

It’s where so much of the real customer experience happens now. And once community and education gets in your blood, it never really leaves you. 

So this year we built the Digital Center Stage at Pulse. DCS. (Yes, the acronym was intentional.) This is a real investment in the people doing the real work in digital customer success, community, and education. 

The ones building programs while also trying to prove ROI. The ones managing platforms, scaling engagement, building courses, moderating conversations, and somehow still showing up every day with energy, empathy, and optimism.

We’ve designed the content of Digital Center Stage with all that in mind.

- A strategy session led by the one-and-only Brian Oblinger (throwback pic below. The nostalgia is real)

- Customer Hub product demos led by Jon Wishart and Joris Dieben

- Birds of a feather roundtables led by people who understand and live this work every day - Samantha Murray, Michelle Kostya, and more.

And lunch right after so the conversations, ideas, and “wait, we’re dealing with that too” moments can keep going a little longer.

The room is almost full which means I think we’re onto something!

If you’re coming to Pulse and spend your days anywhere in community, education, or digital customer success, head to the Pulse app and grab your spot for Digital Center Stage on Day 1. (we just added a dozen more seats - grab them while they’re open!).

This is the beginning of something I’ve wanted to see at our events for a long time. It feels really good to finally create a space for community and education builders to find each other.

P.S. If you can’t make it in person, we’ve got you. We’ll share the sessions and highlights after Pulse so you can still follow along from home.

People have commented on my height for as long as I can remember: “I didn’t realize how small you were.”  

“You have tall person energy.”

Height has been a thing my whole life.

I danced for years. Tap was my jam. I wanted to be a Rockette SO badly – until my dance teacher gently told me I’d need to be at least 5’8”. Dream…over.

And then there’s work.

Short can read as “young.”
And young can read as “inexperienced.”

It’s exhausting at times, but it also sharpens you. You become hyper-aware of how you show up – and how you command a room. 

Competence has nothing to do with height. 
But perception? Perception is real.

Early in my Salesforce days, I delivered training over GoToMeeting (audio only). When customers finally met me in person, they almost always said, “Oh wow, I thought you’d be taller.” (And blond. Not sure what that was about…)

Maybe because I’m small, I built a bigger presence. A stronger voice. A little extra steel in my spine walking into rooms where I was literally looking up at everyone.

But I’ve been thinking…why do we equate confidence with height in the first place?

Why does “presence” get described as “tall”?

Competence doesn’t live in inches.

It’s exhausting enough to work so hard just to prove yourself. Add in that quiet pressure to overcompensate for how you physically show up? And it’s a lot.

Oddly enough, Zoom has been the great equalizer: Little squares. Same size boxes. For the first time in my career, no one’s towering over anyone.

Height is completely outside my control. I can’t help being short.

But I can help how I think about it – and how I show up.

Gainsight Launches Developer Studio and New Skilljar Integration

I've spent a long time watching Community get treated like it's not a "real" part of the business.

I mean that literally. For years, I walked into rooms with VPs and C-level leaders and heard some version of the same thing: "I just don't really get the value of this community thing." Over and over. 

That's the hill this whole industry has been climbing.

So when I see companies like Zoom, Zendesk, ShipStation, Greenhouse Software, Kaseya, PTC, and Cognite actively choosing community as a core part of how they retain customers – and doing it with real creativity and real strategy – it gets me a little emotional 🥹. 

Seeing leaders like Alexis Brown at Zoom, Melanie Vastine at ShipStation, and Anita Hæhre at Cognite create real community programs built with intention, empathy, and a deep understanding of what customers actually need - it’s exactly what I hoped this work could become.

I've had a front-row seat to everything we're announcing today, and a week before Pulse...we finally get to share it.

You know that feeling when you can see exactly what your community needs...and then you wait six months for dev to get to it?

Our new Developer Studio gives community managers the power to vibe code custom widgets, personalized experiences, and deploy them across their community without a single engineering handoff.

And our new Skilljar integration? I’ve wanted something like this for YEARS.

Learning and community have always belonged together. They just haven’t had the infrastructure to act like it…until now. FINALLY a seamless experience you can surface courses, certifications, and onboarding paths directly inside the community — so customers find the right training in the exact moment they need it.

No bouncing between disconnected systems trying to figure out where to go next. Just a clearer, easier path to learn, engage, and get help.

None of this happens without an extraordinary team. So much heart and hard work went into what we're announcing today. I'm just so proud of this team and everything they've poured into it.

Dig into the full announcement here:
https://lnkd.in/gHyTfFxU

I’m convinced there are two types of people in this world:

The people who walk straight down the sidewalk expecting everyone else to move around them…

…and the people who instinctively step aside to let others pass.

I am absolutely the second type.

Every once in a while, I try to be the first. I hype myself up, walk confidently down the sidewalk thinking, “Okay. This time I’m not moving.”

Then I spot someone coming directly toward me and at the very last second…I move. Every single time.

And weirdly, I end up disappointed in myself. Not because moving aside is bad, it’s probably kinder. But because somewhere along the way I connected “taking up space” with confidence.

I’ve noticed the same thing with the word “sorry.”

The elevator door opens and someone walks in before I can get out.
“Sorry.”

A waitress accidentally drops something on my shoe.
“Sorry.”

Someone interrupts me in a meeting.
“Sorry.”

Why am I apologizing for simply existing during these moments?

Better question…why aren’t THEY saying sorry?

I’ve been trying really hard to stop overusing that word. Not because I want to become rude or hardened or one of those people who barrels through life without awareness of others. I don’t. I actually like being considerate.

But I’ve also realized how often over-apologizing gets associated with weakness, uncertainty, or shrinking yourself…and I don’t want that to become part of how I move through the world.

Because when you apologize for everything, eventually your real apologies lose meaning too. It becomes background noise. A verbal reflex.

Habits like this are hard to break, though. So instead of going cold turkey, I started catching myself mid-sorry. Sometimes I just say it in my head. Sometimes I mumble “sorry not sorry” under my breath and keep walking.

One of my favorite replacements came from a friend.

When someone shares sad news, instead of saying “I’m sorry,” she says:
“I’m sympathy sorry.”

I love that so much.

It keeps the empathy without taking responsibility for something that was never yours to own in the first place.

Lately I’ve been realizing how many of us – especially women – were taught to soften ourselves in tiny ways all day long. Move aside. Don’t inconvenience anyone. Apologize first.

Maybe confidence isn’t about never moving aside. 

Maybe it’s about learning to stop apologizing for taking up space in the first place.

Community builders can now vibe-code their way to creating the community of their dreams - custom widgets, integrations, personalized moments…without waiting in a dev queue.

The ability to shape your community in real time, because you’re closest to what the customer needs and wants.

It feels like we’re about to see a wave of communities that are a whole lot more creative and a lot more human. 

The big question now is...what are you going to build first?

I've walked hundreds of miles on golf courses watching my son's tournaments.

Early mornings. Long afternoons. Hot days. Rainy days. Great rounds. Tough rounds.

And somewhere along the way, I realized that a lot of sports mimic life.

But nothing quite like golf.

Sometimes ending up in the bunker isn't the worst thing. What looks like trouble can turn out to be the best angle to the pin.

Use your own strengths and the club that's right for you, not the one that matches everyone else. The scorecard doesn't care how you got there. The goal is simply to get the ball in the hole in the fewest strokes possible.

Don't stare at the leaderboard. Know where you stand, sure. But the players who spend all day looking at everyone else's score usually stop paying attention to their own game.

Conditions change. Some days the conditions are perfect. Some days the wind is howling and nothing feels right. You still have to figure out how to play the course in front of you.

Take full accountability. When you hit a bad shot, own it. Golf doesn't care whose fault it was. Blaming doesn't move the ball any closer to the hole. Figure out the next one.

And maybe my favorite lesson of all:

There's always a lot of golf left.

A bad hole doesn't ruin a round.  You keep taking the next shot. A setback isn't the end unless you decide it is.

Then when the day is over, you replace your divots, repair your ball marks, shake hands, and leave the course a little better than you found it.

That's good golf. And I've come to believe it's a pretty good way to live too.

"Golf is the closest game to the game we call life. You get bad breaks from good shots; you get good breaks from bad shots, but you have to play the ball where it lies." – Bobby Jones

My daughter asked me this weekend: “Should I be worried about the job market right now?”

I was visiting her at college, and we packed it FULL – great food, some rousing tennis, wandering the Saturday market, morning crosswords, and long walks around town. I loved every minute of it.

But that question kept coming up.

If you spend even five minutes reading the headlines right now, it’s a lot.

Layoffs. Hiring freezes.
Entry-level roles disappearing.
AI taking over “junior” work.

It’s enough to make anyone pause – especially when you’re about to step right into it.

I’ve seen this happen before. Different moment, different technology, same feeling of uncertainty about what comes next.

But then I came across a clip from Mark Cuban (link in comments!) that shifted the conversation for both of us.

The idea was, most companies don’t actually know how to use AI yet. They don’t have the people, the time, or the expertise to really transform how they work.

And that gap? It’s an opening.

I showed it to her, not sure how she’d react…

And something clicked.

Instead of feeling like AI was closing doors, she started seeing where she could step in. She started sketching out a plan - how she’d ramp up on Claude, take Anthropic Academy course (she loved discovering it runs on Skilljar), and set a goal to get certified and build a few test apps along the way.

It wasn’t fear anymore. It was curiosity.

And maybe that’s the shift.
Not “AI is taking jobs,” but “AI is creating a new kind of entry point.”

Especially for young people who have a strong foundation and are willing to learn fast, build things, and figure it out as they go.

There’s something powerful about stepping into a moment where no one has it fully figured out yet. 

Not having a playbook isn’t always a disadvantage…

Sometimes it’s the whole point.

Erica Kuhl is featured in Enterprise Times today on the future of scaled Customer Success. 🎉

Read her insights from decades of building customer communities and learning ecosystems, and why the next era of Customer Success will be built on a connected system of community, education, product experience, and AI.

Link to the article in comments below 👇

The Merit Company | LinkedIn

It's rare to meet someone as an adult and feel an immediate connection.

Not just personally. Professionally, too.

Someone who sees you exactly as you are, accepts you, celebrates you, and somehow makes you feel like you've known each other for years.

That was Robin Merrit for me.

I actually fangirled over Robin long before we became friends. Back when I was running my own business and working with Gainsight, I watched her from afar and admired how she showed up as a leader. Smart. Grounded. Authentic. The kind of person people naturally trust.

Then I joined Gainsight, and we became fast friends.

Now she's the one striking out on her own, and I couldn't be happier for her.
Having been a founder myself, I know how hard it is to build something from nothing. I know the pressure, the uncertainty, and the moments when you're making decisions with imperfect information and hoping you're getting more right than wrong.

I also know how much it matters to have people around you who truly understand that journey.

Robin does.

She understands founders because she's lived, advised, and operated through it. And now she's built a company dedicated to helping others navigate it. One of the rare people who can see both the business challenges and the human challenges at the same time

Introducing The Merit Company! 

If you're a founder, operator, executive, or investor whose business has evolved faster than the organization around it, this is one to follow.

Robin, I'm so proud of you and so excited to watch this next chapter unfold.

https://lnkd.in/gqgNYimr

I practiced this keynote so much that my dog could probably give it.

Seriously.

For weeks I memorized every line. I said them to mirrors. To couch pillows. To my husband. To those passing by me on my daily walk. To anyone (or anything) that would listen.

I was one of three speakers opening the Pulse keynote last week alongside Chuck Ganapathi and Ori Entis, and I knew the first few lines mattered most. They set the tone of our whole talk which is how Gainsight is delivering the best of both worlds: the software you buy, and the software you build yourself. 

Those first few lines are supposed to calm the nerves. They help you find your rhythm.

So naturally…

I fumbled them.

Not dramatically. But enough that I noticed. And then something happened.

I settled in.

The script disappeared. The audience appeared. And I found that magical place every speaker hopes for – the flow state where you're no longer reciting words, you're having a conversation.

One of the best lessons I've learned about public speaking is that preparation isn't about sounding perfect. It's creating enough confidence that you can be yourself once you're on stage.

I rewrote every section of the keynote in my own words while staying true to the message. I practiced transitions obsessively. I worked on pacing. Pauses. Energy.

And yes... I spent an embarrassing amount of getting the outfit right too (Raiders of the Lost Ark theme is tough!).

Because for me, all of it matters.

The words I say. How I deliver them. The confidence I exude. The way you show up.

This community means too much to me to phone it in.

The tricky part was keeping the energy high while delivering all the amazing announcements including MCP Servers for Community, Skilljar, PX, CS, and Staircase. CLI. Six pre-built agents. Agent Studio, Developer Studio and more! 

I wanted every announcement to feel as exciting to the audience as it felt to us behind the scenes building it.

Of course, after I walked off stage, all I could think about was that tiny stumble in the opening.

My husband, having heard the talk roughly 200 times, noticed.

Everyone else? Probably not.

Funny how often we're judged far less harshly than we judge ourselves.

I might be falling in love with a new man named Claude…

Kidding. (Kind of.)

What’s surprised me most lately is how AI is sneaking into the smallest, most ordinary parts of life - not just the big, obvious stuff we all talk about.

Case in point: address labels.

We usually only make them once for holiday cards, but this year we’ve got two graduations as well as holiday cards. So instead of doing this once, we’re doing it three times. I was already bracing myself.

It’s a whole thing. Clean up the spreadsheet. Wrestle with formatting in Word. Try to remember how mail merge works (why is this still so hard?). Adjust font sizes. Print test sheets. Flip the paper. Print again… upside down. Repeat.

It’s…not my finest hour. Then I had a moment and thought, there has to be a better way.

So I asked Claude.

Two prompts later: done. Perfectly formatted labels. Centered. The right font size. It even told me exactly how to load the label paper so I didn’t mess it up (which, historically, I always do).

Start to finish: under 30 minutes. The first print worked. No do-overs. No frustration spiral. It sounds like such a small, almost silly example. I know there are people building way more complex things with AI right now.

But this got me thinking a different way.

Because it’s not just about saving time. It’s about removing that low-grade friction we’ve all just accepted. The stuff that used to feel “normal” but was actually kind of painful.

I’ve spent a lot of my career helping teams build systems for scale - community programs, education platforms, all of it. And so much of that work has been about reducing friction for customers.

This feels like that. But for life.

Not everything has to be groundbreaking to be meaningful.

Sometimes it’s just labels.

It feels like yesterday that Chuck Ganapathi whispered in my ear, “come join me and build the education and community products of your dreams.”

My immediate thought?

“Wait…do I actually have any business doing that?”

After all, I have no formal product background. I never ran engineering. And I definitely didn’t come up through the “traditional” path.

Spoiler alert – I said yes to Chuck… and here I am, one year into my Gainsight journey, with MANY imposter syndrome moments along the way. 

There’s still that voice that says:
You don’t have the right experience. You don’t belong in this room. You’re going to get found out.

But then I come back to this:

I may not have come up through traditional channels, but I do know community. And education. And what leaders in those roles actually need from the tools they rely on every day. I’ve spent years in it. Building it. Breaking it. Fixing it again.

And when that voice gets loud, I go back to one of my favorite lines from Ted Lasso: “that young fellow has forgotten more about the sport than I’ll ever know.”

It's a good reminder not to take your own experience for granted.

The other thing that’s helped? Being honest.

Honest about what I know. And very honest about what I don’t (not as a crutch, but as a starting point).

There’s something grounding about saying “I don’t know”…and then going to figure it out. It builds a different kind of trust between me and my teams.

This past year has been one of the most rewarding and challenging of my career:

– A successful Skilljar integration
– A packed (and accelerating) roadmap
– Incredible hires who are way smarter than me in the areas that matter
– And some truly exciting growth and bookings

And still…imposter syndrome doesn’t just disappear. It just gets quieter. A little easier to challenge.

Turns out, the goal isn’t to eliminate that voice. It’s to stop letting it make the decisions.

Today, on International Women’s Day, my daughter turns 21.

And I’ve never felt more sure about the choices that once made people question me. 

When she was little, I chose a high-intensity career. Big roles. Big travel. Early flights and late-night calls. I was building teams and programs from scratch. 

She didn’t love that I traveled. There were hard goodbyes. Moments I questioned myself in quiet airport terminals. There was judgment. Some subtle. Some not.

The narrative was familiar: You can have ambition. You can have young kids. But having both? That’s selfish. Risky. Too much.

But here’s what I know now.

The time we had was intentional. Intense. Fully ours. When I was home, I was home. Big talks. Real talks. The kind where you look each other in the eye and actually see each other. She grew up watching me care deeply about my work. Watching me lead. Watching me recover when things didn’t work. Watching me stand in rooms where I had to earn my voice.

Now she’s 21. Fiercely independent. Kind. Crazy smart. Emotionally connected. She knows who she is. We don’t always see eye to eye - we’re very different women - but there’s deep respect there. On both sides.

She’s told me she understands it now. That seeing me build a life I believed in shaped her more than my constant presence ever could have.

I was judged for my choices. She never judged me.

International Women’s Day can sometimes drift into slogans and highlight reels. But for me, it’s this: women supporting women. Especially when their choices look different than ours.

No scorecards. No side-eyes. Just respect.

Because there isn’t one right way to be a woman. Or a mother. Or a leader.
And I can’t think of a better way to spend today than celebrating the woman she’s becoming  and recommitting to being the kind of woman who makes space for other women to choose their own path.

Bragging doesn't come naturally to most women.

A few weeks ago, I asked a room full of women to do something simple… and kind of uncomfortable.

The rules: Introduce yourself and give me something you're proud to brag about. Not a humble brag. A full-out, no-deflecting, about-YOU brag.

You could feel the shift in the room immediately.

Smiles. Nervous laughter. That pause where everyone’s trying to figure out 
how to say something about themselves without sounding like… too much.

Even with explicit instructions, the qualifiers crept in. 
“Here’s my not humble brag…”
“I mean, my team really - ”
“It wasn’t just me, but…”

Each time, I interrupted. Course corrected. Reminded them that this is a safe space. Let it out.

It was uncomfortable for about 30 seconds.
And then… something changed and it got electric.

Schools built. Millions raised for charity. Program budgets doubled. Awards won. Communities scaled.

A room full of women who had been quietly carrying extraordinary things - finally saying them out loud. Without apologizing for it.

This shows up in the workplace too. Self-promotion often feels uncomfortable, even risky. We default to "we" when the situation calls for "me." We pull the team in out of genuine gratitude - but sometimes at the cost of our own visibility. 

And it can cost us. Promotions. Recognition. Opportunities. 

This might be an unpopular opinion, but…being good at your job isn’t always enough.

Bragging and being gratuitous aren't the same thing. You can own your wins AND be a team player. They're not mutually exclusive.

That doesn’t mean becoming someone you’re not. Or taking credit that isn’t yours.

It just means getting comfortable saying:
 “I did this.”
 “I’m proud of this.”
 “This mattered.”

That little exercise? It felt like a small crack in a norm that's been in place for a long time.

Group Product Manager at Gainsight

Developer Studio for Gainsight Communities is here 🎉

You can now build fully custom community widgets with your own code, connect them to external services, and deploy everything through Git automatically.

Connect your community to GitHub. Declare widgets, scripts, and stylesheets in your repo, push to your watched branch, and it publishes. No manual steps.

Need your widget to call an external API? Configure a Connector once. Any widget can use it securely. No credentials ever touch the browser.

Write in VS Code, Cursor, or whatever you think in. Check the video to see me vibe-coding a widget with Claude.

Your stack, your way. If you're building on Gainsight Communities, this one's for you.

aeounplugged.splashthat.com

There's a land grab happening right now that most companies haven't noticed yet.

It’s not for market share, or for talent. It's for trust – and the content that signals it.

The companies that have spent years building rich community conversations, deep educational libraries, and peer-driven knowledge bases are sitting on something incredibly valuable right now. 

That's because customers aren’t just searching anymore… they’re asking. And AI answer engines are shaping what they hear back.

LLMs don't just surface what's “newest.” They pull what's trusted, well-structured, and deeply indexed. If your brand has years of authentic community dialogue, courses built from real practitioner expertise, and content that actually answers the questions your customers are asking… that is your moat.

And if you don't have it yet… that’s the part I’d pay attention to. 

The teams that treated community and education as core – not side projects – are the ones with an advantage right now.

So here's the question I'd ask anyone reading this: 

If an answer engine like Claude, Perplexity, or ChatGPT was asked about your product category today, would your content show up? Would it be the most helpful part of that answer?

If you're not sure, that’s your entry point.

And if you're not sure where to begin – that's exactly who we built AEO Unplugged for.

For the leaders who see what's coming, feel the urgency, and need a simple starting point. We put together some of the best speakers and practitioners in this space who are in it right now, figuring it out in real time.

If you’re in it too, you’re in the right room. 

https://lnkd.in/gKCbcR22

"Ducks don't travel alone."

I was sitting in the blazing heat at Autzen Stadium this weekend watching my daughter graduate from the University of Oregon when commencement speaker Marlee Matlin  (actress, Academy Award winner, and fellow proud parent of a graduate in the Class of 2026) shared that simple reminder.

As a community builder, it immediately stuck with me.

She encouraged graduates to stay connected to the people who helped them get here, to lean on their support systems, and to help others along the way.

I've spent much of my career building communities, and one thing I've learned is that very few meaningful accomplishments happen alone. Looking back, every meaningful chapter of my career was shaped by people who opened doors, shared wisdom, challenged my thinking, and helped me see possibilities I might have missed on my own.

The second thing she said was equally memorable.

“Ducks appear calm on the surface while paddling like mad underneath.”

Doesn’t that sound familiar? That's most of us.

I've met very few people who aren't working much harder than they let on.

The calm isn't the absence of effort. It's often the result of it.

Maybe that's why those two lessons belong together.

We're all paddling beneath the surface in ways others can't see. And we're all better off when we don't have to do it alone.

As I watched my daughter and thousands of graduates step into what's next, and joined in singing Shout one last time with a stadium full of strangers, I realized that's really the lesson.

Find your people.
Be someone's people.
And keep paddling.

I was convinced the handwritten thank you card was a dying art.

And then…a few showed up in my mailbox.

Not the quick “thanks so much!” kind. The more thoughtful, specific ones – where you can feel the person actually took a minute to sit down and think about what they wanted to say.

A couple of them got me a little choked up.

Which made me laugh, because writing thank you cards was basically drilled into me as a kid. I hated it. Felt like such a generational thing. Why couldn’t I just say thank you and move on?

Now I get it.

I’m that parent. The one who makes my kids sit down and write the card after they open a gift. And yes…they grumble. They negotiate. They tell me a text would be faster (and that “everyone else does that”).

I make them do it anyway.

And every single time, the person on the other end notices.

I’ve been trying to figure out why it hits differently.

It’s not just the words. It’s the effort. The process of picking out the card, sitting down to write it, addressing it, putting a stamp on it.

It’s the time. It’s the intention. It’s…care.

I even started sending cards to my daughter at college. Half the time, when they arrive, whatever I wrote about is already outdated. It doesn’t matter. She still loves them.

There’s just something about seeing someone’s handwriting. It feels personal in a way a text never quite does.

Don’t get me wrong – I love a quick thank you text. I send them all the time.

But a handwritten note? It sticks with you a little longer.

I still remember the call I got from a Salesforce customer who felt left out…but I had no idea that one phone call would spark a global community.

The customer’s name was Peter Fife. 

He told me his company would never send him to Dreamforce. It was too far, too expensive, not a priority. And he figured there were probably a lot of other Salesforce customers just like him…people who wanted to connect, learn, and meet others – but didn’t have access to the big, flagship events.

Then he said something simple:
“Why can’t we just do something locally?”

I paused for maybe two seconds…and said yes.

That was it. No strategy doc or big rollout plan. Just a really good idea from someone actually living the problem.

At the time, we already had a thriving online community - thousands of people helping each other every day. But this was different. This was about bringing that same energy into real life: local, human, and ongoing.

That one idea became the Salesforce User Group program.

Today, there are 2,000+ customer-led groups across 95+ countries.

And what made it work wasn’t scale or structure…it was ownership.

Customers planned the events. They chose the topics. Spoke freely. Helped each other solve real problems. They also shared jobs, built careers, and made lifelong friends.

We didn’t build it for them. We built it WITH them. (And then mostly got out of the way.)

One of the best lessons I learned from that experience?

Nearly all the great community ideas don’t come from inside the company.

They come from the people already showing up…who just need someone to say yes.

I had no idea I was becoming a community builder. My title was "application instructor."

I was standing in a Salesforce classroom teaching early admins how to use a product changing faster than any of us could keep up with.

But something kept happening: people didn't just want training. They wanted to talk to each other. Share ideas. Be part of a movement.

That realization has driven everything I've built since.

The blank check era of CS is over. But customer expectations are higher than ever. The old model with fragmented content and siloed teams isn't holding up.

Here's what I know after 20+ years: AI is only as good as the data it's trained on. And the most valuable knowledge your company has lives in your community, your academy, your help center - created by people who've actually been there.

AI can't replicate that. But it absolutely depends on it.

I got into all of it - what's breaking, what's working, and where this is all heading in a piece for Enterprise Times.  Check it out 👇🏼

https://lnkd.in/g-hiWn7A

The most intense prioritization exercise of my career happened in a windowless conference room in Hawaii… arguing about whether Trust or Customer Success mattered more.

It was a Salesforce leadership offsite – Marc Benioff plus ~400 leaders – and my first real exposure to a V2MOM.

Ever since, I’ve used and refined the V2MOM framework because of what it forced us to do in that room.

At Salesforce, V2MOM wasn’t a feel-good planning doc. It was a forcing function.

It made tradeoffs explicit – and uncomfortable.

From execs all the way down to ICs, everyone could clearly articulate:
– what mattered
– why it mattered
– and just as importantly, what wasn’t getting done

That last part is where most teams fall apart.

What I’ve learned is that V2MOM doesn’t fail because the framework is flawed.
It fails when it turns into a document you fill out, save to a shared drive, and forget.

A strong V2MOM governs your year.

It gives you air cover (and language) to push back when new work shows up:
“Happy to add this… what moves off?”
“What priority does this replace?”
“What decision are we actually making?”

But it only works if it’s ALIVE.

The best V2MOMs show up in 1:1s, performance reviews, and at the start of strategic meetings. They become the grounding reference point for decisions, feedback, and tradeoffs as things inevitably change.

I’ve seen V2MOMs work at the company level, for individual teams, on single projects – even for personal goals.

The real power is shared clarity and permission to say no with context and alignment.

This year, Chuck asked me to help roll out the V2MOM process to all of Gainsight for FY27… and I promise to do it in a bright room full of windows!

I pulled together the best practices we’re using into a short PDF (linked in the comments) in case it’s helpful as you think about your own approach.

I once got hired as a ski instructor in Aspen. But there was one problem: 

My skiing wasn't good enough.

After a couple of years teaching PeopleSoft, I decided to take a swing at a lifelong dream: becoming a ski instructor. So I tried out for the Aspen ski school.

The process was no joke. 

On-mountain ski drills, off-mountain physical tests, and the final "exam" was picking a random topic to teach an experienced instructor to prove your teaching ability (being the daughter of a dentist, I taught them how to floss).

At the end of it all, they gathered us to deliver the verdict.

One guy in my group was the best skier I've ever seen. He grew up in Telluride, could ski anything, but also had an ego the size of the mountain. He was cut immediately.

Then there was me. The girl who grew up skiing low-key hills in Tahoe. 

Standing there, I was convinced I had no chance.

They told me my skiing needed work…but my teaching was strong. And in their words, the job was about 60% teaching and 40% skiing.

Spoiler: they hired me!

That experience changed everything for me – and teaching became the backbone of my entire career. 

The parallels to my work in education and community were impossible to miss:

1️⃣ You meet people where they are, not where you wish they were: One-size-fits-all instruction doesn’t work. Beginners and experts need different pacing, language, and reassurance. You need to read the room and adjust so people actually feel successful.

2️⃣ Confidence matters more than perfection: Good instructors build trust first. In education, learning sticks when customers feel safe asking questions, trying things, and getting it wrong.

3️⃣ Success is when they don’t need you: Great instructors teach themselves out of a job. The win is independence. 

So whatever you’re building in 2026, don’t underestimate this part. 

Lots of people can do the work. Far fewer can teach it in a way that leaves people feeling more confident than when they started.

I’ve launched more than a few super user programs in my career—and I’ll be the first to admit, I didn’t get it right every time. Sometimes I leaned too much on flashy rewards. Other times, I underestimated how much structure it really takes to keep momentum going. But every misstep taught me something, and over the years I started to see the patterns of what actually works.

That’s why I put together this new piece on how to build a successful super user program. It’s a mix of lessons learned, updated tactics, and the kind of practical advice I wish I’d had back when I was flying the plane while building it.

If you’re building or refreshing a program this year, I hope it gives you some ideas you can steal: https://lnkd.in/gwnD9EhS

There’s something special about stepping out of the chaos of Dreamforce and into a courtyard filled with old and new friends with wine in hand, the fall light catching just right, and real talk about what actually makes (or breaks) our communities.

At JAX Vineyards yesterday, we gathered for a Dreamforce-adjacent conversation that felt more like a reunion than a formal event. We laughed, we grumbled, we celebrated, and we got honest about metrics.

I made some bold statements like:
“If you’re not tying community to business metrics, you won’t last.”

We dug into what that really means. The hard truth that great stories and basic stats only go so far if they don’t ladder up to the business. But we also talked about how possible it is to bridge that gap with the right framing, the right allies, and the courage to speak the language of business.

Everyone asked such thoughtful questions, and honestly, I felt like we could’ve gone on for hours. Maybe it was the food. Maybe it was the wine. Maybe it was just the kind of company that fills your tank instead of draining it.

I loved every minute of it.

If you were there...thank you. And if you weren’t…well, we’ll definitely do it again.

I took one of those career tests in high school. You know the kind - answer a bunch of questions and a computer tells you who you’re going to be when you grow up.

Mine said: “Greeting card writer.”

I didn’t even know that was a job. Meanwhile, everyone else was getting doctor, lawyer, programmer. Very official. Very impressive.

Even back then, I remember thinking… nah.

I’ve never been great with being told what I can or can’t do. Call it stubborn. Call it grit. Probably a little of both. But the moment someone tries to define my ceiling, something in me wants to push back harder.

Honestly? If I’d listened to that test, my life would look very different. And sure - I’d probably be a great greeting card writer. No shade.

But here’s the thing I keep coming back to:

When we tell people who they are, we shrink the possibility of who they might become.

Potential doesn’t fit neatly into a multiple-choice quiz. It never has.

And maybe the most greeting-card-worthy truth of all…

“Congratulations on becoming exactly who you were meant to be.”

Gift giving is my love language - because the best gifts don’t impress you. They make you feel seen.

I was recently gifted a custom monogramed robe and a big “E” mug from the Champion team. When I opened it, I just… paused.

Because it was so thoughtful. So specific. So clearly me. 

And it reminded me why I care so much about giving gifts in the first place.

There really is an art to being a great gift-giver.

It teaches you to listen closely. To write things down when someone casually says, “I’ve always wanted one of those…” If I’m out running errands and something screams someone’s name, I’ll grab it and tuck it away for the right moment. Sometimes I forget about it and rediscover it years later. Still works. (Still fun.)

The real gift is the look on someone’s face when they realize you were paying attention.

My parents modeled this for me. Random packages. No special occasion. No reason. Just a “saw this and thought of you.” And one of the best lessons they taught me was simple:

Give, not to get.

I’ve passed this along to my daughter. She once made a thoughtful gift basket for a sick friend - really poured herself into it. And didn’t even get a thank you text. That one stung. For both of us.

But she didn’t stop. She kept giving. And she’s found her people now: the kind, loving friends who show up the same way.

So when I’m on the receiving end of a thoughtful, unexpected gift? It hits differently. 

​​The art of giving isn’t about the thing. It’s the attention, the memory, and the quiet decision to care out loud.

And that kind of thoughtfulness matters everywhere - in community, in leadership, in friendship.

Because being seen is powerful.

I opened my very first board meeting with: “Show me the money.”

Yes, I quoted Jerry Maguire.

Board meetings are new territory for me, and I wasn’t fully prepared for how much work goes into getting them right.

The cross-team collaboration. The weeks of prep. The slides and analysis that never make it off of the cutting room floor. And the uncomfortable part - going back to teams who worked their tails off to say, “We didn’t end up using this.”

It’s oddly both aligning and isolating.

What surprised me most, though, is how much a successful presentation comes down to energy and confidence.

If you speak clearly, confidently, and with conviction, people sometimes don’t scrutinize every slide - they lean into the story you’re telling. That’s not a hack… it’s a reminder of how powerful storytelling really is.

I’ve been pushing myself to bring a little more of me into it too. 

Still leading with data and substance but not sanding off all the personality. That’s been a fun (and slightly uncomfortable) edge to explore.

Data earns you a seat at the table. 
How you show up determines whether people follow.

I used to wrestle with product leaders to get them to engage with community feedback.

I truly believed (and still do) that the best products are co-created. That PMs feel most alive when they’re building WITH customers – not just shipping to them.

I truly believe that insight hits differently when you hear them in a customer’s own words (instead of a summarized doc).

And then… plot twist.

Now I’m the product leader!

And if I’m being honest? I’m not 100% practicing what I used to preach. 😬

Not because I stopped believing in it. But because it is really hard to do well. Calendars get packed. Priorities stack up. 

I caught myself recently and thought,
 “Well damn. When did this happen?”

So I’m naming it. For myself, and for Gainsight.

This year, I’m making co-innovation a real priority again. Not as a philosophy, but as a behavior and a formal program. 

✅ More PMs having direct customer conversations. 
✅ PMs spending more time in our Gainsight community. 
✅ More listening without an agenda.

It won’t be perfect. But it will be intentional. 

If you’re a product leader and this feels uncomfortably familiar… you’re not alone.

Me actually wrestling with my product leader at Salesforce - Shawna Wolverton (one of the best product leaders of all time 💪)

A National Geographic researcher, a temp agency staffer, an HR Generalist, and a museum sales rep all walked into the same retreat.

I was swapping origin stories at my table during the Customer Education Leaders Retreat: “How’d you get into this work?”

One by one, the answers were random, winding…and definitely not linear.

And yet, every single one of them is now a top Customer Education leader.

AI has all of us thinking about how jobs are changing. Roles that exist today won’t exist in five years. And jobs we can’t even name yet will become new career paths.

Customer Education is proof.

Most of the best leaders in this space didn’t plan to be here. They stumbled into it. Said “yes” to something adjacent – and stayed.

But as we kept talking, a pattern emerged:

Every one of them is a lifelong learner. They’re deeply curious, empathetic, patient, resilient, and they THRIVE in ambiguity.

They also have grit. They’re competitive and persistent. And at their core, they genuinely want other people to succeed.

That’s the throughline.

Over the course of the event, the conversations kept reinforcing something I’ve believed since my early days building programs from scratch:

 This work isn’t just about content. It’s about humans. 

It’s *really* hard to do this well. And it only works when you keep people at the center of learning - even as the tech evolves around us.

Their careers weren’t linear. Mine wasn’t either. But I’m so glad they landed here - and I feel genuinely lucky to have spent a few days learning alongside them!

Gainsight CC Hits Milestones: IDC Leader 2025, Moderation Agent

This one feels especially meaningful. 

Gainsight's Community product just hit some major milestones - analyst recognition, incredible customer growth, and new AI innovation that’s redefining how companies connect with their customers.

As GM for Community, I get to see the work up close. The late nights, the “what if we tried this” moments, the small wins that add up to real impact. Watching our teams (and our customers!) push the boundaries of what community can do has been the best part of the job.

But this isn’t just about features or rankings, it’s about proving that community is business-critical. It drives connection, learning, retention, and growth in ways no other motion can.

Huge gratitude to our customers who believe in this vision and to the Gainsight team (Joris Dieben & Gil Michlin) who’s building it with heart and purpose.

Read more about what we’ve accomplished together 👉🏼 
https://lnkd.in/gkktpPyA

I’m so proud of how far we’ve come and even more excited for what’s next.

I was a shy kid growing up – but my mom never let anyone call me that.

It’s kind of funny, because if you know me now, “shy” probably isn’t a word you’d ever use to describe me.

But until I was about 13, that’s exactly how I showed up. Hanging back, watching everyone else go first instead of jumping in.

My mom saw it. But she hated labels. 

She never let anyone call me shy (or anything else). And looking back, that might’ve been the gift.

Because when someone puts a label on you, it creates a box. You either shrink yourself to fit it… or you exhaust yourself trying to escape it. My mom gave me a third option: time. No pressure to “be different.” No subtle message that something needed fixing.

My confidence actually started on a roller coaster.

Specifically, the Tidal Wave at Great America.

I was there with my best friend. I must’ve told her a hundred times I wasn’t going on the ride. She didn’t push or tease me. She was just excited to be with me.

And when I finally said yes? She was all in.

We rode that roller coaster five times that day. And something cracked open. Not that it magically made me fearless - but because I learned something important: 

I wasn’t stuck. I could change my mind. I could SURPRISE myself!

I didn’t walk off that ride confident in everything. But I stopped assuming “this is just who I am.”

So if you’re raising a “shy” kid - or if you were one - growth doesn’t always come from forcing bravery. 

Sometimes it comes from patience, safety… 
and one really well-timed “yes.”

I had a real “aha moment” during Skilljar’s Release Week.

For years, I led teams at the intersection of customer education and community – wanting better tools, clearer stories, and releases that actually reflected how customers learn and move across experiences.

Now, I’m leading from a different seat…helping bring together product, marketing, and engineering to turn those ideas into something real.

And this week, it all clicked!

This was my first Release Week at Gainsight (shoutout to Skilljar for starting the wave) working across our Digital Customer Hub products, and it felt like so much of what’s been building during my first year here is now fully in motion. 

Skilljar closed out the week by stepping into agentic learning with the NEW AI Tutor! 

Because learning isn’t just about content anymore (content still matters, but I’ll save that for another post 😉)

→  It’s about how learning is surfaced.
→  How it earns credibility, especially in a world shaped by LLMs.
→  How you use learner data to guide them, not info dump every course at once.

With our open beta of AI Tutor in Skilljar, we’re taking a real step toward learning that adapts, connects, and meets people in the moment.

That’s what agentic learning represents to me: THE BRIDGE.

If a rapid-fire Release Week says anything about where we’re headed this year…buckle up. 

Here’s to the incredible team I get to build with. Thanks for making this happen!

👉 https://lnkd.in/gBSwbySb

I keep hearing “community is dead” and “customer education doesn’t matter anymore.”

But that’s not what I’m seeing.

At a recent CXO summit, one stat jumped out at me: 47% of Chief Customer Officers now own community and education.

That’s a big jump from even a year ago – and I don’t think it’s a blip.

Headcount is tighter. Expectations are higher. Teams are being asked to do more with less… while still delivering a high-touch, personalized customer experience. That tension doesn’t get solved by more humans. It gets solved by better systems. And content has become one of the most foundational systems we have.

But not just any content.

The most effective content I see today doesn’t come from polished PDFs or generic help articles. It comes from communities and academies:

– Real customers
– Real questions
– Real expertise
– All shared at the moment someone actually needs it 

Layer in AI and this becomes even more interesting…we’re officially swimming in AI slop. 

As LLMs flood the internet with manufactured content, search and discovery engines are starting to reward human-generated, experience-based knowledge. That makes community conversations and education content MORE valuable than ever, not less.

Digital Customer Success isn’t new – we’ve been talking about it for years. 

But what is still emerging is community and education as core pillars of that strategy, not just side projects. Customers want to learn where they want, when they want, and how they want. Async. Live. Peer-led. Structured. Messy. All of it. 

Reaching them is harder than ever – and authentic engagement has quietly become a real differentiator again.

So no, community and academies aren’t dead.

They’re just finally being taken seriously.

Dreamforce week is a BUSY time and I'm excited to cut through the noise to talk about what actually drives community success...the plays, the metrics, and the stories behind them.

Not a keynote. Not a large breakout. A real conversation.

I’m hosting a small, focused session called “The Hidden Metrics of Community” where I’ll share the frameworks I used to turn the Salesforce Trailblazer Community from a side project into a business engine—and how those same ideas are shaping Gainsight's community strategy today.

We’ll swap stories, compare notes, and dig into:
- The hidden metrics execs actually pay attention to
- How to tell the story behind your numbers
- And the simplest ways to prove impact without overcomplicating the data

If you’re craving a space for an honest, tactical conversation with other community pros, this one’s for you. 👉🏼 Register here: https://lnkd.in/g2kpNQYD

My first job out of college, I had a boss tell me, “Sometimes you have to eat sh*t and say yummy.” 

I was 22. Bright-eyed. Brimming with theories from my business classes. Fully convinced I was about to *wow* this team with my big ideas and boundless enthusiasm. My mom called me her “corporate cutie,” and I thought I was ready.

Spoiler: I was not.

He told me I was too eager. I didn’t listen enough. And that passion without patience wasn’t helping anyone.

I was crushed. (Honestly almost quit on the spot.)

But I didn’t. My stubbornness kicked in. And I decided I’d prove him wrong.

Here’s the part that’s taken me decades (and across many different companies) to admit: 

He was right. The delivery? Terrible. The lesson? Spot on.

It’s really hard to do this well when you’re early in your career. You want to contribute, and to be seen. You want to justify why they hired you.

But trust is earned in quieter ways.

– By listening more than you speak.
– By asking good questions.
– By learning the context before trying to rewrite the playbook.

Especially if you want to build something from scratch someday – or influence at the exec level – you have to understand the room before you try to lead it.

Now, when I mentor people entering the workforce, I share the same advice… just with a lot more empathy (and a lot less profanity).

Start by listening. Be curious. Learn the history. Build trust. Then bring your ideas forward when the moment – and the credibility – are there.

You don’t have to shrink yourself.

You just have to sequence it the right way.

On-Demand Webinar | Community Outlook 2026

Community feels like it’s at an inflection point. Not because of a new platform. Not because of AI. But because the expectations have changed.

A few years ago, community often lived as a siloed forum off to the side. Today, it’s expected to drive scale, influence support costs, shape product decisions, drive customer stories, and contribute to retention.

That’s a VERY different mandate!

Community isn’t smaller than it used to be. It’s bigger. More cross-functional. More scrutinized. More strategic.

Join me as I’ll be unpacking all of this with Todd Nilson at the Community Outlook 2026: Trends and Predictions webinar on February 25th

https://lnkd.in/gNqVYUNT

“I don’t want to start a community. It’ll just turn into a complaint forum.”

I’ve heard that more times than I can count.

And honestly… I get it.

Opening the door to customers talking to each other – and about you – feels risky. Especially if you’ve ever watched a Reddit thread spiral or seen your product trending on Twitter for the wrong reasons.

But here’s what I’ve learned after years of doing this:

The conversation is happening anyway.
They’re going to talk no matter what.

So I’d rather they talk where I can see it. Where we can respond – and actually do something about it.

This might be an unpopular opinion, but contentious conversations aren’t a reason to avoid community. They’re a reason to build one well.

I learned this firsthand at Salesforce.

When Analytics Edition was announced, the backlash to the pricing model was immediate. Blogs lit up. Twitter threads exploded. Community posts surged.

Customers had a point.

It would’ve been easy to clamp down. Over-moderate. Defend the decision.

Instead, we leaned in.

I worked with a group of trusted community leaders to aggregate feedback so leadership could clearly see the impact. We enrolled super users as partners – not as a PR shield, but as an extension of the moderation team. The goal wasn’t to shut it down. It was to make it collaborative, not combative.

It was uncomfortable. No one loves reading pages of criticism about a decision their company just made.

But that discomfort led to something powerful.

Our COO published a blog that said, plainly:
“We got it wrong, and we sincerely apologize.”

Pricing was revised. Features were repositioned. And one of the most vocal critics responded publicly:

“It’s an amazing example of a company listening and responding quickly.”

That doesn’t happen if the conversation is happening behind your back.

When you nurture a community well – with clear guidelines, strong moderation, and empowered super users – it becomes self-regulating.

The community will protect itself from bad actors. And they’ll tell you when you’ve missed the mark.

It’s really hard to do this well. 

But avoiding hard conversations doesn’t make them disappear. 

It just means you don’t get to be part of them.

I have not one – but two – kids graduating this year. 

One high school. One college.

How is that even possible?
When did that happen?

Apparently this is the moment you’re supposed to “inspect your identity” as you approach empty nesting. And sure… there’s some of that. But what’s really showing up for me is something else entirely: 

Independence. The good kind.

The years when my kids were 7 & 10 through 14 & 17… those were HARD. Mentally. Physically. All of it.

That’s when I chose to start my own consulting company. I needed to own my hours, my clients, and my energy. I needed flexibility (and I didn’t feel like apologizing for it). 

Less than a year ago, I was evaluating a role at Gainsight knowing full well it would be 10x harder. I wasn’t sure I was ready. 

But I felt a pull - almost a responsibility - to help build the products I wish I’d had when I was a practitioner in the trenches.

Around that same time, a close friend said something that stopped me cold:
“The timing is perfect. You’re about to have a lot more time. And maybe you want something to keep your mind off missing the kids.”

She wasn’t wrong.

As both kids head out into the world, the constant in-your-face mom guilt quiets down. 

I can really dig in now, work hard when it matters, without feeling pulled in ten directions at once.

And as a small but meaningful bonus… Chuck Ganapathi got me a Starlink for Christmas! 

Which means we can do this empty-nesting thing from wherever we want. Somewhere sunny. Or snowy. Just not wandering around empty bedrooms pretending I’m fine.

For those who’ve been here before, how did you “empty nest” well?

I used to think, “Marketing talks AT people. Community happens WITH them.”

Turns out, that belief was holding me back.

I actively leaned away from marketing language. I had this underlying assumption that marketing and community just didn’t mix…

And for a while, that story felt right. 

The problem showed up in an unexpected place.

Our community members were thriving. Engagement was strong. The value was real. But internally? Confusion. Skepticism. A lot of “I don’t really get what this is for.”

At first, I chalked it up to people not paying attention. Then came frustration. Then… a few internal tantrums. 

What I finally realized was uncomfortable but important: 

This wasn’t a community problem. It was an awareness problem. 
And it was MY problem.

Employees are an equally important type of community member.

And just like customers, they need guidance + context. A clear understanding of the vision, the priorities, and the role they play. Without that, engagement doesn’t happen (not because people don’t care, but because they don’t know HOW to show up).

That’s where marketing messaging changed everything.
Not campaigns. Not hype. But clarity.

Messaging helped define the core pillars of the community - what it is and, just as critically, what it is not. It created structure around programs and actions. It gave the organization a shared north star to point to when decisions got hard.

This is where a lot of community teams struggle. 

We stay deeply focused on the customer experience and forget that it’s just as important to bring our own company along for the ride.

Internal clarity is what allows people to position the community, understand its value, and start building it into the DNA of how the company operates.

That shift changed everything for me.

Most companies still treat community like a silo.  A single team with its own segmented metrics and goals. 

The best ones don’t. They treat community like a Center of Excellence acting like a shared service that touches every part of the business: Product, Support, Marketing, Sales, Education.

That’s what I’m sharing tomorrow at Community Week Toronto: how to sell the value of community across your org, build cross-functional momentum, and tie it all to metrics execs actually care about. Because real success isn’t when community “belongs” to one team, it’s when people feel left out if they’re not part of it.

If you’re in Toronto for Community Week, come say hi. Let’s trade stories about what it really takes to make community the heartbeat of your company.

🗓️ October 23–25, 2025
📍 Startwell, Toronto
🔗 https://lnkd.in/e2HCPc9f

Meet Gainsight's Moderation AI Agent: Built for Safe, On-Brand Communities | Gainsight Community

communities.gainsight.com

I’ve been in this space long enough to know one thing: community managers can’t be everywhere at once.

I still remember the early days at Salesforce - we were flying the plane while building it. If a post went sideways, it was on me (or one very tired teammate) to catch it, de-escalate, and hope it didn’t flare up overnight. Exhausting. And honestly, not sustainable.

That’s why this announcement feels like such a big deal. Gainsight just launched a Moderation AI Agent built specifically for community teams. It’s designed to help communities stay safe, on-brand, and human—without burning out the people running them.

Here’s what I love most: it’s not about replacing human judgment. It’s about giving community leaders back time and headspace so they can focus on the work that really matters—nurturing connection, sparking conversations, and helping members feel seen.

I’ve always believed moderation is one of the hardest, least glamorous, yet most essential parts of this job. Seeing tools built with that reality in mind feels like progress.  

How are you handling moderation today? Is it manual? Shared across the team? Or do you already have AI in the mix?  

https://lnkd.in/gPU2AxaN

The Power of Gamification in B2B | Gainsight Software

When people hear “gamification,” they think badges. Leaderboards. Stickers. Fluff.

But what if it’s actually about focus?

The best gamified experiences don’t just entertain—they guide people toward the behaviors you want to see more of:
~ Asking their first question
~ Finishing that onboarding module
~ Helping another user
~ Coming back again tomorrow

That’s what I’ve loved about learning from great B2C examples at REI, Sephora, Starbucks, McDonald’s. They make the journey feel rewarding, but more importantly, intentional.

In B2B? We’re finally catching up. And there’s so much room to experiment.

I shared some of my favorite takeaways in this post on the Gainsight blog:
https://lnkd.in/gtA3D4BG 

Anyone tried something fun—or surprising—that actually worked?

Sales | Business Development | Strategic Partnerships

Do you like a good endurance challenge 🏃‍♂️?  Do you like 🏌️‍♀️

In two weeks, I am participating in my annual #100HoleHike to benefit Youth on Course, Colorado Golf Association and thousands of junior golfers across the country.  

Over the last four years, I have played 413 holes, walked 120.6 miles, spent over 40 hours playing and raised over $15k for this event.  I love a good challenge and this definitely falls into that bucket of fun!  

Any support is welcome, but if you would like to donate to my hike, https://lnkd.in/gussbcYW

Thank you for the support and stay tuned to see if I can accomplish my goal of more than 100 holes!

I’ve seen “digital CS” mean a lot of things.

Sometimes it’s a pile of automated emails no one reads.
Sometimes it’s a well-intentioned journey that’s so complex, even the team can’t explain it.

And sometimes—if we’re honest—it feels like Groundhog Day.
Sending the same messages and solving the same problems over and over and over!

That’s why this idea of a “scale motion” is so interesting to me. It’s not just about doing more with less. It’s about being thoughtful about when to add a personal touch—and when to let digital do its job.

Back when we were building programs at Salesforce, we had to figure this out in real time. We couldn’t give every customer a dedicated person. But we also knew a one-size-fits-all approach wouldn’t work.

So we started asking:
→ Who actually needs a human?
→ When do they need them?
→ And what can we support with community, content, or education instead?

It was messy. We tested a lot. Some things flopped. But that's how Trailblazer and Trailhead were born. We got smarter about how to care for more people—without burning out the team.

If there’s one thing I’ve learned, it’s that scale isn’t about volume. It’s about intention. And when you build from that place, the customer can feel it.

If any of this sounds familiar, this post is worth a read:
https://lnkd.in/gySG6qvZ

This news makes my heart SING!  Customers want information where they want it and when they want it so having learning, CS, and Community in lockstep is hugely important. Excited to see Gainsight leading the charge of a connected and harmonious customer experience.

Wow—what a whirlwind! It’s hard to believe it’s only been a month since I joined Gainsight. If I had to sum up my first month in two words? Full throttle. 
And honestly, I wouldn’t have it any other way. 

From day one, it was clear: Gainsight is my kind of place. Agile, expertise-driven, innovative, and quirky — all wrapped up in one vibrant culture. Joining right on the heels of the Skilljar by Gainsight acquisition has been a unique experience. The energy is palpable, and with Skilljar’s powerhouse talent and expansive reach, we’re solidifying our place at the forefront of customer education.

My first Pulse Conference came just three weeks after my arrival, and there’s no better way to get indoctrinated into the Gainsight Community!  Presenting the power of customer AI agents - enabling delivery of the right learning opportunities and community interactions at just the right moment in the customer journey - was a true highlight.  

I also had so many inspiring conversations with customers and there’s a genuine buzz about creating an experience where learning and community flow seamlessly into each other. We discussed how this integration is key to driving real impact on customer retention—especially by putting the right data in the hands of CSMs.

So what does month two look like for me?  Product deep dives, roadmap analysis, customer innovation workshops, community & education thought leadership roundtables, community reimagined webinars and more! 

As I look ahead, I’m energized by the possibilities and grateful to be part of a team that’s redefining what’s possible for our customers. If the first month is any indication, the journey ahead promises to be fast-paced, collaborative, and deeply rewarding. Onward! 🪄

I used to spend hours perfecting ROI slides.

Benchmarks, ratios, case deflection math—I had it all lined up. But no matter how sharp the numbers were, sometimes I still got blank stares across the table from my leadership.

That’s when it hit me:
The ROI of community and education isn’t just a data problem. It’s a belief problem. The people you’re trying to convince, they need to feel the value before they’ll trust the math. That usually means:
~ Giving them a story, not just stats
~ Showing a real moment when a customer got unstuck
~ Making the connection between programs and outcomes tangible, not theoretical

One trick that’s worked for me? I tie every ROI conversation back to three levels:

Level 1: Activity Metrics – Essential to you foundation

Level 2: Department Impact Metrics - Aligned to each organization; Marketing, CS, Support, or Product 

Level 3: Strategic Business Outcomes – Critical to ensure you’re aligned to the highest level company goals

Most teams focus on level one. But the magic lives in level two and three.

I walked through this in detail in my latest blog called Good Things Come in Threes: The New ROI of Community: https://lnkd.in/gTYTSmvr

What part of the ROI story do you find the hardest to land?

Nick Mehta names Chuck Ganapathi as Successor at Gainsight

Transitions are never easy - even the good ones.

After 13 years, Nick Mehta is passing the baton to Chuck Ganapathi as CEO of @Gainsight!

It’s hard to imagine Gainsight without Nick’s optimism and energy at the center.
At the same time, I couldn’t be more excited about what’s ahead with Chuck Ganapathi stepping in as CEO. Over the past year and a half, he’s shown us what thoughtful, bold leadership looks like and I know this next chapter will be just as human and impactful as the last.

Nick isn’t leaving completely and this feels less like an ending and more like a continuation of the journey.

Here’s to Nick for everything he built - a company, a culture, and a movement. And here’s to Chuck for where we’re headed - Retention-as-a-Service with Atlas, CustomerOS, and agentic AI at the core.

Major congratulations to the whole 1Password community team including Alana Fata, Zo Underdown, and Francis Murphy on the re-launch of their Community.  A huge undertaking that took us all on a wild and exciting roller coaster ride.  Now the fun really begins!  Go check it out at: https://lnkd.in/gQErwBup

I'm so honored to be moderating a panel of esteemed community experts at DigitalOcean's Community Connect Event.  It will be an inspiring conversation between Audra Gibson, David Yakobovitch, and Amy Chen...I really can't wait!  If you're in NYC on Thursday, November 21st, you must register and join us.

We plan to deepen all our integrations across Gainsight! BUT, which Skilljar integration do you want to see improved first?

The author can see how you vote. Learn more

Gainsight Customer Success

Gainsight Customer Communities

Gainsight Product Experience

Now that we are part of the Gainsight family, we are excited to deepen Skilljar integrations across the Gainsight CustomerOS. 

Weigh in on where we should start! 🙏

We’re Hiring—and it's YOUR turn to be part of something special!

At Gainsight, our Community business is at the heart of everything we do. I’m thrilled to share that we’re doubling down on this incredible team—and that means we’re looking for passionate, community-minded people to join us.

If you believe in the power of community as a strategic business initiative and want to help shape the future of community-driven success, this is your moment. If you're an AE, PMM, Solution Consultant, Engineer, Product Manager, or CSM we want to hear from you! 

Let’s grow our community business—and our team—together. Come be part of something truly special. Hit me up and let's start the conversation.

The Messy, Magical Work of Community Groups | Gainsight

Community groups are one of the most flexible, powerful, and under-leveraged tools for community growth.

When I say “community group,” I’m talking about a focused corner of your broader community—where members can self-select based on what they care about most. Smaller groups, deeper connections. That’s the whole point.

Some community groups will start strong and fade. Some will never get off the ground. And honestly? That’s okay.

I’ve seen this happen more times than I can count—at startups, at Salesforce, and with clients I advise. You launch a group with the best of intentions… and a few months later, it’s a ghost town.

But when a group does work? When it becomes a space where people feel seen, supported, and heard? It’s magic. And it’s also a ridiculously powerful engine for product feedback, customer education, CS scale, and even pipeline.

Still, it’s really hard to do this well. That’s why I pulled together the 7 questions I get most from community teams trying to launch or resuscitate a group. Like:

- Why do they fizzle?
- What’s the right rhythm?
- Can employees lead?
- How do you know what members want?

I don’t have all the answers. But I’ve tried a lot of things—and failed at enough of them—to know what’s worth your time.

If you’re thinking about spinning up a new group (or breathing life into a stale one), I hope this helps: 👉 https://lnkd.in/gReh34VK

“How do we scale without losing the soul?”

That's the big question behind this panel—and honestly, behind a lot of the conversations I’ve been having lately.

It’s one thing to run a thoughtful, human-centered program for 20 customers. It’s another thing entirely to do it for 5,000... without burning out your team or turning everything into a bot-ified mess.

And no, AI isn’t the villain here. (Used well, it can actually amplify trust.) But scaling with intention takes more than tools. It takes a mindset shift. Systems that support—not replace—relationships. And a team that’s aligned on what “high-value” actually means.

Come hear Aaron White, Kevin Dunn, PMP®, and me on July 23rd where we'll dig into:

- How smart orgs are balancing automation and authenticity
- The kinds of data that actually help (not just overwhelm)
- Why structure doesn’t have to mean rigidity

One of the best lessons I’ve learned is not everything has to be perfect to be useful. Especially at scale.

Save your spot! https://lnkd.in/gPtdBkir

Curious—how are y'all are tackling this? What’s worked (or flopped) as you’ve gone from one-to-some to one-to-many?

I’ve been thinking a lot about what it really means to invest in community.
Not lip service. Not a “nice to have.” But a serious, strategic bet.
And this week, that bet got a whole lot bolder.

Gainsight just welcomed five Community pros—Jon Wishart, Micayla Severino, Meredith Estremo, Christopher Harrison, and Carlos Huntley-Jimenez—to double down on our commitment to creating a world-class community product and ecosystem.

These are people who’ve been in the trenches. Who’ve supported and scaled community programs at some of the largest and most prestigious companies around the globe. They’ve seen the power of connection and advocacy from every angle—and they’re joining to help us do it better. Smarter. With more heart. And at scale!

This move isn’t just about adding talent. It’s about really “putting our money where our mouth is” when it comes to a commitment to building community the way I’ve always dreamed!. Honestly, that hasn’t always been the case in this industry. But we’re changing that.

To the folks already deep in the community trenches—this one’s for you. You’ve helped show the impact, justify the budgets, and prove it works.

To our new Community Acceleration Crew—welcome, we're SO lucky to have you! Let’s build something truly meaningful and that we are truly proud of!

For those that know my hubby, he can turn ANYTHING into an endurance challenge including GOLF! On 9/23/24 he'll play 100 holes of golf to support an amazing organization called Youth on Course.  I'll even caddy for some of the holes to help save his back 😆 

He'd love your support, any amount matters!  Here's a link to donate and learn more: https://lnkd.in/guJqrfPr

Reserve your seat today for the #DigitalOcean Community Connect in NYC. 🌊🗓️🗽https://lu.ma/7twqx224 

Don’t miss out on connecting with fellow tech leaders, #developers, and innovators.

Director of Product Marketing, Gainsight

In my early days at Skilljar I found myself asking everyone - our CEO, fellow Skillets, and Customer Education pros like Blair Mishleau, Debbie Smith and Zoe Ludwig - one persistent question:

"What's the real difference between an Academy, Help Center, In-App guidance, and Community? And if you've got a stellar Help Center, why bother with an Academy at all?"

I'll boil down their answers to a common situation we're all in everyday: it's like choosing between texting, calling, or meeting in person. Different situations call for different approaches. Sometimes customers just need a quick answer (Help Center). Other times, they need step-by-step guidance (In-App). Sometimes they want to dive deep with video or audio learning they can come back to (Academy), and occasionally they just want to learn from peers (Community).

The key insight? Learning needs to happen everywhere. 

I'm excited that our Customer Education 2025 Trends Report finally backs this qualitative insight with hard data:

-86% of CE teams are shaping the onboarding experience
-53% are contributing to help centers
-28% are building and managing communities

Get all the data here: https://lnkd.in/g6k8anPw

#customereducation

Interesting way to think about how Learning, Support, Community and Product Experience work together and the importance of each approach to creating the best customer experience.  Nice job Sonia Moaiery!

🚨 Happening TOMORROW: The business case for community, finally cracked.

Customer education and community aren’t just feel-good strategies. They’re quietly driving real ROI. We are talking retention, expansion, and reduced support costs. But most leaders still struggle to prove it.

That’s where Erica Kuhl comes in.

She built Salesforce’s Trailblazer Community and scaled it to millions. Now EVP & GM at Gainsight, Erica’s helping teams turn connection into one of their most efficient growth engines.

💻 Community Reimagined: Unlocking ROI Through Connection and Learning
📅 Tuesday, June 24
⏰ 10:00 AM PT
🔗 Register now (seriously, don’t miss this!)

You’ll learn:

🔗 How to tie community and learning to revenue, retention, and real metrics
🧠 Smart ways to get exec buy-in without sounding like a TED Talk
📈 How to scale impact without scaling headcount (or burning out your team)

Show up for the frameworks, the real talk, and the Erica Kuhl masterclass.

Register in the link below 👇 

#CustomerSuccess #CommunityLedGrowth #CustomerEducation #Gainsight

Last Thursday, a $47B IPO validated something a lot of us have known for a long time:

Community is a growth strategy.

That IPO with a 250% first-day pop and 13 million monthly users....that was FIG – Figma's public debut.

Figma made design collaborative – and made community part of the foundation from the very beginning. That mindset shaped everything, from how they handled feedback to how they showed up in every community program.

It’s rare—really rare—for a company to go this far without losing sight of what made them special. The product’s incredible, sure. But the magic? It’s the way they empowered their users to feel like co-creators, not customers. Early adopters gave feedback in real time, taught each other, and built the first how-to guides.

That energy grew into Friends of Figma (https://lnkd.in/g6Q8UycX meetups in cities around the world, run by volunteers, sharing use cases and workflows face-to-face.  

The online community exploded – and just this year, they launched the Figma Forum (https://forum.figma.com/) on Gainsight's Customer Communities to give people an even richer place to connect.  

Their IPO success (which outperformed most major offerings since 2020) was about a lot of things: revenue, profitability, product love, smart execution.

But let's not miss this:
Figma has always put its community at the center. They leaned into community early. Before it was cool. And they still do.  

Jason M. Lemkin wrote about the massive IPO results on @SaaStr.
He said it best: “Figma’s IPO success isn’t just about timing—it’s about building an incredibly sound SaaS business that grows efficiently, expands its market, and generates sustainable profits. Figma proves that great SaaS companies can still command premium valuations and deliver explosive public market debuts. SaaS isn’t dead. In fact, it’s bigger than ever."

For those of us doing the sometimes messy, often underappreciated work of building community, this should feel like a huge milestone.

Because when a company like Figma hits the public markets with this kind of clarity about who they serve and how, it pushes the whole field forward.

I’m beyond proud that we get to support the Figma Forum through our platform at Gainsight. And Even more proud to watch this community (and this company) keep raising the bar.

There’s a particular kind of magic when you get the right people in a room.

Not just smart people. The ones who’ve been in the trenches—building, breaking, rebuilding. People who’ve made community and customer education not just their job, but their craft.

That’s the idea behind Constellation.

We launched Atlas at Pulse in May, and if Atlas holds up the sky, Constellation is the brilliance within it.

This program is  a curated group of leaders—each a guiding star in their own right. Folks who’ve shaped the way we think about learning and connection. People who’ve taught me (and each other) more than any book or conference ever could.

Our first session kicked off last week and the brainpower in the room didn’t disappoint. It was about setting the stage and we already surfaced big meaty questions we want to tackle next time like:
- AI’s impact on measurement
- Customer journey orchestration
- Human vs. AI balance

Meet the Stars Behind Constellation:
Adrianne Poole Allison Able Andy Best Joseph M. McCarthy Katie Brown Shannon Cunningham Jill Glynn Kevin Dunn, PMP® Kevin Lau Stephanie Grice Jeni Asaba Kelsey Taylor Kristen Engelhardt Mary Catherine Plunkett Adam Avramescu Jordan Scott

The first cohort’s already set, but if this sounds like your kind of space, let’s talk. More here: https://lnkd.in/gD6JP9fp

Very exciting news to share! 🎉 Today marks the start of a new chapter for me as Gainsight has acquired Erica Kuhl Consulting (EKC).  I’ll be joining as EVP & GM of a newly created business unit that combines the company’s customer community, learning, and in-app experience offerings.  With an added bonus of being on this journey with Chuck Ganapathi, my Salesforce partner in crime since 2007.

Throughout my career, I've been a passionate advocate for the power of integrated community and learning to drive tangible business results. That’s why I am so excited to shape Gainsight's product strategy and lead strategic advisory services, enabling companies to engage customers in ways that increase retention, spark product innovation, and accelerate revenue growth.

To my valued EKC clients: your trust and partnership have been an integral part of my journey.  I'm so grateful for the incredible work we've done together and for inspiring me every step of the way. I’m excited to continue supporting your success-now with expanded resources and reach as part of Gainsight. Together, we’ll unlock new possibilities with a unified  community, learning, and product experience. 

Here’s to this next chapter and the incredible opportunities ahead!

Read the press release here: https://lnkd.in/gjfmbfVj

🚨 Breaking: Gainsight acquires Skilljar! 🎉 

We're leveling up learning with AI, ditching static courses for "in-the-moment" training. This deal isn't just news, it's a revolution in customer education. Read the story  👉  https://bit.ly/41W1ba6 

#Acquisition #Gainsight #Skilljar #TechDeals #LMS #CustomerEducation

I'm speaking tomorrow about one of my favorite topics - Measuring Community ROI!  Join me and special guest Ali B. from 10-11am PT, June 24th.  I'll share all my secret ROI tricks of the trade! 🤫