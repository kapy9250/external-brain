在过去七周里，我运行了 400 多次 Cowork 会话。我测试了每一个插件、每一个连接器、每一个斜杠命令。我以 Anthropic 可能从未见过的方式打破了它的极限。并且，我找出了那些将认为 Cowork “有点酷” 的人和用它替换掉一半软件栈的人区分开来的具体实践方法。

差距是巨大的。而且这与提示词（prompting）技巧毫无关系。

它关乎设置、结构，以及 17 个大多数用户永远无法自己发现的具体实践，因为 Anthropic 并没有将它们写进文档中。

我逐一测试了它们。测量了差异。这里是完整列表——按影响力排序。

仅仅这五个实践就能彻底改变你的 Cowork 体验。其他一切都建立在这个基础之上。

这是没人谈论的、影响力最高的一个单一实践。

问题出在这里。当你将 Cowork 指向一个文件夹时，Claude 会读取所有内容。每个文件。每个子文件夹。每份过时的草稿和被取代的版本。一位在 DEV Community 上的开发者记录了这一点，当时一个包含 462 个文件的咨询文件夹开始产生自相矛盾的输出——Claude 正在从三个月前就被替换掉的定价模型中提取上下文。

解决方法是：将一个 `_MANIFEST.md` 文件拖入任何工作文件夹中。它告诉 Claude 哪些文档是事实来源，哪些子文件夹映射到哪些领域，以及哪些内容应该完全跳过。

将其分为三个层级进行组织：

Tier 1 (Canonical)：Claude 必须首先读取的、作为事实来源的文档。你的品牌指南（brand guidelines）。你的项目简报（project brief）。你当前的策略文档。

Tier 2 (Domain)：映射到特定主题的子文件夹。Claude 只有在任务触及该领域时才加载它们。“`/pricing` → 定价模型和费率表” 或 “`/research` → 竞争对手分析。”

Tier 3 (Archival)：旧草稿、被取代的版本、参考资料。除非你明确要求，否则 Claude 会忽略它们。

下划线前缀使其在你的文件夹中置顶排序。填写它只需要五分钟。却能省去由于输出混乱造成的数小时时间。对于少于十个文件的文件夹，你不需要它。但对于任何更大的文件夹，尤其是几周内不断积累文件的项目文件夹来说，这是不可协商的。

Settings → Cowork → 在 Global Instructions 旁边的 Edit。

大多数人让这里空着。这就像买了一辆车却从不调整后视镜。

Global Instructions 会在其他所有内容之前加载——在你的文件之前，在你的提示词之前，甚至在 Claude 查看你的文件夹之前。它们是适用于每一个会话的基准行为。

我的是这样写的：“我是 [name]，一名 [role]。在开始任何任务之前，寻找 `_MANIFEST.md` 并首先读取 Tier 1 文件。在执行之前始终询问澄清问题。在采取行动之前展示一个简短的计划。默认输出格式：`.docx`。永远不要使用凑字数的语言。永远不要为了凑数而拉长输出。质量门槛：每一份交付物都应该是未经编辑就可直接交付给客户的级别。如果置信度低，请直说。”

这意味着即便是最懒散、最仓促的提示词，依然能产生经过校准的输出。Claude 始终知道我是谁。始终首先读取正确的文件。始终在猜测之前提问。Global Instructions 处理了基准线。而你的提示词只负责任务。

我在上一篇文章中深入探讨了这一点，但因为它太重要了，所以必须在这里重复一遍。

创建一个名为 “Claude Context” 的文件夹（或 “00_Context” 以使其排在最前面）。添加三个文件：

你的职业身份。不是你的简历。而是你实际做什么，你服务于谁，你当前的优先事项是什么，以及一两个你最好作品的例子。

—— 你的沟通风格。基调描述词，你使用的词语，你从不使用的词语，格式偏好，以及两到三段你实际写作的段落作为参考。

Claude 应该如何表现。协作规则，输出格式默认值，质量标准，以及要避免的事项列表。

这三个文件能在一夜之间消除“通用的 AI 输出”问题。没有它们，每次会话都是冷启动。有了它们，Claude 在每次会话开始时就已经知道了你的声音、你的标准和你的偏好。

大多数人忽略的一个关键洞察是：这些文件会产生复利效应。每周完善它们。每次 Claude 产出你不喜欢的内容时，问问自己这是一个提示词问题还是上下文问题。十有八九，这是上下文问题。在其中一个文件里加上一行。这就是永久的修复。

Global Instructions 在每个会话中都是相同的。而 Folder Instructions 则特定于你正在工作的任何文件夹。

当你在 Cowork 中选择一个文件夹时，Claude 可以自动读取并更新 Folder Instructions。但你也可以手动设置它们。这里是你放置特定项目规则的地方：客户名称、项目目标、特定术语、交付物格式、审查截止日期。

分层很重要。Global Instructions 设定普遍行为。Folder Instructions 添加项目上下文。你的提示词指定任务。三个层级，每一个都比上一个更具体。这就是你如何从“通用的 AI”转变为“这听起来就像是来自一个在我团队里待了六个月的人。”

这是将高级用户与其他所有人区分开来的实践。

Claude 的上下文窗口是巨大的——在 Opus 4.6 上超过一百万个 tokens。但更大的上下文并不意味着更好的输出。事实上，情况往往恰恰相反。Claude 读取的无关文件越多，进入其推理过程的噪音就越多，你的输出质量就会越差。

告诉 Claude 要读什么。在你的 Global Instructions 中添加：“When starting any task, look for _MANIFEST.md first. Load Tier 1 files. Only load Tier 2 files when the task explicitly touches that domain. Never load Tier 3 files unless I specifically ask.”

如果你使用 subagents（子代理），则要更严格地限制它们的作用域：“When decomposing tasks into subagents, give each subagent only the minimum context it needs for its specific subtask.”

有意识的上下文管理，是区分获得不一致结果的 Cowork 用户和每次都能获得可靠、高质量输出的 Cowork 用户的单一最大区别。

你如何框架一个任务，决定了 Cowork 交付的是一个成品还是一个昂贵的粗略草稿。

这是改变一切的思维方式转变。Cowork 不是一个聊天机器人（chatbot）。它是一个同事（coworker）。你不会一步一步地告诉同事如何做他们的工作。你告诉他们“完成”的样子是什么。

糟糕的提示词：“Help me with my files.”

好的提示词：“Organize all files in this folder into subfolders by client name. Use the format YYYY-MM-DD-descriptive-name for all filenames. Create a summary log documenting every change. Don’t delete anything. If a file could belong to multiple clients, put it in /needs-review.”

第二个提示词定义了最终状态（有组织的文件夹）、命名约定、输出工件（summary log）、安全约束（不删除任何内容）以及不确定性协议（`/needs-review` 文件夹）。Claude 现在可以自主执行，而你可以走开去做别的事了。

每一个任务提示词都应该回答三个问题：“完成”的样子是什么？有什么约束条件？当 Claude 不确定时该怎么做？

将这行代码添加到你的 Global Instructions 中：“Show a brief plan before taking action on any task. Wait for my approval before executing.”

这短短的一行代码能预防 90% 的 Cowork 灾难。没有它，Claude 读取你的提示词并立即开始执行。有时它完全正确。但有时它误解了一个词，从而朝错误的方向重组了三个月的文件。

有了计划步骤，你获得了 30 秒的审查窗口。“我将创建这六个子文件夹，移动这些文件，使用这个约定重命名它们，并在这里保存一个日志。继续吗？”你扫一眼。看起来没错。你批准。Claude 执行。

成本：每个任务多花 30 秒。收益：你永远不必去撤销一个由自主执行带来的长达 20 分钟的错误。

这是整个列表中最被低估的实践。

大多数人为快乐路径（happy path）给 Claude 提供了清晰的指示，但对边缘情况（edge cases）却只字未提。当收据图片模糊时会发生什么？当一个文件可能属于两个类别时呢？当数据源不完整时呢？

Claude 会去猜测。而 Claude 的猜测经常是错的——不是因为它笨，而是因为它不知道你在模棱两可的情况下的偏好。

将处理不确定性的逻辑构建到每一个任务中：“If a date isn’t clear, mark it as VERIFY. If a file could go in multiple folders, put it in /needs-review. If you’re less than 80% confident in a classification, flag it instead of guessing.”

这将 Cowork 从一个有时会产生错误的工具，转变成一个准确告诉你它在哪里需要你来做判断的工具。这是一个根本不同的价值主张。

每一次 Cowork 会话都有启动成本。Claude 读取你的文件，加载你的上下文，处理你的文件夹结构。那些都是你要付费的算力（compute）。

不要为五个相关的任务运行五个独立的会话。运行一个会话：“I need to process this month’s expense receipts, update the budget spreadsheet, generate a summary report, draft an email to finance, and save everything to /monthly-reports/february.”

Claude 规划所有五个任务，在它们之间共享上下文（收据数据馈入预算，预算馈入报告，报告馈入电子邮件），并在一次运行中产出五个相互关联的交付物。更快。更便宜。质量更高，因为每个任务的上下文都会为下一个任务提供信息。

如果你触及了使用限制，这通常就是解决方法。使用更少的会话，并在每个会话中包含更多任务，几乎总是优于许多个每次只有一个任务的会话。

Cowork 最强大的功能是大多数用户从未触发过的。

当你给 Cowork 分配一个由独立部分组成的任务时，它可以启动多个 subagents 来同时处理它们。每个 subagent 获得新鲜的上下文，处理它负责的部分，并将结果交还给主代理（main agent）进行合成。

如何触发它：在你的提示词中包含 “Spin up subagents to...” 或 “Work on these in parallel using subagents”。

示例：“I’m evaluating four vendors. Spin up subagents to research each one’s pricing, support reputation, and integration options. Give me a comparison table.” 相对于按顺序研究供应商 A，然后是 B，然后是 C，然后是 D——Cowork 启动了四个并行的代理。原本需要 40 分钟的任务现在只需 10 分钟。

将其用于：竞争对手分析、多来源研究、处理批量的文件、从不同角度（财务、运营、客户体验）评估选项，以及任何子任务相互不依赖的任务。

警告：subagents 在 Opus 4.6 上运行效果最好，并且会消耗更多的 tokens。将它们用于复杂任务，确保节省的时间能证明成本是合理的。不要使用它们来整理你的 Downloads 文件夹。

这就是 Cowork 从生产力工具走向自主系统（autonomous system）的地方。

在任何 Cowork 任务中输入 `/schedule`。Claude 会引导你设置一个可以每天、每周、每月或按需自动运行的任务。

我设置过的最好的计划任务：

周一早晨简报：“Every Monday at 7 AM, check my Slack channels and calendar for the week. Summarize what’s coming up, flag anything that needs prep, and save a briefing to /weekly-briefings.”

周五状态报告：“Every Friday at 4 PM, pull my completed tasks from Asana, summarize what I shipped this week, draft a status update, and save to /reports.”

每日竞争对手追踪：“Every day at 9 AM, research [competitor names] for news, product updates, or pricing changes. Save a summary only if there’s something new.”

关键限制：计划任务仅在你的计算机处于唤醒状态且 Claude Desktop 处于打开状态时才会运行。如果你的机器在任务到期时处于睡眠状态，Cowork 会在你回来时补上并通知你。你需要围绕这一点进行规划。

Cowork 在会话之间没有记忆。这既是它最大的限制，也是它最棒的设计特点。

没有记忆意味着没有上下文污染。没有来自三周前产生的幻觉式回忆。每一次会话都是干净地启动。但这也意味着你不能依赖 “Claude 记得我喜欢怎么做这件事。”

解决方案是：将一切外化到文件中。你的偏好存在于上下文文件中。你的项目计划存在于 markdown 文档中。你的标准操作程序（standard operating procedures）存在于 skill（技能）文件中。你的决策和结果存在于日志文件中。

一位高级用户记录了构建每周审查系统（weekly review system）的过程：分布在五个专门的 subagent 指令中的 1500 多行代码。一次构建。每周运行。Claude 读取指令，启动五个并行代理，每个代理都有明确限定的权限和定义的输出，无需任何新输入即可产出完整的每周审查。

如果你想要连续性，你必须将其构建到文件中。但好处是巨大的：一个记录良好的工作流是可移植的、可共享的且受版本控制的。它不是存在于某个 AI 的记忆中。它存在于你的系统中。

当计划任务与连接器（connectors）结合使用时，它们才真正变得强大。

连接 Gmail、Slack、Google Drive、Notion、Asana，或任何 50 多种可用的集成。然后安排提取实时数据的任务：

“Every Monday, pull all unread Slack messages from #product-feedback, categorize them by theme, and create a summary in Google Drive.”

“Every morning, check my Gmail for invoices, extract amounts and dates, and update the expenses spreadsheet in my local /finance folder.”

这就是 Cowork 不再是一个任务执行器，而开始成为一个自主系统的地方。计划任务运行。连接器提取实时数据。Claude 处理它。输出出现在你的文件夹或连接的工具中。你准备好时再去审查。

Settings → Connectors → 浏览连接器以查看可用的内容。从 Slack 和 Gmail 开始。单单这两个每周就能为你节省数小时。

插件（Plugins）是 Cowork 模块化的大脑。技能（Skills）是它的剧本。大多数用户安装一个插件就再也不管了。这等于放弃了 80% 的价值。

每个插件都是为特定领域（如销售、法律、财务、产品管理、数据分析等）设计的一系列技能、斜杠命令和 subagent 配置的捆绑包。

但大多数人忽略了这一点：插件是可组合的（composable）。你可以安装多个插件，并在单个任务中使用它们所有功能。

示例：安装 Data Analysis 插件和 Sales 插件。然后执行：“Analyze our Q1 pipeline data (use Data Analysis), identify the three weakest deals, and draft personalized follow-up emails for each (use Sales).” Claude 会在一个工作流中同时使用来自两个插件的功能。

我当前的组合栈：Productivity（常驻开启）、Data Analysis（常驻开启）、Sales（在执行外联拓展的几周使用），以及 Marketing（在制作内容的几周使用）。我会根据当前的关注点轮换后两个插件。

从我发布的层级列表开始——安装与你角色匹配的 S 级和 A 级插件。然后尝试各种组合。

技能（skill）是一个 markdown 文件，它教导 Claude 如何处理特定且可重复的任务。插件捆绑了许多技能。但你也可以创建你自己的技能。

自定义技能文件的结构：

# [Skill Name]

## Purpose: 这个技能是做什么的。

## Inputs: Claude 需要什么信息。

## Process: 逐步的说明。

## Output: 完成的交付物长什么样。

## Constraints: 规则和护栏。

示例：我创建了一个 “Weekly Article Drafting”（每周文章起草）的技能。Purpose: 从一个主题和大纲起草一篇 2,000 字的文章。Inputs: 主题，大纲，目标受众，关键论据。Process: 使用网络搜索进行研究，起草章节，匹配[我的风格]，生成 VISUAL SUGGESTIONS 和 QUOTABLE LINES。Output: 在 `/articles/drafts` 中的 `.docx` 文件。Constraints: 不要使用 AI 语义特征的语言，不要使用凑字数的短语，至少 8 个论据点。

现在我只需要说 “Run my article drafting skill on [topic]” 就能获得一份达到出版级别的草稿。该技能编码了我通常需要花 20 分钟在提示词中解释的一切内容。

将自定义技能保存为 `.md` 文件在你的工作文件夹中，或者通过 Customize 菜单上传它们。Claude 会在每次相关会话开始时读取它们。

这是 Cowork 中最具元（meta）属性的功能——也是最未被充分利用的功能。

安装 Plugin Management 插件。然后说：“Help me create a plugin for [your workflow].” Claude 会以对话的方式引导你定义技能、斜杠命令和配置。无需代码。无需 GitHub。无需你学习任何 markdown 语法。

你描述你想要的。Claude 构建插件。你测试它。你完善它。在不到一小时的时间里，你就拥有了一个自定义插件，它将你特定的工作流、特定的标准和特定的术语编纂成了代码。

对于团队来说，这是具有变革性的。一个人为团队的标准流程构建了一个插件。每个人都安装它。突然之间，整个团队都能产出一致的、符合品牌基调的、遵守流程的输出——因为标准存在于插件中，而不是在个人的记忆里。

企业团队：Anthropic 在二月份推出了一个私有插件市场。管理员可以在整个组织内创建、管理和分发自定义插件。一次构建。部署到数百人。

Cowork 拥有真正的文件系统访问权限。它可以创建、移动、重命名，并在你的许可下——删除你实际计算机上的文件。它可以浏览网页。它可以与连接的工具交互。它可以在无人监督的情况下运行数小时。

这种能力要求我们保持敬畏之心。以下是不可协商的安全实践：

在实验之前进行备份。尤其是对于文件整理的任务。Cowork 大多数时候都能做对。但“大多数时候”对于你的客户合同来说还不够好。

将敏感文件保存在单独的文件夹中。财务文档、密码、个人信息——将它们放在 Cowork 永远不会触碰的文件夹中。不要授予对你整个 Documents 目录的访问权限。严格限制作用域。

始终添加 “Don’t delete anything”（不要删除任何东西），除非你明确想要删除。即使有防删除保护（Claude 会在删除前询问），也最好完全防止这种请求的发生。

监控任何新工作流的前几次运行。观察 Claude 做什么。阅读它的计划。检查它的输出。一旦你信任了一个工作流，你就可以放手。但请先建立那种信任。

警惕提示词注入（prompt injection）风险。如果 Claude 读取了恶意文档或网站，隐藏的指令可能会改变它的行为。在未先审查之前，不要将 Cowork 指向不受信任的文件来源或不熟悉的 URL。

追踪你的使用情况。Cowork 消耗的配额明显多于普通的聊天。使用 subagents 处理多步骤的复杂任务是计算密集型的。如果你触及了限制，请批量处理相关工作，使用 “revise section 2 only” 而不是 “redo everything”，并通过文件预加载上下文，而不是在聊天中重新解释。

如果你退一步来看，这个列表中的每一个实践都遵循同一个原则：

投资于前期设置。减少在提示词上的努力。

那些在 Cowork 上挣扎的人正在为每个任务编写冗长、详细的提示词，却得到了不一致的结果。而那些在 Cowork 上如鱼得水的人花了一个下午来构建他们的上下文架构——manifest 文件、全局指令、上下文文件、文件夹指令、自定义技能——现在，他们只需写十个词的提示词就能产出可交付给客户的成果。

这是从 ChatGPT 时代思维到 Cowork 时代思维的根本转变。ChatGPT 奖励提示词工程（prompt engineering）。Cowork 奖励系统工程（system engineering）。

在一场 Cowork 会话中，提示词是最不重要的部分。你围绕它构建的上下文、结构、技能和约束条件——那才是输出质量的来源。

正如一位在早餐前运行五个并行工作流的 Substack 作者所说：“这感觉不再像是一场对话，而更像是把任务交给了一位能干的同事。”

那才是目标。不是一个聊天机器人。不是一个“提示词-然后-响应”的工具。而是一个已经了解你的标准、你的声音、你的项目和你的偏好的同事——因为你将这些知识构建进了它每次都会读取的文件中。

按顺序做这些事。每一个都将建立在上一个的基础之上产生复利。

今天（30 分钟）：创建你的三个上下文文件，并设置你的 Global Instructions。仅仅这一点就能让你领先于 95% 的 Cowork 用户。

本周：为你最常用的项目文件夹添加一个 `_MANIFEST.md`。安装两到三个与你角色匹配的插件。设置一个计划任务。

本月：为你最重复的工作流构建你的第一个自定义技能。在一个复杂的研究任务中尝试使用 subagents。根据输出质量完善你的上下文文件。

到了第一个月底，你将拥有一个能够在比你以前用过的任何 AI 工具都要短的时间内产出更高质量输出的 Cowork 体系。

将 Cowork 视为一个玩具与将 Cowork 视为一个系统之间的区别，仅仅在于 17 个实践和大约两个小时的设置。

了解这些实践的人与不了解这些实践的人之间的差距已经非常巨大。

在六个月内，它将成为一道鸿沟。