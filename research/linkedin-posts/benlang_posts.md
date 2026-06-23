# Recent Posts for benlang

1-month free trial with 24/7 support. We’ll remind you 7 days before your trial ends.

Your next job is an InMail message away

Contact the right people with InMails.

Get rewards from Headspace, Notion and more (up to $845 value). Terms apply.

Get access to exclusive events with industry leaders and professional experts in Premium-only conversations.

Reach out to anyone on LinkedIn, from recruiters to hiring managers, even if you're not connected. InMail messages get a 4.6x higher response rate compared to emails or cold calls.

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

Digital Creative Director at Spyglass

A little marketing savvy to kick off the weekend.

10 Small Design Mistakes We Still Make – UX Planet

Great little article on the basics of good UX on what can quickly get in the way of building an experience that is truly focused on the user. 
https://lnkd.in/evNUWBk

CEO, President and Founding Partner at Spyglass ● Brand Marketing ● Corporate Branding, Strategy + Positioning

At Spyglass we believe your brand is 3 things -- 
 
1. Your brand is your word.
It’s how you describe yourself and tell your story—both the language you use and the tone of voice it’s expressed in. It is also your word in the sense of the promise you are making to your audiences and the world. 

2.  Your brand is your deed. 
It’s how you show up—how you behave and what you do. It lives in your service offerings and the way you treat people. It is experiential and evidenced in the tangible interactions people have with you. 

3. Your brand is your presence. 
It is the impression you make with every presentation, package or post you put forth. It is expressed graphically through color, typography and imagery of course, but it also emerges in the stance you take and the vibe you emit. 

Are you watching -- and keeping -- your words?
Are you paying attention to your actions?
Are you putting your best foot forward? 

#brandingstrategy #minneapolisbranding #brandstrategy

I was thrilled to host I SPY AI last week - a CEO roundtable with Andrew Hecker Bill Kirkpatrick Gwen Martin Jeff Peterson Gavin Quinn Elizabeth Ross Murad Velani and Sherry Essen, M.A.  Lots of good conversation about their brand narratives in the age of generative AI and many views about AI as a utility, as a teammate, and as a way to unlock talent. Special thanks to Spyglass strategic partner Tim Brunelle who presented and led the conversation. #ai #brandnarrative #ISpyAI

Spyglass September Newsletter: The Story Edition

The latest Spyglass Newsletter Edition is here! The power of storytelling, Apple’s AR taking center stage, and a fast, cool way to tell a data-driven story from Google about the how-to's people are searching for. Be sure to check it out.

Measuring the value of a Photo/Video Experience.

Hey hey, great piece on evaluating the kind of impact a powerful photo/video experience can have. Spyglass has been working with Hal and his team for years and and attest to just how well they do it!

Great article here on the upcoming AR apps for the iPhoneX. Is anybody else as excited as me to try them out?

Yay! It’s Awards Season (at Spyglass, too!)

Honored to announce our Platinum and Gold dotCOMM Awards for Post Consumer Brands and Minnetronix, Inc. Check out the latest news on our website! #awards #brandingagency

What an honor it has been to partner with Andrew Reeher and his leadership team to brand, position and launch Brighton Science, the global leader in surface intelligence. Congrats!

We have a unique leadership opportunity for an experienced Account Director who is ready to make a bold move away from a more traditional consulting/analyst or branding/advertising agency role, is confident in their abilities and is ready to up their game in terms of responsibility, contribution, and diversity of clients and challenges.

Apply Here: https://lnkd.in/eVHDz4jH 

#hiringmarketing #accountdirector #twincities #branding #opportunity

Client Strategy and Services at Spyglass

Want to work with me at Spyglass? We are looking for a strong Project Manager to join our fun (see picture for proof), growing team. If you are interested, or know someone who would be, reach out! Info about the role and Spyglass can be found here - https://lnkd.in/gMWc-BH

SpyTimes May Newsletter: The Transformation Edition

Paradigm shifts.  Strategic resets.  Motivating morning routines.  All in the May Transformation Edition!  Change starts here...

So lucky to have such great clients and team members at Spyglass. Congrats to everyone!

Spyglass is on the hunt for a Senior Project manager, and we're looking for the great minds of LinkedIn to help us connect with our future Spyglasser!

Does your brand pass this test?

Spy5: A Conversation with Ghadeer Garcia

In this episode of Spy5, Molly Rice talks with Ghadeer Garcia of The BrandLab who offers some timely takeaways for anyone reflecting on issues of equity and inclusion. Take 5 and check it out!

AI is both a cultural and technological force that can’t be ignored—especially by leaders. This was the hot topic of conversation at our most recent I Spy AI Executive Roundtable with Andrea Specht, Brian Call, Amy McNeil Lund, Chris O'Brien, Bonnie Speer McGrath and Amy Langer. We decided the best ways to get started: 1) Engage with it personally. 2) Develop a buddy system. 3) Empower your teams. 4) Create a task force. 

Special thanks to Spyglass strategic partner Tim Brunelle who led the conversation. More here: https://lnkd.in/gVm2ShW5 

#ai #brandnarrative #ISpyAI

brand-oracle.spyglasscreative.com

We’re all about brands.  You’re all about spirit animals (okay, maybe you’re not, but you should be).  See what’s in store for you in 2018 with our freakily omniscient Spirit Brand Animal Oracle! 
https://lnkd.in/dCxBkQJ

Spyglass is on the look out for a new Senior Project Manager! If you love to drive change, impact processes, collaborate on award-winning work – and enjoy keeping everyone and everything around you organized – this is the role for you, and we can’t wait to connect. 
https://lnkd.in/gAbtiZKb

#hiring #jobalert #projectmanagementjobs

What's the value of a strong brand position? The bajillion dollar question.

So proud to be part of a team that gets to help great companies like these.

Spyglass is looking to hire!

Spyglass October Newsletter: The Spooktacular Edition

Ready to take off your brand mask? Should you be afraid of the dark (post)? What is your state's top candy? This, along with the latest client news, in the Spooktacular Edition of Spytimes - read now.

Had a GREAT event with Spyglass clients and strategic partners exploring how AI is reshaping their industries, defining their business strategies, and influencing how they lead. Big thanks to Mary Maijer, Nicole Althaus, Peter Hutchinson, Ashley Hume, Scott Taylor, Kyle Scott, Rachael Marret and Scott Mayer for coming to I Spy AI! And big thanks to Tim Brunelle for leading the conversation.

Five major themes emerged, and two of them really stood out to me because they demonstrate how boldly these leaders are approaching AI. 

1. Thinking of AI as Augmented Intelligence (vs Artificial)
2. Cultivating an AI-first culture 

Check out my latest blog post for more – and let me know if you’re surprised by these or have any thoughts to share!
https://lnkd.in/ggtSCyyj

ICYMI, more great insights into what it takes to boost your brand and brainstorm with the best of them.

Looking for someone to join a great group of people!

New Year, new name! BTG Labs is now Brighton Science.

We are grateful for our customers and partners who have helped us grow and evolve as a company. So much so, in fact, that we’ve made some significant changes we’d like to share with you.

Read the full letter from Brighton Science CEO, Andy Reeher:
https://bit.ly/3nbUKuN

#NewYear #NewName #CompanyUpdate #Reband #BrightonScience #2022

Thrilled to be able to have such amazing leaders in at Spyglass to discuss the current state of AI and how it can help move their businesses forward. Spyglass #thefutureisbright #leadershipmatters #ai

Really excited to be able to share this conversation between Molly Rice and Ghadeer Garcia. Ghadeer, and her company, The BrandLab do such great work in the field of equity and inclusion. I hope you can take the time to listen and learn.

So excited for the Lakewood Cemetery team and for the community they serve.

Excited to celebrate with Lakewood Cemetery at the opening of their new Welcome Center. This beautiful space was created to host families and the community for important conversations about living with loss and choosing meaningful ways to be remembered. We are honored to partner with you to help bring this vision to life.
Pictured: Sara Martin, Julia Gillis, Molly Rice