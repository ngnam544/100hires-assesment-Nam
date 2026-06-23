# Recent Posts for jonobacon

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

LinkedIn Ads Expert + AI @ Speedwork.io | Top 50 LinkedIn Certified Marketing Expert | LinkedIn Learning Instructor | Ex-IBM | Host, LinkedIn Ads Radio Podcast

NEW research shows where top CMOs are moving their budget to in 2026 (and it’s NOT search this year)

Factors.ai new data is in:

• 6.3% of budget share is shifting from Google → LinkedIn
• LinkedIn’s budget share grew from 31% to 37%
• B2B CMOs prefer LinkedIn

Why? Because LinkedIn ROAS = 1.8x versus Google’s 1.25x when analyzed across 100+ B2B organizations.

We see this at Speedwork -- LinkedIn Ads Agency every day too. Social is where demand is created. Search often takes the last touch “credit”, masking the real trends and with reporting from LinkedIn Partners like Factors.ai, marketers are able to tie impressions to revenue.

Get started today with a new LinkedIn Ads account and if you implement a partner like Factors.ai, you’ll get a $500 ad credit. Click here to learn more: https://lnkd.in/gw8Khzee

#LinkedInPartner LinkedIn for Marketing

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

Product Owner | Business Analyst | Business Administration @NEU’25

Lecturer at Ho Chi Minh University of Banking

Data Engineer | Databricks Certified Data Engineer Professional | Databricks Certified Data Analyst | AWS Certified Solution Architect

Tech, Cloud, AI, and more

Business Analyst/ Product Owner

Senior Talent Acquisition | HR | TaLi Do | HR at Dat Xanh Services

GenAI | AI Automation| Multi-Agent | Ex-CocaCola-VN

Generative AI | LLM | MLLM | MLOps Engineering 
@Cake By VPBank

Financial Consultant | Chuyên Gia Thu Xếp Vốn & Tín Dụng Doanh Nghiệp | Hỗ trợ dòng vốn ngắn - trung hạn cho Doanh Nghiệp & Cá Nhân Kinh Doanh

CEO of Stateshift. GTM for technical people who hate being marketed at. 📓 Author ‘People Powered’ by Harper Collins. Not related to Kevin 🥓.

My fave coffee shop in San Francisco. Sightglass Coffee 🤘

Live online events are the BEST form of developer engagement. Convince us otherwise.

Because the version of a traditional webinar you're thinking of is probably the exact thing we're arguing against.

45 minutes of someone droning over slides while the audience does their email is just background noise with a calendar invite.

We use something internally called the Engagement Triangle.

The idea is simple. You can have intimacy or you can have scale. Almost nobody gets both.

In-person dinners, coffees, small meetups? Incredible for trust. You get the full human experience. But you can't scale a dinner to 10,000 people.

Social media, blogs, newsletters? Massive reach. But your developers have limited sense of who you actually are. It’s words on a screen with no intimacy.

The sweet spot sits in between…A GOOD developer workshop.

A good developer workshop feels like a working session, not a lecture where you're holding your attendees hostage with a screen share.

Your attendees actually turn their cameras on. You gather an agenda at the start based on what people are wrestling with. No more than ten minutes of training. The rest is a real facilitated conversation where people interact with each other, not just with a presenter.

We do this with a ton of our clients. The trust it builds is real, the cost is surprisingly low, and it consistently leads to the kind of relationships that turn into actual business.

Stop defaulting to the extremes. The middle is where the results are.

One again, outwitted by a kid.

Your competitors are several times your size, and they're handing out hundreds of dollars in free credits just to get developers in the door. How are you supposed to compete with that?

We had a client in exactly that spot recently. They looked at all those credits being thrown around and asked us the same question.

Our answer surprised them.

"Don't." 🙅 

Think about the last time you evaluated an infrastructure product. You weren't looking at one company. You were looking at five, six, maybe ten. Every one of them had a website full of benefits and trade-offs and pricing tables that all started to blur together.

That's an enormous amount of cognitive load. And in infrastructure, where getting it wrong is expensive and hard to undo, the confusion compounds fast.
Free credits don't solve that. A person does.

Not a salesperson. Someone who'll sit with a developer and help them figure out whether the product is actually right for what they're trying to build.

The worry we hear is always the same: that sounds expensive to deliver. But look at how it actually plays out. Most people don't book a call for every little thing. They fire off a quick async question and move on. The number who need deep, hands-on help is small, and the cost of showing up for them is far more manageable than it looks.

In a market flooded with AI, the companies that win developer trust aren't the ones with the biggest credits.

They're the ones still investing in real human connection.

Farewell to writer, mother and friend Sara Peyton

PROGRAM MANAGER + COMMUNITY RELATIONS I create programs to engage community for O’Reilly Media and for the Russian River area in Sonoma County, CA.

For those of you who knew Sara Peyton who worked for O'Reilly for many years leading our PR department, she passed last week. There’s a service in Occidental, CA on Saturday, June 20th. 

I had the pleasure of working with Sara and traveling with her and sometimes her husband George. It was a magical time at O’Reilly. We worked long hard days for events, books, people, and other special projects—always with a sense of humor.

Thank you Sara for always being there for me when I needed you. 

https://lnkd.in/gHNyDMp7

Don't skimp on your docs, peeps. 👇

So, OpenAI hits 1billion active users, the fastest in history...but also...52% of people are worried about how AI impacts their job, 57% of people are "secretly" using AI at work, and 80%+ of companies have struggled to report an enterprise-grade AI benefit in their companies.

What is going on? Here's my take 👇

Any chance we could go back to a LinkedIn without all the political ranting? Let’s not turn this into Dorkier Facebook.

We revolutionize broadband customer experience - at DT and for the industry

1 Million RDK Routers Online – and growing!
We are proud to have surpassed 1 million RDK-powered routers on the Deutsche Telekom platform.

This milestone enables our customers to benefit from better Wi-Fi performance, innovative features such as Security and Parental Control, and improved diagnostics that help us deliver faster and more effective support.

A huge thank you to everyone who contributed to this success, especially our colleagues from B2C Broadband, Product Management, Development, Testing, Delivery, Sales & Service, and all supporting teams.
Your dedication, expertise, and teamwork made this achievement possible.

Here's to the next million!

#DeutscheTelekom #RDK #Broadband

Want to know why every tech company who survives goes open source?

Ft. The Linux Foundation, React, PostgreSQL Global Development Group, Neon Postgres, Netflix, Cloud Native Computing Foundation (CNCF), Kubernetes (Official), Red Hat, Canonical, LibreOffice, MariaDB, Microsoft, Salesforce, Stateshift

This is how we think about which channels to prioritize in GTM...the balance between intimacy/trust and scale 👇

3D printing in the backyard with the boy. 🤘

GitHub didn't win 150 million developers by running ad campaigns.

They won by talking like a developer to developers.

No buzzwords. No "enterprise-grade collaboration platform." They called it what it was: a place to share code. Then they wrapped it in a concept developers immediately understood and wanted to be part of. Social coding.

The genius was in how they designed the whole experience around that idea. Your profile showed your contribution history, not your job title. Your work was public by default. You could fork someone's project, improve it, and send it back. Every interaction matched the way developers actually work.

And the language stayed authentic the whole way through. The docs read like they were written by engineers, because they were. The community guidelines felt like they came from someone who had contributed to open source, because they had.

Most developer companies are still trying to impress developers with polished messaging. GitHub proved developers don't want to be impressed. They want to be understood.

GitHub gained far more developer mindshare than Atlassian...and this was a crucial ingredient 👇

Believe it or not, there are more important things than free tokens/credits...

This is so sad. Sara was amazing.

The story of how Mozilla Firefox took on Internet Explorer (and won) is fascinating...and there were 3 core ingredients that made it work... 👇

The way in which Patrick Collison and John Collison at Stripe took on PayPal...is a masterclass in "simplicity is the ultimate sophistication" applied to developers. Here's the story. 👇

"AI saves you so much time!"...*proceeds to spend hours doing nothing but bloody AI...*

Sitting on my throne defended by the hounds of doom. Just don’t chuck a snausage or I am screwed…

Love, Ronny, but thinking you can "kill AI" is just delusional. AI isn't going away...and we need to figure out a world where the magic of human creativity and the usefulness of AI coexist. Sticking your head in the sand isn't going to work.

There is one boring thing that every successful developer tools company has:

Great documentation.

Developers evaluate your docs early, sometimes before they touch your product.

If your docs are confusing, outdated, or buried behind a sign-up wall, most developers will close the tab before they ever try it. 

If the quickstart guide takes more than five minutes to reach a working example, they leave.

If the API reference reads like it was written by someone who has never used the product, they leave.

If the docs look like they were last updated six months ago, they leave.

Your documentation is your first product experience. 

Before the free trial.
Before the demo.
Before any conversation with sales.

It's the moment a developer decides whether you are worth their time.

The companies that understand this treat their docs the way they treat their product. They version it. They test it. They measure how far developers get before they drop off. They write it in the language developers actually use, not the language the marketing team approved.

You can have the better product and still lose. Developers never got far enough to find out.

One of our clients at Stateshift is the RDK project, an open source project for powering video, broadband, and IoT devices. Here is one of many examples of the impact they are having. 🤘

It took me way too long to realize that fear/anxiety massively dictates not just what I *avoid* doing, but also where I *justify* spending my time too...

"Opposite positioning" is a powerful way to compete when you are an underdog - e.g: Red Bull charged 3x more than The Coca-Cola Company, used tiny cans, and it tastes disgusting. Today they dominate a $10B+ market.

Stripe, 37signals, and Kit did the same. Here's how to do it.

Here is how we doubled active engagement for one of our Stateshift clients:

1. Get razor sharp on (1) the economic buyer and (2) technical user.
2. Build differentiated positioning. You have to be unique in a sea of average LinkedIn bollocks.
3. Measure activation: Interest > Intent > Implement. All the growth in the world means nothing if people can't get started without smacking their heads into a wall.
4. Review *all* data on (1) needs, (2) common problems, (3) trending topics/interests and anchor new new content and engagement to them.
5. Show up *every day* not just with content, but with *engagement*. Be a human - build relationships, be a shoulder, be a mentor, solve problems, challenge your audience on broken beliefs - this is what separates out experience from a transaction.
6. Focus on #ProgressOverPerfection. Sweating bullets on a campaign is a waste of time and energy. Do it, be imperfect, measure it, optimize it.
7. Intuition is good, data is better. AI enables us to play data like Dave Mustaine plays guitar in Megadeth. Use it to make informed decisions, your gut is unreliable.
8. Banish bullshit enterprise/marketing speak. Technical audiences hate enterprise and marketing talk. Talk like a person, not a LinkedIn post.

The key is rapid iteration. Bit by bit, day by day, the numbers will climb.

I can't be the only one wrestling with how to maintain and manage agent sprawl...how are you all handling it?

How many of you are using open models? What has been your experience? Considering deploying some for us…

There is no such thing as an "average user", and we need to STOP building products around them. Here's how Stripe and Nintendo lean into the edge cases to build incredible products...

Best swag ever… (in my opinion at least).

"Vibe coding will kill SaaS", but the data suggests otherwise:

→ Enterprise build-vs-buy ratio flipped from 53% buy in 2024 to 76% buy in 2025 (Menlo Ventures)
→ 35% of teams have already replaced at least one SaaS tool with a custom build. 78% plan more in 2026...but they're not abandoning software. They're building lightweight tools NEXT to the heavy ones they're still paying for. (Retool)

We use vibe-coding (shout out to Anthropic's Claude Code) extensively at Stateshift, it is awesome, but be aware that vibe coding takes the money cost of software and converts it into tokens (cheap) then quietly hands you back a time bill that's enormous.

SaaS isn't dying. It's reshaping towards MCP servers, composable components, embeddable pieces you plug into your workflow rather than monolithic platforms you log into.

People will keep buying software. They'll just buy smaller, sharper, more composable pieces of it.

Developers can sniff out marketing bollocks from a mile away, and it sends a message that you and your company don't understand them.

A lot of companies get wrapped up how write for devs, but it is simple: talk like an *actual* human...like someone you would meet in a pub or coffee shop.

No buzzwords. No flowery language. No complex language that makes you sound smart.

The reason developers are suspicious of marketing is because they consider it inauthentic and manipulative. When you are straightforward and to the point, devs engage.

Developer Relations Engineer

Head of Developer Relations @Tailscale

My team at Tailscale is hiring a Devrel Engineer! You get to build cool stuff, talk about it, and play with fun tech all day. UK, Canadian, and US applicants welcomed.

https://lnkd.in/eSgwdSKZ

Community Marketing Manager at Coder

Caught up with Jono Bacon at Open Source Summit. Reminded me how, his book, People Powered was such a reliable resource while navigating my start in developer communities. 

You should give it a read: https://lnkd.in/eba2iPTZ

The Redpoint InfraRed 100 is now live.

These are the companies building the infrastructure that powers everything happening in AI right now, from world models and agent runtimes to the sandboxes, databases, and security tools agents depend on.

Congratulations to this year's honorees! 

Read the full 2026 InfraRed Report: our state of the union on AI and cloud infrastructure 👉 https://lnkd.in/eEevP-Wd

I am generally skeptical of these kinds of lists...but the InfraRed 100 has real depth in terms of the quality of the companies features as well as the material, data, and analysis in the report. Well worth a look. 👇

Taking a bit of time off makes you better at your job, and is an antidote to a pretty nasty burnout cycle. If you are in the US, take some time off today...

Agreed. (1) fun, (2) useful, (3) quality design, (4) not another damn water bottle.

What are the best examples of realistic fiction that people believe in tech? We often see these:

 * "This problem is catastrophic" (it is usually a pain, not world-ending)
 * "We need a meeting every week for this" (usually not needed)
 * "He is an asshole, but really smart/productive" (an asshole is still an asshole)
 * "My website is fine" (nope, it is too dense and confuses people)
 * "We don't need to track this" (if you don't measure it, you don't improve it)

What are yours?

If you want to build a large, engaged technical audience, you need to focus on this sweet spot. We do this with our clients at Stateshift, and users/devs love it. 🤘

Awareness building is the sexy part of developer marketing.
Fixing your activation process is DISTINCTLY unsexy.

And it's the one most companies are ignoring.

Try this. Out of every 100 people who land on your website, how many click to start signing up?

Not complete it. Just start it.

For most companies, when we baseline this for the first time, it's around 10%. That means 90 people you worked hard to attract just left. And no amount of awareness spend fixes that.

Fixing your headline. Fixing your subheading. What's above the fold. How you present the problem you solve and the proof that you solve it.

Not glamorous. But it's what determines whether all that awareness building actually produces anything.

We always look at this first with our clients. Because pouring budget into awareness when the activation process is already leaking is the most expensive mistake in developer marketing.

Is your team spending more time getting people to the site, or improving what happens once they get there?

My Whoop gets real mad at me when I am on the road. A tiny little lecture every day.

If you are not using MCP to access dev/user usage data, you are flying blind (and making yourself miserable.)

CMO, Board Member, Advisor

Easy to get going. Fast to start.

Great to see old and new friends alike at the The Linux Foundation Open Source Summit such as Jim Zemlin, Barton George, Manish Dixit, Kier McDermott, Jeremy ☕ Meiss, Katherine Druckman, Paul Hinz, Angela Brown, Sean 👋🏼 O’Dell, Donnie Berkholz, Ph.D., Dave Neary, Brian Proffitt, Marco Martinez,  many others.

This is SUPER important. All the social/podcast/YouTube/influencer traffic in the world means nothing unless you can convert them into users...

We designed Guild for how everyone works... including right out of the CLI. 

Check out this little demo from Corbett Waddingham to see how you can build and manage agents with Guild in the command-line. 

One control plane to rule them all.

Remember when getting stuck on a CSS bug meant posting on Stack Overflow, sifting through 40 comments, and finally finding the one answer that saved your project?

That was what once built developer communities.

Developers debugging each other's code at 2am… Conferences where you'd finally shake hands with the person whose repo taught you more than your degree did.

AI has changed that. Stack Overflow went from 200,000 new questions a month to under 50,000 in three years. Developers get answers in seconds now. 

The friction that used to force people to ask publicly, learn together, and accidentally find each other is disappearing.

And no, this isn't an anti-AI post. We build with it every day. We think it's one of the most important tools developers have ever had.

Instead, we see a shift in what actually drives developer communities now. It's less about SOLVING…and more about CREATING together.

More spaces built around what people are creating, not just what they're stuck on. More hackathons where people leave with friendships, not just a repo. More local meetups where someone demos a side project and gets real feedback, not a forum page.

AI handles the answers now. So it gives us the room to invest more deliberately in the things it can’t replace.

So here's one thing worth asking: "If AI could answer every question in your community tomorrow, would people still show up?"

If not, it might be time to build the thing that would make them want to.

Has anyone figured out how to manage skills files  (and how they inherit skills) effectively?

I just donated. You should too.

Goodbye boring "Verbose/Debug Mode", hello Waffle Mode. This may be my greatest ever achievement.

TIL: Microsoft Publisher still exists. What other ancient tech is still alive?

Installed OpenClaw over the weekend and blown away...but want to tap your brains.

I hear some horror stories of people who give it guardrails (e.g. "don't post ANYTHING without my express written permission") and it ignores it and posts anyway.

I am sure this can happen, but would love to know how much you have experienced it yourself?

How big of a problem is it that OpenClaw ignores your guardrails, and what have you done to prevent this from happening?

Travel Hack #212: Don't have an iron in your room? Hairdryer gets wrinkles out of clothes. OK...now share your travel hacks for when on the road...

Lots of people are saying SaaS and open source are dead because of AI. I think we're just in honeymoon period. Would love your thoughts? Am I right? Wrong?

cc/ Heavybit, Paul Dix, Brian Douglas

Anyone heading to the The Linux Foundation Open Summit next week in Minneapolis?

Saw this in Hawaii - get a tattoo, discount for life. Crazy but it worked. What is the most inventive incentive you have seen?

Don’t skimp on your skills when building agents…

3 simple but effective things to focus on when building agents 👇

Everyone needs a role model.

Software Ecosystem Leader | Building Developer Communities at Scale | Open Source Security and AI Advocate

Something I've been working on for a while is finally happening! Next weekend I'll be in San Francisco for the JetBrains Codex Hackathon at SHACK15, and I could not be more excited.

We're bringing together serious AI builders for two days of hacking on real projects using JetBrains IDEs and OpenAI Codex. I can't wait to see the REAL projects people build over the weekend.
I'm especially excited about the judges I get to hang out with. Thank you, Jono Bacon, Kyle Rankin, Avi Press, and other friends of JetBrains and Cerebral Valley. This is going to be a great crowd!
First place wins something very cool.

If you're in SF and this sounds like your kind of weekend, applications are still open: https://lnkd.in/gYqDMGgr
See you there! 🛠️

You can dominate LinkedIn, podcasts, and YouTube, but traffic isn't the problem. Activation is. Here's the system we use to turn visitors into customers 👇

Naming is hard...took forever to come up with Stateshift. Naming the Eight Sleep...was harder.

So, our approach to agent evals is (1) one or more eval criteria ranking agent output from 1-10 (LLM as a judge), (2) each eval criteria is weighted to calculate a final score. How are you doing evals?

In the age of AI, the most underrated competitive advantage isn't more automation. It's a human you can actually talk to.

Earlier last year, a client asked us which AI search tools were recommending their product to developers. They had no idea. Neither did we. Nothing in

Your Developers Are Searching AI for Tools Like Yours. Are You Showing Up?

Most developer-focused companies are optimizing for Google but have no idea whether they appear when developers turn to AI tools for recommendations.

We tested that for six months across our own brand and client accounts. 

Here’s what we learned.

Donate to Troy feeds everyone. Now he needs us. Let’s help!, organized by Noel Ponthieux

Retired from The New Stack

Hey all, Troy Howard got the triple whammy. He had a heart attack, a big bill, and then got diagnosed with a rare genetic condition that means some changes for Troy. There’s more about what this means for Troy on his GoFundMe page. 

https://lnkd.in/gu4hzEDK

I’ve been chatting with Troy over the past few weeks and you should, too. Troy is a hero of the docs world. Ask him how Twitter found him and hired him to manage their docs.

Just reach out to him. And help him out if you can. He’s been helping feed people for years. He’s a big spirited,  geeky guy. And he could use your help. 






.

We spent the last month building 25 AI agents. But we realized we were doing some things wrong.

Here are 3 things that made them significantly more effective:

1. One agent. One job.

Every time we gave an agent more than one role, the quality dropped. When we split research, writing, and quality checking into separate agents, the consistency improved immediately.

Specialists outperform generalists every time.

2. Your agent is only as strong as what you give it.

Our writing agent kept producing generic output. Then we gave it three things: voice guidelines to follow, the proper content structure, and real examples of what good looks like. We also started feeding it context - voice note transcripts, reference materials, anything that gave it the raw material to work from.
That fixed it. Without those inputs, it had nothing to build on.

3. Don't just re-prompt. Ask the agent what went wrong.

When output went sideways, we stopped immediately re-prompting with more instructions. Instead, we asked the agent to explain why it went off track.
Then we used that feedback to fix the agent instructions themselves - not just work around the problem, but update the underlying prompt so it wouldn't happen again.

If your agents keep making mistakes, the problem is probably not the agent itself but what you are giving it to work from.

Guild Forge — For Developers · Luma

One our favorite clients at Stateshift is Guild.ai - they have built a control plane for AI agents, with collaborative tools to make it easy to both deploy and manage agents across organizations and projects easily.

I am kinda choosey about who we work with at Stateshift, and only work with companies with a killer product that lines up with how devs think, and when James Everingham and Chris Waterson demoed it, I was super-impressed.

Well, they are doing a dev meetup at their office in San Francisco on the 29th April where they will be building agents that can run in production and live-coding open source agents from scratch. No slides, no BS.

If you are interested in going, you can register here:
https://luma.com/bjsqe9se

So, Erica Brescia and I had been looking for a piece of art for the end of our living room...and in doing so immortalized a whole bunch of our friends with keyboard keys.

The story started when we went to dinner with Sid Sijbrandij and his wife, Karen, and we saw an amazing piece of art of they had commissioned, made from old keyboard keys.

On the ride home we had the idea of commissioning a piece of art from the same artist and putting the names of people who we care about weaved throughout the piece. You can see Jonas Rosland as an example here.

We wanted something happy and bright, so with our 13-year-old son, and a liberal amount of AI and Canva, we came up with the artwork together.

Why 'Smile'? Well, when I first met Erica, I wrote and recorded a song for her called 'Smile', and that word has become the ethos of our family. :-)