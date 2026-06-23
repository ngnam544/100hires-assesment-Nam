# Recent Posts for noeleflowers

1-month free trial with 24/7 support. We’ll remind you 7 days before your trial ends.

Your next job is an InMail message away

Contact the right people with InMails.

Get rewards from Headspace, Notion and more (up to $845 value). Terms apply.

Get access to exclusive events with industry leaders and professional experts in Premium-only conversations.

Reach out to anyone on LinkedIn, from recruiters to hiring managers, even if you're not connected. InMail messages get a 4.6x higher response rate compared to emails or cold calls.

IT Recruiter - Looking for Solution Consultant, Senior PM/BrSE, Engineering Consultant.

7 years experience in Software QA, Process Audit, IT Business Analsyt, Project Lead/SME in Tech industry.

C&B Specialist, Payroll, PIT

AI Lead & Head of AI Center of Excellence (CoE) @Merkle, a dentsu company

Managing Economist at Swiss Economics

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

Community Director @ Articulate

Thank you Paz Pisarski for featuring me on The CC Coffee Corner! 

You can check out my interview here, it's basically all about how I want to have lunch in person with Bri Leever: 

https://lnkd.in/ekGyv8KP

Template Creation Guilds for Sales Enablement & Customer Service Trainers

I'm working on a new pilot project in the Articulate Community, E-Learning Heroes, that I'm really excited about: Template Guilds 🎉 

tl;dr—guilds will bring together 15-25 trainers specialized in a specific subject-matter area. These specialists will to work together over the course of four weeks to create a "core template hub" of all the essential Rise courses needed to get started training in that subject matter. 

The first two guilds we're launching are for: 

💼  Sales Enablement - if you create workplace training to help sales teams thrive, from quarterly product kickoffs to competitor battlecards, this is for you

💁‍♀️ Customer Support Trainers - if you create workplace training to help customer support teams thrive, from soft skills training to new agent onboarding, this is for you

If you're in the L&D space, please  share this widely to help it reach the right people! 

You can view all the details on this program from scheduling to how to join here:

https://lnkd.in/eaBhpibM

Very proud of what Rachael Silvano is accomplishing here at Articulate — congrats to her on her Zappy win!

The conversation around online communities x AI is over-indexed on the fear of answer engines supplanting the use of communities. 

What often feels missing from the conversation is the way that online communities are about to become an even more crucial business tool in the age of answer engines. 

Online communities have a superpower. The authenticity, flexibility, and context-richness of the "content" (i.e., conversations) happening in online communities is uniquely positioned to rank in a search landscape that is suddenly not just about SEO, but AEO & GEO, too. 

We need to think more about that advantage and how to use it. Evan's post here gives a great example of just one possible way that communities can play to their strengths as the search landscape evolves.

I'm thrilled to be speaking as a part of The Community Collective's 5th cohort—cohort based learning around community is near and dear to my heart and I'm so excited to support this group. 

Paz Pisarski, thank you for having me.

Articulate - Community Strategy Manager

Thrilled to share that my team here at Articulate is growing! 🥳 

If you're an experienced community professional specializing in either strategy or content & engagement, we're looking for you 👀 

Come work with me, Ginger Swart, Kell Ording, and our incredible community of E-Learning professionals we call "E-Learning Heroes." 

Check out the two roles we're hiring for here: 

Community Strategy Manager: 
https://lnkd.in/eRf5QkZR

Sr. Community Content & Engagement Specialist: 
https://lnkd.in/eD8ZKr87

Comments open for questions, and will triage DMs as possible!

Founder & Managing Director @ FeverBee | Writes and consults about how to build thriving enterprise communities.

The Killer Mistake of A $250k+ Enterprise Community 👇

In 2021, we worked with an insurance firm whose customer community was on life support—just months after launch.

→ They had the right platform.
→ They ran a major promotional campaign.
→ They even had strategic services from the platform provider.

But activity was dead.

The issue? The community managers didn’t know how to engage people.

Here’s a common mistake they made:

Every discussion was a generic “What do you think about…?”

Sounds harmless, right? But here’s the thing:

🛑 Asking strangers for random opinions doesn’t work.

It’s like walking up to someone at an event and saying, “Hey, here’s an article—what do you think?”

Awkward, right? That’s why people ignore those discussions online.

The Real Reason People Engage:
We respond when we feel we can help. The more specific the problem, the more likely people will jump in. We want an emotional payoff.

Example:
❌ “What are your thoughts on productivity tools?”
✅ “I’m overwhelmed with deadlines. Can anyone suggest a simple tool to track them?”

The second example invites empathy and action.

💡 Pro Tip: If you want engagement in your community, ask questions that:
1️⃣ Are specific.
2️⃣ Show vulnerability or urgency.
3️⃣ Make people feel their answer will genuinely help.

Here’s a formula:
“I’m [struggling with X]. Does anyone know [a specific solution or advice]?”

Engagement isn’t about random activity. It’s about making people feel useful.

If you want to learn more, sign up for our advanced community skills course. DM me for details. 

#community #skills #courses

Dear Bri: Community Strategy, Fiascos, and Drama | Ausha

I had WAYYYY too much fun recording my episode of Bri Leever's new podcast, Dear Bri. 

This is such a wonderful idea for a show combining community strategy with some levity & drama 😎 

SO excited to see that the first three episodes are now live—check 'em out, rate, review, subscribe, all the stuff: 

https://lnkd.in/etz88MYH

CONGRATS BRI!!

Co-founder & CEO at Zapier, YC & Mizzou Alum

2 new Zappy Winners this month.

Neither of them are engineers.

Jeff Hirsch is a systems architect at Redis. He started using Zapier and within weeks, 5 internal teams were using it. People were lining up to be next before he'd even built the onboarding. He and his team shipped it with SSO and SCIM in place from week one.

Rachael Silvano (a former Zapien!) runs Community at Articulate. The gamification feature she needed wasn't on their platform’s roadmap, so she built it herself for 140k members.

Both times, the person closest to the workflow was the one who fixed it.

Congrats to our first ever monthly Zappy winners. Know someone using Zapier in incredible ways? 

Nominate them (or yourself) here: https://lnkd.in/gX82aRTs

How to Audit Your Online Community (with a real case study example + template to show you how!)

When was the last time you did an audit of your online community? 

Excited to share a new post on my blog today on this topic. 

Above and beyond the 'what, when, and how' of community audits, my obsession with practical, tactical, actionable tips continues—in this post, I included: 

✍ A free template you can use to get a head start on a self-audit of your community
🔍 A case study example of a pro-bono audit I did with Private Label People Private Label 

Thanks are due to the PLP team for generously agreeing to have your audit featured on my blog! 

Thanks are also due to Max Pete and Tiffany Oda, whose writing & resources on community audits are also included here.

Hope y'all enjoy reading this one as much as I enjoyed writing it! 

https://lnkd.in/eZCnHesr

We’re excited to launch our Community Cohort #5 with our new speaker lineup 🎉 Why? 

Because community is the new currency, especially for businesses.

But building an impactful one can be tough, exhausting & lonely.

We're building a movement to change that.

Our 8-week cohort is for community builders, operators & founders to level up and build impactful communities, together.

160+ alumni have said YES to our cohort from companies such as Canva, Blackbird, MYOB, UNSW Founders, Tractor Ventures, LaunchVic, Founders Factory Africa and more. Are you next?

If so, check out our speakers 🔥

🏵️Seth Godin @ The Carbon Almanac, altMBA and Author
🏵️Jeanette Cheah @ HEX
🏵️DeMario Bell @ Culture Amp
🏵️Monica Rysavy, @ Forte Labs, Systematic You 
🏵️Sheree Rubinstein @ One Roof 
🏵️Max Pete @ Square
🏵️Dara Simkin @ Culture Hero
🏵️Simon Thomsen @ Pinstripe Media, Startup Daily 
🏵️Noele Flowers, Community Consultant
🏵️Joel Hines @ Being Human, TEDX Speaker and Author
🏵️Emily Casey @ What The Health, Tenmile

Not to mention Coaches Tim Duggan, Yana Belova & Ben Davies and Cohort Hosts Jess Walker & Paz Pisarski. 

Are you excited? Tag someone who needs to know 👇

📅Cohort #5 Dates: Mon 16 Sept - Fri 8 Nov 2024
📍Location: 100% online, IRL socials in Melbourne, Sydney & Lagos
🧡Attend an Info Session 👉 https://lnkd.in/gSMjxTGK 
👉Apply before Fri 23 Aug @ 12pm AEST 👉 https://lnkd.in/g534S2Ru

We can't wait to welcome you in 🏵

Four deceptively simple principles of community building: 

1. Balance give & take ⚖ 
2. Create feedback loops ⭕ 
3. Less is more ⏬ 
4. Lead by example 👩‍🏫 

I say "deceptively simple" because although these on their face feel like pretty broadly applicable (and maybe even trite) statements, I think that if you keep them in your pocket throughout every step of community building—from your platform choice to your engagement plan—you could end up basically "stumbling" into a pretty sophisticated community strategy, without necessarily mastering any of the more "subject-matter" oriented parts of community building, like, say, building an engagement calendar. 

If you're on my newsletter, you know I've spent the last four weeks breaking these principles down and giving examples of how they show up alllll across community strategies. 

But, I wanted to broaden this conversation to LinkedIn, too. 

If you're a community builder, do you agree with these principles? Where do you see them showing up? What would you add?

Saw this shared via Evan Hamilton, re-shared with my new team this morning.

Some great principles in this just around the importance of getting really, really good at asking questions when we're running, or even just participating in, communities. Some extra musings on this I thought I'd share—

📣 Ultimately, the questions we ask in communities function as a "call-to-action," so they're often the most important part of what we share in communities as staff members. This may seem obvious, but to many community teams, it's not—we can tend to get way, way too focussed on the content/value we're sharing with communities and not put nearly enough focus on the mechanisms we use to solicit value back *from* members. This manifests as sharing lots of articles or best practices as the "expert" in the space but forgetting to put intention behind how you ask your members to contribute. But, usually, especially in communities of practice, what members have to say to each other is more valuable than what we have to say to them. 

🤝 The other principle, beyond asking good questions, that I think Richard Millington is invoking here is one I'm really passionate about—as an admin, we're better off trying to participate *as model community members* than to participate "as admins." Why? Because our participations in communities serve to model for other members how *they* can step up and spark participation, too. So, if you're asking a lot of questions, but from a very admin-driven perspective, don't be too surprised if you're the only one who ever asks a question in your community. Members won't be able to emulate you if you're not giving them an authentic model that is replicable for them. Study how your best members participate, and make your engagement efforts about modeling and amplifying those behaviors. 

Thanks for the thought-provoking shares, Rich & Evan!

Community builders: come work with me (+ Kell Ording and Rachael Silvano this spring! 

I'm looking for a part time (10-15 hrs/week), ~3 month contract to support my team at Articulate while our stellar Community Content & Engagement Specialist Katie Jordan heads out on maternity leave. 

The ideal person:
-Is a strong writer & a fast learner 
-Has some experience building and deploying community-specific content & engagement calendars, and understands the difference between content built for community vs. outbound social 
-Has some experience moderating a community with not just an eye toward maintaining guidelines, but sparking meaningful engagement along the way
-Is comfortable nurturing member relationships in community settings and 1:1
-Is super organized, good at following & maintaining process & documentation, and managing their time 
-Is familiar/comfortable working in a SaaS environment (comfy communicating on Slack, working with Notion + GSuite, etc)
-Can generally work either EST or PST 
-Mega bonus points if you've worked with either or both: Khoros (Aurora) + Articulate (Storyline + Rise)

This would be a great position for someone in the community space between FT roles and looking for a bridge, or a more jr community person looking to hone skills in engagement-specific work on a larger community team. 

My company is taking referrals for this contract through a freelancing partner, so if this interests you, shoot me a quick message letting me know why you think you'd be a fit, and if I see alignment I'll get you referred to our partner to submit a proposal. 

Heads up: I'll do my best to read as many of these as I can, but I may not be able to respond to everyone. Especially if volume gets big over the next couple of days, I may update this post & let y'all know I'm closing referrals. So, if this feels like a fit to you please shoot me a message on the early side! Thank you!

I couldn't be more thrilled to share that today I'm joining the team at Articulate as their new Director of Community. 

There is more to say about this transition than can fit into one LinkedIn post—in time, I'd love to share with my network more about choosing to return to full-time work after spending time working for myself as a consultant & a 'retrospective' of what my job search was like in this extremely unusual market (if you're in it right now, I feel for you). 

But, for the moment, I want to focus on celebration & gratitude—a little of the former, a *lot* of the latter. 

In celebration: sometimes against my better judgement (😅), I was *super* picky in my job search. I had a big list of priorities for my next opportunity and I'm so happy that I was able to land at a place that checks all of those boxes: continuing to grow my career in community management, sitting at the intersection of community and learning, stepping out of 'tiny-startup land' into a bigger organization, and continuing to grow as a strategic leader. Thank you to Tom Kuhlmann for helping me find such a great fit—I'm so excited to work with you, + Ginger Swart, Kell Ording, David Anderson, and Alyssa Gomez! 

In gratitude: finding the right next step wasn't easy, and I couldn't have done it without the support of my family, friends, and colleagues. There are too many people who helped me—whether that was by reviewing a resume, giving advice, or making an intro—than I could list, something I'm grateful for in and of itself. In particular, my friends and colleagues in The Community Community provided every kind of support you could imagine. Thank you! 

A few people deserve individual 'thank you's here—they are: 

Brian Oblinger made valuable intros, talked me off a few ledges, and sent me dog pics to lift my spirits🍸🐕. Jocelyn Hsu & Rachael Silvano were involuntarily subscribed (😇) to the 'daily updates' version of my job search, which meant they listened to basically every up, down, twist, and turn of the search. I am endlessly grateful for your friendship, humor, and wisdom. Special shouts to Krystal Wu for job-search solidarity when I really needed it. To nobody's surprise, Max Pete deserves special thanks for exceptional & consistent cheerleading. 

TL;DR: I'm extremely excited to embark on this next step in my career and can't wait to continue to share with you all things community!

Very excited to share that my mini challenge, 'Engage 10 community members in 1 week,' will run from December 2- 6 and is now open for enrollment. 

I'm pumped to work with the folks who have already enrolled via the early enrollment period and my newsletter, and would love to see some more folks jumping in from my friends on LinkedIn. 

You can see all the 'nuts & bolts' of the challenge (dates, session times, specifics of the content, etc) on the enrollment page, which I'll paste in the top comment.

But, I want to highlight a few other things about this challenge that I think make it special, and that might be tie-breakers for you in deciding whether or not to enroll—

🏇 You're actually going to finish this challenge. My superpower in working with online cohorts like this is that I'm usually able to get unheard of completion rates out of my groups. That's probably because my background is in public school education—so I know how to make a learning experience with the right scope and the right scaffolds. Plus, I keep my groups small enough that I'm able to be fanatical about paying close attention to where everyone is at. 

🫂 We're focussing small to go big. You might be like, "ugh, *just* engaging 10 people? That seems small." But the purpose of this is to put new engagement strategies into practice in a manageable way, so that we can test what works with your different engagement sectors, and make a plan to scale them. This is why this challenge is a good fit for total newbies and community veterans alike. 

📹 If you enroll early, you get access to my community group coaching calls right away. So, if you were to enroll today you would get access to the call this week on Wednesday and the call on the 20th in advance of the challenge starting. I think this alone makes this a no-brainer for anyone who has been wanting to work with me on coaching. 

Interested? I'd love to have you join me—look for the enrollment link in the comments. 

If you have any questions at all feel free to either shoot me a DM or leave a comment. Excited to get to know some of y'all more deeply!

I am on the hunt for my next full-time role 🕵‍♀️ 

Some of my close network already know this—shoutout to my friends in The Community Community & everyone who has supported me so far with referrals, advice, and camaraderie 🙌 

But, someone recently told me they hadn't reached out to me about an opportunity because they didn't think I'd be interested and didn't know I was looking 🤦‍♀️ 

So, in the interest of serving that old adage about job-hunting that you should make sure everyone and their mother knows you're looking for a job, let it be known: 

📣 📣 📣 I AM LOOKING FOR MY NEXT FULL-TIME ROLE IN THE COMMUNITY INDUSTRY! 📣 📣 📣 

Now, for some specifics. 

📜 Here's what I've done before: 
- Community & education for SaaS startups for 8 years 
- Built & ran a community of practice/support program at Teachable for 4 years
- Built & ran an education program for community pros at Commsor for 2 years, leading a team of 5 
- Worked for myself consulting on community & education strategy projects for brands teeny (solo entrepreneurs) to enormous (multiple Fortune 500 companies) for 2 years 

🔎 What I want to do next: 
- A community role that focusses on strategy, learning/practice, or team leadership, ideally continuing in the SaaS space 
- Work for either a mid sized co / enterprise where I can grow with experienced community/marketing/customer leaders OR with a startup whose leaders have prior scaling or corporate experience on their resume
- A mid or sr. level role depending on the size of the org, team size, & role scope 
- A remote or hybrid role (more flexibility on hybrid for the right opportunity!) 

⁉ What this means for consulting 

I'm still at it, and still will be at it until I find the right fit—and in this job market, that could be next week or it could be in six months.  

I will continue to book projects with clients up until the point where my calendar no longer allows me to do so. I feel incredibly fortunate that consulting has given me some flexibility to be slightly picky about timeline & fit as I look for my next full-time role, and even after my client schedule tightens, I suspect I'll still have an interest in creating newsletter & blog content on community, which has been such a huge part of growing my thinking about this industry throughout my career. 

I love working with my clients, I just know that part of growing my career further means embedding further in another big project. 

Thank you so much for reading—if you have a role in mind that you think might fit my past experiences and future wishlist, I would absolutely love to hear from you!

And, if you're my community bud and you're in my network reading this, mind leaving a comment for encouragement & reach? 

👋

Community Mini-Challenge: Engage Ten Members in One Week — Interest Form

Let's deeply engage 10 members in a week together 🤓 

I've shared with y'all in the past that I've run a few community strategy challenges in my community, but I've gotten some brilliant feedback from my community members that they'd like opportunities to make more focussed efforts on smaller topics over shorter periods of time. 

So, I've decided to run a mini-challenge in my community.

The TL;DR: 

 📅  This'll be a week-long challenge (a Monday through a Friday) focussed on helping you activate a small group of members, with a daily focus on using strategic approaches to different member segments 
📚  Challengers will get an engagement playbook with a dozen + engagement strategies tailored to connect with and gain impact from different engagement segments (inactive, partially active, and active), and will get a chance to deploy 3-6 strategies during the challenge
📹 On day one, challengers will all participate in a kickoff engagement workshop to build literacy around engagement strategies and approach, identify engagement segments, and get to know the program 
🤝  On days two, three, and four, challengers will complete independent challenge tasks, and have the option to participate in live 30-minute check-in calls where they can bring challenges, questions, or simply come to co-work or listen in. Multiple sections of check-in calls may be available depending on the number of registrants, so that calls can remain small enough for everyone to get questions answered. 
📹 On day five, challengers will all participate in a closing engagement planning workshop to help systematize their learnings into a more ongoing engagement plan  

This is for you if...
💚 You're brand new to community and need to learn the basics of engagement strategy 
🫂 You have a newly established community and need to begin building engagement among founding members
🤓 You have an established community or engagement practice, but you need some accountability to keep your strategy fresh 

If you want to take part in this, make sure you're on my newsletter so that you can see when registration opens. If you want access to early registration (this'll likely be capped), fill out this form & help me break the tie between the two weeks I'm considering offering this: 

https://lnkd.in/eBSvRURB

Hope to get to work with lots of you during this!

Excited to participate in this panel-style talk next week with Talkbase! 

I'll be chatting about one of my favorite topics, community content—and this event is free & open to all, so please do pop in and say hi :) 

And, if there are any questions about community content you want me to address during this, leave a comment here—I always like going into panels with a few extra questions or scenarios in my pocket.

#CommunitySkills – How to Build a Content Strategy

📆 Join us next week for #CommunitySkills – How to Build a Content Strategy with Noele Flowers

Content is key to attracting, retaining, and nurturing your community members.
Without a clear and compelling strategy, engaging your audience and keeping them coming back consistently is challenging.

🎟️ Grab your free spot here: https://lnkd.in/eMBsi76r

In our session, we'll walk through:
🖊️ Build an effective content strategy that aligns with your community’s values and keeps members engaged. 
🖊️ Understand your audience to plan and deliver content that drives conversations
🖊️ Learn how to craft a strategy that supports long-term community success

#content #community #strategy

Finally got it together yesterday to put together a newsletter with some reflections on my job search. 

Reflections/revelations include: 

📊 some unoriginal, but maybe comforting, thoughts on the current job market for community builders 
🍻 how doing a brief stint as a bartender helped me be pickier in my overall job search 
🌳 some shade to a hiring manager who really did me dirty 
😇 what I did during my job search that got me "un-rejected" on multiple occasions 

Read the whole thing here: 

https://lnkd.in/eHGpj3fv

And, if you're a community person job searching now & there's any way I can support you—from making intros to being a listening ear for venting—I'm here!

Yesterday I posted asking whether anyone knows if the Olympic Village has community managers, and all your comments were alternately insightful and hilarious. 

This got me thinking: are there other communities—traditional or non-traditional—we're dying to get a peek under the hood of? i.e., "is there a community for..." / "does x thing have a Slack workspace"?

Leading community, customer marketing, customer education, and scaled success teams to drive business outcomes. Privileged to have worked at HubSpot, Reddit, and more.

Weirdly...I think Ideas Forums are due for a comeback.

I wouldn't have guessed this a year ago. It felt like they were on the way out.

But as more and more people use LLMs, you're going to get even more questions like "Does [product] offer [feature]?".

Here's the thing: even a great Knowledge Base team generally doesn't write about features that don't exist. Neither does Marketing.

Who does?

Your competitors and your community.

ESPECIALLY if the feature is coming soon, would you rather LLMs regurgitate your competitor saying "[product] doesn't have [feature], but we do!" or your Ideas Forum saying "[feature] is coming soon!"?

Even if it's not coming soon, wouldn't you rather people come vote for it and give you data rather than go explore a competitor's site?

With the long-form, long-tail queries of the LLM era, communities are an essential tool for filling the AEO gap.

Does anyone know if the Olympic Village employs community managers, or even if there's an online community component for the atheletes?

I've been watching this year's Olympics and so curious if anyone knows anything about the behind-the-scenes—

1. Does the Olympic Village have community guidelines/codes of conduct? 
2. Are all the Olympians in some kind of Slack workspace right now coordinating after-even drinks/chocolate-muffin intel? 
3. Are there any official social events/programming being run for the Olympians? 

I welcome inside knowledge and speculation on this thread 😂

I've never been so happy to have had to re-do something. 

I hope Bri Leever doesn't mind me sharing this story, but we actually had to record my episode of her new podcast Dear Bri TWICE because technology hates us...or so I thought. 

Turns out technology actually loves us and was looking out for us, because when we did our re-record, we had SO MUCH FUN and ended up making an episode for you that I'm somehow even more excited to be sharing with you. 

That episode is live today—Bri and I talk all things platform selection, creeping on Nextdoor when you live in a small town, and onboarding strategies. I think it's equal parts tactical & fun, and I hope you'll listen: 

https://lnkd.in/eWSTdjBG

Leading a challenge in my community has been the most enjoyable aspect of my work this year. 

In my work, I do a fair amount of one-off consultations where I'm meeting with a community builder for an hour to weigh in on strategy. I really enjoy those calls, but I don't always get to find out what happened! 

Did they launch their community in time for their big event? Did they solve their engagement challenges? Did they implement their onboarding flow? 🤷‍♀️ 

But, in my challenge, I get to see the same community builders week after week as they progress through, build upon, and implement their strategy work. 

It's *so* gratifying to get to say, "building on what you worked on last week..." 

And, it's even more gratifying to hear from folks like Avely Pütsep that they're enjoying this process as much as I am. The members make the experience and I'm lucky to have the ones I do. 

As the group I'm working with is coming to a close, I'm starting to think about launching another cohort of my community strategy challenge. 

I'd like to keep the group small—my current members have share that the intimacy of the experience is part of what's making it feel valuable, and I want to repeat that. 

I'd love to find 5-10 community builders who want to either build from scratch or transform their community strategy in the span of just under two months. 

Anyone who wants to hone their community strategy is welcome, but I have a feeling this'll be the best fit for: 

- Community entrepreneurs/founder community builders: i.e., if you run a business that community is central to, like a membership or educational business 
- Early->mid career community managers who work for early->growth stage startups 

If that sounds like you, I'd love to chat with you more—leave a comment here.  

I'm thinking of kicking off this next cohort in late June, and would love to meet some of the folks who are interested so that as I make updates, I can build it specifically for you ✨

If I could give community professionals trying to launch new programs one tip, it would be this:

You should be running STUPIDLY simple tests.

I see SO many community teams spend months building highly-polished programs, only to discover it's not interesting enough to their community to make a difference.

Your members don't care about polish, they care about value. And it can be HARD to cut through the noise to create real value. Which is why lots of simple tests are a much better approach than one big roll of the dice.

Think your community might benefit from a conference? Host ONE EVENT. See if people show up and stick around.

Want to build a mentorship program? Connect TWO PEOPLE. See if it makes a difference for them.

Think a jobs board might be useful? Do ONE POST rounding up jobs. See if anyone reacts.

Have an idea for a new group? Host ONE MEETUP. See if anyone comes.

Experiments should be THE simplest, most boiled-down version of what you want to launch. Anything else is betting too much money on a roll of the dice.

I hear LinkedIn likes pictures now, so here's one of my supervising this morning while my dog Cheez wrote my newsletter for the week. 

Training my dog to write my newsletter for me has been a GAME CHANGER in helping me free up some of my time so I can focus more on my 1:1 work with my clients.

Given the fact that he appears to be mostly sleeping or chewing on his squishy toys most of the time, turns out he's surprisingly knowledgeable about the community industry. 

(And he can type?!?!) 

Cheez wrote this week about what community builders need to understand about SSO, and how to think about whether you need it for your community project. I know, kinda technical for a dog?! 

Read here: 

https://lnkd.in/e4WTGSnc

Don't worry, this isn't going to be another post asking you if community and marketing are the same 😂 

I think we can close the case on that one—community and marketing aren't the same, but they are related, and learning about one can support your work in the other. 

That's why I finally wrote a blog I've been wanting to write for some time now: it's a sort of Marketing 101 for Community Builders. 

It goes over super-foundational concepts in marketing—lead generation, funnels, the mechanics of content marketing, referral/affiliate marketing and puts them in a community context. 

Whether you're a community builder working with a big brand or a community entrepreneur, I'm convinced brushing up on these concepts can help you create stronger community strategies *and* make a better business case for your work. 

You can check out the post here: 

https://lnkd.in/ehtbkSkF

Community builders—what other concepts in marketing have been absolutely essential to doing your community work effectively?

Community ROI Template Walkthrough

Watch me crunch numbers 🏋‍♂️ 🔢 

I shared with y'all last week that I built a new blog post & plug-n-play (ish) template "calculator" on proving community ROI. 

But even though I built the template to be as easy-to-use as possible—

The input fields are color-coded 💛 , the output fields have pre-loaded, linked formulas so you just have to fill in your data and it spits out results—

Any time we're looking at a biiiiiiig spreadsheet 📊, we're in brain-melting territory 😰. 

To take us out of brain-melting territory and back onto solid ground, I put together a video walkthrough where I use the ROI calculator on a made-up (but highly plausible) example of a community team proving ROI. 

I input numbers on: 
👤 Headcount
⬇ Churn 
🎣 Lead generation
🤑 Product cost

...And more to spit out a Return on Investment figure, attempting to explain the formulas along the way.  

Watch me and my fledgling team of three make well over a million dollars through the power of churn reduction and content leads, I mean, ahem, the power of community. 💪 

What should we spend the money on? 🤣 

https://lnkd.in/ehV8DGZp

Recently one of my clients shared with me Liz Wilcox's newsletter on email marketing. 

Liz's stuff really encouraged me to not shy away from incorporating my real personality into my newsletter. 

One of the ways Liz does that that I felt inspired by is through super-casual video. Oftentimes, I want to incorporate video into my work, but I don't because it's just too much dang effort. 

Liz's stuff is a great reminder that you don't have to put on a different outfit, set up a ring light, or do any fancy editing to make video a valuable format for your audience. 

I took Liz's cue and made a super-casual, off-the-cuff video for my newsletter this week, talking through the answers to three common engagement questions I've been asked at various events over the past few weeks. 

You can check it out here: https://lnkd.in/g8rJP74h 

Thank you, Liz, and thank you to my client who shared her work with me!

Wow. Incredibly honored to have received this message from one of my community strategy challenge participants, Avely Pütsep, after our group coaching call today. 

I've been having the best time with the group of community builders who have joined in the challenge, and there is no better feeling than seeing that that excitement is translating to the folks that are taking part, too. 

Sharing with Avely's permission 🧡 — she made my week!

Hey community pals—I'm working on writing up a biiiiiig blog post (& corresponding plug 'n play-ish template) on measuring community ROI. 

My basic POV on measuring community ROI is that since every company's financial priorities (and community instance) vary significantly, no two measurement schemes are going to look exactly alike. 

But, I also think that most companies are drawing from a standard-ish menu of options, and that if you learn that menu & the common methodologies, you can apply them to almost any instance. 

Basically: finite components, huge number of output combinations. 

I'm aiming to publish this post next week—but before I do that, I wanted to ask my network: 

⁉ What questions do you have about measuring community ROI that you'd like me to address in this post? 

Or, 

📚 What stories can you tell me about how you've measured ROI in the past that might be great examples to bolster this work? 

Thanks so much for whatever you can share—we make great content together 💪

Y'all I just sent out my 100th newsletter 🤯 

Having this thing has been a wild ride and I've definitely done a lot of it 'wrong.' 

For one thing, I've been wildly inconsistent with it—there have been times I've sent it out every week and times I've gone months between an issue. 

But, I've now been at it for FOUR YEARS, so I thought I'd share my takeaways anyways: 

1. If you're someone who develops thoughts by writing, a newsletter is your friend. Doesn't matter how many people are reading it—having an outlet & routine to think through writing is invaluable. 

2. You don't have to be doing it for some business reason to get something out of a newsletter. I started mine when I was employed full-time, now it's a big part of my consulting business, and I suspect I'll still have it in some version when I'm full-time again. It's shifted & grown with me, and it will continue to. 

3. It's not that serious. People like puns. People like when you show up to your newsletter, or whatever you're putting out there, as your real self. Don't overthink it, especially if that stops you from doing it. 

4. It's a medium to try new things. I've lately been using my newsletter as a way to test out short-form video. I literally just downloaded Loom for the first time today. Keep testing stuff. 

5. Above all, the community principle of *at least* giving as much as you take really applies to newsletters. I will always focus on value first before I use my newsletter as a sales channel, and I think this is what has kept my open rates high this whole time (they consistently hover around 45%). 

If you're one of my subscribers, thank you for helping me get here! If you're not, I hope I'll see you some time in the next 100 issues 😂

community+marketing // mission-driven af // 6 years of slow-traveling the world

taking Noele Flowers’ community strategy course is 1 of the biggest things I’ve done for my community career 

I’ve been very hesitant taking a course as the last 2 marketing courses I took weren’t great and I was afraid of paying for something meh 

☕️ 
a Sunday learning: currently putting together user research through interviews & setting content+engagement+features strategy

(Ps: I don’t usually work at weekends and don’t vouch for it, but sometimes life’s crazy and you gotta do what you gotta do) 

it’s genuinely so interesting to learn in detail how another community builder approaches topics; putting together my previous know-how with the new methods, I’m learning A LOT 

#communitybuilding

Took a little break from the newsletter over the last few weeks, but I'm excited to be back!

In this week's letter, I share an exercise you can do in five minutes to connect your engagement goals to business goals—I call it: The Relentless "Why?!"

For the nerds: I also share a picture of the first garden zucchini of the season I harvested THIS MORNING! 

Read it here: https://lnkd.in/eMUMegJ8

The Complete Guide to Proving the ROI of your Online Community

I spent the last couple of weeks melting my brain so you don't have to 😅 

I give you, my new blog post: 

The Complete Guide to Proving the ROI of your Online Community 🎉 

This is probably the post on my blog I feel most proud of—it's super comprehensive and I hope it'll be just as helpful. It's a long read, but it had to be in order to cover: 

🔨 Three tried-and-true building blocks for the most common ways professional community builders measure business impact 

🤝 An approach to understanding which measurement cases are a fit for your business, and tips on approaching data infrastructure 

💲 An exploration of how impacts might stack up against losses by understanding the components of a typical community budget 

🗣 Examples and quotes from professional community builders using these strategies today (h/t to Scott Baldwin and Rachael Silvano for being game to chat about this)

If you're someone who knows how to talk about the impact your community has on your members, but struggles to translate that into dollars and cents to prove why your business should continue investing, don't skip this one. Read it here: 

https://lnkd.in/eghqk2xM

ANNNND...I'm also super pumped to share that I built a corresponding paid template for those who want to take this even further: 

It's a responsive Community ROI Calculator. (!!!!) 

I'm a spreadsheet girlie who uses responsive spreadsheet formulas for every area of my life (you DO NOT want to see my personal monthly budget template), and I love using tools like this at work, too. 

But, I know from lots of my clients and peers that spreadsheets and number crunching make their brain go all fuzzy. So, I built a tool that you can input your biz numbers into and it'll spit out an ROI calculation for you. 

I love this thing so much not just because it's a time-saver, but because it gives you building blocks that demonstrate some of the most common community ROI calculations, that you can still adapt to your use case. 

Plus, this template has a whole section that lets you input your community budget, complete with the most common spending categories for community projects. 

PLUS plus, I think this template would be a great tool for someone who doesn't yet have "real" numbers to input who wants to model out potential scenarios with the biggest impact, or a team leader who's trying to set targets or make a case for headcount. 

I'm really excited to share this all with you, and I hope you're just as excited to receive it. 

Hit me up in the comments if you have questions ✌

Don't @ me but I'm not that interested in the eclipse 🙈 😎 

I am, however, very interested in collective experiences, and the fact that people are so clearly *very hungry to share an experience together* fascinates me.

How do you think about expected uptake rates when you launch a new community? 

A lot of my clients & peers—and myself!—are interested in benchmarks to help us understand what to expect from a community launch. 

In other words, if I invite x number of people to join my community, how many can I expect to take me up on that invite? 

Unfortunately, benchmarks can be hard to find—companies don't like to release their data to their competition or even their peers. 

But even when we can get this data, can we trust it? I tend to think that since each community project is so different from the next, it's hard to understand how "benchmarks" may or may not translate.

But, all that hemming and hawing out of the way—I actually think you can still make decent guesses about community invite > uptake rates if you start from good proxy data, and then ask some critical questions about your project. 

The "proxy data" I find useful: 

📧  Conversion rates on digital email campaigns to paid products average around 2% 
🎉 Conversion rates on live events from digital campaigns average around 12% 

But wait—there's a huge difference between 2% and 12%, and online communities are different, so how is this helpful? 

Because it gives us a good ballpark to understand how people convert online—and in my experience, community isn't so drastically different that we should expect to be delivering results that are 2, 3, 4, or 5x as good as event or digital product conversions. 

So, this proxy data gives us a gut check: we shouldn't expect that half the people we invite to our community will join—instead, we should expect to be seeing rates in the single digits or low teens. 

How do we qualify that further and get closer to an estimate? Here's what I would consider: 

 🥇 What's the quality of the channels I have available to advertise my community? Am I using brand new channels, like paid ads that I haven't tested (low quality), or am I using well-established channels I've been consistently giving value to for a long time and am seeing good metrics on, like an email newsletter with good open rates and clickthrough rates (high quality)? Higher quality channels = better conversions. 

👩‍💻 How confident am I that my community offering is a good match for my audience? Have I created a product that's a good match for the persona I have access to talk to, or have I created something that's likely only a fit for a small subset of my audience? Have I done my due diligence to validate my community product and my marketing language? Stronger validation = higher conversions. 

🔧 What friction is required to convert? Do my members have to pay for my community, or be otherwise qualified? Do they have to go through a long onboarding survey? Higher friction = lower conversions. 

Community builders, does this align with how you currently think about estimating invite > uptake rates? What would you add?

Community Strategist | Discover which community platform is the best place to host your people and build it right the first [or second] time. Get my free platform comparison guide below!

I get asked about the Mighty Networks community platform a lot.

And while I'm not personally a big fan, I was pleasantly surprised by what I found in the education-centric Lifebook community, hosted on Mighty Networks. 

Join Noele Flowers, Tamanna Bavishi and I as we explore the member experience and discuss:
- the importance of making it OBVIOUS
-  the platform you pick matters
- how to prioritize connection, even for an education-centric design

Find it here: https://lnkd.in/g2hRDghG

Looking ahead at my April, I'm excited that I'm doing A LOT of speaking & workshops this month ✨ 

While I learned early in my community career that in-person events are Not My  Vibe (😅), facilitating & teaching online very much are, and I'm pumped for each and every one of these: 

🐎 On April 16th I'm giving a workshop on Community Content Calendars for The Community Roundtable 

🧡 On April 24th I'm giving a workshop on...you guessed it...Community Content Calendars! This time for my friends at Heartbeat

🔵 On April 25th I'm hosting a masterclass/AMA on community engagement with my friends at Circle

📅 All throughout the month, I'm giving weekly workshops & group coaching in my client community synced with my community strategy challenge on research & validation, community engagement, technology selection, and more ✨ 

I hope I'll see some of y'all at some of these events! 

What are you excited about this month?

Always such a pleasure to get to be a part of any content Bri Leever makes. 

Check out her most recent episode of her community dissection series where we talk about community architecture, Mighty Networks, engagement strategies, and more!

Templates | Noele Flowers

Heads up: I now sell templates on my website. 

https://lnkd.in/eJj-Wu_a

Late last year I launched an On-Demand Coaching program that includes video instruction, templates, coaching scenarios, and group coaching in a community setting. I've absolutely loved working with my clients there (if you're doing my challenge right now huge shoutout to you!) and am still excited to grow that program. 

But, I've also heard from some folks that they want just one little piece of that and not the whole thing. So, I decided to make all five of the templates from my On-Demand Coaching program available for a la carte purchase. 

You can now buy any of my templates on goal setting, research & validation, content & engagement, technology comparison, or launch & rollout. 

OR, you can buy them as a bundle and get a discount + all the templates I've ever made and ever will make for my blog in one place. 

Hope this is helpful for some of you!

What's a "pet theory" you have about community that you're convinced is true but isn't necessarily talked about? 

Mine is that I'm convinced people basically don't inherently see the value in community until *after* they feel it, so they don't make decisions based on the promise of future community. Instead, they make decisions based on the promise of tangible value and *then* community & connections become a stickiness factor that super-cedes that original decision. 

Life example: you don't really move somewhere because you think you might make friends there, but you might move somewhere where you already have friends OR avoid moving away from your friends. 

Online example: community members don't seem to often respond to "connection and networking" in marketing materials, but they will show up for a really good workshop and then stick around when they make friends. 

Tell me all your theories, and what you think of this one?

You should track engagement metrics to support your own decision making, but you (mostly) shouldn't share them with executives & leaders. 

Do you agree?

I unpack my stance more in this week's newsletter: 

https://lnkd.in/eabJkumQ

Community AMA with Noele Flowers—RSVP & Question Pre-Submit Form

Just for funsies—I'm doing an AMA tomorrow morning. 

I do a lot of what I lovingly call "tippity tapping" (typing) about community management but what I really love is *talking to people about it live.* 

I didn't have any events scheduled in the next couple of weeks so I decided to schedule one of my own—join me tomorrow (Thursday) at 10am EST for a super-casual (i.e.: bring coffee) AMA session on community strategy. 

RSVP here and I'll send you the link to join (you can also use this form to pre-submit questions if you can't join live but want the replay): 

https://lnkd.in/gms9NmZC

See y'all tomorrow!

📝 Should you start a forum for your online community? 

➕ Are forums and online communities the same thing? 

In today's blog post, I address these questions and present five reasons why you might NOT want to start a forum, even if you ARE starting an online community. 

https://lnkd.in/e8Q6NYxJ

5 Reasons You Shouldn't Launch a Forum for Your Online Community

Earlier this week, I shared a new post on my blog detailing some of the reasons why forums aren't always the best options for centering online communities around, even if we often *feel* like they're essential part of online community experiences. 

Today I want to deep dive on an example of that that's part of what inspired me to write the post. 

Recently I worked with a client who was trying to figure out a community strategy for an alumni program. The client felt that while the recurring event program they were running for their alumni was working well, the forum wasn't, and they were looking for strategies to increase activity in the forum. 

While there are of course tons of strategies you can use to increase engagement in forums (and I talk/write about them a lot!), I'm a fig fan in my work of "questioning the premise." 

So, instead of immediately brainstorming on forum engagement, I wanted to push back on the *why*—what would forum engagement yield, theoretically, and why did we think forum was the best option to yield those results? To figure that out, the client and I worked together to talk through the overall business objectives of the alumni program. 

The objectives of the program centered around: 

-Activating alumni to word-of-mouth marketing for future students (referrals)
-Keeping alumni engaged in the brand ecosystem for future course purchases (retention/repeat purchasing)

After identifying those, we found in our conversation that the recurring calls the client was already holding were very effective in accomplishing the stated objectives. 

Comparing the effort of expanding that call program, which was already succeeding, versus introducing and scaling a forum program, we felt the former was a more well-tested and lower-effort strategy to try first. 

I'm sharing this to illustrate a scenario in which digging into the why can help you really determine which community-building strategies are actually a fit for your project, rather than doing what so many community builders do accidentally: reproducing *other* community programs without questioning whether they're the right one for their use case. 

If you haven't checked out the post yet, it's here: https://lnkd.in/e8Q6NYxJ

Have you ever had a scenario where questioning the "why" changed your entire engagement strategy?

Exciting week next week—onboarding for my Zero -> Community Strategy in 7 Weeks Challenge starts Monday! 

That means this is your last chance to join the other community builders who are committing to building and presenting a comprehensive community strategy over the next two months in a supported, sequenced challenge. 

If you have ever considered working with me before, this is your sign. This challenge is by far the most valuable way I have ever offered for us to work together. For less than the cost of working with me for two 1:1 sessions, it includes: 

- My entire On-Demand Coaching library — video instruction and dozens of pages of templates across a wide range of community building topics
- Challenge-specific materials, including a strategy deck template 
- A sequenced, guided approach to completing and presenting your community strategy 
- Weekly group calls to help you stay on track and ask any questions 
- Your first quarter in my client community (includes bi-weekly group coaching calls even after the challenge ends) 

You do not want to miss this—the other folks already taking part in the challenge are incredible. 

This challenge is perfect for entrepreneurs trying to launch their first community, or more seasoned community builders who would like a more structured approach to strategy. Some challengers have gotten this approved through professional development budgets, which I would highly recommend if you have that available.

I'll post a link for you to learn more & enroll in the top comment, and if you have any questions I encourage you to comment them here or shoot me over a DM. 

Looking forward to getting to know some of you more closely as a part of this!

Just wrapped up a tutorial session with the Heartbeat community and I have to give a special shoutout to all the attendees and to Murtaza Bambot ❤️. 

Murtaza is easily one of my favorite founders in the community space—it's rare to see a CEO who leads with as much authenticity and presence as he does. One of my favorite things about sending my newsletter is getting replies from Murtaza. 

He also did a really fun facilitation technique I'll definitely be stealing, which he called a "waterfall"—at the end of the session, he asked everyone to type in the chat their biggest takeaway from the session but NOT HIT SEND YET, and then had everyone click send at the same time so the chat was flooded with responses. 

This was so fun as the guest—big ups to you, Murtaza, and to everyone who joined us. Looking forward to the next one!

Y'all this is the very last day you can get the early bird special on my ✨ community strategy challenge ✨  that's running from March 18-end of April. 

ICYMI, this challenge is for you if: 

-You have EVER considered working with me. Through the challenge you get access to all my best resources I use with my clients, my client community, structured accountability, and check-in calls with me to help you get un-stuck. By far the most valuable way I've ever offered for us to work together. 
-You need to put together a comprehensive community strategy in a short period of time and you could use a kick in the pants to get going
-You've done community strategy before but could use an alternate structure/lens to approach it from 

If you enroll now, you get: 
-Access to my client community & coaching calls right away 
-Access to my five-part on-demand program (which you'll keep forever, even after the challenge is over) 
-Weekly support to complete the challenge structure through the community & extra video calls 

Here's what the challenge covers week to week: 
Week 1: Welcome & onboarding
Week 2: Community goal-setting, business alignment/model, pricing/ROI
Week 3: Research & validation
Week 4: Engagement, content, and community value proposition
Week 5: Technology selection
Week 6: Launch & rollout planning
Week 7: Peer strategy presentations 

If this is for you, shoot me a DM and I'll get you the discount code. 
If this is for someone you know, tag them. 

Hope to get to know many of you better of the course of this thing!

Hey Community Builders — mark your calendars for March 18th, I'm running a challenge 🚀 

I'm calling this the "Zero to Community Strategy in 7 Weeks Challenge." 

TL;DR: 
- Over the course of 7 weeks you'll be guided through my entire On-Demand Coaching program in a community of supportive peers. We focus on goal setting & biz alignment, validation, engagement, technology, launches, and more 
- Each week you'll be prompted to complete a module, share your work for peer feedback, and attend office hours calls where you can ask questions about the content
- The challenge will culminate in peer - peer strategy presentations 

If you join, you get access to my On Demand Coaching Core Bundle for life (so even if you don't complete the challenge, you still get access), plus your first quarter in my membership community which includes biweekly coaching calls. So, if you join now you'll get to do the whole challenge + participate in the community through mid May. 

I just sent out an email to my newsletter with all the details + an early bird discount code that's active til March 1st. If you want in on that and you're not on my newsletter, leave me a comment here and I'll shoot you over the code in a message. 

If you're an entrepreneur or a pro community builder and have been needing a push + some accountability to take action, this is it. Hope to get to know many of you better over the course of the challenge!

The more I think about it, the more I'm convinced: if the way you express your community goals doesn't take into account *both* the business impact and the member impact, those goals aren't going to be very effective. 

It often seems like community builders have a bias toward one or the other—it's either "my members are all that matters, why am I being asked to prove business impact?" OR "I'll do whatever's best for my business and my members are chopped liver" (*cough* glassdoor *cough*). 

We need both. 
We need both. 
We need BOTH.

New Client—1:1 Coaching Session Request Form

Hey friends—recently I was chatting with Bri Leever and she said she felt like I *wasn't promoting myself enough.* 

This shocked me because as someone who doesn't always feel super comfortable marketing myself, the level of self promotion I *do* do can feel uncomfortable. 

Interestingly, I feel that I often attract clients who have this same personality type—they're really interested in creating value for their audience, but when it comes to the hard sell, that part doesn't come naturally. (Psst—if you're reading this, I'm curious if this resonates!) 

To those clients, I usually tell them to not worry so much about seeming annoying to their audience. When I was a teacher it was often said that you have to say something at least three times for your students to learn it, and I think being an entrepreneur is largely the same—you have to do a lot of repeating, and that's ok. 

As community builders, we should get comfortable with the fact that we're largely being ignored—our members are busy and they don't have time to read everything we say. So, we should repeat, repeat, repeat. 

Now, if you've gotten this far, I'm going to take Bri's advice and repeat myself again, because I am running a January special on my 1:1 community coaching services that I think a lot of you might not know about. 

As a 1:1 coach, I work with clients in hour-long blocks to help them with the most important aspects of their community strategies. I work with clients on things like: 
- Fine tuning community architecture
- Creating catered engagement plans
- Pricing and value propositions
- Online course development in a community environment 

If it's an aspect of community strategy, I work on it. 

Most of my clients are community builders who are either entrepreneurs selling directly monetized communities, or early-career community managers working for brands and looking for some expert support. I've been building communities for almost a decade and I'm really proud of the outcomes my clients are able to reach with me. They've launched, monetized, and grown amazing programs (and they're all incredibly nice people, very luckily for me!) 

If you've been thinking about working with a coach, now is the time to do it. 

My January special lets you book your first call with me at a reduced rate (and the call doesn't have to actually happen in January, you just have to complete your booking in January). 

Plus, getting on my "existing client list" pays off—it gets you access to my existing client package sales I run a couple of times a year, plus discounts on joining my membership community and accessing my online courses. 

Convinced? Shoot me a DM to get started, or fill in my new client form here and mention my January special: 

https://lnkd.in/eUqgRGCX

Hoping to get to work more closely with many of you in 2024!

I see a lot of discussion here on LinkedIn about why community =/= marketing. 

And I agree. Of course community and marketing aren't "the same"—it's almost always the case that one word doesn't "exactly equal" a completely different word (except if we're talking about use and utilize 😂 ). 

But, a lot of times I find this conversation to be incredibly overly simplistic. What exactly do we mean by "marketing" when we push back on this equivalence? Are we talking about new user acquisition through paid ads? Are we talking about a brand's share of voice? Are we talking about organic content marketing? Are we talking about churn reduction? 

Ultimately, I don't think we can have a very meaningful conversation about the differences between "community" and "marketing" as umbrella terms without  specificity, and I think that specificity comes from the community profession actually embracing growing our knowledge of marketing and the connective tissue between community and marketing. 

At the end of the day, even if there isn't total equivalence between these two things, many many many community programs serve similar metrics and objectives and even rely on similar mechanics as certain marketing strategies. 

In fact, I think you'd be sort of hard pressed to find a community that's delivering tangible business impact that is wholly *unrelated* to marketing. 

Where should we start? To me, building a solid understanding of the basic mechanics of lead generation has been indispensable to my career in community. I talk more about why on this week's newsletter: 

https://lnkd.in/g4ZB-mYQ

And if you're a community builder, I'd love to hear from you—how has tapping into standard marketing concept and strategies supported your work in community?

Reminder: most of the time, your community members are ignoring you. 

This should feel comforting 😂 

Why? 

I hear from a lot of my clients that they have awesome engagement plans created but they're afraid to execute them because they're afraid they're "annoying" their community members. 

And while the risk of community managers dominating the conversation is real, I always find it helpful to remember that not everything I say as a community manager is actually being paid attention to. 

Community members are busy people and they're not opening every email you send or clicking on every engagement post you create. Most of the things you say they aren't aware you've said at all. 

So go ahead: repeat, repeat, repeat.

Before you get bummed out that your forum isn't getting enough engagement—

Are your *non-forum* peer-to-peer connection points producing the business outcomes you're looking for already? 

This week in my membership community's group coaching call, this idea came up and I wanted to share it here more broadly. 

I often hear community builders saying some version of: "Nobody's posting in my forum. Engagement is so bad. My members only show up to the live events—how can I get them to talk in the forum?"

Baked into this question is the assumption that a buzzing forum = a healthy, impactful community—and that you can't have the latter without the former. But, sometimes we arrive at a different conclusion if we start not from judging the outcomes we assume we'll see but from really backing up to the business goals community is there to achieve, and evaluating success and making decisions based solely on them. 

For example, assume you have a totally dead feeling forum, but your weekly office hours calls are popping off—a quarter of your members show up every single time and have really rich conversations. Say your business goals for community look something like this: 

🎯 Engaged community members should churn from overall product experience x% less frequently than non-engaged or non members, and should have a higher lifetime value
🎯 The community should yield actionable insights about product and marketing direction, and help the business better support customers 

Now, say when you evaluate those who show up at your office hour calls vs those that don't, you find that you are producing your desired business outcomes with those calls. That's a success—even if it feels like it's "missing" something that you assume must be part of an engaged community. 

Now, of course you may hypothesize that having an engaged forum could be a way to build on that success, and maybe there are aspects to a forum that you think are worth investing in on top of what's already working. 

But, in 2024 I want to really see community builders recognizing that community programs are built on more than just forums, and that we should always be interrogating *why* we're prioritizing certain building blocks over others. 

Do you agree with this? Have you ever made the decision to "de-center" your forum from your community experience because of what your data was telling you?

This week on the newsletter: 

An exercise I do with my clients to help them start getting not just *more,* but higher-quality community engagements. 

Plus, for some reason, a pun about Keira Knightley?! 

Check it out here: 

https://lnkd.in/eYpD4xUA

I've been talking a lot about de-centering forums lately. 

This is because I personally run a new-ish and really small community where forum engagement isn't really the main deal—the vast majority of engagement happens in live calls, and the forum serves as a space for resource sharing and reminders in between. 

This really mirrors the way many many of my clients community engagement plays out when their communities are small and just getting started. 

But, even if you're not focussed solely on forum right now, it's important not to throw the baby out with the bathwater, because forum engagement can become really critical to communities in the process of scaling. 

So, this week in my client community we're theming our group coaching call around forum engagement. That call's on Wednesday, so in advance of that I wanted to put out the call to my LinkedIn network—

1. What questions do you have about forum engagement right now? 
2. What are you struggling with in creating forum engagement? 
3. What is working for you to create forum engagement? 

I'd love to hear from you so I can bring some questions from the larger industry into my community, and I'll double back with any insights our conversation yields 😄

Real talk: have you ever felt embarrassed when you realized someone you know in your "real life," outside of a "business context," follows you on LinkedIn? 

(Related: have you ever felt embarrassed when one of your friends overheard you on a Zoom call using your "business voice"?) 

I've been having lots of conversations lately—with both professional contacts and with personal friends—about this itchiness many of us feel about what my former-coworker-turned-real-life-bestie Haleigh Fullilove recently called "The Briefcase App." 💼 

What's this all about? I suspect it's different for every person, but I also suspect this feeling might be more widespread than we realize, and so I want to talk about some of my thoughts on this— 

🤝 Authenticity: I often struggle with how different I think I am in my "regular life" vs. my "business life." Compartmentalization can be a good thing that has helped me set boundaries around work, but it can also lead to less good stuff. This can show up especially on LinkedIn because I simply do not write in the same way in these settings, and it can feel as a result like I'm being "inauthentic" here. And at the same time, a devision in how and what we talk about in business settings sometimes feels appropriate. 

💌 Values: There is not always a 100% overlap between my personal values and my working values. In particular: my personal values are not aligned with the system of American capitalism as a whole. But, that's not a system I invented or have the ability to step out of completely. Within it, I still care about my work, enjoy talking about it, and make values-driven decisions about how I support myself, my coworkers, and my clients. But, that friction is sometimes still felt. 

🌈 Identities: I hear again and again that "it's business, it's not personal"—but to me, this has always been hard to swallow. This isn't Severance—I take my memories and feelings with me between work & home! Because of that, it feels essential, but often difficult, to bring the entirety of my identity through every context of my life. For me, I feel that in how I show up as a queer & gender-non-conforming person at work. 

There's no answer or "aha" to any of these—but it's my hope they feel resonant to some of you who may also be quietly struggling with how to show up here on LinkedIn, even if you enjoy talking about your work. 

Why'd I choose to share about this here on LinkedIn rather than in a private conversation with my "real life friends"? 

Because I think a lot of us are struggling with this here, and I've found again and again in my career that "saying the quiet part out loud" helps me make stronger connections in an area of my life that I spend about a third of my time. When I can do that, I do better in my work and I do better personally. 

And—many, many of my closest friends in "real life" are people I met at work. Taking applications (& looking forward to hearing your thoughts on all of this!) in the comments 🤣

Gotta give a shoutout to DeMario Bell. I had the pleasure of speaking with him today on a panel hosted by LikeMinds on community use cases that drive business impact and holy cow was I lucky to share the stage with him. 

One of the kernels of wisdom he shared with all of us that I have to boost here (paraphrasing, sorry!)—"don't survey for things you aren't able to deliver on."

There were seemingly endless nuggets of gold in what he shared today but this one really stuck with me because of how it acknowledges that community is about creating win/win situations. We can only ask for what we're willing to give, and vice versa.

If you are DeMario's coworker I am officially jealous 😂 

And, always just a pleasure to be reminded of how many smart and awesome people work in the community industry. Thank you to the LikeMinds team for introducing me to one of them!

I love running challenges in communities—they used to be one of my favorite community x content things to run when I was at Teachable. 

I think people mostly think if "challenges" as an exercise in framing—if you call something a "challenge" you're tapping into folks desire for accountability, "streak" completion, and even some (hopefully friendly!) competitiveness. 

But, in my mind challenges do more than just that—here are some of the reasons I love them:  
🎢 They give some structure/accountability to help your members habituate in a new space. Challenges are a great “showstopper” to launch a new community with, almost like a way to structure onboarding so it feels like content. 
🔭 They can give you the chance to test out an online course before or as you build it—you can use them to sort of “drip” your planned content to your community before you immortalize it in an online course format
🏃‍♀️ Conversely, if you already have an online course that’s not getting completed, they can be a way to help pace people through that process in a community setting 

Structurally, challenges are not very different from cohort-based-courses, so if you’ve never designed or run one before, my curriculum design for community builders blog post could be your friend (I’ll link it in the first comment). Fun fact that post has a template download in it that is exactly what I used to design my online course that lives inside my client community 😁 

To get meta, if you’re looking to see a challenge in action and have been wanting to launch a new community or community strategy, I also want to invite you to join me in my “Zero to Community Strategy in Seven Weeks Challenge” which kicks off March 18th. 

I’ll pop a link in the comments with more info on that as well, but basically it’s just like it sounds—the challenge will walk you through a course that covers community x business alignment, research & validation, engagement, technology selection, and launch in just over two months. 

I hope you’ll join in, and to get *reeeeealllly* meta maybe you’ll plan to launch your community with a challenge as part of the strategy you make in my challenge 😅 

Whether you join or not though, I'm curious—do you use challenges as part of your community engagement strategy?