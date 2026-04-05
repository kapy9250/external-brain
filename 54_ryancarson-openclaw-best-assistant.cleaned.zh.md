# 如何将你的 OpenClaw 变成世界上最好的助手

我将我的 OpenClaw 变成了我共事过最高效的助手和幕僚长 (chief of staff)。我以前在公司雇佣过行政助理 (executive assistants)，而这个系统的运作效果让我彻底震撼。如果你想走捷径，从这里开始：

* 帮我安排会议
* 解析预订链接并预订合适的时间
* 每 15 分钟检查一次我的收件箱，只呈现重要内容
* 主动跟进那些没有得到回复的邮件
* 监控我的日历，标记冲突，并提醒我即将到来的事件
* 基于一个权威的 markdown 任务列表来安排我的一天
* 在我醒来之前准备好我的任务列表
* 通过避免重复条目来保持任务清晰
* 根据电子邮件活动更新我的外联跟踪器 / CRM
* 研究供应商或合作伙伴并主动联系他们
* 仅在需要采取行动时向我发送简短、高信号密度的更新
* 基于文件、memory、Gmail、Calendar 和 Sheets 中持久的上下文进行工作
* 适应我的业务、我的偏好和我的运营风格

优先地图 (priority map)、自动解决器 (auto-resolver) 和摄取管道 (ingestion pipeline) 的许多想法都受到了 OpenClaw 设置的启发，他在 Core Memory 节目中与 ... 讨论过：

```bash
clawchief/
├── README.md
├── clawchief/
│ ├── priority-map.md
│ ├── auto-resolver.md
│ ├── meeting-notes.md
│ ├── tasks.md
│ └── tasks-completed.md
├── skills/
│ ├── business-development/
│ │   └── SKILL.md
│ ├── daily-task-manager/
│ │   └── SKILL.md
│ ├── daily-task-prep/
│ │   └── SKILL.md
│ └── executive-assistant/
│ └── SKILL.md
├── workspace/
│ ├── HEARTBEAT.md
│ ├── TOOLS.md
│ ├── memory/
│ │   └── meeting-notes-state.json
│ └── tasks/
└── cron/
    └── jobs.template.json
```

在对 clawchief 执行任何操作之前，请确保 OpenClaw 本身已安装并正常运行。

clawchief 不是 OpenClaw 的替代品。它是其上方的一个操作层。

此设置期望 gog 能够正常用于：
* Gmail 消息搜索
* Calendar 列表和事件读取
* Google Sheets 元数据读取
* Google Docs 读取（如果你需要摄取会议纪要）

如果这些功能损坏，你的助手将无法可靠地执行真正的行政助理工作。

将这些 skill 目录复制到 `~/.openclaw/skills/`

```bash
/executive-assistant
/business-development
/daily-task-manager
/daily-task-prep
```

这些是行为构建块。

它们教导 OpenClaw 如何：
* 表现得像一名行政助理
* 管理一个真正的任务列表
* 主动准备一天的工作
* 处理运营业务开发工作流

将这些复制到 `~/.openclaw/workspace/`

```bash
clawchief/
/HEARTBEAT.md
/TOOLS.md
/memory/meeting-notes-state.json
```

此文件告诉助手如何保持主动。

它告诉助手去：
* 读取优先地图
* 读取自动解决器
* 读取会议纪要策略 + 账本 (ledger)
* 读取实时的任务文件
* 运行正确的工作流
* 仅在事情真正重要时才给我发消息

这就是你如何阻止你的助手处于被动状态，同时又不让它变成一个嘈杂的烂摊子的方法。

这是我保留特定于环境的笔记的地方。

例如：
* 首选电子邮件帐户
* 跟踪器 / Google Sheets 笔记
* 本地环境的怪癖
* 目标市场笔记
* 我不想埋没在 prompts 中的战术操作规则

这是整个系统中最重要文件之一。

我保留一个权威的 markdown 任务列表。

这意味着当助手检查今天重要的事情时，它正在查看一个活的真实来源，而不是从陈旧的对话历史中进行猜测。

重度定制这些内容：
* AGENTS.md
* SOUL.md
* USER.md
* IDENTITY.md
* MEMORY.md
* memory/

这就是 OpenClaw 成为你的助手而不是我的助手的地方。

这些文件定义了：
* 谁是人类
* 谁是助手
* 语气和边界
* 个人和业务偏好
* 长期记忆
* 跨会话连续性

如果你跳过此步骤，你将获得一个不错的模板。

如果你很好地完成它，你将拥有一个感觉很个性化、接地气且日益出色的助手。

该 repo 包括用于明显内容的占位符：
* 所有者姓名
* 助手姓名
* 助手电子邮件
* 主要工作电子邮件
* 个人电子邮件
* 业务名称
* 业务 URL
* 时区
* 主要更新渠道
* 主要更新目标
* Google Sheet ID
* 目标市场
* 目标地理位置

然后针对你的真实世界定制这些文件：
* workspace/TOOLS.md
* clawchief/priority-map.md
* clawchief/tasks.md
* skills/business-development/resources/partners.md
* cron/jobs.template.json

这是助手开始感觉活生生的地方。

该 repo 包含一个 cron 模板。建议的初始任务是：
* executive assistant 清理
* 每日任务准备
* 每日 business-development 寻源

你可以稍后添加可选工作，例如备份或自我更新。

重要的一点是：

> 当助手唤醒自己去执行循环性工作时，它会变得极其有用。

这正是它从被动转变为主动的原因。

使用 repo 中的检查清单，并确保整个系统端到端工作。

一个真正的安装意味着助手可以：
* 正确读取真实来源的文件
* 将主动更新路由到正确的位置
* 使用 Gmail 消息级搜索
* 在预订前检查所有相关日历
* 将跟踪器 / sheet 视为实时的外联真实来源
* 将今日到期项目提升到 ## Today
* 归档前一天的完成项
* 将会议纪要摄取为实际任务和跟进项

如果这些行为不起作用，你还没有完成。

将 clawchief 作为起点，而不是终点。

此设置的最佳版本将反映你的实际世界：
* 你的收件箱
* 你的日历
* 你的首选渠道
* 你的任务习惯
* 你的业务工作流
* 你的记忆模型
* 你的中断容忍度

你对其进行的定制越多，它变得越有价值。

通用的助手之所以通用，是因为它们配置不足。

出色的助手是有主见的、特定的，并且深深围绕着一个人的运营现实而塑造。

我获得世界上最好的助手并不是通过向 OpenClaw 提出更好的问题。

我得到它是因为给 OpenClaw 提供了一个更好的操作系统。

那就是 clawchief 的本质。

如果你想走捷径，从这里开始：

如果你想正确地执行它，请使用该 repo，积极地进行定制，并让你的助手负责真正的重复性工作。

那才是事情变得有趣的时候。