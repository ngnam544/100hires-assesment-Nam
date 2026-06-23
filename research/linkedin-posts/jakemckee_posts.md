# Recent Posts for jakemckee

Business Analyst/ Product Owner

AI Engineer | Building Production LLM Application | RAG & Fine-Tuning

AI Engineer @SmartGift Solution

Talent Connector | IT & Non-IT Recruitment | 3 Years Experience | Growth-Oriented

Backend Engineer @ cigro | Typescript Developer | Golang Developer

Principal AD/ADAS & AI Architect

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

Secondhand insights don’t lead to great products.

Quick reminder: The PDMA - Product Development and Management Association AI Threshold Project survey is still open and we're collecting some interesting data. 

If you work in product/innovation, your input helps shape what we share back with the community. It only takes about 5 minutes, and your input will feed three things we're sharing back with the product community:

* A Survey Report with the full data on how product teams are using AI today 

* An Interview Series digging deeper into what's working and what isn't  with AI for product/innovation teams

* The Field Report pulling it all together into something teams can actually use

Join in here: https://jakemckee.com/pdma 

And huge thanks for the support! I think we're creating something really cool that will be beneficial to anyone working in product/innovation.

This podcast interview discussion was fantastic. I had a lot of fun with it… And what a great way to start Monday morning. It just dropped so check it out!

I met this week's podcast guest, Terry Miesle through scale modeling. We were both into the hobby, and I learned he's a Master Flavorist by trade as an accident. Terry has spent thirty five years building the flavors you taste in meats, snacks, and dairy.

I figured the job was mostly lab work, smelling strips and matching samples until something tastes right. Then he told me the lab part is the easy part. The hard part is the conversation.

That didn't surprise me as much as our conversation about his work. Mainly because what he describes about trying to align teams, understand clients and customers through conversation, and the creation of shared language is what I hear from product/innovation teams every day in my own work.

The new episode of the Conversation Lab Podcast is live and I really hope you check this one out. It's fascinating!

PS: If you are looking for more great content, check out the full podcast, I have a bunch of great conversations and explorations ready to download.

 https://lnkd.in/dpYYF3SB

Earlier this week, Jake McKee joined Gradual for Context First: Beyond Secondhand Insights: The Customer Conversation Compass Framework.

The conversation focused on a problem many teams run into during customer listening: it’s possible to hear from customers often and still lose the context that would help teams make better decisions.

That can happen when conversations are too broad, notes are over-summarized, or the customer’s language gets translated too quickly into internal categories.

In the recap, we pulled together the most useful takeaways from the session.

Read the recap here: https://lnkd.in/gZSKjenU

CMX Summit is tomorrow! Since I can't be there, I wanted to offer something useful to those of you who are.

As someone who thinks about conversation for a living and still finds it genuinely hard to sustain at a two-day event, I have spent a lot of time thinking out what works to keep energy high and conversations interesting/valuable. 

So I created a free guide, as much for myself as for y'all.

The Conference Survival Guide has 26 specific moves covering every stage of a conference conversation. Before you arrive. Starting the conversation. Staying in it. Getting out cleanly. And capturing what you actually heard before it disappears. It's a living document, and I'll be adding to in the weeks to come.

Let me know what you think!

https://lnkd.in/gscev89C 

#CMXSummit #CommunityBuilders #ConversationCompass

Years ago I had dinner at Eleven Madison Park. Easily the best meal of my life.
But the thing I still talk about, years later, isn't the food.

It's what happened when I made a throwaway joke at the end of the night.
The staff caught it. And what they did next taught me something I now teach product teams about customer conversations.

I tell the whole story in this week's episode of the Conversation Lab Podcast, and break down why most product teams miss these moments on customer calls, even when they're sitting right in front of them.

Listen here: https://lnkd.in/dpYYF3SB 
˘

If you've been following me for a while, you've probably heard me talk about one of my main hobbies: scale modeling. I build small versions of big thi

Scaffolding: Why struggle is not part of belonging or learning

Researchers figured out in the 1970s that the best mentors and teachers don't just hand over answers or (even worse) make you "earn" them. We've all felt that uneasy response when we're trying to gain new knowledge and someone who knows more than we do thinks that because they had to struggle to learn it, we should have to struggle too. 

Scaffolding is the idea that good mentors and teachers meet people exactly where they are and give them just enough to take the next step. Not everything, not nothing... just enough. 

It sounds simple, but it's actually quite difficult. Especially since most of us default to one of the two wrong options without even realizing it: 

We either dump everything we know on someone who asked a simple question. Or we brush them off with "you'll figure it out" and call it tough love. 

The gap between those two responses is where belonging and connection either gets built or gets broken. And most of us are doing more damage there than we realize.

My latest newsletter article goes into what scaffolding actually is, why it's important, and what we can do to learn this incredible skill.

Someone came up to Josh Zerkel after a community event he ran and told him he had the easiest job in the company. All he did was throw parties.

He had been up since 6am. He spent weeks planning. He thought through every single thing that could go wrong so none of it would.

This is the community problem in one sentence. The work looks effortless when it's done right, so people assume it is effortless. And then you spend your time defending how you work instead of talking about what it produces.

Josh's new book, The Community Code, is about getting out of that trap. Check out the latest episode of the Conversation Lab podcast for some fascinating insights from Josh!

https://lnkd.in/dpYYF3SB

Next week I’m dropping two new podcast episodes and at lease my one newsletter article. In the meantime, I thought I’d reshare the article I written about Conversation Architecture, the second pillar of the Conversation Compass Framework. 

In case you need something to read this weekend, check it out!

I want you to take a deep breath, clear your mind, and put yourself into the mindset of the parent I'm about to tell you about. The mental health prog

Introducing Conversation Architecture

Most product teams have a conversation problem. They only talk to customers, if they talk to customers much at all, when something breaks or when a launch is coming. Or worst case...when someone upstairs asks why the numbers are off. Then it's a scramble to book some calls or spin up a quick turn voice of the customer project.

That's not a conversation practice; it's a fire drill.

Conversation Architecture is about building the system so customer conversations happen consistently, programmatically, strategically. My latest newsletter article goes into detail on what Conversation Architecture is and how to properly think about it. I even bring in a story about one parent's experience, in the midst of crisis, of Conversation Architecture gone really wrong.

Huge thanks to the Trevor Greenberg, PMP 🥓 for inviting me on his show, The Disgruntled PM Podcast. It was a great conversation. Check out the full interview!

Customer Conversation Compass

A quick reminder: The AI Threshold Project survey is open, and I’d love your input.

I’m working with PDMA’s kHUB team to better understand what product and innovation leaders are actually experiencing with AI right now.

The survey takes about 5 minutes, and the results will help shape a public report, interview series, and field report published through PDMA’s kHUB.

If you work in product, innovation, strategy, research, customer experience, or AI-adjacent work, your perspective would be incredibly useful. Check out the link here: 

https://jakemckee.com/pdma

Thanks in advance. This only works if the community weighs in!

The Disgruntled PM Podcast

The latest episode of The Disgruntled PM Podcast is available with guest Jake McKee, and it’s a guide to having a meaning conversation 

Jake McKee joins the show to explain why secondhand insights are destroying your roadmap and the actual mechanics of conversation design

Jake McKee discusses that building genuine connection is the key to uncovering real insights, not simply sending out surveys and hoping for the best data to just show up

Jake McKee’s background includes:
☑️ Pioneer of the adult fan community strategy for LEGO
☑️ Former community builder for global brands like Apple and EA Games
☑️ CEO of Community5 and founder of Jake McKee Consulting

Reasons to listen:
✅ Learn to stop interrogating users with scripts and let genuine curiosity drive your interviews
✅ Construct a conversational architecture that builds human connection before extracting data
✅ There is a lot more to a conversation that just waiting for your turn to speak, Jake explains some of it

Connect with Jake:
LinkedIn: https://lnkd.in/eQJryVuW
Website: https://jakemckee.com
Podcast: jakemckee.com/podcast
Conversation Lab: https://lnkd.in/eV_vCvH3

Like, Follow, and Subscribe  
 
LinkedIn Show Page:https://lnkd.in/gSCSGzwZ
Instagram: https://lnkd.in/eE3zsR47
📺YouTube: https://lnkd.in/e3s8UKnv
🎙️Spotify:  https://lnkd.in/geDJ-JNV  
🎙️Apple Podcasts: https://lnkd.in/gJ_rMm_z
💵 Patreon: https://lnkd.in/giZgz5zt

I've been running Conversation Lab for almost 8 years now, every single month, and I realized I haven't properly introduced it in a long time. Let me (re)introduce you to Conversation Lab.

Once a month, I bring together 5 wicked smart people for a two-hour virtual conversation. No slides, no agenda, no speaker, no pitches. Just a small, curated group of smart people from product, community, support, and CX who want to talk openly about their work and their challenges. Even across industries, what we need and what we’re dealing with is remarkably similar, but hearing from others with different perspectives is magical  

Before the session, I mail every attendee a box of snacks. This isn’t some random a bag of pretzels. It’s a curated collection of unique, interesting snacks chosen to pair well and spark conversation all by themselves. Think unexpected flavor combinations, things you wouldn't pick off a shelf on your own, little surprises that give you something to talk about while you're warming up. People look forward to the box as much as the session itself!

The structure for each session is simple: we go where we need to go based on who attends. Some sessions we spend the whole time on AI and what it means for how teams work. Other sessions it's product insights and customer communication.
The group is intentionally small and intentionally curated. Five people is the sweet spot. Intimate enough that everyone participates openly in a “cone of silence” environment.

If you've ever sat through a webinar wishing you could just have a conversation with the panelists rather than listening quietly to pre-built content, this event is perfect for you.

Applications are open for upcoming sessions at:

Https://https://lnkd.in/gd-HA9w8

Lee LeFever started Common Craft back in 2003 with a simple idea: technology only spreads as far as people can understand it. His "In Plain English" videos broke down everything from RSS to Twitter using paper cutouts, hand-drawn art, and a whiteboard that lived on the floor of his house. Millions of people watched, educators licensed them, and a whole genre of explainer videos grew up around what Lee was doing.

In this episode of the Conversation Lab Podcast, Lee and I go back about 20 years to talk about how it all started, why simple beat slick, and what it taught Lee about explanation as a real skill people can learn.

Subscribe to the podcast here: https://lnkd.in/dpYYF3SB

A few years back I was at dinner with a group at the fantastic Eleven Madison Park and I made a joke at the end of the meal that we did not need a coffee cart, we needed a whiskey cart.

A few minutes later, one rolled in. They had stripped down the coffee cart and rebuilt it with whiskeys and bourbons, just for us, on the spot. I still think about it. I even wrote a whole article about that night and what it taught me about knowing your customers. Check it out here: https://lnkd.in/gmFhJnYi

How do you make this kind of magic happen on purpose, over and over, instead of just getting lucky once?

That is what my newest Conversation Lab episode is about. It is the last pillar of the Customer Conversation Compass, and it is where most product teams fall apart. We hear our customers all the time, but turning that listening into action is the trick.

The episode is live at: https://lnkd.in/dpYYF3SB. Subscribe and listen! Next week we have a great interview coming up with UX and AI designer, Erik Summa!

The latest episode of The Conversation Lab Podcast has dropped! 

Episode 9 is an introduction to the third pillar of my Conversation Compass framework: Conversation Amplification. 

You had a great customer call. You wrote up notes. You sent them around your team/company. Annnnnndddd....nobody did anything with it.

That's an amplification problem. And it usually comes down to one of five blockers: visibility, authority, capacity, translation, or trust.

If a product/innovation team even notices they have an Amplification problem, they often try to tackle all 5 key blockers at once. Which is too much to take on all at once and nothing really changes. 

Episode 9 of the Conversation Lab podcast breaks down each blocker and shares some info about where to start. 

Check out the podcast at: jakemckee.com/podcast

If you're a product person, I'd love to hear your voice in my joint venture project with PDMA - Product Development and Management Association. The survey only takes a few minutes and if you're interested, you can volunteer to have a 1:1 interview as well. 

All results will be published and shared with those who asked to be included!

Will Guidara ran a restaurant called Eleven Madison Park. It went from average to the best restaurant in the world. Not because the food got dramatica

Listening is the easy part

Most product teams are decent listeners, but where they fall apart is turning what they heard into something that actually changes what (or how) they build. The insight sits in a document or gets a nod in a meeting. Or worse, gets cited six months later to justify a decision that was already made.

That is not traction. That is the appearance of traction.

In my latest Conversation Field Note, I use a story from Will Guidara's book "Unreasonable Hospitality" to talk about how you can turn listening into power.

Best part is that it involves a hot dog, a silver platter, and the best restaurant in the world. Read with caution: you are going to want to go out to eat after this read.

My buddy Joshua Zerkel, CPO invited me to have a great conversation about... conversation! This was a ton of fun and I think there's a ton of value in this short discussion. Well worth your time, so check it out!

I have been a scale modeler, a photographer, and a woodworker my whole life. I was crafting as a toddler and never stopped.With a history like that, y

Stop giving away the best part

Every craft has one thing in common. The skill lives in the contact. The woodworker feels the grain. The cook tastes the sauce. Take away that direct touch and you do not just lose the quality. You lose the part that made it worth doing.

Customer conversation is a craft too. And most teams have quietly handed off the exact part where their own hands touch the work. The pause before someone answers. The thing they almost said. You cannot get that from a report.

My latest Conversation Field Notes article is up and I hope it gets you excited to hone your customer conversation craftsmanship!

A few months ago, I launched the Conversation Lab podcast. The idea was to blend informative content about the Conversation Compass with folks who use conversational skills as part of their own work. The goal wasn't to interview a stream of product folks, although I do love some good product nerdery. Instead I wanted to sit down with people whose careers live or die on their ability to have great conversations.

To say I've been having a blast is a big understatement. So far this first season, I've talked to a Pentagon spokesman, a flight attendant, a Jewish culture trainer who works with private security firm and law enforcement, an explainer-video pioneer, and a 20-year community builder. Five very different jobs, all leaning on the same conversational soft skills. Once you start seeing conversation as a craft, you spot great teachers everywhere.

And there's more conversations already recorded and on the way. I sat down with a psychologist to dig into what's really happening under the surface when two people engage. A flavor designer, whose work depends on building and using a shared language so people can actually communicate effectively about visceral experiences. And a UX and AI designer thinking hard about what conversation even means when a machine is part of it.

If you want to get better at talking to your customers, the smartest move might be studying people who do it for a living somewhere else entirely. You can add the podcast at jakemckee.com/podcast

And if you or someone you know uses conversation as a core part of your work, drop me a line. I'd love to talk with you about sitting down for an episode conversation.

And a huge thanks to my guests, friends, and supporters who have cheered this project on!

Enjoy a clip from the latest episode of The Disgruntled PM Podcast with guest Jake McKee

Like, Follow, and Subscribe  
 
LinkedIn Show Page:https://lnkd.in/gSCSGzwZ
Instagram: https://lnkd.in/eE3zsR47
📺YouTube: https://lnkd.in/gUvhaYmB
🎙️Spotify:  https://lnkd.in/geDJ-JNV  
🎙️Apple Podcasts: https://lnkd.in/gJ_rMm_z
💵 Patreon: https://lnkd.in/giZgz5zt

My Conversation Lab Podcast guest this week, Erik Summa, has been in the UX and design space for years. Erik told me his most painful presentation failure had nothing to do with his actual design.

He had done the prep work. He stood in front of a senior executive, walked through all of it, felt good about it. And then the exec said one thing back to him that made Erik realize he had been talking past this person the whole time. The design and content were spot on, but he assumed the exec understood what he was even looking at.

I am not going to tell you what the exec said. You will want to hear Erik tell it. Our conversation was fantastic and goes into everything from the impact of vibe coding on UX teeams to sorting out what AI actually changes about his craft and what it does not. 

The episode is live at: https://lnkd.in/dpYYF3SB. Subscribe and listen!

PDMA - Product Development and Management Association

AI is changing product innovation fast — and PDMA wants to hear how your team is experiencing it.

The AI Threshold Project is gathering insights from product and innovation professionals on the opportunities, challenges, and realities of AI adoption today. The survey takes less than five minutes, and the findings will help shape future kHUB content, interviews, and industry insights.

Add your perspective here: https://lnkd.in/gSiUEFSu

#PDMA #AI #ProductInnovation #InnovationLeadership

Most product teams I talk to believe they're close to their customers. They have NPS scores. They have Slack channels full of support tickets. They ha

You Might Have More Conversation Debt Than You Think

Today I'm dropping two things at once!

Episode 3 of The Conversation Lab podcast goes deep on Conversation Debt: what it is, how it accumulates, and why most product teams don't realize how much they're carrying until it's already costing them.

And right alongside it: the Conversation Debt Assessment Tool.

It's only 12 questions, takes 3 minutes and at the end you get a mini-report that calls out where your team's customer conversation practice is breaking down. There's even some next steps. 

I'd suggest taking the the assessment to see where you and your team are and then listen to the episode to think about where to go next. 

→ Episode 3: jakemckee.com/podcast
→ Assessment: jakemckee.com/compass

As we wind down the week and head into a (hopefully) beautiful spring weekend, I wanted to remind you to check out the latest Conversation Lab Podcast episode, focused on introducing Conversation Architecture. 

But first, let me give you something useful to mull over this weekend... 

A great dinner party doesn't just happen because the host is a great chef. It doesn't matter how good the food is if the kitchen has no ventilation, the table is in a hallway, and nobody knows whose job it was to send invites.

The same thing is true with customer conversations.

Conversation Architecture is the infrastructure underneath every conversation your team has. And most teams never consider it, much less purposefully design it. This shows up in very real ways:

A mental health support group with bad facilitation. Customer calls that keep going sideways. A feedback loop that never closes isn't a process problem. It's a design problem. And good design starts with questions: 

* Who actually owns your customer conversations? 
* What are your foundational principles around how you talk to customers? 
* What happens to what you learn? Is there a real path from insight to decision? 
* How do you know if your conversations are actually having a team/business impact?

If you can't answer those cleanly, you have a Conversation Architecture gap.
I dig into all of this in the latest episode of the podcast. You can also check out the accompanying newsletter article for even more detail:

https://lnkd.in/gmFhJnYi

Now go enjoy that weekend. ☀️

10 minutes until the March Conversation Lab event, and my snacks are ready to go!

I’m booking April and May events now and if you’re interested in joining… And getting a tasty box of snack as part of the event, you can sign up here:

Https://https://lnkd.in/gd-HA9w8

My friend, Conversation Lab alumni, and all around wicked smart guy, Joshua Zerkel, CPO has released a book that I cannot WAIT to read. 

Josh is one of those community folks who really thinks about the business impact of community, so his book is going to be quite a treat to read. 

Check it out at: https://lnkd.in/gjKr4h_7

Years ago, I was part of a small internal team at LEGO. Our job was to establish the strategic future of the LEGO Community program.Don’t get me wrong

Have You Ever Seen a $1.5 Billion Document? I Helped Write One.

Have you ever seen a $1.5 billion document? I helped write one.

Years ago I was part of the 10 person team that created LEGO's first formal community strategy. That work is now connected to about $1.5 billion in annual revenue from LEGO's 18+ product line.

This past weekend I came across the original document that outlined our community strategy. And amusingly, it aligns perfectly with the Customer Conversation Compass framework. (Learn more at: compass.jakemckee.com)

Check out the full story. It was a wild ride.

𝗧𝗵𝗲 𝗖𝗼𝗻𝘃𝗲𝗿𝘀𝗮𝘁𝗶𝗼𝗻 𝗟𝗮𝗯 𝗣𝗼𝗱𝗰𝗮𝘀𝘁 dropped its second Exploration episode this week and the feedback has been great. Thank you for that!

This Exploration was on Conversation Debt. Next up: Conversation Architecture. Dropping in about a week.

In the meantime, I've been getting some great questions about the Conversation Compass framework. And I'd love more ... I'm looking to answer some of them on the next Exploration episode. Drop me a DM or shoot an email to jake@jakemckee.com and I'll do my best to answer them. 

Until then, here's a question that came in via email. 

====
𝙃𝙤𝙬 𝙙𝙤 𝙮𝙤𝙪 𝙜𝙚𝙩 𝙩𝙝𝙚 𝙥𝙧𝙤𝙙𝙪𝙘𝙩 𝙩𝙤 𝙖𝙘𝙩𝙪𝙖𝙡𝙡𝙮 𝙬𝙖𝙣𝙩 𝙩𝙤 𝙩𝙖𝙡𝙠 𝙩𝙤 𝙘𝙪𝙨𝙩𝙤𝙢𝙚𝙧𝙨 𝙬𝙝𝙚𝙣 𝙩𝙝𝙚𝙮'𝙫𝙚 𝙗𝙚𝙚𝙣 𝙩𝙤𝙡𝙙 𝙣𝙤𝙩 𝙩𝙤?
====

That's a trust problem wearing a policy costume. Usually it's because of something like Sales protecting their relationships, or Legal overcorrecting after something previously went sideways. The rule sounds reasonable on the surface, but what it actually does is sever the product team from reality. You end up building for a customer you're not allowed to talk to.

You have two options and you probably need both. First, figure out the "cost" of the policy and make it visible to the people who can change it. Missed features, retention problems, a roadmap that made sense internally and landed flat externally are all things that trace back to access, and when you can show that connection, the policy starts to look a lot less protective. 

Second, find the edges. Ask if you can sit in on a sales call, just to listen. Get on the phones with the support team and just absorb what you hear. Show up to a user meetup and just be a person, not a company rep. Read every support ticket yourself instead of waiting for a summary. Nobody told you not to do any of that.

This is *guerrilla learning*, not formal policy and procedure. But you're not trying to blow up the system, you're just refusing to let it be a blocker. Even a little direct exposure changes how you talk about customers. You start speaking with more authority because you actually heard something tangible and unique. Your colleagues notice that. It builds trust. And trust, over time, opens doors that policy had closed.

https://lnkd.in/gErnpwbV

Most people think a conversation starts when someone opens their mouth. It doesn't. It starts long before that, when the other person trusts you enough to say something real.

The guest on the latest Conversation Lab Podcast, Larry Glickman, is the founder of JCAT Partners, where he trains law enforcement and private security professionals to work more effectively with the Jewish community. His program isn't a checklist. It's a foundation. Before anyone can have a quality conversation, they need to understand the language, rituals, and cultural context of the people they're working with. Without that, what you get isn't a real conversation. You get surface-level compliance and a lot of missed signals.

In this episode, Larry and I dig into what it takes to build the conditions for honest conversation, and why product teams skip this step more than they realize.

Find the episode and subscribe to the podcast at: https://lnkd.in/dpYYF3SB

This was a lot of fun. If you hadn’t had a chance to check out the episode, you definitely should!

Https://jakemckee.com/podcast

Are you drowning in "secondhand insights"?

Most product teams think they’re customer-centric, but they’re actually playing a massive game of "telephone." Between sales summaries, support tickets, and research decks, the actual voice of the customer gets filtered and sanitized until it’s barely recognizable.

Jake McKee calls this Conversation Debt. Like technical debt, the interest eventually comes due in the form of missed launches and features that just don't land.

In the latest episode of the new Conversation Lab Podcast, Jake sits down with William Marks to discuss how to break this cycle. William isn't a "tech guy"—he’s a Navy veteran and former Pentagon spokesman who has managed communication in some of the highest-stakes environments imaginable, from aircraft carriers to CNN studios.

Here are three unconventional takeaways from their discussion:

1. Stop Over-Engineering the Chat

We often decide what we want to hear before we even sit down with a user. William notes that "over-engineering" a conversation before you have it is exactly what kills the signal. The real value lives in the unscripted "mess and nuance"—not a rigid deck.

2. The "Introvert’s Trick" for Direct Access

Think you need to be a social butterfly to lead these talks? Both Jake and William are self-described introverts. William’s secret for walking into a room of strangers: Don’t plan. Walk straight to the first person you see and say anything to break the ice. Momentum beats a "perfect" strategy every time.

3. One Conversation Isn’t a Strategy

You can’t change a mindset in one sitting if the person goes right back into the same ecosystem that formed their belief. Whether it's a resistant stakeholder or a frustrated customer, "Conversation Architecture" means building these touchpoints into your team's actual system, not treating them as a one-off project.

The gap between what you think customers need and what they actually need is widening every sprint you skip a real conversation.

Is it time for your team to pay down its debt? You can start by listening to the Conversation Lab Podcast.

https://lnkd.in/gwVcRssz

#ProductManagement  #ConversationLab

CMX Summit is eight days away and sadly I am not going to make it this year. So I wanted to offer something useful to those of you who are.

As someone who thinks about conversation for a living and still finds it genuinely hard to sustain at a two-day event, I have spent a lot of time figuring out what actually works. How to take the first step. How to keep the conversation going in a way that feels good for both people. How to protect your energy so Day 2 does not find you running on fumes.

I turned all of it into a free guide.

The Conference Survival Guide has 26 specific moves covering every stage of a conference conversation. Before you arrive. Starting the conversation. Staying in it. Getting out cleanly. And capturing what you actually heard before it disappears.

Grab it before you pack. And it's a living document, and I'll be adding to in the weeks to come.

https://lnkd.in/gscev89C 

#CMXSummit #CommunityBuilders #ConversationCompass

The Navy figured something out after Vietnam: if you only talk to people who already speak your language, you will always be misunderstood by everyone else.

So they built a program to fix it. 

My first guest on the Conversation Lab Podcast tells us all about that program and much, much more. William Marks is a decorated Navy combat veteran, former Pentagon spokesman, Meta Community Liaison, and most recently a congressional candidate.

And strange as it may sound, he's also an introvert. Listen/Subscribe to the podcast to find out why that matters :) 

You can find the podcast (and sign up to be a guest or sponsor the show) at: https://lnkd.in/dpYYF3SB

Most product teams I talk to are running on secondhand insight.

Not because they're lazy. Because the systems they built (the dashboards, the ticket summaries, the Sales briefs) slowly replaced the actual conversations. And at some point, nobody noticed.

That's Conversation Debt. And in Episode 3 of The Conversation Lab, that's what we're getting into.

Check it out at: jakemckee.com/podcast

Hey Austin product people! ProductCamp Austin is this weekend and I hope I’ll see you there. 

My session pitch this year is one I’m really excited about. It's called "𝗬𝗼𝘂𝗿 𝗥𝗼𝗮𝗱𝗺𝗮𝗽 𝗶𝘀 𝗕𝘂𝗶𝗹𝘁 𝗼𝗻 𝗥𝘂𝗺𝗼𝗿𝘀" and it's about 𝗖𝗼𝗻𝘃𝗲𝗿𝘀𝗮𝘁𝗶𝗼𝗻 𝗗𝗲𝗯𝘁. That’s the gap between the direct customer conversations your team should be having and the ones that are actually happening. Most product teams don't even realize how deep in debt they are until they stop and count.

It's a live workshop where we actually dig into 𝗖𝗼𝗻𝘃𝗲𝗿𝘀𝗮𝘁𝗶𝗼𝗻 𝗗𝗲𝗯𝘁 together as a group. I'm bringing my newly created live Conversation Debt Tracker so that we can all see and discuss what Debt looks like for the room. Participants run their own personal Conversation Debt Assessment, and results are displayed and averaged in real time, displayed on the big screen. It’s a pretty eye-opening moment when you see where a room full of product leaders actually lands.

ProductCamp Austin works by having attendees vote for the sessions they want to join. So if you're coming out this weekend, I'd love your vote and I'd love to see you there.

Drop a comment or DM me if you're planning to come. Let's connect!

I've been lucky enough to eat at some truly amazing places in my life. But none left a lasting impression like Eleven Madison Park (EMP) in New York.

Eleven Madison Park: The Whiskey Cart

I love food. I try to eat at as many amazing places as I can, and I've been lucky enough to hit some truly great ones over the years.

But nothing topped Eleven Madison Park. And honestly, it wasn't just the food, even though the food was world class. It was the service. It was the surprise. It was the feeling that the whole evening had been built just for us.

Here's the thing about great experiences like that: they don't just happen. They're designed.

Today's article walks through my EMP experience and why it lines up so perfectly with what the Customer Conversation Compass is all about. If you lead product and you've ever wondered what it actually looks like to build a real system around knowing your customers, this one's for you.

I’m very excited to share that I’m working with the Product Development and Management Association (PDMA) kHUB team on a new research initiative: 𝗧𝗵

Announcing The Threshold Project

I’m very excited to share that I’m working with the PDMA - Product Development and Management Association (PDMA) kHUB team on a new research initiative: 𝗧𝗵𝗲 𝗔𝗜 𝗧𝗵𝗿𝗲𝘀𝗵𝗼𝗹𝗱 𝗣𝗿𝗼𝗷𝗲𝗰𝘁.

The idea is simple: We are hearing a lot about how AI will impact product development and innovation, but we’re not hearing much from the product and innovation teams themselves. Our goal is to capture what product and innovation leaders are experiencing right now. 

Everything we learn will be published on PDMA’s kHUB, including:

𝗦𝘂𝗿𝘃𝗲𝘆 𝗿𝗲𝗽𝗼𝗿𝘁 - A grounded look at how product/innovation teams across industries are actually approaching AI

𝗜𝗻𝘁𝗲𝗿𝘃𝗶𝗲𝘄 𝘀𝗲𝗿𝗶𝗲𝘀 - 1:1 conversations with people willing to talk honestly about what’s working, what’s not, and what’s still unclear

𝗧𝗵𝗲 𝗳𝗶𝗲𝗹𝗱 𝗿𝗲𝗽𝗼𝗿𝘁 - A short, plain-language read on the signals worth paying attention to if you’re leading a product or innovation team right now

Here’s where you come in...

This project starts with a short survey that takes about 5 minutes. It covers what you’re seeing, what you’re trying, what you’re worried about, and what you think product/innovation leaders need to understand before they blindly sprint into this.

If you’re willing and interested in being part of this project, please click the link below!

https://jakemckee.com/pdma

Founder of Operation Caged Bird

We’re podcasting! 
  Jake McKee is a superstar host and community builder. List to our chat about the US Navy , Meta, and how I lost an election.

Huge thanks to the PDMA Seattle folks for the shout out of my new Conversation Lab Podcast! Subscribe/listen here: https://lnkd.in/dpYYF3SB

How Will Pattison built a 12,000+ member online community on brutal honesty, fierce standards, and the radical willingness to lose members he never wa

Anarchy with an Iron Fist

Most teams think conversation just... happens.

It doesn't. It's designed. And if you don't design it intentionally, it defaults to something you didn't choose.

Will Pattison built a 12,000-member scale modeling community around one simple idea: honest feedback flows freely, or the whole thing is worthless. Unsolicited critique is the default. Work-in-progress posts are the most valued content. Passive-aggressive hedging gets flagged before it takes root.

That's Conversation Architecture at its finest.

My latest Conversation Fields Notes article dives into this story and shares what product teams can steal from it.

You wouldn't open a restaurant without a kitchen.

But most teams open conversation spaces with no structure, no assigned responsibilities, no plan for what happens when things go wrong.

They just... open the door and hope.

Conversation Architecture is the kitchen; it makes great conversation possible. Episode 5 of the Conversation Lab Podcast is live and I dive into Conversation Architecture. 

Check it out!
https://lnkd.in/dpYYF3SB

Community isn’t just vibes. It’s GTM infrastructure. | Community-Integrated GTM | $94M Pipeline Influenced (Asana) | Head of Marketing & Community @ Gradual | Author: The Community Code

Today my new book, The Community Code, is out.

It’s about a pattern I kept running into.

Community clearly influences how customers learn, adopt, and talk about products. But inside most companies, that impact gets split up depending on where it sits.

Marketing sees advocacy.
Product sees feedback.
Customer success sees adoption.
Sales sees pipeline.

All of those are true. They just don’t add up to a shared way of operating.

So teams invest in community, see real pockets of impact, and still struggle to connect it to how the business actually runs.

I used to think the challenge was convincing stakeholders that community matters. Sometimes it is. But in practice, the harder problem is why something that clearly has impact so rarely translates across the organization.

A lot of what gets labeled as “community-led growth” tries to solve this by reframing the work. In my experience, that only gets you part of the way there.

The issue is structural.

Community doesn’t sit neatly inside one function, but most organizations are still built that way.

The Community Code lays out what changes when community becomes part of how the business runs.

It’s out today: https://lnkd.in/g9JYr5NB

Conversation Debt is the gap between what your team thinks it knows about customers and what's actually true.

It builds up slowly: A summary here, an assumption there, and plenty of secondhand insights passed along like a grade school game of Phone. Before long your roadmap is running on assumptions nobody has tested in months.

I built a quick assessment to show you where yours stands. Answer 12 questions, get an overall health score, see exactly which categories are hurting you most, and walk away with one specific thing you can do about it this week. Check it out!

👉 jakemckee.com/compass

If your results scare you, let's talk!

Most people think good conversation is a personality trait. You either have it or you don't.

Martin Drayton has spent 39 years proving that wrong.

He's a snowboard instructor and a flight attendant; two careers where reading a stranger fast and figuring out how to reach them is critical. We talked about what that actually looks like in practice and what product teams can learn/steal from it.

Episode 4 of the Conversation Lab podcast is live now. Subscribe to hear a ton of content I'll be dropping in the coming weeks!

https://lnkd.in/dpYYF3SB

Of all the bird brain decisions… this is one of the stupidest things I’ve ever heard. Moderation is not censorship. This is an infuriating position for the US government to take. WTAF.

Powerful post by my friend, Wesley Faulkner. 

In today's modern corporate world, we hear a lot about how we're all a family. About how we need to give 110%. But we also hear a lot about how those damn Millennials or those foolish GenZ folks just "don't want to work". Is it any wonder? Business in general has removed every bit of security while demanding excessive work and complete dedication. All while reducing every form of long term benefit that used to be part of the relationship between company and employee. Pensions? Gone. Long term expectation of stability? Gone. Benefits? Nope. Pay that can sustain a family? Haha. 

Hell, the core idea of being an employee with a full-time job is being challenged. 

All this is worse for people with these kinds of community roles. Community professionals dedicate so much more than their time and energy. They form bonds with their members/customers in a way that most others in a business don't every see or experience. They pour emotion and connection and care into their programs, communities, and members in a way that most parts of a business don't or don't understand. 

Check out Wesley's post, learn about the AWS community, and introduce yourself to Jason Dunn.

Author of The Community-First Advantage | I help executives use community as a strategic growth and adaptation advantage. ADAPT Leadership Framework | Executive Advisor | Speaker

I cut open a box today.

Not just any box — the first shipment of The Community-First Advantage. 

Fifteen years of helping leaders build community-driven companies. Hundreds of conversations with founders, executives, and community builders who changed how I see business. Lessons from LEGO, Airbnb, Figma, Canva and 50+ community-led companies. 

Now sitting in my hands as ink and paper.

I thought I'd be cool about it. Instead I stood there like a proud, very sleep-deprived and over-caffeinated parent holding a newborn.

This book isn't theory for me. It's lived community-driven leadership I know we need more in our organizations.

As I flipped through the pages — the mountain tops and deep valleys came rushing back. Wins that surprised me. Mistakes that humbled me. People who pushed me, challenged me, and transformed how I communicate the value of community.

And today, it all became real.

To anyone building something that feels impossible right now — keep going. The moment you open the box is worth it.

🙏 If you've already grabbed the ebook, a review on Amazon helps more than I can explain. Algorithms are wild, humans are kinder.

And if you've ever held something you created and whispered, "I can't believe this is real," tell me in the comments. I want to celebrate with you.

Let's keep the community-first leadership movement growing.

Head of Trust & Safety @ Musubi --​> AI for T&S

⚠️ Breaking news-- Trust & Safety workers will be rejected for US H1B visas. 

"We do not support aliens coming to the United States to work as censors muzzling Americans," a State Department spokesperson said, according to Reuters. 

From Reuters: "The Trump administration announced increased vetting of applicants for H-1B visas for highly skilled workers, with an internal State Department memo saying that anyone involved in "censorship" of free speech be considered for rejection." https://lnkd.in/ef-sUv-f

And a great overview from NPR here (including a quote from me, much of which I say here-- I don't often talk to press on the record but I did for this). https://lnkd.in/eDAdgUQq
Love the irony of this: "Even as the administration has targeted those it claims are engaged in censoring Americans, it has also tightened its own scrutiny of visa applicants' online speech."

This applies to people working on fact-checking, content moderation, online safety, trust & safety, and combating misinformation and disinformation, among others. 

Interestingly they also call out anyone working on compliance and adopting "global content moderation policies" or "complying with censorship demands from a foreign entity." -- aka DSA or OSA compliance.

They're checking resumes and LinkedIn profiles of H-1B applicants - as well as info from family members who would be traveling with them.

(Time to scrub your LinkedIn if you need to). 

First-- Trust & Safety work isn't censorship. 

It's a very broad category that includes life-saving work like child safety and preventing sextortion, as well as fighting fraud and scams. These are things that almost everyone can agree are important. 

Secondly -- If we're purely talking about what's good for Americans (and avoiding talking about how the internet is global anyway). Bad actors who target Americans come from all over the world (also Americans come from many different backgrounds), so it's important to have people who understand different languages and cultures on Trust & Safety teams. Having global workers at tech companies in T&S absolutely keeps Americans safer. 

This is completely unacceptable and gut-wrenching. It goes against everything I believe in and I'm just so mad about it. 

I'm sure a lot of people are really scared right now.

I'm not sure how I can help folks, but let me know if there's anything I can do. If you don't feel comfortable posting about this publicly but want to get info or thoughts out there, let me know and I can post on your behalf.

AIX Sessions - Jake McKee

0-1 AI Product | Driving Growth, Retention & Acquisition | Google, SCAD, NIFT

Thank you so much, Jake McKee, for hosting AIX Sessions. I walked away energized and inspired. It was fun connecting with Emma Harper, Lief Zimmerman, Rochelle Sonnenberg and Brian Fabian! Each of you brought a fresh lens to AI, and the conversations pushed my thinking in the best way!

It was an incredible group with perspectives from across industries, sparking ideas, friendly debates, and the kind of brainstorming you wish you could bottle!

If you’re even a little curious about AI and want to stretch your thinking, AIX Sessions is absolutely worth joining. It’s a rare space to connect, learn, and grow, and yes, have a good time doing it! 🚀 🤌 

https://lnkd.in/gHpTatrF

Today's the day!

The St. Louis PDMA - Product Development and Management Association has invited me to speak tonight about two of my favorite topics: Star Wars and AIX. 

Nearly 50 years ago, Star Wars imagined a future where humans and machines worked side by side...and perhaps accidentally, predicted how we’d feel about it too. Luke, Leia, and Han don’t just use droids like tools; they adapt their tone, shift expectations, and form real relationships based on what each droid is and how it behaves.

Today, we’re living in that future. AI is quickly being embedded in products across every industry. But while the technology has accelerated, many teams still design around output, not interaction. The result? Confusion, mistrust, and missed opportunity.

This session introduces AI Experience Design (AIX) as a practical framework for product managers who want to move beyond functionality and start shaping how users actually relate to intelligent systems. Blending human psychology, storytelling, and real-world product strategy (plus a healthy dose of sci-fi nostalgia) this talk will reframe how you think about your roadmap, your features, and your AI’s place in the world.

You’ll walk away with:
* A new lens for understanding AI-driven UX and product decisions
* Psychological principles that shape user trust and emotional response
* Frameworks for designing clarity, tone, and expectation into intelligent AI systems

Session is free and should be a fun ride! Join me this afternoon!

https://lnkd.in/grnE9dBh

I've spent nearly thirty years thinking about one thing: how organizations actually connect with the people they serve. Not the dashboard version. Not

The Conversation Lab Podcast is live!

I'm insanely excited to announce the first of several new Conversation Compass projects: The Conversation Lab Podcast is now live!

This podcast delves into the craft of conversation through real discussions with individuals who engage with it daily. I will be featuring designers, researchers, psychologists, community builders, politicians, detectives... basically anyone who relies on effective conversation to do their job. 

There are currently two episodes available: 

A solo episode where I introduce the Customer Conversation Compass, the framework behind my work. 

A conversation with William Marks. William is a US Navy veteran, retired Meta Community Liaison, and a Democratic candidate who ran in a very red congressional district in Ft. Worth. 

I encourage you to listen and subscribe at jakemckee.com/podcast or find it on Apple Podcasts and Spotify. I'd love to hear what you think, what you loved, and how I can make it better. 

Let's talk!

Next week I'm launching a podcast about something most of us do every single day... and almost never think about.

Conversation.

Not the theory of it. The craft of it.

The Conversation Lab Podcast brings together designers, politicians, culture trainers, researchers, psychologists, and a whole lot of other people from wildly different fields, all of whom rely on conversation in their work in fascinating ways.

Short episodes. Real exchanges. Practical insights you can actually use in your daily work.

More details dropping on Monday. Stay tuned!

Chris has been hard at work with this book for a while and I can't wait to read it. It was a joy and an honor to be included in. Great work, Chris! Can't wait to order my copy!

Online Community + Interactive Product Leader, Ex-CNN/Warner Bros. Discovery ● Experience Building D2C, Membership, Streaming, and Subscription Services

I was watching a series of TikTok videos where a woman discussed her efforts to track down and hold accountable a man who left a horrendous, highly offensive comment on one of her videos, from his business account.

She has reported the man's behavior to groups that he is a member of, licensing agencies for his business, and other relevant professional parties.

One thing I found fascinating in her videos was how she talked about the fact that many commenters had labeled her actions "petty" (in a good way). She made a point to say that it wasn't pettiness, that everyone should take these steps to hold men accountable for harassment and, crucially, that "the very existence of these reporting structures indicates that this behavior can and should be reported."

YES. YES!

I can't tell you how many times I have told an online community member to *please* report bad behavior so that we can take appropriate action, only to be told something along the lines of:

- We're all adults here, I'm not going to run and tell on someone
- I'm not a snitch.
- It's not that deep.

LOUDLY: USE THE REPORTING STRUCTURES THAT I DESIGN in order to more quickly bring issues of concern to the attention of my team, and myself. That's the whole point. Please do it. 

I understand the world is also conditioned by the poor-to-mediocre reporting actions of huge platforms like Facebook, Instagram, LinkedIn, and Twitter, so that's part of it. But the vast majority of platforms (especially smaller communities) do review reports and use them to make these places more like what they were designed for and less like what others want to make them.

I’m excited to be speaking for the SME (Society of Manufacturing Engineers) community on February 18 as part of SME’s Spotlight Series. Here's the lowdown:

Manufacturing teams talk to customers every day, yet much of what they learn never makes it into real product decisions. In this 30‑minute, member‑exclusive session, I’ll introduce the Customer Conversation Compass, a practical framework for turning everyday customer conversations into clearer insight, better tradeoffs, and stronger product direction. 

I'll share my thoughts on: 

✅How to structure customer conversations to surface real needs 
✅How to tell meaningful signals from noisy feedback 
✅How small changes in how conversations are shared can improve product decisions 

This session is for SME members, but it's a solid group. If you're interested in joining, you can join here: https://www.sme.org/join

The Conversation Lab Podcast is officially in the world! Add the feed to your app of choice, grab the trailer to hear what's coming, and get ready: Season 1 drops soon.

Great podcasts are supposed to *be* great conversations. Mine goes one layer deeper: it's conversations about the craft of conversation.

The season mixes short, practical lessons in conversational design with long-form conversations with people whose work lives or dies by their ability to connect with another human being.

A Democrat running for office in a deep red Texas district. A UI/UX designer who has fully embraced AI. An expert in the field of explanation. A Jewish culture instructor who trains private security and law enforcement. A seasoned flight attendant. And more.

Most of these folks wouldn't call themselves a "product person," but all of them have something product people desperately need to hear.

If you are interested in learning more about what makes a great conversation and how that can impact your work, this is the podcast for you!

Feed link in comments and at the link below. Sign up and stay tuned for the first episode to drop!

🎙️ https://lnkd.in/dpYYF3SB

Always a wonderful day when I'm hanging out with a friend and AIX Sessions alumni! Larry Glickman is up to some cool stuff. I'll share more when he launches.

I had a really great time chatting with Christian about community+product design on his podcast. Check it out!

In 1878, when the first telephone exchange opened in New Haven, Connecticut, the technology was revolutionary. You could transmit your voice across mi

The AI Operator: Why Product Teams Need Human Connectors More Than Ever

I've spent my entire career helping disparate groups hear each other. Turns out that's exactly what AI-augmented organizations need right now.

The emerging AI Operator role isn't about deploying tools or writing code. It's about reading signals across teams that can't see each other's patterns.
When your engineering team's AI analysis points one direction, your product research suggests another, and your business projections assume a third, someone needs to interpret what those contradictory signals actually mean together.

What they actually *mean*. 

The skills that made me effective in community work—translating between contexts, spotting invisible assumptions, recognizing when different groups are describing the same problem in different languages—those are intelligence skills. And they're what organizations need as AI amplifies the gap between generating insights and acting on them.

I wrote about the AI Operator role and why it's less about technology expertise and more about signal interpretation.

If your teams are producing more insights than they know how to integrate, or if you're seeing smart people drift apart while each claiming data supports their direction, that's the signal interpretation gap. I can help you resolve that gap.

The St. Louis PDMA - Product Development and Management Association has invited me to speak next week about two of my favorite topics: Star Wars and AIX. 

Nearly 50 years ago, Star Wars imagined a future where humans and machines worked side by side...and perhaps accidentally, predicted how we’d feel about it too. Luke, Leia, and Han don’t just use droids like tools; they adapt their tone, shift expectations, and form real relationships based on what each droid is and how it behaves.

Today, we’re living in that future. AI is quickly being embedded in products across every industry. But while the technology has accelerated, many teams still design around output, not interaction. The result? Confusion, mistrust, and missed opportunity.

This session introduces AI Experience Design (AIX) as a practical framework for product managers who want to move beyond functionality and start shaping how users actually relate to intelligent systems. Blending human psychology, storytelling, and real-world product strategy (plus a healthy dose of sci-fi nostalgia) this talk will reframe how you think about your roadmap, your features, and your AI’s place in the world.

You’ll walk away with:
* A new lens for understanding AI-driven UX and product decisions
* Psychological principles that shape user trust and emotional response
* Frameworks for designing clarity, tone, and expectation into intelligent AI systems

Session is free and should be a fun ride! Join me on December 9:

https://lnkd.in/grnE9dBh

It's hard to get excited about AI and especially hard to get excited about supporting AI companies when they have absolutely zero commitment to the safety measures they build their brands around. 

"But in recent months [Anthropic] decided to radically overhaul the RSP. That decision included scrapping the promise to not release AI models if Anthropic can’t guarantee proper risk mitigations in advance."

We simply cannot rely on AI companies to self-regulate.

Already booking February’s event!

Anthropic Drops Flagship Safety Pledge

Tech correspondent at TIME

Exclusive: Anthropic is dropping the central pledge of its flagship safety policy, company officials tell TIME.

In 2023, Anthropic committed to never train an AI system unless it could guarantee in advance that the company’s safety measures were adequate. For years, its leaders touted that promise—the central pillar of their Responsible Scaling Policy (RSP)—as evidence that they are a responsible company that would withstand market incentives to rush to develop a potentially dangerous technology. 

But in recent months the company decided to radically overhaul the RSP. That decision included scrapping the promise to not release AI models if Anthropic can’t guarantee proper risk mitigations in advance. 

Read the full story: https://lnkd.in/eF4E9_ZF

Community Builder | Podcaster | Public Speaker | DevRel Professional

“It is what it is.”

That phrase is one of the most dangerous ideas we’ve normalized at work. 

Not because the world is fair, but because it isn’t, and this is how we stop demanding better.
I want to talk about one person.

Jason Dunn

Jason was laid off from Amazon last week. Many people knew him as the leader behind Community Builders, an influential AWS community made up of people creating videos, blog posts, talks, and learning resources, mostly on their own time and largely for free. The value that the community created was easily in the millions.

Jason made people feel seen and valued.

What most didn’t see was the work. Nights and weekends reviewing applications. Obsessing over process, fairness, tools, and timing. Fighting for recognition of long-time contributors while still welcoming new voices. Testing vendors. Sweat equity everywhere. This wasn’t just a job. It was his identity.
Everything he built still exists. It still creates value. It still belongs to AWS.

Jason was separated from it.

There will be no walkout.
No mass petitions.
No resignations in protest.
And the people in charge know that.

They know that when people feel powerless, they go with the flow rather than push back. So everyone moves on by saying, “It is what it is.”
That phrase is how unfair systems stay intact. It’s how we normalize extracting passion and unpaid labor, then cutting people loose with a spreadsheet decision.

“It is what it is” isn’t wisdom.
It’s a resignation.
And Jason deserves better. We all do.

AI stopped being a demo in 2025. Last week, we explored what happens when it becomes part of the foundation.

We brought together senior technology leaders for a private Gild conversation on how this past year’s AI deployments are reshaping the road ahead. The focus wasn’t on hype, but on the real lessons that emerged when AI moved from experimentation to day-to-day operations.

Jake McKee, Principal Consultant in AI Experience Design and Customer Engagement, helped frame the evening by opening the conversation and guiding a series of small-group discussions throughout the session. He created space for leaders to share candid experiences, challenge assumptions, and connect customer understanding to the practical realities of building and operating AI-powered systems.

The themes that surfaced were clear: AI maturity now depends on clarity, alignment, and the ability to build responsibly at speed. The leaders who can turn 2025’s learnings into 2026’s advantage will set the pace for what comes next.

Thank you to Tecla for sponsoring the evening and supporting teams building meaningful outcomes with U.S. and nearshore engineering talent.

If you’re a senior technology leader in Austin shaping your 2026 AI strategy, reach out to learn more about the Gild community.

The best way for us to keep our online spaces positive is to report the HELL out of the bad actors. And our community management/moderators need to be more present, known human entities that are clear about what happens with moderation and why. This helps build culture that allows a community to be and remain a positive space. 

The news has harped on the various White House requests to the big platforms to moderate in particular ways, and it's made many people believe that moderation is inherently bad... or that it shut down/censors conversation. 

That's not true. Setting boundaries and calling out bad behavior, especially in anonymous or semi-anonymous spaces is a core part of building successful human relationships. It's not "censorship". 

You can't be a great party host AND let your guests destroy your house and walk out with your silverware.

For more than 7 years, I’ve been hosting small, invite-only conversation sessions. The name and focus have evolved over time, but a few things have stayed constant: five wicked-smart people, tasty snacks, and genuinely great conversation.

As my consulting practice has evolved, I wanted the event to evolve with it.
So today, I’m introducing Conversation Lab.

Conversation Lab is a monthly, five-person, two-hour virtual session built around something simple and increasingly rare: giving peers a trusted space to talk honestly about what they’re struggling with and get help from people who actually understand the work.

This isn’t a webinar.

There’s no deck. No expert monologue. No watching from the sidelines.
In this format, each participant brings a real issue they’re dealing with and takes a turn facilitating a conversation around it. Before we meet, I share a handful of practical cues to help shape the conversation, but the point isn’t learning moderation techniques. It’s creating the conditions for thoughtful, useful discussion. We stay present to how the conversation unfolds, what helps people open up, where things get stuck, and how small moves change the energy of the room.

The learning happens naturally because it’s grounded in real problems and real people. But at its core, Conversation Lab is about spending time in a smart, generous room with peers, helping each other work through what actually matters right now.

New name. Evolved format. Same heart.

If you’re interested in joining a future Conversation Lab, you can sign up here:
https://lnkd.in/gd-HA9w8

Every month, AIX Sessions runs on the same simple rule: the conversation goes where it needs to go. No slides. No big-company varnish. Just five peopl

AIX Sessions November Recap

This week was the last AIX Sessions event for 2025 (I typically take off the month of December to rest, recharge, and recalibrate). And once again, five people who’d never met ended up wandering through maps, medicine, culture, authenticity, and why teenagers think AI is basically cheating. 

These monthly Sessions always remind me that the real conversation about AI and product and community aren't happening in boardrooms. They're happening in small groups where people feel comfortable saying, “I’m excited” and “I’m freaked out” in the same sentence. 

If that’s the kind of conversation you want more of in your world, give it a read ... and signup to join an event in 2026!

I have a last-minute opening for the Conversation Lab: March 26, noon–2p CT.

This is a small, free, virtual gathering for product, community, and customer experience leaders. Five people, no agenda, no slides, no pitch. Just honest conversation about the craft of understanding and engaging customers. And the best part? The amazing box of tasty, pairable snacks that every attendee gets on their doorstep.

If you've been meaning to check it out, now's your shot!

Apply to attend (this event or an upcoming event) at https://lnkd.in/gd-HA9w8

Engines Of Creation | Podcast on Complexity and Innovation by Christian Mastrodonato

Data & AI Leadership | Navigating Complexity in Organizations | Host of Engines of Creation

Is Community just a cost center? Or is it your company's central nervous system?

In the rush to automate, many organizations are falling into the "Synthetic User Trap." It is incredibly sexy to think that AI can replace user testing, generate synthetic data, and automate support to zero.

But as Jake McKee argues in our latest episode of Engines of Creation, this creates a fundamental fragility.

"AI is a retroactive tool. It looks backwards at what exists and creates pattern. We cannot come up with innovative products looking forward if all we rely on is what people have already thought about."

If you remove the human friction, you remove the spark of innovation.
In Episode #29, we deconstruct the Octopus Theory of community. We discuss why a Community Manager isn't just a moderator—they are a CIA Intelligence Analyst, interpreting the raw feed of the market to prevent leadership from flying blind.
We cover: 🐙 The Octopus Theory: How community tentacles reach into Product, Marketing, and Strategy. 🤖 The Retroactive Trap: Why AI is a critical partner, not a replacement for connection. 🏗️ Platform Thinking: Building "emotional texture" into your product to avoid commoditization.

If you are building a product or a movement, you need to understand the physics of these relationships.

Listen here: www.enginesofcreation.co

#CommunityStrategy #SystemsThinking #AI #ProductManagement #EnginesOfCreation

Founder and CEO of JCAT Partners, providing Jewish community awareness training to security professionals protecting Jewish people and institutions.

I first met Jake McKee as part of his amazing Dinner 5 online community professionals program many years ago, and since then he has become a good friend and trusted advisor.

Over a long (and long overdue) breakfast today in Austin, Jake dropped a rapid-fire series of business start-up knowledge bombs that….
-Left my head spinning.
-Confirmed for me that I am the right track.
-Made me even more excited for the work and adventures ahead.

I will have some exciting news to share soon, but in the meantime…thank you, Jake! World class consultant, networker, and creator!!!

As we step into 2026, a lot is changing for me, both personally and professionally.Yes, I’m moving houses. But more importantly, I’m intentionally nar

Introducing the Customer Conversation Compass

As we step into 2026, a lot is evolving both personally and professionally in the Jake McKee Consulting world. I'm not just moving to a new home, but also refining my entire consulting focus. Today, I want to introduce you to something that's been at the heart of my work for over two decades: the Customer Conversation Compass.

This framework is all about helping product teams regain meaningful control over their customer relationships. For years, product teams have found themselves distanced from customers as other departments took over those interactions. Yet the mandate to be "more customer-centric" never faded, it just got a little lost.

So in 2026, you’ll see a fresh focus from me on the Conversation Compass in everything I do. That includes rebranding my monthly sessions, refining the content of my LinkedIn newsletter, and shaping the very core of my consulting practice around it. Stay tuned, there’s a lot of exciting change ahead!