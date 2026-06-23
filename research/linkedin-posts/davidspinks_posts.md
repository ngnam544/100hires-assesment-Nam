# Recent Posts for davidspinks

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

founder and community coach | writer of the “enough already” newsletter | author of “the business of belonging” | dad to three feral kids, hiker, baller, zen meditator | davidspinks.com

you're not stuck on a career decision. you're negotiating with a five-year-old who was taught they needed to achieve in order to be loved, and is terrified that if they slow down, they'll stop mattering.

if you're ever anxious, or find yourself comparing yourself to others, try this one neat trick:

remember that everyone, yes everyone, has at least a little bit of poop in their body. 

og anunoby while tipping in the game winning shot? poop in his body. 

taylor swift on stage at the final show of the eras tour? poop in her body. 

your ceo? probably a lot of poop in their body because they're so busy they forget to drop the kids off at school. 

go ahead and walk around your neighborhood, and as you look upon the people passing by, note how each one has at least a little bit of poop in their body. we all do. it never fully empties you know? like, there's always a bit more cooking. 

there, don't you feel better now?

follow me for more life changing advice that might get me banned from linkydinky.

there are 1-2 slots remaining in the community business mastermind!

we already have a great group of five community business owners who:

- are generating at least $100k/year
- are looking to grow and scale up their operations
- are looking for a group to go deep with, both on their business and themselves

if this sounds like you, message me or comment and i'll reach out. we're finalizing the group this week.

the root of much suffering today: our lives are filled with connection yet devoid of intimacy.

Building a Community Business 101 - Day 3:

How to make money! (everyone’s favorite topic)

So money is a prickly subject for a lot of community builders.

For many of us, there’s a feeling that community is one of those things that should be free, like water and air. Don’t we all have a right to community? Should we be charging for belonging? Feels ick don’t it?

Well, this is one of the primary reasons I see community founders burnout and community businesses fail. 

I want to see community builders be wealthy! And by wealthy I mean your needs are met, you have abundance, so you can put your energy into building community without any financial fear or resentment. 

The reality is we live in a system where we need money to survive. Love it, hate it, run from it, and money (and your relationship to it) will be waiting for you. 

If you want to build a sustainable community business that both provides for your needs and the needs of members, then getting the money equation right is critical.

How much to charge is really variable and based on your audience, their ability to pay, the value the community is driving for them, and how big you expect the community to be.

You can make your community highly affordable ($15-$50/month) and have thousands of members, like the Old Girls Club or Generalist World. Great businesses. 

Or you can charge a premium and keep it small ($100-200/month), like The Creator Lab. 

Or you can do both, high cost, and thousands of members, like Hampton, Chief, or YPO! These end up being much larger businesses so just make sure that's actually the job you want. 

Each of these communities are very successful as a business, and it’s because their pricing and size is right sized for their members, the value they’re delivering, and the needs/visions of the founders.

Some of them also offer different tiers, so you can have a more affordable option for most, and charge more for members who want to make a bigger investment for more value.

I’m a big fan of membership fees because it aligns the community with the business model. It’s also subscription based, which brings a bit more consistency to your business.

But there are lots of other models to use for your business:

- Sponsorships - charge for the ability to reach your members
- Recruiting - charge companies who want to hire your members
- Investment funds - raise capital from members and/or invest in member companies
- Events - sell tickets to one-off events and workshops
- Products and services - have a free community that you sell products and services to

Whatever you do, PLEASE don’t undercharge. 

Consider this: what if you're actually doing your members a disservice by not charging them more? 

Chew on that and see what truth emerges. 

--

Hit +Follow for more community business 101 tips this week. 

And check the comments for info on the two Community Business Masterminds I'm kicking off. Apps due on June 14!

quick sunday note to say LETS GO KNICKS

and also that applications for the Community Business Mastermind closes today! 

we're bringing together two small, curated groups of community business owners for a 6-month mastermind where we're going to work together to help you achieve your goals and build the communities, businesses, and lives you dream of.

there are two masterminds:
1. for those launching new community businesses
2. for those with established community businesses looking to scale growth and ops

get the details at davidspinks.com/mastermind

can't wait to kick off this journey with you all!

you know what makes me weird? 

...ok you know ONE of the things that makes me weird?

i like taking surveys.

they're so fun! you get to learn a lot about yourself when you complete a survey. it gives you a little snapshot of where you are at this moment in time. i've never not found it valuable to be asked a bunch of questions about myself or my work.

so, if you're also weird and like getting interviewed via internet form, and you're working in the community industry, you're in luck! the cmx community industry survey doesn't close until TOMORROW! 

take 15 minutes and fill it out now. this research has been provided free to the community industry for many years, with the intention of providing benchmarks, track trends over time, and give you some juicy actionable stuff you can bring to your work.

15 minutes today, to support your profession. what a deal! do it! 

still not convinced?

come onnnnnnnn

convinced now?

cool, you can take the survey here: https://lnkd.in/euKMCHKa

here's what i'd love for people to do every time they share a graph of their business growth online:

include a graph tracking their joy, connection, time with friends and family, and mental and emotional health over that same time...

just so we can get a clearer idea of exactly what that growth may have cost them before we put it on a pedestal.

Co-founder & CEO of Blomma 🌼 A Career Coach powered by AI, accessible to all. Former leader at Canva, Pinterest.

On June 22nd, I'm hosting an evening in Brooklyn at the Fabrik HQ with 🌀 david spinks Gwen Wiscount and Devin Karbowicz about something I think about a lot: what it actually takes to step into the career you want without leaving your values behind. 

This evening is for community professionals who are building careers as intentionally as they build communities. We'll get into the tensions that come with ambition and what shifts when you stop treating it as the enemy. 

To close the night, I'll lead a live coaching demo with Blomma so you can see exactly what that support looks like in practice. 

A delicious dinner, great people and conversation will be had. We hope to see you there! Link to join us is in the comments.

Ok, real talk time: the business side of my coaching practice has been on the struggle bus these past few months.

At the start of the year, things were poppin, and I hit an income goal I didn’t expect to hit for another couple years. “I’m doing it! I’ve figured out how to be a full-time coach!” I thought to myself as I shook my fist at the imaginary haters in my mind.

But what goes up must come down (must it though?) and after some existing clients concluded, and leads slowed down, my income dropped substantially.

I wish I could say I was as cool as a cucumber about this... alas, with a new mortgage, 2/3 kids still in childcare, and depleted savings after the big down payment, this triggered all sorts of money fear for me. Going broke is right up there with being buried alive and losing my kids at the carnival in my list of top fears.

So I spent about a month feeling very ungrounded and had a frantic energy around the marketing and sales side of my coaching practice. I could feel the desperation seeping into what I was writing online and in my conversations with potential clients. I spun on my coaching positioning, trying to nail down exactly what my niche is, convinced that this was the problem. I spent hours with Claude trying to get the language just right on my website (I’ve learned that AI is an especially dangerous timesuck during these moments of panic).

To make things harder, I received some critical feedback from a couple of my clients as we concluded. They shared that they started to feel lost with coaching, unclear of what to focus on in each session, and that they wanted more direction from me. So I started to doubt my abilities as a coach, and worried that I’m not going to succeed in this work that I love so much.

It’s hard to be honest about these moments because I tell myself a story that people want to hire a coach who’s unflappably confident and in high demand. But I’m not here to put on a show for anyone. For anyone who hires me as their coach, I want to be 100% in integrity with them. I’m feeling very confident again in my practice now (more on that in a minute), but for a little while there, I was questioning myself.

I also want to practice what I preach. I work with my clients regularly through their moments of panic and self-doubt. We all have them, even your coach or therapist. And so these moments give me an opportunity to practice exactly what I offer to my clients, which will in turn help me better serve them.

I’m really proud of myself for how I moved through this slow period. Past me would have just kept trying to push through, and been stuck in panic for months… maybe never leaving it. To some degree, I think I remained in this state for most of the eight years of leading my company. 

This time I responded differently. If you're curious about how I moved through this season, and what I've learned and adapted in my coaching practice, I just published a newsletter with the details. Link the comments 👇

isn't it ironic that in our pursuit to combat loneliness, we community builders put ourselves in a position of great loneliness?

there are few places more lonely than being responsible for a community. i know this from experience, and from talking to thousands of community builders in the last 10 years. every single one of us feels alone with our challenges to some degree.

we spend every day serving others.

we feel like they can't be totally honest about our struggles,

like we have to put on a brave, confident face for our community and team.

we feel like there's no one else to lean on, 

like it's all on our shoulders to figure it out.

we want to build genuine community while also taking care of our personal financial needs,

but we're afraid of being seen as greedy, which feels shameful.

shame is the root of a particularly brutal form of loneliness.

regardless of how a community is organized, it's lonely. it's lonely at the top. it's lonely in the middle. it's lonely to hold responsibility for a group of people.

we could say "just distribute leadership" but that comes with tradeoffs too. decentralization isn't always the answer. 

the one thing that has worked for me throughout my career as a community founder: forming an intimate group with other community founders.

the key is to find people who are:
- at a similar stage as you
- willing to be vulnerable and transparent with you
- open to sharing everything they're learning and experimenting with
- committed to being part of a group where you actively help each other succeed

when i have a group like this, i no longer feel so alone. i feel like i'm part of a team, with a group of people who truly understand what it's like to be in my position, and are ready to show up for me.

on the weeks where i'm struggling, i find peace in knowing that i have a call coming up with my group, or i can message the group and get support, reflections, and ideas.

want a group like this for yourself?

make a list of five people you'd want to have on your personal "board of advisors", who meet the above criteria, and ask them if they'd want a group like this.

major key: creating a strong container is critical. these groups fade quick when expectations and agreements aren't made clear up front. how is everyone expected to show up? what are attendance expectations? what intentions are you agreeing to? 

i've done this probably 10 times throughout my career and, every time, it's been life and career-changing.

if you try it, let me know how it goes. i'd love to see more people have access to groups like this.

--

p.s. if you're building a community business, and looking for a formally facilitated version of this, i'm kicking off two masterminds later this month. i'll be facilitating, holding the structure, and personally coaching the group over six months. i'm taking applications until this sunday, june 14th.  drop a comment below if you're interested in joining and i'll send you more info!

do community builders place a glass ceiling on their own growth? 

many do, yes. 

i know because:
- i did (and it's still an edge for me)
- i see it regularly in my coaching clients

the stories usually look something like this:

"i want to grow my personal brand but i don't want to take up too much space"
"i want to feel financially secure, but i don't want to be greedy"
"i want to build community for a living, but something feels ick about making money through community"

it's these tug-o-wars that community builders have going on within us that keep us stuck. we believe that if we get too big, or make too much money, or come across to salesy, that we'll be violating our values or hurting others. so we make ourselves smaller and self-sabotage any time we reach a level of leadership or wealth that crosses our "upper limit" as gay hendricks talks about in his book, "the big leap"

but here's what i've learned: it's not either-or

you can take up space and still be of service
you can make lots of money and not be greedy
you can make money by building community without violating anyone

in fact, i've found that the more a community builder learns to welcome in the parts of them that long for these things, the more they're able to serve their communities in bigger ways.

there's a lot more to unpack here, and that's exactly what we're going to be doing on monday in brooklyn.

join Silvia Oviedo Lopez, Gwen Wiscount, and me for a panel moderated by Devin Karbowicz on ambition, community, and career growth, hosted by Blomma, CMX, and Fabrik.

Register: https://luma.com/bv3opcmp 

excited to see you all there!

anyone who thinks ai can replace coaching is exactly who needs a coach. 

because to believe that, you'd have to believe that life is just about access to information, and you've forgotten the experience of being in a body, connected to other people being in their bodies. 

that's exactly what great coaching can help with. reconnecting you with your humanity, after a lifetime of treating yourself like a machine.

building a community business 101 - day 6️⃣

let's talk about the silent community killer:

i call it "community creep"

no, i'm not talking about funky frank who talks way too close to your face at the community happy hour (though that's also a problem)

i'm talking about the unconscious tendency to add more programming, spaces, channels, and stuff to your community (like feature creep, but for communities)

it usually starts simple. a slack group. occasional workshops and dinners. a newsletter.

and then more programs and spaces creep in. annual research. masterminds. office hours. local chapters. a knowledgebase. courses. sock parties where everyone can only talk to each other through sock puppets

and one day you look up and realize the community went from a small village to an urban metropolis with a lot of dead ends.

it’s what happens when we try to add more and more value to our community, but never cut or clean up anything.

i know i know... it can feel hard to cut things from a community. what if some people still want it?

a quick story...

recently i coached a community founder who was feeling overwhelmed. there was SO much to do and they couldn’t keep up with it all.

together, we audited their community and found that there was a monthly event series that was taking up a huge amount of time and energy, but wasn’t nearly as well-attended as it used to be.

but they didn’t want to get rid of it. it felt like an important tradition, going back to the origins of the community. 

alas, the writing was on the wall. the community had become too bloated. they had to make cuts to their programming or they were going to drown.

we decided they would host a funeral for the program. they invited all their members to attend, and made it into an incredible experience where they got to celebrate their best memories from the event program, and grieve its ending together. 

what originally felt like a loss to the community ended up bringing everyone together even more deeply. and on the other side, the founder and their team felt SO relieved to have the space to focus on more meaningful programs. AND there was one less program for community members to have to decide if they were going to engage with.

win win win

here's how to do your own community audit:

list out EVERYTHING going on in the community. every channel, program, event, piece of content, etc. anything that’s there on an ongoing basis.

for each one, give it a rating:

1. is it providing value to members?
2. how much time does it take us?
3. is this bringing us joy to organize?

shut down dead spaces. cut programs that have long run their course. eliminate what’s draining your team and the community of energy.

your community and your calendar will thank you 

--

p.s. if you're building a community business (or want to) i'm kicking of two (2!) six-month masterminds to help you achieve your wildest community goals. take a look see here: davidspinks.com/mastermind apps due June 14th!

Building a Community Business 101 - DAY 2: 

How to design meaningful onboarding experiences:

Most onboarding experiences either do way too little, putting all of the pressure on the member to figure things out, or way too much, overwhelming the member with a huge task list right when they walk in the door.

You have to right-size the difficulty of onboarding for the community.

For *most* communities, I think about onboarding like I'm welcoming a friend to a party where they don't know anyone. Welcome them at the door. Spend quality time with them to help them feel settled and connected. Offer them a drink. Show them around the house, point out the bathrooms, and then, when it feels right, introduce them to a small circle.

But for some communities, having a more intense onboarding is part of the experience. Like converting to a religion, for example. The friction is intentional. 

Neither approach is better or worse; it's just about the type of community and experience you're designing for.

To be really intentional about designing onboarding, I like to ask five questions:

1. What do you want this member to learn?
2. How do you want this member to feel?
3. What do you want this member to experience?
4. Who do you want this member to be connected to?
5. What do you want this member to do?

For example, you might say:

1. I want this member to learn the purpose of our community and how to navigate the platform. I also want them to learn a bit about the culture and vibe of our community.
2. I want this member to feel like they just found a group of people who care about their success, and are ready to show up for them. I want them to feel safe, welcome, and energized.
3. I want this member to experience a little magic moment, getting something above and beyond what they expected. And I want them to experience a moment of connection with at least one other person.
4. I want this member to be connected with someone on our team first, who will then connect them with a “buddy”, and to new members who are going through the same initiation experience as them.
5. I want this member to book a call with a team member and their buddy, and when they’re ready, to introduce themselves to the community. Otherwise, I don't want them to have to do too much. I want them to take their time and engage in the community at their own pace.

Next, go through each one and write down at least one action or ritual you'll take to create this experience. 👇 I'll put some examples in the comments 👇

Boom! You have an intentional onboarding.

It doesn’t have to be perfect. Keep it simple, try something, and keep tinkering.

And remember: You're taking the first steps of a long journey together. You don't have to speedrun their experience.

--

P.S. I'm kicking off two mastermind groups: One for launching a community biz and one for scaling an existing community biz. Applications due June 14. Deets in the comments! 👇👇

can we take a moment to talk about what makes great swag? 

there are levels to this game. 

people don't want to wear your cheap polyester, ill-fitting tshirt with your logo on it. 

what people want in swag is something that:
- feels high quality 
- makes them look sexy
- communicates something that represents an identity they want to project to the world 

it could communicate that i have a sense of humor, like the shrug socks Niv D. once sent me 

it could just look cool  like the blackbird hat Joel Connolly once gave me. 

or it could have a message about something i believe in and start conversations like this hat Raechel Lambert just sent me. 

this IRL > URL hat has it all. super high quality, fits my sexy dad motif, and has a message that i believe in and will undoubtedly start conversations. 

which means that when people ask me about it, i get to say "oh yeah my friend sent me this. she runs a company that helps creators launch dinner clubs with their audience. i know, cool right? yeah they spell it DNNR, look them up. what? sure you can take a pic. 😘✌️"

which is 1,000x better than if she just sent me a cheap shirt that said DNNR on it, which would promptly become a dish rag. 

i'm going to wear the crap out of this hat just like i did with those shrug socks and that blackbird hat because it makes me feel good to wear. 

that's what good swag optimizes for. making the person wearing it feel good, not making them feel like a cheap billboard.

i don't know about you all but i'm seeing *a lot* more community businesses coming out these days. 

lots and lots of professional memberships, masterminds, and creative IRL experiences. more than i've ever seen before. 

i think it's a combo of a response to the loneliness epidemic, layoffs leading to more solopreneurs, ai making it easy to build and design community spaces and assets, social media quality declining which is sending people to more private intimate communities, ai making us crave irl human connection, and more and more great examples of successful community businesses to model after. 

it's an exciting time to be building a community business.

Just received this email after a coaching session.

Let this be a warning: You might leave with something different than what you came for when booking a coaching session with me 😁

This was a complimentary coaching session. I offer a bunch of these every month. If you're interested in doing a session together, you can apply here: https://lnkd.in/eYfQK-kt

(sharing the email with the clients' permission)

Building a Community Business 101 - DAY 4

How to get a NEW community off the ground 🚀

I get this question all the time. You have a community idea in mind. How do you get started? Should you start looking at tools and software? Create a marketing plan? Kick off a beta? Start designing a brand?

There are so many things you *could* do to get a community started. Knowing where to begin can feel very overwhelming.

Here's how I look at it: 

Communities are a lot like solar systems 🪐 (stick with me here, I promise it'll be good...)

And people? People are like space dust. And just like space dust, we're attracted to each other. More precisely: we're attracted to where there is "social density". When there's a group of people connecting in a way that we want for ourselves, we're attracted to that group. It's social gravity.

And so, class, when you're getting a new community off the ground, focus on creating social density. 

It doesn't have to be big. Every planet starts with two regular ol' pieces of dust coming together. 

For example, I'm in a group with two other coaches we've self-organized called "The Space". We meet every month for two hours, and give each other our undivided care and attention to process whatever it is we want to process. Every time I tell people about it, they say, "I want to join that!!!". We created social gravity.

When you have social gravity, community will just start flowing. You'll know you have it when growing doesn't feel so effortful.

How do you do this in practice? Here's the process I recommend to my clients:

1. Form a Hypothesis: Feel into the ideal community member you'd like to bring together

2. Connect and Validate: Identify 10 people who fit that identity and get on the phone or face-to-face with them. Learn about them and their potential need for community.

3. Cross-Pollinate: Offer to introduce them to each other. Start weaving social density one relationship at a time.

4. Gather Live: When it feels right, invite them all into a shared experience. A group call or an in-person experience works great here. It's better to do a live experience to start because everyone gets to spend quality, present time together.

5. Build a Home: If, after that experience, you feel a clear need for an ongoing conversational space, then open up something simple. WhatsApp or Signal can work great here. 

Boom, you have the foundation of community: A group of people who are feeling authentically connected, who care about each other, and want to continue to grow together.

If the need isn't there, start at step 1 again. 

Questions? Comment below and I'll do my best to help.

--

Thanks for tuning in! Hit +Follow to get the rest of the Community Business 101 series.

P.S. I'm kicking off two Community Business Masterminds, and we have a few spots left for the right people. Learn more here: davidspinks.com/mastermind (Applications due June 14th)

Building a Community Business 101 - DAY 5

Mapping the community commitment curve:

Once members are onboarded, over time, they’ll move up what’s called “the commitment curve”. 

This is a tool I first learned from Douglas Atkin who led community for Meetup and Airbrnb, where he used this model.

The idea here is that you don’t want to ask for too much commitment from members when they’re still early on the curve. Start with small asks. Over time, build up to bigger ones.

How to create your own commitment curve:

1. Set a timer for 10 minutes and just brain dump everything that a member does or will one day do in your community

2. Go through the list and mark each with colored markers one as low commitment, medium commitment, high commitment

3. Draw a blank curve, and put the actions in their sections

THEN PUT IT INTO ACTION:

Once you’ve mapped your commitment curve, you can start designing intentional pathways that help members gradually deepen their participation over time.

For example, after someone:

- attends an event → invite them to join a smaller group
- comments regularly → invite them to start a discussion
- helps others → invite them to mentor newcomers
- becomes a regular → invite them into leadership

Sometimes members are ready to make a deeper commitment; they just need an invitation. Now you know what invitation to offer them.

Remember: the map isn’t the terrain here. Some members will want to jump ahead. Some will hit a ceiling of commitment. Some will drop back down. That’s all okay. 

--

Are you building a community business? 

I'm kicking off two masterminds focused on helping you achieve your goals:

- One focused on helping you launch a new community business
- One focused on helping you level up your existing community business

It will be an incredible group of thoughtful, high agency founders all invested in supporting your growth and the growth of your business. I'll be personally coaching and facilitating these cohorts.

I'll drop the link below. Applications due June 14th. We'd love to have you join us for this 6-month 

--

Thanks for tuning in! Hit +Follow to get the rest of the Community Business 101 series.

NYC community builders! Come hang with me and the incredible Silvia Oviedo Lopez  Gwen Wiscount and Devin Karbowicz.  

We're going to talk about the prickly tension between ambition and community. 

I promose to keep the trauma dumping to less than 50% of my speaking time.

one of the risks of ai is that it rarely completes a conversation. 

with humans there's always a natural ending to a conversation. 

with ai you can just keep going endlessly. 

i've found myself deep in an ai hole where suddenly i've spent two hours going back and forth with it, totally lost track of time, and didn't do the tasks i was supposed to during that block. 

i think those of us with adhd are especially susceptible to this.

can businesses build genuine community? yes. BUT! we have to be clear on the conditions for belonging that business communities require, and not expect businesses to provide community beyond those conditions. 

a business isn't your family, or friends, or neighborhood, or spiritual center, or healing circle. 

we should never expect a business to fulfill the forms of belonging that it can't.

another great community role. noticing a lot of new, senior roles lately. cool to see!

Alright, this is happening! I'm kicking off a mastermind group for folks launching new community businesses.

What is a community business? Any biz where the core product is a form of community (people connecting with people). Think paid memberships, masterminds, cohorts, events, etc. 

Some of the community businesses already signed up:

- a paid membership community for folks with generational wealth who are on consciousness journeys 
- a paid membership community for folks working at the intersection of AI and community
- a community for mid-career lawyers navigating life transitions
- you?

If this is speaking to you and you'd like to calmly *get after it* with a group of action-oriented, good-vibes-only founders, comment below and I'll send you the deets! You can be pre-launch, or recently launched.

For funsies, also include a sentence about what community you're building or hoping to build so we can all get excited about the community ideas floating around the universe. 

--

P.S. I'm still curating a mastermind for existing community businesses focusing on growth, which is also half-full. If you're interested in that one, let me know too!

Decision-making is a learnable skill. Here's how to become a more powerful decision maker:

STEP 1: First determine if it's a complicated or complex decision.

Complicated Decisions: There's an objective, correct answer. The solution either works or it doesn't.

Examples:

- Filing taxes
- Running data analysis
- Writing code

Complex Decisions: There's no objective, correct answer. there are many paths and all of them have trade-offs

Examples:

- Should we raise capital or not?
- Should I hire this person?
- Should I break up with my cofounder?

If it's a complex situation, stop trying to find the right answer. There isn't one.

Instead, go to...

STEP 2: Form a hypothesis and take a small step toward testing that hypothesis.

You don't have to be right. You just need to bring some motion to the situation. Some step that gives you a new perspective.

Still, if the stakes are high, it's very common to feel stuck in indecision. Our minds want certainty. So we go back and forth in our minds, endlessly weighing pros and cons, and we start to stress, freezing in inaction.

When you notice that happening, go to...

STEP 3: Take a pause from trying to solve the problem by thinking your way through it. 

We are now in the domain of your emotions. You have to turn toward the parts of you that are afraid of what might go wrong if you choose each path. 

What I'm about to suggest sounds SUPER weird if you don't have this as a practice yet. I get it. But if you let yourself feel the fear, and all the emotions around the decisions fully, it's very likely the decision will become more clear.

--

If you're new to this practice, good news! Astrid Schanz-Garbassi and I are hosting a "Powerful Decision Making" workshop this Friday where we'll personally take you through this exact process.

I'll drop the link below...

them: listen to your gut

me: ok *closes eyes*. it sounds...um... gurgly

them: no not literally your gut... like listen to your intuition

me: um... is intuition in the room with us now?

them: dude just follow your heart!

me: like my literal heart or...

them: 👁️👄👁️

me: 👁️👄👁️

--

there's a lot of vague advice out there about how to use your intuition to make decisions and not a lot of practical guidance on what any of it means.

but BUT there are methods. really super cool methods that help you tap into sources of wisdom and information that you probably just aren't seeing (or haven't practiced using yet).

want to learn how?

join me and Astrid Schanz-Garbassi this friday for the ⚡️ Powerful Decision Making⚡️ workshop. We're going to take you through a method for tuning into your intuition, and increasing your capacity to make decisions with confidence and clarity. 

🎟️ RSVP here: https://luma.com/hc86wjxd - it's pay what you can, and no one will be turned away for lack of funds.

putting this idea out there to see if there's interest: who wants to join a mastermind group for launching a NEW community business?

some quick background:

i've been curating a community founder mastermind group for folks with established community business (still a few spots open!), and a few people who are launching new community businesses have expressed interest in participating in a mastermind of their own.

so i'm putting this out there to see if there's enough interest for me to kick off another mastermind for this group.

by "community business" i mean any business where the core product focuses on connecting people to each other. think: paid memberships, cohort-based programs, masterminds, events/conferences etc.

the idea:

⭕️ bring together a circle of 6-8 community founders for 6 months
🚀 everyone will be in the launch phase of building a NEW community business
🎯 we'll focus on helping you refine your target membership, nail down your business model, run experiments, and build the core foundation of a healthy, long-lasting community
👨‍🏫 i'll coach and facilitate, sharing all that i've learned from 18 years of building community businesses and coaching many community founders
💰this will be a paid mastermind with sliding scale pricing from $300-$500/month (additional assistance avail for those who need it)

let me know if this tickles your fancy! if there's enough interest, i'll create a brief application form and we'll start curating this thing 🙌

✨ ✨ ✨ 

^ adding some magic so that this post finds the right people

how do you keep your ai in check?

i'm curious what kinds of boundaries you've given your ai to help you manage your usage and relationship with it.

for example, i found myself going down endless rabbitholes with it when i started with a simple question that i thought would take 5 minutes. 2 hours later i've forgotten to eat lunch, didn't do my tasks, and desperately have to pee. hello adhd my dear friend!

so i gave claude the instruction: "whenever i start a new chat, ask me to state my goal for the chat, and how long i'd like to work on it right now. then check in when you sense that we may be going over time, or are drifting away from that initial goal."

this has really helped me keep my usage in check.

i bet a lot of you have figured out some elegant instructions to adjust how you use ai, and how it interacts with you. would love to share more ideas with each other so we can all benefit from them. 

drop a comment if you have a good one!

to the guy at the coffee shop who just asked me to watch his laptop while he goes to the bathroom:

ay. i shall. i vow to defend your laptop until my final breath. should someone lay a finger on your beloved technology, they will be met with unthinkable retribution. you may not have known this, dear stranger, but you have entrusted this sacred task to the right person. my singular purpose in life is to protect laptops from coffee shop evildoers. from this moment on, i will not rest. not until you return and i know that your keyboard sandwich is safe. thank you for entrusting me with this most honorable  responsibility, dear sir. i pray i do not fail you, or may god have mercy on my soul.

Can a business really make you feel like you belong? The answer is no, and the reason is in the contract.

🌀 david spinks co-founded CMX, spent years advising top companies on belonging and community, and wrote the book Business of Belonging.

Every relationship inside a business is conditional by design. It becomes harmful when companies claim to offer the same unconditional connection that true belonging requires.

Watch the full episode with Derek Andersen, link in the comments.

#belonging #community #leadership #business #divotpodcast

The ambition vs. well-being tradeoff is one of the most accepted myths among high performers.

🌀 david spinks co-founded CMX, helped define the community-building industry in Silicon Valley, and wrote the book Business of Belonging.

He challenges the idea that ambition requires sacrificing your well-being. True well-being isn't about wellness routines. It's about a sense of enoughness and a genuinely healthy relationship with yourself.

Watch the full episode with Derek Andersen, link in the comments.

#leadership #mindset #highperformance #startups #divotpodcast

when business is slow, there are two ways you can respond: 

a. you can look at it as a threat and commit to working harder

b. you can look at it as a natural ebb and an take opportunity to rest, reflect, and reorient for the next busy season 

i've always taken approach a: business slows and i panic, working 3x harder to get things back on track. 

i'm learning to take approach b: trust that i'm already doing the right things and i don't have to panic. 

it requires trust that what will ebb will flow. you don't need to do anything different. the cycle will cycle. 

curious to hear how you all respond when your business is slow. do you panic? or do you stay calm? what's your strategy?

when Justin Welsh lovingly calls you out in his newsletter to tens (hundreds?) of thousands of people 💀

if this doesn't get me to learn how to use claude code, i don't know what will. 

btw that three hour hike was like getting a masterclass in marketing while in the woods. so so good. AND we saw a porcupine. what?!

i spent the whole day yesterday working around the house. 

planted my veggie garden, power washed the deck and patio (better than sex), turned on and tested the sprinkler system, blew up the pool for the kids, cleaned the garage, did laundry and dishes, and even played basketball in the evening. 

by the end of the day my body was tired but i felt soooo good. clear minded. energized even. something about using my body, getting my hands dirty, caring for our home and family. it's almost like this is what humans are built for. 

i compare it to how i feel after a full day at my computer. also working, caring for others, using my brain... but i feel totally mentally exhausted by the end of the day. foggy. body aching but not in the good ways. 

who knows, maybe ai will be a blessing if it gets us off our screens and back to engaging physically with the world. 

--

p.s. here's a before and after of the patio. had no idea these stones were under there!

imma just say it: anyone telling you that success requires you to have bad mental health is just trying to justify their own toxic behavior.

another cool community role here in nyc

a few years ago, i created a full ebook called "how to sell your community business".

in addition to sharing my lessons from selling CMX, i interviewed 15+ community founders who took their community businesses to acquisition to learn all about why they decided to sell, how they found an acquirer, what the process was like, and the experience for them and the community after the acquisition.

part of me just wanted learn, and share more insights about how community acquisitions actually work, and to help others thinking about selling their community business.

i was also curious to learn if it's ever a good idea to sell a community business. it's not like selling a software product. there are a lot of complex social dynamics, and based on my research, the results were rarely good for the community on the other side (not always... some did well after).

anyway, after spending many many hours working on this ebook and getting it close to done, a bunch of really hard shit happened in my life, which is when i paused work and writing for a while, and this project went on the shelf.

but i still have the full draft. and i'm curious if folks would still be interested in a deep dive on this topic.

should i pick it back up and publish it?

so cool!!! LinkedIn invited me to share the behind the scenes of my viral potluck post. 

of course, i post daily here about coaching, mindfulness, enoughness and other important stuff. but it was my post about hosting a potluck for my neighbors that went insanely viral. 

but hey, the people love potlucks! or anything that isn't ai and actually gets people meeting the humans in their neighborhood irl. 🤷‍♂️

this was really fun to do. thanks for inviting me to share the behind the scenes of this post linkydinky!

p.s. they wouldn't let me call it linkydinky in the video. i'm sorry i had to go off brand 

p.p.s. also im realizing i need to get one of those cute microphones creators use. my audio sounds like 💩

p.p.p.s. the moral of the story is to have fun with posting content here. people can feel when you're having fun. they can feel when you're not.

How I Did It with David Spinks

LinkedIn Guide to Creating

How did a post about a neighborhood brunch go viral?

🌀 david spinks shares how posting about a wholesome local potluck led to his most viral post and why everyday moments are sometimes the most relatable. 

Have you ever been surprised by what people connected with?

Careers | Join Our Team Today — Female Founder World — Home

I’m building the world’s biggest entrepreneurship brand for women, Female Founder World.

I'm hiring an events and programming lead based in Sydney (in-person/hybrid), LA or New York (mostly remote with some travel). This job isn't just about operations. Yes, you must have deep experience managing large scale events, but you will also be a custodian of the brand and a host for our community, so taste and attitude matter.

This role is a key hire for the team and will be working very closely with me to build Female Founder World: https://lnkd.in/gGr7Ykrk

how do you make decisions?

if you're like most people, you try to think your way to an answer. 

sometimes, this works.

other times (most times?), you get caught in an endless loop of thinking and never land at a decision.  which, of course, stresses you the f out, which makes it even HARDER to make a decision, and we just keep getting more and more stuck and stressed. 

if you're finding yourself in that second bucket, you're not alone (literally everyone struggles with this) ANd id love to offer something that can help. 

in today's newsletter, i share a three-step process you can use to navigate complex decisions, leveraging parts work / IFS (i explain more in the essay)

this is also the process that Astrid Schanz-Garbassi and i will be taking you through in our workshop tomorrow! 

📰 read the newsletter here: https://lnkd.in/d3vi6BkZ

🎥 attend the live workshop here: https://luma.com/hc86wjxd 

it'll be a wonderful, intimate group. hope to see you there!

if you ask ai for a business strategy, it can give you 73 practical frameworks you can use immediately. 

but what it will never do is spontaneously interrupt the conversation and say "woah look at that cloud! it kind of looks like a dinosaur eating a muffin" 

and that's why i'm not worried about ai replacing us.

Building a Community Business 101 - DAY 1

Are you building the community that you want for yourself or the community that you think others want?

This question is a *big* deal and will shape a lot of what your life looks like after you launch your business.

If you’re building the community you want for yourself, showing up every day is going to feel easy. You’ll want to ask question because you actually want the answers. You’ll enjoy reading comments because you’re actively trying to learn. You’ll be a natural leader because people will see that you’re one of them.

if you’re building a community for others, but you don’t actually want it for yourself, that’s fine… BUT you might find it hard to keep showing up with energy every day. 

Often, the ones building the community for others, that they don't want for themselves, end up hiring others to engage and lead the community.

It's common for someone who's become an expert in a field to do this. They want to help the up-and-comers. So they create a community, share their expertise, but don't participate as a peer quite so much.

You may still love to engage with the community as a teacher. That's great. It just creates a different kind of community. It'll feel less peer-oriented, and more teacher-led.

There's a third category: The folks that are totally outside of the space, and just see an opportunity to build a community business. This is really hard. Really, you'd just have to hire a community leader who is of the community. You're more of an investor than a community leader in this kind of business.

Remember: It’s much easier to start a community than it is to keep showing up for years.

A community is a long-term commitment. You have to ask yourself if you’re really excited to make that commitment. 

It doesn’t mean you can’t quit or adapt in the future if you’re no longer feeling it or if the community experiment doesn't work.

But if, from the get-go, you know you're only in it for the short run, you may want to create a cohort model that has an ending, rather than an ongoing, open-ended community.

Hope that helps someone who's thinking about starting a community business!

--

This is Day 1 of 7 of Building a Community Business 101. Hit +follow to get the rest of the posts this week in your feed!

studies show that coaches with green walls are 145% more effective

Community Engagement Lead - Careers at Airbnb

Global Director Community Voice

Incredible role for those who have deep expertise in community! https://lnkd.in/gG8RW45G

hot take: the loneliness epidemic is about much more than community and our connection to others.

just ran into two neighbors on my walk. one offered me leaf mulch and one offered me native plant seeds. pinch me, i think i'm dreaming!

Unstuck! A Workshop to Help You Get Out of Your Head and Make More Confident Decisions · Zoom · Luma

i used to suck at making decisions. this method changed that:

it's called parts work, or IFS. it's primarily a therapeutic and coaching methodology, but i've found that it's an incredible decision making tool as well. 

the core premise is that we're made up of parts. those voices in your head? they're all different parts of you who want different things. 

when we're stuck with a decision, it's usually because two parts of us want different things, and they're fighting for your attention. 

let's say for example you're stuck trying to decide when to launch your product. 

there's probably a part of you that really values action and momentum, that wants you to ship sooner. 

and another part of you that's optimizing for quality and reputation, and doesn't want you to risk putting something unfinished out there. 

you may also have a part of you criticizing you for not making a decision. 

and here's the thing: they all hold some truth. one isn't wrong or right. they just have different strategies for protecting you. 

which is why we get stuck. a pros and cons lost won't solve this problem because every path has trade offs. this is a complex decision without an objectively right answer. your parts get stuck on a tug-o-war and momentum comes to a halt. 

the first step is just identifying the different parts of you showing up in this decision. sometimes, just getting a map of what's happening in your mind is enough to stop the spinning and make a decision. 

but sometimes, what we need to do is turn toward one part at a time and actually listen to them. once we better understand them, and they feel heard, they tend to trust you to make the right decision and takes their needs into account. it will feel easier to make a decision. 

there's a simple process for working with your parts one at time. it's best done with a guide, at first. 

so on friday next week, Astrid Schanz-Garbassi and i are going to take you through that process at the Unstuck! workshop. 

it's donation based, and all are welcome. bring your big hairy decision of the moment, and we'll help you loosen the lid and get flowing again. 

🫙rsvp here: https://luma.com/hc86wjxd

when someone offers to pay for the bill, i've been doing something unthinkable...

i accept.

i know. how absurd. i should be pushing back. "you don't have to do that!" "let's split it!" or at least, "i'll get the next one!"

but all of those responses are defenses. 

this person wants to offer a gift, and i'm trying to take that away from them, or turn it into an IOU, all because i'm uncomfortable receiving a gift. 

because what would it say about me if i accepted a gift? that i'm in need? that i'm not an independent adult? that i'm now indebted?  

what if we just accepted gifts when offered to us? not just externally, but actually welcome the gesture into our heart. 

this person wants to send me kindness. this person wants to be in non-transactional community with me. can i receive it?

them: i'm always the one to reach out to my friends. they never reach out to me.

me: how do you feel about that? 

them: it's frustrating. i'd like my friends to be thinking about me and reaching out more often.

me: got it. that makes sense. and how do you think it's been serving you to be friends with people who rely on you to check in? 

them: huh? i dunno. it's not serving me i don't think. 

me: well, when someone regularly reaches out and checks in with you, how does it feel? 

them: it's good to know they're thinking about me. but i guess it feels a bit like i'm under pressure to respond thoughtfully. and i don't always have the time or energy. sending something brief feels rude. so often i don't respond at all, which is even ruder. and then there's even more pressure and...ohhhhhh

me: yeah

them: really???

me: yeahhhh 

them: so this whole time i've been surrounding myself with people who need me to follow up with them because i'm afraid of the pressure that comes with people who check in on me and so i subconsciously let those relationships wither while maintaining the ones that let me retain autonomy over when and how i have to communicate with people?!

me: sounds like it?

them: damn. 

me: yeah. 

them: so what do i do now?

me: i dunno. just notice the pattern and start to decide if/how you want to respond differently? 

them: ok i'll try that.

me: want me to check in with you in a couple weeks? 

them: hell no!... i mean... yes... yes i do

me: see? you're already doing it. 

them: hate you 

me: love you too

launching a new low-cost coaching option:

for $5 a month, you tell me what it is you want to do, and i'll text you occasional selfies of me glaring at you until you do it. 

no chit chat. no introspection. just pure, unadulterated eyeballs. 

here's a freebie to wet your whistle...

"i've never experienced anything like this. working with you is so raw and weird. i have no script with you."

direct quote from a client call recently that made me do a little happy dance inside. 

they had been running scripts of how they're *supposed* to show up in many parts of their life. 

our container was the first place where they could let all of their scripts drop and just be. 

which felt really weird and raw for them. we're just not used to not having to perform. it feels foreign to reveal ourselves so fully. 

but we practiced and it started to feel normal and accessible. 

and it starting to expand back out into other parts of their life. 

they're finally showing up as themselves, no script. 

they're starting to feel free. 

--

if you're tired of running scripts to fit in, to please others, to avoid the fears that have been ruling your life, get in touch. i'd love to work with you.

i think we hit the neighbor jackpot

IT'S OUT!!! This might just be my favorite podcast interview I've ever done. I'm so excited to share it with you all.

Getting to go deep with my good friend Derek Andersen was super special. We've gone so many ups and downs together in work and life (he also bought my company!), so we were able to get real personal.

We cover a full range of my favorite topics:

~ what is true belonging?
~ can businesses build true belonging?
~ how communities are mirrors of our inner worlds
~ can you be ambitious and prioritize your well-being?
~ what it was like to step away from CMX and why I felt so empty
~ what it means to live, work, and build things from enoughness
~ why a lot of tech founders have a skewed view of the importance of "impact" and "making a dent in the universe."

During a time when VCs are proudly proclaiming that you need to sacrifice your health and relationships in order to succeed, I feel more fired up than ever to call BULLSHIT and talk about a different way of approaching entrepreneurship, success, and achievement.

I haven't done many podcasts in the last four years as I've been going through my own career and life transition. This conversation feels like a bit like a coming-out party. It encapsulates so much of what I've learned these last few years.

I truly hope you enjoy it, especially my terrible Larry David impression.

prompting your community members to help them ask better questions is a genius move.

Announcement: I'm kicking off a new cohort of the Community Business Mastermind!

This will be a group of 6-8 founders and high-level operators of community-based businesses.

Each member:

~ Will have an established community / paid membership business up and running
~ OR is starting one up and has a proven track record as a founder / operator
~ And is a good-hearted, enjoyable human that I want to hang out with

Groups like this have been so so helpful for me throughout my career. Learning from others in similar businesses, and not feeling so alone with decision-making and navigating it all... it's powerful to have a group of people who are all invested in your success.

I'll be personally coaching and facilitating this group. It will last for six months, and then switch to month-to-month after that. 

I've already started curating this group, and it's half-full. Would love to fill the last few spots with some great people.

Please comment below if you're interested, or know someone who might be! 

I'll drop more info in the comments.

Co-Founder at Bevy / Startup Grind

This week on Divot I interviewed 🌀 david spinks, author of the Business of Belonging and creator of CMX. We talked about success, loneliness, ambition, why high performers often feel inadequate, and if making a dent in the universe is worth the cost. David is one of the most thoughtful people I know and cares deeper about the people around him than almost anyone I have come across. Links to the full chat below!

what if belonging is about more than community? 

i think that when we only look at belonging, and loneliness, through the lens of our connection to each other, we miss critical elements of what we need to feel like we truly belong. 

the way i see it, there are three fields of belonging:

- belonging to self 
- belonging to each other
- belonging to universe / oneness / God 

we need fulfillment in all three fields. all three feed each other and dance together. if one field is lacking, something critical feels like it's missing. 

this is the focus of my newsletter today where i go into more detail about each field, which you can read here 👉🏼https://lnkd.in/eeRpAf9z

and as you read, i invite you to reflect on these questions:

- does this way of looking at belonging make sense to you? does it feel true to your experience? what’s missing?
- what opens up for you when you expand the fields of belonging beyond just our connection to each other?
- for those of you committed to creating belonging in the world, how does this change how you approach your work?

excited to hear your thoughts and experiences!

i've been reading about changing my relationship to money. doing all the woo woo stuff like letting it flow in and out freely, giving my money happy energy, trusting the universe to take care of me, etc. and just now my son found $0.35 in the playground. my mind is blown. this stuff works.

Founder & Managing Director @ FeverBee | Writes and consults about how to build thriving enterprise communities.

There aren't many slam-dunk wins to improve engagement, however...

Adding a community-question form wizard appears to be one.

We get to test many things with many clients. And many, if not most, experiments have had limited or no impact. That's the nature of experiments. 

And every now and then we run a client example where the results are like 'woah, more people should know about this'.

This is one of those results. 

Instead of letting members ask whatever question they wanted, we created a question form wizard which would ask THEM questions and then generate the question from the responses. 

These questions prompted them to describe issue, product type, what they have already tried, ideal outcome, any constraints, etc...

(Our first attempt let members bypass the wizard and write a question as normal. Almost everyone did exactly that. So we removed it.

The result was a slight decline in the quantity of increases and a huge increase in the quality of questions and responses. 

I'd strongly recommend trying it - drop us a line if you want help.

you're suffering because you believe you're not free. you'll be free when you recognize you don't need to achieve anything to be enough.

this is one of the most helpful management frameworks i learned in 10 years as a ceo:

it's called "the competence / confidence matrix" 

it was created by noel burch in the 1970s

why its helpful: because we tend to either over-delegate (give people full autonomy when they're not ready for it) or under-delegate (micromanage people who could have handled things themselves). 

this framework helps you discern how hands-on or hands-off to be based on where the employee is on the map: 

low competence / low confidence: this is a novice. they need a lot of clear instruction. hand-holding is okay here. like riding with training wheels. 

low competence / high confidence: this person is motivated and ready to roll, but needs guidance on where to put their energy. help them with planning and decision making. 

high competence / low confidence: this person knows what to do but they doubt themselves. be their cheerleader. offer them moral support. remind them it's okay to fail. 

high competence / high confidence: hand it off and stop thinking about it. this person has it locked down and will solve for problems that arise on their own. this is where ultimate leverage lives and how companies grow. 

note: until you have people in that last quadrant, you'll still be involved with everything everyone is doing to some degree. that's okay for small businesses. not okay if you want to scale beyond yourself.

let me know how this lands for you. and if you have any juicy management frameworks, share them in the comments. i love this stuff!

edit: it sounds like this original concept was created by blanchard and hersey in 1969, and is called situational leadership. today i learned!

*cough cough* got a bad case of the CMX FOMOs right now! 

hope y'all are livin it up over there, sending loads of love, wish i could be there with you. 

please send selfies

RIP to saying a word is "doing a lot of heavy lifting". 

another phrase lost to ai

take a minute and look through the next 20 posts in your timeline. ￼ notice how many times a post sparks the thought, "i should do this" or "i need to do this" or "i'm not good enough to do this". then consider how many times in a day you're consuming content that's telling you how to live your life and pointing out all the ways in which you are not yet enough.

Why do so many people feel lonely even when they're surrounded by others?

🌀 david spinks co-founded CMX, helped define the community-building industry, and wrote the book Business of Belonging.

He argues that loneliness runs deeper than social connection, and that most people are trying to fix it at the wrong level.

Watch the full episode with Derek Andersen, link in the comments.

#loneliness #community #mentalhealth #leadership #divotpodcast

a clear sign your personal brand is starting to click:

"this made me think of you" texts. 

when people start sending you links to articles and content related to your word or topic, you know you're developing trust and reputation in that field. 

this is how humans' brains seem to work. we try to find a "go to" person for topics, to make it easy on ourselves. so when someone uses a word or phrase a lot, and we trust them, they become attached the topic in our minds. 

it's like when i hear "creator" i think Jay Clouse.

when i hear "newsletter growth" i think Chenell Basilio.

when i hear "sponsorships" i think Justin Moore 🧲.

when i hear "generalists" i think Milly Tamati.

when i hear any combination of "weird", "linkedin", and "butthole" i think of Jillian Richardson

this happened for me with "community" over the years.

now it's finally starting to happen for me with "enoughness" after three years of writing about it. 

two examples just in the last week:

the other day Maura McInerney-Rowley (who i think of when i hear "death") sent me the enoughness post by the Tom's founder, Blake Mycoskie. my bestie Emma Mayerson (who's my go-to for "social enterprise / philanthropy") said "you could have written this!" 

then Ray Batra (no word association for me yet, but wonderful human) just sent me this brilliant onion article about the soybean who wishes it could be enough (i feel you, soybean...)

all spot on in knowing i'd love these posts, and seeing how aligned it is with what i've been putting out into the world.

feels like something is starting to click here. 

curious if you all notice this happening with your personal brands. what's your word that makes all your friends think of you?

quick story time...

when i was in college, i had the most boring job possible: working the information desk at the student union.

i sat for hours and hours in a tiny booth with nothing to do. nothing, that is, except shoot the shit with Ivan Cash, who was also assigned to this most mind-numbing role. 

and shoot the shit we did. i can't even tell you what we talked about. anything and everything. stupid shit. the news. random ideas. we flicked paper footballs through finger field goals. we watched weird videos on the school's very old computer. just a couple of kids with our lives and careers ahead of us, and a whole lot of time to kill.

i had no idea at the time that i was sitting next to someone who would become one of my biggest creative inspirations. ivan has had a prolific career since those days at suny geneseo. he's now an artist and videographer. he's created viral interactive social art like "snail mail my email" where thousands of people created art out of each others' emails and "the passenger project" where strangers on airplanes got create art together. his short films are some of the most beautiful, human works of art i've seen in video form (watch them all at www.ivan.cash, you won't regret it)

it's funny how the universe twists and twirls. because more than 15 years after those days in the info booth, ivan and his team were brought in by substack to create a film about writing. i had been writing my newsletter on substack for some time, and ivan asked me if i'd be open to participating. 

me?! in an ivan cash production??!! yes please.

the result is beautiful and inspiring. i felt very privileged to be able to share my experience alongside such a prolific group of writers and learned a lot from the wisdom everyone shared. 

for anyone writing, or creating something in the world, i hope you enjoy it. 

watch the full director's cut of "On Writing" here: https://lnkd.in/eEt8uY5B