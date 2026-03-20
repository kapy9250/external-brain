# 50 个 Claude Code 日常使用技巧与最佳实践

你使用 Claude Code 已经有一段时间了，并且知道它确实有效，现在你正在寻找所有可以提升效率的技巧。我整理了 50 个 Claude Code 的最佳实践和技巧，无论你是刚用了一周还是已经深度使用了几个月，它们都会对你有所帮助。这些内容来源于 Anthropic 的官方文档、其构建者 Boris Cherny 的分享、社区的经验以及我自己过去一年的日常使用总结。

这是我开启每一个 Claude Code 会话的方式。将此添加到你的 ~/.zshrc（或 ~/.bashrc）中：

```bash
alias cc='claude --dangerously-skip-permissions'
```

运行 `source ~/.zshrc` 来加载它。现在你只需输入 `cc` 而不是 `claude`，这样你就能跳过所有的权限提示。这个标志的名称刻意起得很吓人。只有当你完全理解 Claude Code 会对你的代码库做什么并且确实会这么做之后，才可以使用它。

输入 `!git status` 或 `!npm test`，命令会立即运行。命令及其输出结果会进入上下文中，这样 Claude 就能看到结果并采取相应的行动。这比要求 Claude 运行命令要快得多。

Esc 键可以在不丢失上下文的情况下中途停止 Claude 的操作。你可以立即重新引导它。

Esc+Esc（或 `/rewind`）会打开一个可滚动的菜单，显示 Claude 创建的每一个检查点。你可以恢复代码、会话或同时恢复两者。“Undo that”也是可以的。有四种恢复选项：代码和会话、仅恢复会话、仅恢复代码，或者从某个检查点向前总结。

这意味着你可以尝试那些你只有 40% 把握的方法。如果成功了，那太好了。如果没有，只需倒回。没有任何损失。需要注意的是：检查点只跟踪文件的编辑。bash 命令（如迁移、数据库操作）所做的更改不会被捕获。

要从上次中断的地方继续，使用 `claude --continue` 会恢复你最近的会话，而 `claude --resume` 会打开一个会话选择器。

给 Claude 提供一个反馈循环，让它自己发现错误。在你的提示词中包含测试命令、linter 检查或预期的输出。

```markdown
Refactor the auth middleware to use JWT instead of session tokens.
Run the existing test suite after making changes.
Fix any failures before calling it done.
```

Claude 会运行测试，发现失败的地方，并在你不需要介入的情况下修复它们。对于 UI 更改，可以设置 Playwright，让 Claude 能够打开浏览器，与页面交互，并验证 UI 是否按预期工作。这种反馈循环能够捕捉到单元测试遗漏的问题。

LSP 插件在每次文件编辑后为 Claude 提供自动的诊断信息。包括类型错误、未使用的导入、缺少返回类型等。Claude 会在你注意到这些问题之前就看到并修复它们。这是你可以安装的影响最大的单个插件。

选择你需要的并运行安装命令：

```bash
/plugin install typescript-lsp@claude-plugins-official
/plugin install pyright-lsp@claude-plugins-official
/plugin install rust-analyzer-lsp@claude-plugins-official
/plugin install gopls-lsp@claude-plugins-official
```

C#、Java、Kotlin、Swift、PHP、Lua 和 C/C++ 的插件也可用。运行 `/plugin` 并前往 Discover 选项卡以浏览完整列表。你需要在系统上安装相应的语言服务器二进制文件（如果缺失，插件会告诉你）。

GitHub CLI（`gh`）可以在没有单独的 MCP 服务器的情况下处理 PR、issue 和评论。CLI 工具比 MCP 服务器更能有效地利用上下文，因为它们不会将工具的 schema 加载到你的上下文窗口中。这也同样适用于 `jq`、`curl` 以及其他标准的 CLI 工具。

对于 Claude 还不知道的工具：“使用 'sentry-cli --help' 了解它，然后使用它来查找生产环境中最近的错误。” Claude 会阅读帮助输出，弄清楚语法并运行命令。即便是小众的内部 CLI 工具也能正常工作。

`/effort` 是一个关键字，它将工作量设置为高，并在 Opus 4.6 上触发自适应推理。Claude 会根据问题动态分配思考资源。将它用于架构决策、棘手的调试、多步骤推理，或任何你希望 Claude 在采取行动前先进行思考的场景。

你也可以使用 `/effort` 永久地设置工作量级别。对于不太复杂的任务，较低的工作量级别可以保持速度和较低的成本。将工作量与问题匹配。在变量重命名上消耗思考 token 是没有意义的。

Skills 是按需扩展 Claude 知识的 markdown 文件。与每次会话都会加载的指令不同，技能仅在与当前任务相关时才会加载。这使你的上下文保持精简。

在 `.claude/skills/` 中创建技能，或者安装打包了预构建技能的插件（运行 `/plugin` 来浏览可用项）。将技能用于特定领域的知识（API 约定、部署过程、编码模式），这些知识 Claude 有时需要，但并非总是需要。

运行 `claude remote-control` 启动会话，然后通过浏览器或 iOS/Android 上的 Claude 应用连接到它。会话在你的本地机器上运行。手机或浏览器只是一个查看它的窗口。你可以在任何地方发送消息、批准工具调用并监控进度。

如果你正在使用技巧 #1 中的 `cc` 别名，Claude 已经拥有所有权限，并且不需要针对每个动作进行批准。这使得远程控制变得更加顺畅：启动任务，离开机器，只有当 Claude 完成任务或遇到意外情况时才在手机上查看。

Sonnet 4.6 和 Opus 4.6 都支持 100 万 token 的上下文窗口。在 Max、Team 和 Enterprise 计划中，Opus 会自动升级到 1M 的上下文。你也可以在会话中途使用 `/model opus[1m]` 或 `/model sonnet[1m]` 切换模型。

如果你对较大上下文大小下的质量感到担忧，可以从 500k 开始并逐渐增加。更高的上下文意味着在压缩开始之前有更多的空间，但响应质量可能会因任务而异。使用 `CLAUDE_CODE_AUTO_COMPACT_WINDOW` 来控制压缩何时触发，并使用 `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` 来设置百分比阈值。为你的工作流找到一个最佳平衡点。

将 Plan Mode 用于多文件更改、不熟悉的代码和架构决策。它确实需要一些前期成本（前面会多花几分钟），但它可以防止 Claude 花费 20 分钟自信地解决一个完全错误的问题。

对于范围明确的小任务，请跳过它。如果你能用一句话描述差异，直接做就行。你可以随时按 Shift+Tab 在 Normal、Auto-Accept 和 Plan 权限模式之间循环切换，而无需离开会话。

一个有明确提示的干净会话胜过一个杂乱的三个小时的会话。任务变了？先使用 `/clear`。

我知道这感觉像是在丢弃进度，但是重新开始你会得到更好的结果。会话质量会下降，因为早期工作中积累的上下文淹没了你当前的指令。花五秒钟使用 `/clear` 并编写一个专注的起始提示，可以让你免于陷入 30 分钟的收益递减中。

用文字描述一个错误是很慢的。你看着 Claude 猜测、纠正，然后重复。

直接粘贴错误日志、CI 输出或 Slack 线程并说“修复”。Claude 会读取来自分布式系统的日志并追踪问题发生的地方。你的解释增加了抽象层，这通常会丢失 Claude 定位根本原因所需的细节。给 Claude 原始数据，然后让它自己去解决。

这对于 CI 也适用。“去修复失败的 CI 测试”并粘贴 CI 的输出是最可靠的模式之一。你也可以粘贴一个 PR 的 URL 或编号，让 Claude 检查失败的检查项并修复它们。如果安装了提示 #6 中的 `gh` CLI，Claude 会处理剩下的事情。

你也可以直接从终端通过管道传递输出：

```bash
cat error.log | claude "explain this error and suggest a fix"
npm test 2>&1 | claude "fix the failing tests"
```

`/btw` 会弹出一个覆盖层，用于快速提问，而不会将其进入到你的对话历史记录中。我用它来获取关于当前会话的澄清：“你为什么选择这种方法？” 或 “另一种选择有什么权衡？” 答案显示在一个可关闭的覆盖层中，你的主上下文保持精简，Claude 也能继续工作。

`claude --worktree feature-auth` 会创建一个包含新分支的隔离工作副本。Claude 会为你处理 git worktree 的设置和清理工作。

Claude Code 团队将其称为 Agent Teams。启动 3-5 个 worktree，每个 worktree 并行运行自己的 Claude 会话。我通常运行 2-3 个。每个 worktree 都有自己的会话、自己的分支和自己的文件系统状态。

本地 worktree 的上限取决于你的机器。多个开发服务器、构建过程和 Claude 会话都在竞争 CPU。Claude Containers 将每个 Agent 移至拥有浏览器预览功能的独立云容器中，让你的本地机器可以空余出来，去做需要你动脑的工作。

你正在编写一个很长的提示，写到一半突然意识到你需要先得到一个快速的答案。按 Ctrl+S 暂存你的草稿。输入你的快速问题，提交它，然后你暂存的提示就会自动恢复。

当 Claude 启动一个耗时的 bash 命令（测试套件、构建、迁移）时，按 Ctrl+B 将其发送到后台。当进程运行时，Claude 会继续工作，你也可以继续聊天。当进程完成时，结果就会显示出来。

状态栏是一个 shell 脚本，在 Claude 的每一次回合之后运行。它在你终端的底部显示实时信息：当前目录、git 分支、按窗口饱满度进行颜色编码的上下文使用情况。

最快的设置方法是在 Claude Code 内部使用 `/statusline`。它会问你想要显示什么，并为你生成脚本。

“使用子代理（subagents）弄清楚支付流程是如何处理失败交易的。” 这会生成一个独立的 Claude 实例，它有自己的上下文窗口。它会阅读所有的文件，推理代码库，并报告一个简明的摘要。

你的主会话会保持干净，有足够的空间来构建一些东西。深入的调查在编写任何代码之前就可能会消耗掉你一半的上下文窗口。子代理将这种开销从你的主会话中分离出去。内置类型包括 Explore（Haiku 模型，快速文件搜索）和 Plan（只读分析）。

这是实验性但很强大的功能。首先通过将 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` 添加到你的设置或环境变量中来启用它。然后告诉 Claude 创建一个团队：“创建一个由 3 个团队成员组成的代理团队，以并行重构这些模块。” 团队负责人将工作分配给成员，每个成员都有自己的上下文窗口和共享的任务列表。成员之间可以直接发消息来协调工作。

从 3-5 个成员开始，每个成员分配 5-6 个任务。避免分配修改相同文件的任务。两个成员编辑同一个文件会导致覆盖问题。在尝试并行实现之前，从研究和审查任务（PR 审查，bug 调查）开始。

当上下文压缩时（自动或通过 `/compact`），告诉 Claude 要保留什么：“`/compact` focus on the API changes and the list of modified files.” 你还可以在设置中添加长期生效的指令：“当压缩时，保留已修改文件的完整列表和当前的测试状态。”

`/loop 5m check if the deploy succeeded and report back` 会安排一个定期在后台运行的提示词，同时你的会话保持打开状态。时间间隔是可选的（默认是 10 分钟），并支持 s、m、h 和 d 单位。你也可以循环运行其他命令：`/loop 20m /review-pr 1234`。任务的作用域是会话级别的，并在 3 天后过期，因此被遗忘的循环不会永远运行。使用 `/loop` 来监控部署、观察 CI 管道或在专注于其他事情时轮询外部服务。

运行 `/voice` 启用按住说话（push-to-talk），然后按住空格键进行口述。你的语音会实时转录到提示词中，并且你可以在同一条消息中混合语音和打字输入。语音提示通常比打字提示包含更多的上下文，因为你会解释背景、提及限制并描述你想要的东西，而不会为了少打字而偷工减料。需要一个 Claude 帐户（而不是 API 密钥）。你可以将按住说话键重新绑定到 `~/.claude/keybindings.json` 中的一个组合键（如 meta+k），从而跳过按住检测的预热时间。

当你和 Claude 陷入一个不断纠正的死胡同，而问题仍然没有解决时，上下文中就会充满失败的尝试，这会主动阻碍下一次尝试。使用 `/clear` 并编写一个更好的、融合了你学到东西的起始提示。一个具有更明确提示词的干净会话几乎总是优于一个被累积死胡同拖累的长会话。

使用 `@` 直接引用文件：`@middleware.ts` 包含会话处理。`@` 前缀会自动解析为文件路径，所以 Claude 确切知道去哪里查看。

Claude 可以自己使用 grep 和搜索代码库，但它仍需缩小候选范围并确定正确的文件。每个搜索步骤都需要花费 token 和上下文。从一开始就将 Claude 指向正确的文件，可以跳过整个过程。

“你在这个文件中会改进什么？”是一个非常好的探索提示词。并非每个提示都必须很具体。当你希望用新眼光审视现有代码时，一个模糊的问题会给 Claude 留出空间，揭示你可能根本想不到去问的内容。

当我在熟悉一个陌生的代码库时会用这个方法。Claude 能指出一些模式、不一致的地方以及改进的机会，这些是我第一次阅读时会遗漏的。

当 Claude 提出一个计划时，按 Ctrl+G 在你的文本编辑器中打开它以进行直接编辑。在 Claude 写下任何一行代码之前添加约束、删除步骤或改变方法。这在计划基本正确，但你想微调几个步骤而不必重新解释整个事情时非常有用。

`CLAUDE.md` 是项目根目录下的一个 markdown 文件，用于给 Claude 提供持久化指令：构建命令、编码标准、架构决策、仓库规范。Claude 在每个会话开始时都会读取它。`/init` 会根据你的项目结构生成一个初始版本。它会拾取构建命令、测试脚本以及目录布局。

这个输出的内容通常比较冗余。如果你无法解释为什么某一行会出现在那里，那就删掉它。修剪掉那些噪音，补充缺失的部分。

对于你在 `CLAUDE.md` 里的每一行，问自己：如果没有这一行，Claude 会犯错吗？如果 Claude 凭借自身能力已经能把某件事做对，那么这条指令就是噪音。每一条不必要的线索都在稀释真正重要的线索。在遵从度下降之前，大概有 150-200 条指令的额度，而系统提示词已经用掉了大概 50 条。

当 Claude 犯错时，告诉它：“更新 `CLAUDE.md` 文件，以便不再发生这种情况。” Claude 会写下它自己的规则。在接下来的会话中，它会自动遵循这些规则。

随着时间的推移，你的 `CLAUDE.md` 会成为一个基于真实错误而形成的活文档。为了防止它无限增长，可以使用文件引用功能引用诸如 `rules.md` 这样的独立文件来处理具体的模式和修复。这样你的 `CLAUDE.md` 就能保持精简，Claude 也可以按需读取细节。

将 markdown 文件放入 `.claude/rules/` 以按主题组织指令。默认情况下，每个规则文件都会在每次会话开始时加载。若要使规则仅在 Claude 处理特定文件时加载，可以添加 paths 的 frontmatter：

```yaml
---
paths:
  - "**/*.ts"
---
# TypeScript conventions
Prefer interfaces over types.
```

这让你的主要 `CLAUDE.md` 保持精简。TypeScript 规则在 Claude 读取 `.ts` 文件时加载，Go 规则在读取 `.go` 文件时加载。Claude 永远不需要浏览它没有涉及的语言的约定。

使用 `@api.md` 引用文档。你还可以引用 `@types.md`、`@schema.json` 或甚至 `@~/.claude/my-project-instructions.md`。

Claude 会在需要时读取该文件。把它看作是“这里有更多上下文，以防你需要”，而不会使 Claude 在每次会话中读取的文件变得臃肿。

别再为你第一百次运行 `npm run lint` 去点击“批准”了。`/permissions` 让你把可信命令加入白名单，让你能保持工作流的连贯。只有对于那些不在列表上的命令，你才会收到提示。

运行 `/sandbox` 启用操作系统级别的隔离。写操作仅限在你的项目目录内，网络请求被限制在你批准的域名内。它在 macOS 上使用 Seatbelt，在 Linux 上使用 bubblewrap，所以限制适用于 Claude 衍生的每一个子进程。在自动允许模式下，沙盒命令运行而没有权限提示，这让你可以带上护栏获得近乎完全的自主权。

对于无人监督的工作（如连夜进行的迁移或实验性的重构），请在 Docker 容器中运行 Claude。容器为你提供了完全隔离的环境、简单的回滚功能，以及让 Claude 连续运行数小时的信心。

与动态使用子代理不同，自定义子代理是保存在 `.claude/agents/` 中的预先配置好的代理。例如，一个安全审查代理（使用 Opus 模型和只读工具），或者一个追求速度的快速搜索代理（使用 Haiku 模型）。

使用 `/agents` 浏览并创建它们。你可以设置隔离模式：需要自己独立文件系统的代理可使用 worktree 模式。

值得入手的 MCP 服务器：用于浏览器测试和验证用户界面的 Playwright，用于直接查询表结构的 PostgreSQL/MySQL，用于读取 bug 报告和跟进讨论上下文的 Slack，以及从设计图直接生成代码的工作流工具 Figma。

Claude Code 支持动态加载工具，所以只有当 Claude 真的需要服务器的定义时，它们才会被加载。

运行 `/config` 并选择你偏好的风格。内置的选项包括：Explanatory（详细说明、逐步指导）、Concise（简明扼要、专注行动）以及 Technical（精确严谨、适用专业术语）。

你还可以在 `~/.claude/output-styles/` 目录下以文件的形式创建自定义输出风格。

`CLAUDE.md` 提供的是建议，Claude 大约会在 80% 的时间里遵循它。而 Hooks 则是确定性的，100% 必须执行的。如果某件事每次都毫无例外地必须要发生（比如代码格式化、静态检查、安全检查），那就把它做成 Hook。如果这只是 Claude 应该参考的指导方针，放在 `CLAUDE.md` 里就足够了。

每次 Claude 编辑文件时，你的格式化工具都应自动运行。在 `.claude/settings.json` 中添加一个 PostToolUse Hook，确保在 Claude 编辑或写入任何文件后运行 Prettier（或你使用的其他格式化工具）：

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "npx prettier --write \\\"$CLAUDE_FILE_PATH\\\" 2>/dev/null || true"
          }
        ]
      }
    ]
  }
}
```

代码中的 `|| true` 可以防止 Hook 执行失败从而阻塞 Claude。你还可以把其他工具串联起来。比如，添加 `npx eslint --fix` 作为第二条 Hook 配置。

如果你的编辑器打开着同样的文件，可以考虑在 Claude 工作时关闭保存时自动格式化。一些开发者反映，编辑器的保存操作可能会使提示词缓存失效，迫使 Claude 重新读取文件。让 Hook 来处理格式化反而更好。

通过在 Bash 上设置一个 PreToolUse hook 来拦截 `rm -rf`、`drop table` 和 `truncate` 模式。Claude 将不会尝试执行这些操作。该 Hook 在 Claude 运行工具之前触发，所以在具有破坏性的命令造成损害之前，就能将它们拦截下来。

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "type": "command",
        "command": "if echo \\\"$TOOL_INPUT\\\" | grep -qE 'rm -rf|drop table|truncate'; then echo 'BLOCKED: destructive command' >&2; exit 2; fi"
      }
    ]
  }
}
```

将其添加到你项目的 `.claude/settings.json` 中。你可以通过 `/hooks` 以交互方式设置它，或者直接告诉 Claude：“添加一个拦截 `rm -rf`、`drop table` 和 `truncate` 命令的 PreToolUse hook。”

在长时间的会话中，当上下文进行压缩时，Claude 可能会丢失它正在处理的内容。带有 compact 匹配器的 Notification hook 会在每次触发压缩时，自动重新注入你的关键上下文。

告诉 Claude：“设置一个 Notification hook，以便在压缩后提醒你当前的任务、已修改的文件以及任何约束。” Claude 会在你的设置中创建该 Hook。非常适合用于重新注入的内容包括：当前任务的描述、你所修改的文件列表以及任何硬性约束条件（“切勿修改迁移文件”）。

在长达数小时、你深度参与某个特性开发的会话中，你绝对无法承受 Claude 失去思路的代价，此时这个功能将发挥最大的价值。

Claude 擅长写代码。但这些决定需要人类来做。包括授权流程、支付逻辑、数据变动以及具有破坏性的数据库操作。无论代码的其他部分看起来有多好，都必须审查这些内容。一个错误的授权范围、配置错误的支付 webhook 或者静默丢弃列的迁移，都有可能让你失去用户、金钱或是信任。任何自动化测试都无法完全捕捉到这些所有问题。

`/branch` (或者 `/fork`) 会在当前会话的节点创建一个副本。在这个分支中尝试有风险的重构。如果它成功了，就保留它。如果失败了，你原本的对话不会受到任何影响。这不同于时间倒回（rewind），因为这两条路径都同时存在。

你清楚自己想要构建什么，但你觉得你没掌握 Claude 把它构建好所需的所有细节。让 Claude 来问问题。

```markdown
I want to build [brief description]. Interview me in detail
using the AskUserQuestion tool. Ask about technical implementation,
edge cases, concerns, and tradeoffs. Don't ask obvious questions.
Keep interviewing until we've covered everything,
then write a complete spec to SPEC.md.
```

一旦规范完成，启动一个包含干净上下文的全新会话并按照该完整规范开始执行。

首先由一个 Claude 来实现功能，接着由另一个 Claude 来进行审查。这个负责审查的 Claude 不了解任何实现上的捷径，它会对每一个捷径提出质疑。

同样的思路也适用于 TDD（测试驱动开发）。会话 A 负责编写测试，会话 B 则负责编写通过这些测试的代码。

不要让 Claude 进行一次性 PR 审查（当然你也可以，如果你想的话）。在会话中打开 PR 并就此进行对话。“请给我讲解一下这个 PR 中风险最高的修改。” “如果并发运行，什么地方会出问题？” “错误处理方式是否和代码库其他部分保持一致？”

对话式的评审能够发现更多问题，因为你可以深入探讨那些真正重要的领域。一次性的代码评审往往只会标记代码风格上的小问题，而经常忽略架构上的缺陷。

`/rename auth-refactor` 会在提示词栏放置一个标签，让你清楚哪个会话是干什么的。`/color red` 或 `/color blue` 用来设置提示词栏的颜色。可用的颜色有：red、blue、green、yellow、purple、orange、pink、cyan。当你并行运行 2-3 个会话时，给它们命名和上色只需五秒钟，就能避免你在错误的终端里输入内容。

添加一个 Stop hook，在 Claude 完成回复时播放系统提示音。开启一个任务，切换到其他工作，等任务完成时就能听到“叮”的一声。

```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/afplay /System/Library/Sounds/Glass.aiff"
          }
        ]
      }
    ]
  }
}
```

通过非交互模式循环处理一系列文件。`--allowedTools` 界定了 Claude 在每个文件中可以执行的操作。使用 `&` 并行运行它们以获得最大的吞吐量。

```bash
for file in $(cat files-to-migrate.txt); do
  claude -p "Migrate $file from class components to hooks" \\
    --allowedTools "Edit,Bash(git commit *)" &
done
wait
```

这非常适合转换文件格式、在整个代码库中更新导入内容，以及运行重复性的迁移操作——在这种场景下，每个文件的处理过程都是互相独立的。

当 Claude 思考时，终端会显示一个微调器（spinner），伴随着像“Flibbertigibbeting...”和“Flummoxing...”这样的动词。你可以把它们替换成你想要的任何内容。告诉 Claude：

> 将用户设置中的思考动词替换为这些：Hallucinating responsibly，Pretending to think，Confidently guessing，Blaming the context window

你甚至不需要提供一个清单。直接告诉 Claude 你想要的感觉就行：“用哈利波特的咒语替换我的思考动词。” Claude 会生成这个列表。这是一个小改动，但能让等待的过程变得更有趣。

你并不需要全盘掌握这 50 个技巧。挑选一个能解决你上次会话中最令你困扰问题的技巧，然后在明天尝试一下。一个能被你记住并使用的技巧，胜过 50 个只是被你收藏的技巧。
