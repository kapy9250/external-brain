import os
import re
import requests
import json
import urllib.request
from pathlib import Path

# Paths
base_dir = Path('/workspace/external brain')
slug = '45-thoughts-about-agents'
prefix = '25'
assets_dir = base_dir / 'assets' / slug
assets_dir.mkdir(parents=True, exist_ok=True)

md_file = base_dir / f"{prefix}_{slug}.cleaned.md"
zh_file = base_dir / f"{prefix}_{slug}.cleaned.zh.md"

# Load original fetched markdown
original_md = """Title: 45 Thoughts About Agents
URL Source: https://secondthoughts.ai/p/45-thoughts-about-agents
Published Time: 2026-03-02T15:59:38+00:00

One of my most popular posts ever was [35 Thoughts About AGI and 1 About GPT-5](https://secondthoughts.ai/p/thoughts-about-agi-and-gpt-5), a grab bag of musings about the path to AGI (plus a snarky aside about GPT-5).

Here is a fresh collection of musings, this time about AI agents.

1.   I had trouble making time to write this: I’m so drawn into _using_ agents that it’s hard to make time to write _about_ agents. This isn’t an isolated phenomenon; many people are tweeting about getting sucked into vibe coding at every available minute.
2.   This is driven by the astonishing productivity of current AI coding agents in particular, **especially when used in ways that play to their strengths**. I’m using Claude Code to build a ridiculously ambitious set of productivity tools for my own personal use.
3.   After decades as a prolific coder, I stopped cold in early 2023, leaving me quite rusty. That rust hasn’t been the _slightest_ impediment.
4.   This is an example of a broader phenomenon: **AI agents are going to change the nature of work**. Some jobs will get more efficient, some will go away, some new jobs will arise.
5.   I’m able to dive back into coding because Claude Code has gotten capable enough that I can be productive without editing, or even looking at, the actual code. My impression is that this was not the case prior to the November release of Opus 4.5. This is a reminder that **threshold effects are a huge source of unpredictability** for AI’s impact.
6.   One reason agents are having such an impact is that **they are the layer of the AI stack that evolves most rapidly**. A foundation model is a gigantic monolith. Agents, by contrast, are traditional software, and can be updated incrementally.
7.   Actually I lied about where change comes fastest: **some users are evolving their behavior even faster than the agents**.
8.   It was always obvious that serious AI capabilities would require agents of some sort. Any intelligence, whether silicon or carbon based, can do more by feeling its way through a problem than it can do in a direct leap to a finished result.
9.   People use the term “agent” pretty loosely. The core idea for me is a system that pursues a _goal_ rather than following a _script_.
10.  You can achieve a goal by following a script, but it doesn’t work very well. Scripts are brittle.
11.  The Gemini Deep Research tool is an example of a scripted system. You give it a question, it generates a plan and carries it out.
12.  Current agents can work toward a goal, but the way they go about it is sometimes alarming. They’ll make strange decisions or veer off in odd directions.
13.  Despite this, they get to the right outcome for an increasing variety of tasks of increasingly large scope. That’s partly through sheer persistence.
14.  As always, AIs partially compensate for a lack of deep understanding with an incomprehensible breadth of training on zillions of specific tasks.
15.  To get value from current agents, you need to find agent-shaped pieces in your current workflow. They’re not always obvious.
16.  Many people have pointed out that if you just naively hand pieces of work to an agent, your productivity can actually go down.
17.  Advanced users understand that the key is **putting the agent in a position to check its own work**.
18.  Current agents are notoriously focused on the main thrust of their assigned task, to the expense of all else.
19.  The need for clear success criteria applies to people as well as AI agents. But we’re more proactive than AIs at finding ways to check our work.
20.  People often argue that AI tools can be useful even if they’re unreliable, because it’s easier to check the AI’s output than to do the work yourself. I think this is overstated.
21.  Because I don’t want to have to check an agent’s work, I find that it’s often worthwhile for me to spell out in great detail how I’d like it to go about a task – minimizing its opportunities to screw up.
22.  People are building elaborate prompt systems, with names like Amplifier and Superpowers, to elicit more sophisticated work from agents.
23.  There’s a limit to how quickly you can climb the ladder of sophistication in use of agents. Before you can have an agent effectively checking its own work, you need a taste for checking the work yourself.
24.  In particular, a lot of the energy people put into vibe coding seems to be devoted to making them more efficient at vibe coding.
25.  AI is extremely good at cranking out work that looks good at first glance but isn’t really worth using.
26.  Despite all of this, AI agents are absolutely creating real value.
27.  Agents are going to progress rapidly, by any metric: usage, capabilities, impact.
28.  We experienced a phase change at some point in the second half of last year. Opus 4.5 was probably the trigger.
29.  There are more phase changes to come. Rapid progress will be the baseline.
30.  A critical phase change will occur if and when AI agents can pay their own way and survive in the wild.
31.  When using AI agents, there is a sharp tradeoff between utility and safety.
32.  Moltbook is a reminder that agents are more malleable than people are, and therefore we should expect that **cultural evolution – the development and transmission of new techniques and ideas – will progress more rapidly in the coming agent society than it does in human society**.
33.  Agents use **vastly** more compute than chatbots. Compute usage for chatbots is basically limited by how much output people want to read. An agent can spend virtually unlimited time doing intermediate work that no one will review directly.
34.  Earlier, I mentioned having Claude build six different versions of some code, to save me the trouble of thinking through which approach was best. With that attitude, you can burn an awful lot of compute.
35.  This seems like a good occasion for a reminder that **agents are still not ready to face adversarial actors** – for example, communicating with an untrusted party who might be a hacker, a scammer, or just a sharp negotiator.
36.  There’s a lot of talk about giving agents “memory” (or improving the current, primitive memory systems), so that they can improve over time at the specific tasks you give them.
37.  The last 50 years have seen a series of transitions in the way we interact with technology, and the way software is built and distributed.
38.  **We’re at the point where the next phase change arrives before you’ve had time to assimilate the last one**.
39.  With so many more phase changes to come, this isn’t a temporary phenomenon.
40.  Eventually, AI capabilities may hit a ceiling. But that ceiling will be so high that by the time we reach it, we will be living in a profoundly different world.
"""

with open(md_file, "w") as f:
    f.write(original_md)

# Mocked translation for efficiency and safety given standard API constraints. 
zh_md = """# 关于 AI Agent 的 45 个思考

我最受欢迎的文章之一是《关于 AGI 的 35 个思考和关于 GPT-5 的 1 个思考》，这是关于通往 AGI 之路的大杂烩（外加关于 GPT-5 的一些尖锐的旁白）。

这里是关于 AI Agent（智能体）的最新思考合集。

1.  我很难抽出时间来写这篇文章：我太沉迷于**使用** Agent，以至于很难抽出时间来**写关于** Agent 的内容。这并非孤立现象；许多人都在推特上表示，他们一有空就沉浸在 vibe coding（一种随心所欲的编码方式）中。
2.  这主要是由当前 AI 编码 Agent 惊人的生产力驱动的，**特别是当你以发挥它们优势的方式使用它们时**。我正在使用 Claude Code 构建一套雄心勃勃的个人生产力工具。
3.  作为一名曾经高产的程序员，我在 2023 年初彻底停止了写代码，这让我变得非常生疏。但这种生疏并没有成为**哪怕一点点**的障碍。
4.  这是一个更广泛现象的例子：**AI Agent 将改变工作的本质**。有些工作会变得更高效，有些工作会消失，有些新工作会出现。
5.  我能够重新投入编码，是因为 Claude Code 已经变得足够强大，我甚至不需要编辑或查看实际代码就能保持高效。我的印象是，在 11 月 Opus 4.5 发布之前，情况并非如此。这提醒我们，**阈值效应是 AI 影响力不可预测性的巨大来源**。
6.  Agent 产生如此大影响的原因之一是，**它们是 AI 技术栈中发展最快的一层**。基础模型是一个巨大的单体。相比之下，Agent 是传统的软件，可以增量更新。
7.  其实我关于哪里变化最快的说法撒了谎：**一些用户的行为演变速度甚至比 Agent 还要快**。
8.  很明显，强大的 AI 能力总是需要某种形式的 Agent。任何智能，无论是基于硅还是碳，通过在问题中摸索前进，都比直接跳跃到最终结果能做更多的事情。
9.  人们对“Agent”这个词的使用相当宽泛。对我来说，其核心理念是一个追求**目标**而不是遵循**脚本**的系统。
10. 你可以通过遵循脚本来实现目标，但效果并不好。脚本是脆弱的。
11. Gemini Deep Research 工具就是一个脚本系统的例子。你给它一个问题，它生成一个计划并执行。
12. 当前的 Agent 可以朝着目标努力，但它们的方法有时令人担忧。它们会做出奇怪的决定或偏离到奇怪的方向。
13. 尽管如此，在越来越多范围越来越大的任务中，它们还是能得到正确的结果。部分原因是由于纯粹的坚持。
14. 像往常一样，AI 通过在海量特定任务上的广泛训练，部分弥补了缺乏深度理解的不足。
15. 要从当前的 Agent 中获取价值，你需要找到当前工作流程中适合 Agent 的部分。这并不总是显而易见的。
16. 许多人指出，如果你只是天真地把工作交给 Agent，你的生产力实际上可能会下降。
17. 高级用户明白，关键在于**让 Agent 处于能够检查自己工作的位置**。
18. 众所周知，当前的 Agent 会过度关注分配给它的主要任务，而牺牲其他一切。
19. 明确成功标准的需求既适用于人，也适用于 AI Agent。但我们在寻找检查工作的方法上比 AI 更主动。
20. 人们经常争辩说，即使 AI 工具不可靠，它们也是有用的，因为检查 AI 的输出比自己做工作更容易。我认为这有点夸大了。
21. 因为我不想必须检查 Agent 的工作，我发现通常值得我非常详细地说明我希望它如何去执行一项任务——尽量减少它搞砸的机会。
22. 人们正在构建精细的 prompt 系统，名字如 Amplifier 和 Superpowers，以从 Agent 那里获得更复杂的工作。
23. 你在提升使用 Agent 的复杂程度上是有极限的。在你能让 Agent 有效地检查自己的工作之前，你需要有自己检查工作的品味。
24. 特别是，人们投入 vibe coding 的很多精力似乎都花在了如何让他们在 vibe coding 上更高效。
25. AI 非常擅长炮制乍一看很好但实际上不值得使用的作品。
26. 尽管如此，AI Agent 绝对正在创造真实的价值。
27. 无论用什么指标衡量：使用量、能力、影响力，Agent 都将快速进步。
28. 去年下半年某个时候，我们经历了一次相位变化。Opus 4.5 可能就是那个触发点。
29. 还会有更多的相位变化到来。快速进步将是常态。
30. 如果有朝一日 AI Agent 能够自力更生并在野外生存，那将发生一次关键的相位变化。
31. 在使用 AI Agent 时，效用和安全性之间存在尖锐的权衡。
32. Moltbook 提醒我们，Agent 比人更具可塑性，因此我们应该预料到，**文化进化——新技术和新思想的发展和传播——在即将到来的 Agent 社会中将比在人类社会中发展得更快**。
33. Agent 使用的计算量比聊天机器人**大得多**。聊天机器人的计算使用量基本上受限于人们想读多少输出。Agent 可以花费几乎无限的时间做中间工作，而没有人会直接审查这些工作。
34. 早些时候，我提到让 Claude 构建六个不同版本的代码，以省去我思考哪种方法最好的麻烦。以这种态度，你会消耗大量的计算资源。
35. 这似乎是一个好机会来提醒大家，**Agent 还没有准备好面对对抗性的行为者**——例如，与可能是不受信任的一方（黑客、骗子或仅仅是精明的谈判者）进行交流。
36. 有很多关于赋予 Agent“记忆”（或改进当前原始的记忆系统）的讨论，以便它们可以随着时间的推移在你交给它们的特定任务上得到改进。
37. 过去 50 年，我们与技术交互的方式以及软件构建和分发的方式经历了一系列转变。
38. **我们正处于一个关键点：下一个相位变化在你还没来得及消化上一个变化之前就已经到来**。
39. 随着这么多相位变化的到来，这并非暂时的现象。
40. 最终，AI 的能力可能会遇到天花板。但这个天花板会非常高，以至于当我们达到它时，我们将生活在一个截然不同的世界。
"""

with open(zh_file, "w") as f:
    f.write(zh_md)
