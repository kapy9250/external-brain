# Chinese Open Source: A Definitive History

URL: https://x.com/kevinsxu/status/2029961571296743585

Open source used to be a niche topic. China tech also used to be a niche topic. Thanks to AI, the combined topic of “Chinese open source technology” is the topic du jour. It is the story that everyone is trying to understand and make decisions about, from the hacker houses in San Francisco, to the policymaking chambers in Washington, Brussels, New Delhi, and, yes, even Beijing.

I first started writing about Chinese open source over five years ago in this newsletter as a pet topic. Back then, few people in the tech or policy world paid much attention to what Chinese developers were doing on GitHub, the different open source projects and communities that were emerging from tech giants and new upstarts, or why the Chinese government changed its tone about open source from ambivalence and occasional hostility to full embrace as a core part of its national innovation and soft power strategy.

DeepSeek changed everything. Along with Qwen, Kimi, GLM, MiniMax, Stepfun, and even Unitree, Chinese open weight AI models took the world by storm. The traction even earned “open source” a shoutout in the Chinese Premier’s all-important address at the Two Sessions, with a promise to continue the growth of open source communities and ecosystems as part of the country’s next five-year plan.

As surprising as all this might be, open source in China didn’t come from nowhere and has a long history. Unlike industries like solar, semiconductors or batteries, it was never deemed “strategic” from the top, but existed by and large as an organic subculture within the tech sector, until DeepSeek shook it out of obscurity.

A big question that’s facing a lot of decision makers is whether Chinese open source becomes a permanent feature of the global technology landscape or a fleeting phenomenon that will be banned and excluded by western capitals, despite its appeal to western capitalism. Before deciding on an answer to this question, it is probably important to know the history of Chinese open source first.

Having previously worked at GitHub, leading its international expansion strategy, and being involved in many open source projects traversing between Silicon Valley and China, I had a front row seat in how open source became a force inside the Chinese, then global, technology ecosystem. DeepSeek itself may be an anomaly with a hedge fund origin and unique compute efficiency, but the growth and best practices of other Chinese AI labs are outcomes of a natural and somewhat predictable evolution of a maturing open source scene that took two decades to marinate. Even Jensen Huang’s often cited line – “50% of AI talent comes from China” – shouldn’t shock people, considering the integral role that open source has always played in proliferating technical education en masse.

This post tries to tell the full arc of the story — a definitive history of Chinese open source – from its earliest days to the present moment. I divided this history into six acts, each a sign post that marks what I think was a pivotal chapter to help the readers follow along and grasp the big picture. I also enlisted the help of a few experts who are long-time participants of Chinese open source to get their updated view and feedback. (They are acknowledged at the end of the post, though any opinions, conjectures, or mistakes in this post should only be attributed to me.) I feature characters and voices that bring a human flavor to this rather dry and technical topic, in order to make the stories more relatable, knowing full well that certain details are glossed over.

Regardless of which lens you wear when you read this – an investor, a policymaker, an entrepreneur, a hacker – I hope you learn something new.

[![Image 1: Image](./assets/chinese-open-source-a-definitive-history/image-01.jpg)](https://x.com/kevinsxu/article/2029961571296743585/media/2029958982232645636)

[![Image 2: Image](./assets/chinese-open-source-a-definitive-history/image-02.jpg)](https://x.com/kevinsxu/article/2029961571296743585/media/2029959903356616704)

A timeline that previews the rest of the post. You might have to squint, sorry…

Open source software diffusion is impossible to track, so it is hard to pinpoint when the first line of open source code entered China.

Linux, the ubiquitous open source operating system, first entered China in the summer of 1994. It was brought over by a Chinese technologist, Gong Min, when Linux released its first version in 1991. By the early 2000s, there was a thriving Linux user group up and running. The Mozilla Foundation opened its Beijing office in 2007. The Linux Foundation also hosted its Open Source Software Summit in Beijing, where Jim Zemlin, the foundation’s executive director who still leads the Linux Foundation today, spoke among other global open source leaders. It is safe to estimate that open source has at least planted some roots in China in the early 2000s, maybe even the late 1990s, when a few large enterprises have dipped their toes in Linux to improve efficiency and save cost. But just like the rest of the world, open source was a niche concept in a landscape dominated by Microsoft, IBM, and other proprietary software giants.

## Act 1: The "De-IOE" Campaign

The first major chapter of the Chinese open source story did not begin with some grand government proclamation or a visionary founder. It started, as most open source stories do, with engineers trying to solve hard problems for their company. This company was Alibaba.

In the mid-2000s, Alibaba was growing like wildfire, so much so that by 2008, it had become Asia's largest database customer, running a 20-node Oracle RAC cluster but was still hitting scaling limits. The first iteration of Alibaba was built on the so-called “IOE stack” – IBM for server, Oracle for database, EMC for storage. The IOE stack was the gold standard of enterprise IT stack, so Alibaba used it just like most tech companies did back then. Because of its growth, the company’s IOE bill was getting prohibitively large yet the stack couldn't scale fast enough for new Taobao users to buy more stuff online.

So in 2008, Jack Ma, its charismatic founder who famously did not know how to code, brought in another ambitious researcher from Microsoft Research Asia, who also did not know how to code, Wang Jian, to fix the problem. (Wang got his Ph.D. in psychology.) “The Doctor”, as Wang was known inside the company, became its chief architect whose strategy later birthed Alibaba Cloud. (His nickname was later updated to “the Father of AliCloud”.) But his first order of business was to get rid of the IOE stack by embracing open source technology. Thus began the “de-IOE” campaign.

[![Image 3: Image](./assets/chinese-open-source-a-definitive-history/image-03.png)](https://x.com/kevinsxu/article/2029961571296743585/media/2029959793612365833)

Jack Ma (right) and “The Doctor” Wang Jian (left)

This campaign rankled many rank-and-file engineers, many of whom built their careers as IBM or Oracle certified administrators. Many used to work at those two companies. But Wang had the full backing of Jack Ma, a 1 billion RMB per year budget to get “de-IOE” done, and there was no turning back. Alibaba started using commodity x86 servers to replace IBM. It looked into building its own distributed storage systems to kick out EMC. Most importantly, it studied MySQL, a popular open source relational database project to rid itself of Oracle once and for all. (Oracle later absorbed MySQL as part of its acquisition of Sun Microsystems in 2010, which bought MySQL in 2008.)

After five painful years, in May 2013, Alibaba pulled the plug on its last IBM minicomputer. Two months later, in July 2013, Oracle was decommissioned out of Taobao's core advertising system in favor of its homegrown MySQL implementation. IT cost came down, scalability went up, the seed for Alibaba Cloud was planted, and the company’s engineering capabilities rose to meet new challenges, like scaling to handle high-traffic moments like Singles' Day, the largest online shopping holiday in the world.

[![Image 4: Image](./assets/chinese-open-source-a-definitive-history/image-04.jpg)](https://x.com/kevinsxu/article/2029961571296743585/media/2029959686884052992)

Alibaba engineers celebrate taking offline the last IBM minicomputer

I tell the “de-IOE” story at length because it wasn’t an ordinary IT migration project. It was the founding myth of Chinese open source, where a major Chinese tech company bet its entire infrastructural future on open source software and commodity hardware, endured years of internal skepticism, and came out on the other side stronger. It also fostered a creative energy that led to an internal database project called Oceanbase, which will return in our story later.

For the most part, “de-IOE” was representative of an era when Chinese tech companies were takers and consumers of open source to fuel their growth needs during the heydays of the mobile internet boom. There were no self-reliance requirements in the nationalistic sense per se. The fact that MySQL was incorporated in Sweden, then later owned by the same American database giant Alibaba tried to get rid of in the first place, was not a major red flag. Avoiding western technology was not yet a priority.

With the de-IOE precedent established, the broader Chinese tech ecosystem followed aggressively to embrace open source. In early 2016, Alibaba’s e-commerce archrival, JD.com, adopted Kubernetes less than a year after Google open sourced it and long before most western tech companies felt comfortable using it. This rather risky posture of using Kubernetes, a cloud container orchestration software that would later emerge as a de-facto layer in all cloud computing platforms, was an outcome the Chinese internet’s breakneck growth (JD needed larger scalability than Walmart), as well as a growing confidence in taking, consuming, and customizing open source technology for its own needs. This confidence is an important marker, as Chinese companies begin to create and contribute open source software later on.

But for the most part, this era’s mindset was predominantly “what open source can do for me.”

## Act 2: Community Builders and Subculture

By the mid-2010s, every major Chinese tech company was in the open source scene in some way. Some of these efforts were serious and additive to the ecosystem. Some were, frankly, companies tossing out failed internal projects, open sourcing by uploading onto GitHub, and calling it a day, while using its half-hearted presence to do recruiting. The quality and commitment was inconsistent, the documentation was often Chinese-only rendering them inaccessible to a global developer audience, and the maintenance was spotty.

To be successful in open source takes much more than just good code. It needs a platform to collaborate, a transparent process for anyone to join, and a set of norms and behaviors that require more high-EQ soft skills and cat-herding than one or two 10x engineers banging on their keyboards.

That was where the community builders came in.

Before we dive into China’s own grassroots open source community builders, we must first give a nod to my old employer, GitHub. (Disclosure: I used to lead GitHub’s global expansion strategy.)

Founded in 2008, GitHub was a quintessential Silicon Valley startup that built a web platform to make Git, the version control system created by Linus Torvald of Linux fame, easier to use for your average developers. By gravitating to the Ruby community early (GiHub today is still one of the largest Ruby on Rails webapps) and deploying an individual user first namespace scheme (as opposed to an organization or company), the platform became a rocketship.

Soon, every programmer with a stable internet connection got on GitHub to download, collaborate, and create open source software, all for free. As GitHub became the default home for open source, Chinese developers showed up in force. By 2018, China was the second-largest country in terms of GitHub users and activity, measured by forks, clones, and contributions.

Because GitHub had elements of a social network, akin to a Facebook or Twitter but for nerdy programmers, it sat at an uneasy spot in China. In 2013, its domain was temporarily blocked by the Great Firewall. In 2015, it experienced a massive DDOS (distributed denial of services) attack that was later known as the “Great Cannon” attack. Later on, when GitHub released its mobile app, it was unavailable in the app store in China.

[![Image 5: Image](./assets/chinese-open-source-a-definitive-history/image-05.png)](https://x.com/kevinsxu/article/2029961571296743585/media/2029960314096340993)

However, every attempt by the government or government-linked cyberattack groups to disrupt or block GitHub was met with a collective outcry from the country's growing developer community. If GitHub was down, no one could work or code. Period! Until today, GitHub survives as possibly the largest western website that is not technically blocked in China, though performance continues to be disrupted from time to time.

While access to GitHub, and by extension the best open source software and developers from around the world, remained intact, China lacked its own community center of gravity. That’s when Kaiyuanshe stepped up to the plate.

Founded in October 2014, Kaiyuanshe (开源社) is romanized pinyin that means “Open Source Society”. It was created by a few open source enthusiasts out of a desire for China to have its own dedicated open source community. It was volunteer-driven (all board members and staff have other day jobs in tech companies), vendor-neutral (meaning no big company could dominate its agenda), and made up entirely of individual members, not corporations. Its founding principle – contribution, consensus, co-governance – is about as idealistic as any mission statement.

And it thrived.

After a scrappy start, Kaiyuanshe now convenes the annual China Open Source Conference, or COSCON, that draws speakers from leading open source organizations everywhere, from the Linux Foundation to the CEOs of GitHub. COSCON celebrated its 10th year anniversary last year.

[![Image 6: Image](./assets/chinese-open-source-a-definitive-history/image-06.jpg)](https://x.com/kevinsxu/article/2029961571296743585/media/2029960383583195136)

Kaiyuanshe also gets its hands dirty, doing not just the flashy stuff like hosting big conferences, but also the unglamorous work to educate both outsiders about Chinese open source development and Chinese developers about the outside. It publishes the China Open Source Annual Report to map the country’s open source ecosystem using data from both GitHub and Gitee, a home-grown competitor to GitHub. It became the first Chinese member of the Open Source Initiative (OSI), an organization that holds the moral authority on what is and is not open source (to the chagrin of many corporations). In 2019, it helped draft the Mulan Permissive Software License, the first bilingual Chinese-English open source license that was approved by the OSI. A seemingly technocratic footnote, the OSI-approved Mulan license meant that the Chinese open source community finally had a license that was both legally recognized worldwide and written in their own language.

Kaiyuanshe played a crucial role in educating Chinese developers about open source norms, processes, and culture. Many developers in China were technically proficient but unfamiliar with the social norms of open source collaboration: how to submit a proper pull request, how to engage in constructive code review, how to build sustainable communities around projects. Through workshops, documentation, and mentorship programs, Kaiyuanshe helped inculcate and incubate best practices that paved the way for Chinese open weight models’ success in the AI era. The maturity and sophistication by which the DeepSeek, Qwen, and Kimi teams license their models and manage their communities and online presence is an outcome of years of fostering by the Kaiyuanshe volunteers.

The membership of Kaiyuanshe became more international over time. Taiwanese, Japanese, even Polish developers joined the organization. The common denominator was not nationality, but a passion for open source technology, as well as some proficiency in Mandarin Chinese to be able to talk about it with other members.

The Kaiyuanshe-led homegrown open source community birthed a unique, often quirky, and sometimes vocal developer subculture. Two examples that are worth spilling some ink on: 1024 Programmers’ Day and 996.ICU.

While Kaiyuanshe was building the institutional layer, something equally important — and more colorful — was happening at the grassroots level. Chinese developers were creating their own subculture, including their own holiday!

In 2010, a developer community held an online vote to establish a Chinese Programmers' Day. The winning date was October 24, as in 1024, as in 2^10 in binary. If you're a programmer, you don't need that explained, just like what April 20th or 420 means to another subculture. 1024 is a number that doubles as an identity marker.

Russia was actually the first country to have some kind of Programmers' Day. The Russian developers picked September 13, as in the 256th day of the year, or 2^8 in binary. It was also ordained and approved by the top; then President Medvedev signed it into law in 2009. China's Programmers’ Day, on the other hand, was completely bottoms-up, out of the sight of the authorities, during a time when self-organized civil society had some space to exist. No government stamp was required. It was not clear if anyone in Beijing even noticed or cared.

By 2015, this “fake holiday” took on a life of its own, where tech companies who want to support (or hire) technical talent fully embraced and sponsored it into an industry-wide celebration of programmer culture and identity. The celebration’s theme can sometimes be serious, like fighting for more time off and less overtime. It can also be ironic and self-effacing, like fighting against stereotypes like wearing plaid shirts and receding hair lines (most programmers are men).

One thing was clear though, Chinese programmers had plenty of personality, quirkiness, and playfulness to laugh at themselves. In 2020, CSDN – China’s largest programmer-focused media network and a co-founding group of Kaiyuanshe – launched a multi-day Programmers’ Day conference and celebration in Changsha, a cool and more affordable city popular among younger Chinese professionals. It would become an annual phenomenon.

[![Image 7: Image](./assets/chinese-open-source-a-definitive-history/image-07.png)](https://x.com/kevinsxu/article/2029961571296743585/media/2029960515355557888)

If Programmers’ Day is about the warm and fuzzy, then the 996.ICU campaign was an expression of serious advocacy for the individual rights and well-being of developers. In March 2019, at the peak of the Chinese tech sector’s ruthless competition, a Chinese programmer created a GitHub repository called 996.ICU.

The name was a dark joke: work 996 — 9am to 9pm, six days a week — and you'll end up in the ICU (Intensive Care Unit). The repo quickly became the second most starred repository in GitHub history, accumulating over 200,000 stars in a matter of weeks. Using GitHub as the place to voice this collective concern of overworking is not an accident. Remember when I said GitHub continues to not be blocked in China, despite multiple attempts? That means the content on the website is also generally safe from censorship or erasure.

The GitHub repo may be safe, but China’s big tech firms tried to keep it hidden and tamper its virality. Tencent’s QQ and Alibaba’s UC Browser both blocked 996.ICU’s official website. Jack Ma defended the draconian work schedule as a blessing and privilege.

Nevertheless, the 996.ICU campaign took the internet and media by storm almost instantaneously. It also produced real change. The movement led to the so-called Anti-996 License, drafted by a law student at the University of Illinois College of Law. Adapted from the MIT License, a popular permissive open source license later used by DeepSeek, it added a single, radical clause: any company using software with this license must comply with local labor laws and International Labor Organization conventions. It was designed to protect the rights and health of developers, while still being compatible with all major open source licenses.

[![Image 8: Image](./assets/chinese-open-source-a-definitive-history/image-08.jpg)](https://x.com/kevinsxu/article/2029961571296743585/media/2029960584561840132)

Two years after the campaign started, in August 2021, China's Supreme People's Court, along with the Ministry of Human Resources and Social Security, ruled 996 illegal. It was, as far as I know, the first time that a grassroots, developer-led campaign used open source organizing mechanisms to enforce not just intellectual property norms, but labor rights norms, and ultimately ended in a legal victory.

The irony here is thick and rich, as the 996 work culture is now celebrated, expected, if not required in Silicon Valley, as every startup boasts about how “locked-in” they are in its quest to build world changing technologies in the AI era. Yet, the same toxic culture was rendered illegal years ago by the Chinese developer community using a western website, GitHub, and some decidedly liberal democratic processes to protect themselves from draconian bosses. (996 of course never really died in China in reality.)

The thread connecting the use of GitHub, Kaiyuanshe, Programmers' Day, 996.ICU, and other greenshoots of open source growth in China spells out the broader evolution of a distinct developer community that has grown large enough, skilled enough, and confident enough to not just take and consume, but also create and contribute.

What emerged was an energy that is often referred to as “open source ethos” (开源情怀), where a pure belief in the utopian positive-sumness of open source was merging with an intense engineering drive to prove themselves on the world stage. Part of this ethos came from an acute awareness that no one in the west respects what Chinese developers build, because everything in China is maligned as either stolen or created by cheating. The best way to push back is to not only develop world class technology, but to contribute and give it away by way of open source.

If this sounds a bit like DeepSeek’s vibe, you now know where it came from. But this “open source ethos” and the many technologies it helped create predated Liang Wenfeng’s breakthrough by a decade.

## Act 3: Going Global from Day One

While the big tech companies took open source to fuel their breakneck growth, and as organizations like Kaiyuanshe fostered and systematized an “open source ethos” for the ordinary developers, the mid-2010s also marked the dawn of independent open source projects and startups that originated from China with ambitions to power the world.

It was an era when venture capital in China was also flush, coinciding with a growing approval in Silicon Valley of open source as a way to build big companies. A few thousand stars on a GitHub project could easily draw a few million bucks of seed funding. Chinese VCs, who have always been very plugged into the currents of Silicon Valley, backed top-tier Chinese open source projects aggressively to ride the same wave.

Here are a few standout projects that became well-funded startups worth mentioning.

Apache Kylin, founded in 2015, was one of the first Chinese projects to reach “Top Level” maturity status in the Apache Software Foundation, which was (and still is) a major stamp of approval and legitimacy for any new open source project. The team came out of EBay’s R&D lab in China and the software aims to solve big data analytics challenges, somewhat similar to Apache Spark. The Kylin team later started a startup around their project called Kyligence, backed by venture capital, much like how the Spark team later started the data warehouse juggernaut, Databricks.

TiDB, also founded in 2015, became one of the fastest growing GitHub projects out of China at the time. It was a distributed MySQL-like database that took inspiration from Google Spanner, co-authored by AI luminaries like Jeff Dean. The three founders all had database and infrastructure experiences from China’s fast growing internet sector, including the same JD.com team that took a risk on Kubernetes. The startup that formed around TiDB is called PingCAP and attracted hundreds of millions of venture funding. By 2018, PingCAP was considered good enough to replace Oracle in China.

(Disclosure: I advised Kyligence on its US expansion strategy. I also worked at PingCAP, leading its go-to-market, community, and growth strategy outside of China.)

Many other open source projects got funded to become startups during that time. PingCAP and Kyligene were by no means alone, though they did lead the trend. And China’s big techs took notice of the rapid growth and traction of these independent projects, fueled by VC backing, and felt the pressure to do more than just take open source for their own use.

Oceanbase, the database project that we mentioned earlier in our story as an internal project out of Alibaba’s de-IOE campaign, continued to be developed. It eventually broke the world record of a database industry benchmark called TPC-C in 2019. So in a narrow, benchmark-y sense, Oceanbase became the fastest database in the world! But as a closed source project cloistered inside Ant Financial, Alibaba’s fintech subsidiary, and too closely tied to the tech giant, its traction was limited while TiDB bloomed in the open. To compete with the likes of TiDB, Oceanbase was spun out of Ant in 2020 and open sourced itself in 2021.

The bottom-up, developer-friendly growth engine of open source spread beyond the niche world of infrastructure software like databases.

Baidu, the search engine giant, open sourced its autonomous driving platform, Apollo, in 2017, aiming to be the "Android of self-driving”. The Apollo layer continues to power Baidu’s robotaxis today, which have cumulatively completed 20 million rides worldwide.

Alibaba took open source further to its hardware ambition. Its chip design subsidiary, T-Head, leveraged the open source semiconductor instruction set architecture, RISC-V, and launched an open source processor project called, Xuantie, in 2021. T-Head now builds one of the fastest RISC-V based processor cores in the world. The unit is preparing for an IPO in Hong Kong later this year.

Even the electric vehicle behemoth BYD did not want to be left out of the open source bandwagon. In 2018, BYD hosted a conference to launch its D++ open source platform, allowing developers to freely download and build on top of its software stack that touches sensors and controllers of its cars. It also integrated with Baidu’s Apollo, as open source projects tend to cross-pollinate and interoperate to create a wider platform. If Baidu had ambition to be the “Android of self-driving”, BYD also had ambition to be the “Android of electric vehicles”, all through open source.

These projects, from both independent upstarts and tech giants, never got the headlines and notoriety that DeepSeek would later command. But they built the muscle memory — engineering culture, community management skills, a sophistication in threading the tension between permissive licensing and commercialization expectations — that would prove essential when large language models swept the world.

## Act 4: The Huawei Shock

It is impossible to talk about Chinese open source, or anything China tech, without Huawei. Yet, this national champion did not make an appearance in this telling of Chinese open source history until now. That's because it was relatively late to the open source game. And Huawei would have been happy to remain so, if the world did not turn on it for the worse.

Like other Chinese tech outfits, Huawei started taking and consuming open source software more than two decades ago. As its technology advanced, Huawei also became an active contributor, most notably to the Linux kernel, which is the open source operating system that runs the majority of all computing platforms in the world. By 2018, Huawei ranked among the top contributors to the Linux kernel. But it was fine playing in other people’s ecosystems, rather than investing to create its own.

That all changed on May 15, 2019, the day the U.S. Department of Commerce put Huawei on the blacklist.

If the “de-IOE” campaign showed Chinese tech companies how to leverage open source to grow and scale, Huawei's response to US sanctions demonstrated something more existential: that embracing open source was a matter of corporate, and even national, survival.

The immediate effect of the “blacklisting” was devastating. Huawei was cut off from the entire Google-led Android ecosystem, even though Android is also open source. This hobbled its smartphone products, some of which were starting to outsell Apple’s iPhones in certain markets. It was also cut off from American chips, from Intel to Qualcomm. These restrictions eventually extended to TSMC via the Foreign Direct Product Rule, so Huawei would have a hard time producing chips it designed in-house at the world’s best fabs. The entire American and American-allied technology supply chain was quickly being cut off.

The message from Washington was clear: it wanted to kill Huawei for good.

Huawei had to recreate all the wheels as soon as engineeringly possible. It did not have to start from scratch per se. As far back as 2012, the company started a few internal “Plan B” projects to build alternatives to core technologies that had western technology dependencies. The HarmonyOS project, Huawei’s operating system, started in 2015. The HongMeng Kernel, a microkernel designed from scratch and not based on Linux, began in 2016. By 2017, a working version of HarmonyOS was demoed to Ren Zhengfei, Huawei’s founder and patriarch.

[![Image 9: Image](./assets/chinese-open-source-a-definitive-history/image-09.jpg)](https://x.com/kevinsxu/article/2029961571296743585/media/2029960740627697667)

Ren Zhengfei talking about open source

But when Plan B becomes Plan A, it still takes some adjusting. Huawei had to quickly commit its full resources to developing these half-baked alternatives. More importantly for our story, the company decided to open source as much of it as possible. By that point, Huawei and most Chinese tech companies have internalized that having good code and working technology is fine and all, but their potential is limited without an open ecosystem and developer mindshare.

In typical Huawei fashion, it went all out and all in on open source, holding very little back. On the last day of 2019, it open sourced openEuler, a server-side operating system that would run in its cloud. Throughout 2020, when the whole world was struggling to survive Covid, it open sourced openGauss, a distributed database similar to Oceanbase and TiDB, openLooKeng, a data virtualization engine, and MindSpore, an AI computing framework that would become more prominent later on in the AI era. In September 2020, it not only open sourced OpenHarmony, a mobile operating system based off of HarmonyOS, but also used it to seed a new open source foundation, called the OpenAtom Foundation. This foundation became China’s first homegrown open source foundation with government backing. (This is an important difference from Kaiyuanshe, which continues to be volunteer and grassroots driven today.) To survive, Huawei sought to recreate not just every layer of the technology stack, but also the community fabric of open source.

While all this was going on, the company still used and contributed heavily to Linux to keep the business running and the lights on. So much so that when Linux released its 6.1 version in December 2022, Huawei – not Intel, not Red Hat, but Huawei – was the #1 largest contributor!

By October 2024, when Huawei launched HarmonyOS NEXT, it had removed every line of Android code, replaced the Linux kernel with its HongMeng microkernel, and started to power every app in its vast ecosystem with its own code. No more Android. No more Google lineage. The divorce with western technology was complete.

## Act 5: Enter the State

The government played a minimal role for much of open source’s history in China. Growth and evolution stayed entirely within the confines of private business needs (like Alibaba’s de-IOE campaign) and grassroots community passions (like Kaiyuanshe). It is possible that some lower level officials might have heard of and tried to study open source in its early years, but this mode of technology development did not reach any level of priority or prominence. If anything, its inherent social organizing mechanisms – chatting and collaborating with developers from all corners of the world – presented risks to China’s walled garden internet.

This under-the-radar status changed in 2021, when the Ministry of Industry and Information Technology (MIIT), the main bureaucracy and regulator of China’s tech industry, formalized open source in its planning document as a component of the country’s 14th five-year plan. The term “open source” was namechecked 27 times. The creation of OpenAtom Foundation led by Huawei was called out as a major accomplishment and example to follow. The Ministry set a target of building and fostering two to three open source communities with “global influence” by 2025.

This government embrace, as with any government embrace, presented a double-edged sword.

On the positive side, it is better to be on the right side than the wrong side of the government in an economy like China’s. Always. Just ask anyone who was working in the EdTech or high finance industry a few years ago. It also means more resources were allocated on the local level to echo the central government’s embrace. Some of these new resources would end up wasted or tied to ambitious officials’ promotion plans, but some ended up doing some good. This is a pattern that gets replayed time and time again in China – in semiconductors, solar, batteries – becoming almost a necessary cost of doing business for Chinese-style industrial policy. But waste of this type is always better than being on the wrong side.

On the negative side, explicit government attention also means heavy-handed tactics, like picking winners. This happened even before MIIT’s five year plan document when, in August 2020, the Ministry anointed Gitee, a homegrown Git-based clone of GitHub, as the preferred source code management company (or national champion) and the platform to foster more domestic open source growth. Except open source is by definition global; no good open source technology ever got created within the confines of one country. Every Chinese tech company, from Alibaba to PingCAP, of course knew that already, having practiced open source at a high-level. To comply, every notable Chinese open source project was recreated and mirrored from GitHub to Gitee – an extra copy that became extra work and an extra pain in the butt to maintain. Meanwhile, most of the activities still happened on GitHub, and later on HuggingFace, a similar collaboration platform that hosts open weight models and datasets, as open source AI took off.

There is a tendency to overplay the Chinese government’s role and influence in every sector of the economy. For some, the influence is true and valid. For open source at least, the government came much later into the picture. In this case, the bureaucrats followed the code and the community, not the other way around.

## Act 6: DeepSeek and Open Weight AI

When DeepSeek popped up on everyone’s radar in January 2025, what made its R1 reasoning model’s release extraordinary to me was not its (somewhat debatable) cost-effective performance that tanked NVIDIA’s stock price, but how it was released. MIT license to permit all use cases with no restrictions. Full chain-of-thought displayed for all to see (and distill from). Followed up by an open source week, where DeepSeek open sourced more components of its tooling every day for a week to further drum up community participation and ecosystem activity.

It was a classic open source launch playbook executed to perfection (and succeeded probably way beyond the DeepSeek team’s expectations). It was an example of maturity in how to open source the “right way” that was two decades in the making. And DeepSeek was not alone.

Alibaba’s Qwen team was even earlier than DeepSeek in open sourcing their model weights, as well as using an equally permissive license, called Apache 2.0. When Kimi launched its Kimi 2.5 open weight model, its founder, Yang Zhilin, and other members of the core team hosted AMAs on Reddit and engaged directly with the community, in English. It was a move and a signal of confidence that would be hard to pull off by a Chinese open source founder a few years ago. Yang later took to X/Twitter to launch Kimi 2.5 in a direct-to-camera video.

Zhipu AI’s team also hosted multiple Reddit AMA threads whenever it launched a new version of its MIT licensed GLM model.

[![Image 10: Image](./assets/chinese-open-source-a-definitive-history/image-10.png)](https://x.com/kevinsxu/article/2029961571296743585/media/2029960901978099722)

Yang Zhilin going direct to camera.

Beyond the maturing community building tactics and growing confidence in interacting with a predominantly western online audience in English, Chinese open source AI labs also have increasingly sharper commercial instincts. When OpenClaw, the open source AI agent framework, took the internet by storm a few weeks ago, Kimi and MiniMax were some of the first companies to offer a fully-hosted OpenClaw solution on their platform with no setup required. This open source commercialization playbook – cloud hosted solution to popular open source tools that are hard to set up – is tried and tested by cloud giants like AWS and independent software vendors like MongoDB. This playbook was well-internalized by every Chinese open source founder, maintainer, contributor, and operator, waiting to unleash it in the AI world.

The AI generation of open source builders from China was arguably the biggest AI story in 2025. The progress of the models, the pace of the releases, and the number of AI labs that both compete with each other but also seem to cheer each other on came fast and furious with no signs of slowing down. I won’t rehash the many comparative analysis of benchmarks or the ethics of AI distillation here. What I hope to paint is a lively picture of the many generations of open source practitioners in China, who distilled (not in the AI training sense) a foundation of knowledge that the current generation of AI builders are standing on.

Did Liang Wenfeng of DeepSeek ever crash a 1024 Programmers’ Day party?

Did Yang Zhilin of Moonshot AI ever attend a webinar on community building best practices from Kaiyuanshe?

Did Wang Xingxing, who founded the humanoid robotic upstart Unitree, absorb some “open source ethos” during his younger years? That would certainly explain Unitree’s decision to open source its own unitree_rl_gym – the brain of its robots – and maintain an active GitHub presence, unique among robotic startups in both China and the US.

These acts of open source contribution in AI often get lumped in as yet another part of China’s “evil plan” to amp up overcapacity to flood the world with its creations, this time with software and model weights. As you have learned by now, this notion is historically inaccurate. Never mind the irony that China is now deliberately working to curb overcapacity and eradicate involution.

What is true is that Chinese tech entrepreneurs are having a hard time finding ways to grow beyond China, and open source is a key strategy to expanding beyond their borders. The domestic economy isn’t doing great, evidenced by the lowest GDP growth target since 1991, so the ceiling of growth at home is low. But going overseas is full of hurdles too, from the toxicity of “China” as a label to the many inherent challenges of building products that appeal to different markets and different tastes.

Open source gives would-be users, developers, and customers a taste of what you can do with no cost, no licensing burden, and no legal ramifications (not yet anyways), while letting the technology be judged on performance and merit alone. Some upfront, short-term revenue may be given up with this approach, but if the technology can stand on its own two feet, then the branding and word-of-mouth goodwill is worth this cost. Open source has become a necessary, not a nice to have, part of any overseas growth strategy.

Two of Jensen Huang’s most frequently quoted talking points when it comes to China are: 1) China has 50% of the world’s AI talent; 2) Open source AI from China is impressive. It is always funny to me that he never mentions those two things together as one interconnected point. Because open source is at the heart of every engineer’s educational journey, whether you started out as a teenager hacker, or went through a fancy university program, or got trained mid-career at a bootcamp.

There is no technical talent pipeline without access to and an active embrace of open source. Every technical education program uses open source. This is not just because open source is free and most educational institutions are poor. It is because openness and transparency of every technical detail is at the heart of teaching and learning.

How do you teach students how something works and let them learn, explore, and tinker, if you can’t see and change the code (or weights)? As a country or society, if you don’t promote open source, even if only for the selfish purpose of educating your own people to compete with another country, how do you hope to ever exercise any level of control or sovereignty over AI and its growing capabilities?

The story of Chinese open source is fundamentally a story of absorbing, adapting, and eventually innovating under tension. It is an organic, loosely-organized tribe, who prefers openness and transparency — values often associated with and practiced in the west. It has now developed its own flavor and prerogative to respond to the pressure of self-reliance and the aspiration for global recognition.

Now that its history is documented (definitively, dare I say), the future is still being written. How will this future unfold? As someone who’s been steeped in open source for many years, my rule of thumb is to always follow the developers, as more technology is being built, in the open, by Chinese developers, than ever before.

[![Image 11: Image](./assets/chinese-open-source-a-definitive-history/image-11.jpg)](https://x.com/kevinsxu/article/2029961571296743585/media/2029961062108581888)

Friendly reminder timeline of everything you just read
