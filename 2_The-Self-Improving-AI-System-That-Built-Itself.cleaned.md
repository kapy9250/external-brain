# The Self-Improving AI System That Built Itself

I was trying to ship faster

I had a codebase, a backlog of things to build, and not enough hours in the day. So I started running AI coding agents in parallel — give each one a task, let them write code, review the PRs, merge, repeat. I started with two or three. Then five. Then ten.

The agents were fast. The problem was me. I couldn't keep up with them. I was the one checking if CI passed, reading review comments, copy-pasting errors back. I'd gone from writing code to babysitting the things that write code. That doesn't scale.

So I wrote some bash scripts to automate the coordination — about 2,500 lines that managed tmux sessions, git worktrees, and tab switching. Each agent got its own isolated tmux session and worktree. The orchestrator could spawn them, peek at what they were doing, forward CI failures back, and let me jump between sessions just by asking "take me to the tab for PR #1121." It worked, barely.

Then I pointed the agents at the bash scripts themselves. They built v1 of a proper orchestrator. v1 managed the agents that built v2. And v2 has been improving itself since.

[![Image 1: Image](./assets/The-Self-Improving-AI-System-That-Built-Itself/image-01.jpg)](https://x.com/agent_wrapper/article/2025986105485733945/media/2025981847025713152)

From bash scripts to self-improving system

The result: 40,000 lines of TypeScript, 17 plugins, 3,288 tests — built in 8 days, mostly by the agents the system orchestrates. Every commit has a git trailer identifying which AI model wrote it. There's no ambiguity about what humans did vs what agents did. We've open-sourced it: Agent Orchestrator (

). The key thing to understand: the orchestrator itself is an AI agent. Not a dashboard. Not a cron job. Not a script that polls GitHub. It's an agent — it reads your codebase, understands your backlog, decides how to decompose a feature into parallelizable tasks, assigns each task to a coding agent, and monitors their progress. When CI fails, it injects the failure back into the agent session — the agent reads the logs and fixes it. When a review comment comes in, it routes it to the right agent session with context. No human plumbing. That's what makes this different from every "run agents in parallel" setup. The thing managing the agents is itself intelligent.

[![Image 2: Image](./assets/The-Self-Improving-AI-System-That-Built-Itself/image-02.jpg)](https://x.com/agent_wrapper/article/2025986105485733945/media/2025982239675478016)

Most people get the AI coding agent problem wrong. The agents can code. That's not the bottleneck. You are.

You spawn five tasks, go grab coffee, come back 20 minutes later and now you're just refreshing GitHub tabs — waiting for PRs, checking CI, reading review comments. Congratulations, you've automated engineering and replaced it with project management. Bad project management.

The orchestrator agent replaces you in that loop. Not with a script — with an actual AI agent that has context on every active session, every open PR, every CI run. It tracks everything, watches for failures, forwards review comments back to coding agents, and only pings you when something actually needs a human decision. Once that bottleneck — your attention — goes away, things start compounding fast.

You open the dashboard to see status. But the orchestrator agent is already working — it's looked at all your workstreams and it tells you: "This PR is blocking three other tasks, this CI failure is a flaky test, and this review comment is the one that actually matters." It's not showing you data. It's giving you decisions.

[![Image 3: Image](./assets/The-Self-Improving-AI-System-That-Built-Itself/image-03.jpg)](https://x.com/agent_wrapper/article/2025986105485733945/media/2025983426160156672)

[![Image 4: Image](./assets/The-Self-Improving-AI-System-That-Built-Itself/image-04.jpg)](https://x.com/agent_wrapper/article/2025986105485733945/media/2025983228377743360)

The other thing that matters: plug anything in. Different agent runtime? Different issue tracker? Different notification channel? Swap it. The orchestrator doesn't care if you use Claude Code or Aider, tmux or Docker, GitHub or Linear. Eight plugin slots, all replaceable

People see "40K lines in 8 days" and assume I went into a cave. I have a day job. This was maybe ~3 days of actual focused work spread across 8 days, with agents filling the gaps.

[![Image 5: Image](./assets/The-Self-Improving-AI-System-That-Built-Itself/image-05.jpg)](https://x.com/agent_wrapper/article/2025986105485733945/media/2025983806960967680)

The pattern was simple: set up sessions before bed, agents work overnight, review and merge in the morning before work, set up new sessions, repeat.

The standout day: Saturday Feb 14. 27 PRs merged in a single day. The entire platform shipped — core services, CLI, web dashboard, all 17 plugins, npm publishing. I was reviewing and merging PRs faster than I could read them, but every PR had passed CI and automated code review first.

[![Image 6: Image](./assets/The-Self-Improving-AI-System-That-Built-Itself/image-06.jpg)](https://x.com/agent_wrapper/article/2025986105485733945/media/2025984517765570562)

Daily activity — commits and PRs merged over 8 days

Every commit tracks the model via git trailers:

[![Image 7: Image](./assets/The-Self-Improving-AI-System-That-Built-Itself/image-07.jpg)](https://x.com/agent_wrapper/article/2025986105485733945/media/2025984634157498368)

Totals exceed 722 commits because some commits were written by one model and reviewed/fixed by another. Opus 4.6 handled the hard stuff — complex architecture, cross-package integrations. Sonnet handled volume — plugin implementations, tests, docs.

Agents don't just write code and throw it over the wall. There's a full automated review cycle:

1.   Agent creates a PR and pushes code

2.   Cursor Bugbot automatically reviews and posts inline comments

3.   Agent reads comments, fixes the code, pushes again

4.   Bugbot re-reviews

[![Image 8: Image](./assets/The-Self-Improving-AI-System-That-Built-Itself/image-08.jpg)](https://x.com/agent_wrapper/article/2025986105485733945/media/2025984890546900992)

700 automated code review comments. Bugbot caught real stuff — shell injection via exec(), path traversal, unclosed intervals, missing null checks. The agents fixed ~68% immediately, explained away ~7% as intentional, and deferred ~4% to future PRs.

[![Image 9: Image](./assets/The-Self-Improving-AI-System-That-Built-Itself/image-09.jpg)](https://x.com/agent_wrapper/article/2025986105485733945/media/2025984966509940736)

Code review pipeline — from agent PR to ship

The most dramatic example: PR #125, a dashboard redesign. It went through 12 CI failure→fix cycles. Each time, the agent got the failure output, diagnosed the issue (type errors, lint failures, test regressions), and pushed a fix. No human touched it.

12 rounds. Zero human intervention. Shipped clean.

[![Image 10: Image](./assets/The-Self-Improving-AI-System-That-Built-Itself/image-10.jpg)](https://x.com/agent_wrapper/article/2025986105485733945/media/2025985118519861249)

All 41 CI failures across 9 branches were eventually self-corrected by agents. Overall CI success rate: 84.6%.

[![Image 11: Image](./assets/The-Self-Improving-AI-System-That-Built-Itself/image-11.jpg)](https://x.com/agent_wrapper/article/2025986105485733945/media/2025985185297379328)

The orchestrator uses a plugin system with 8 swappable slots:

[![Image 12: Image](./assets/The-Self-Improving-AI-System-That-Built-Itself/image-12.jpg)](https://x.com/agent_wrapper/article/2025986105485733945/media/2025985270169161729)

Session lifecycle:

1.   Tracker pulls an issue (GitHub or Linear)

2.   Workspace creates an isolated worktree or clone

3.   Runtime starts a tmux session or process

4.   Agent (Claude Code, Aider, etc.) works autonomously

5.   Terminal lets you observe live via iTerm2 or web dashboard

6.   SCM creates PRs and enriches them with context

7.   Reactions auto re-spawn agents on CI failures or review comments

8.   Notifier pings you only when human judgment is needed

[![Image 13: Image](./assets/The-Self-Improving-AI-System-That-Built-Itself/image-13.jpg)](https://x.com/agent_wrapper/article/2025986105485733945/media/2025985361395220480)

Session lifecycle — from issue to merged PR

Don't use tmux? Use the process runtime. Don't use GitHub? Use Linear. Don't use Claude Code? Plug in Aider or Codex. Swap any piece.

The most useful feature. Automated responses to GitHub events:

yaml

```
reactions:
  ci_failed:
    action: spawn_agent
    prompt: "CI failed on this PR. Read the failure logs and fix the issues."

  changes_requested:
    action: spawn_agent
    prompt: "Review comments have been posted. Address each comment and push fixes."

  approved:
    action: notify
    channel: slack
    message: "PR approved and ready to merge."
```

CI fails? Agent picks it up. Reviewer requests changes? Agent reads the comments and fixes the code. PR approved? You get a Slack notification. This is how those 41 CI failures got self-corrected — the reactions system just forwarded failures back to agents automatically.

I had 30 concurrent agents working on Agent Orchestrator. They were building the TypeScript replacement while I was using the bash-script version to manage them. The thing being built was the thing managing its own construction.

What I actually did:

*   Architecture decisions (plugin slots, config schema, session lifecycle)

*   Spawning sessions and assigning issues

*   Reviewing PRs (mostly architecture, not line-by-line)

*   Resolving cross-agent conflicts (two agents editing the same file)

*   Judgment calls (reject this approach, try that one)

What agents did:

*   All implementation (40K lines of TypeScript)

*   All tests (3,288 test cases)

*   All PR creation (86 of 102 PRs)

*   All review comment fixes

*   All CI failure resolution

I never committed directly to a feature branch. Every line of code went through a PR.

[![Image 14: Image](./assets/The-Self-Improving-AI-System-That-Built-Itself/image-14.jpg)](https://x.com/agent_wrapper/article/2025986105485733945/media/2025985682469249024)

One of the trickier problems: figuring out what an agent is actually doing without asking it.

Claude Code writes structured JSONL event files during every session. Instead of relying on agents to self-report (they lie, or at least get confused), the orchestrator reads these files directly:

*   Is the agent actively generating tokens?

*   Is it waiting for tool execution?

*   Is it idle?

*   Has it finished?

The agent-claude-code plugin knows how to parse Claude's session files. A future agent-aider plugin would read Aider's equivalent.

Next.js 15, Server-Sent Events for real-time updates. No polling.

*   Attention zones — sessions grouped by what needs your attention (failing CI, awaiting review, running fine)

*   Live terminal — xterm.js in the browser, showing the agent's actual terminal output in real time

*   Session detail — current file being edited, recent commits, PR status, CI status

*   Config discovery — automatically finds your ao.config.yaml and shows available sessions

Every agent session generates signal. Which prompts led to clean PRs? Which ones spiraled into 12 CI failure cycles? Which patterns caused merge conflicts?

Most agent setups throw this signal away. Session finishes, you move on, next session starts from zero.

Agent Orchestrator has a self-improvement system (ao-52 — itself built by an agent) that logs performance, tracks session outcomes, and runs retrospectives. It learns which tasks succeed on the first try and which need tighter guardrails.

Agents build features → orchestrator observes what worked → adjusts how it manages future sessions → agents build better features. The loop compounds.

And since the agents built the orchestrator, and the orchestrator makes the agents more effective, and those agents keep improving the orchestrator — it's recursive. The tool is improving itself through the agents it manages.

I think this is why orchestration matters more than any individual agent improvement. The ceiling isn't "how good is Claude Code at TypeScript." It's "how good can a system get at deploying, observing, and improving dozens of agents working in parallel." That ceiling is much higher. And it rises every time the loop runs.

Talk to your agents from anywhere. Right now you need to be at your desk. You should be able to message the orchestrator from Telegram or Slack — check status, approve a merge, redirect an agent — while you're on a walk.

Tighter mid-session feedback. Agents drift. They start solving the wrong problem, over-engineer a simple fix, go down rabbit holes. The orchestrator needs to check agent work against the original intent and inject course corrections before they've burned 20 minutes going the wrong direction.

Automatic escalation. Agent can't solve something? Escalate to orchestrator. Orchestrator needs judgment? Escalate to you. You only see things that genuinely need a human decision. Everything else resolves itself.

Beyond that: a reconciler for automatic conflict resolution between parallel agents, auto-rebase for long-running branches, Docker/K8s runtimes for cloud deployments, and a plugin marketplace for community contributions.

bash

```
git clone https://github.com/ComposioHQ/agent-orchestrator.git
cd agent-orchestrator
pnpm install && pnpm build
ao init --tracker github --agent claude-code --runtime tmux
ao start
```

Start the orchestrator, open the dashboard, and talk to it. Tell it what to build. It handles the rest — spawning agents, creating PRs, watching CI, forwarding review comments. You just make decisions.

We're looking for contributors: new plugins (agent runtimes, trackers, notifiers), Docker/K8s runtime, a reconciler for automatic conflict detection, and better escalation rules.

The repo is live:

Full metrics report:

Interactive visualizations of the build data:

I'm building Agent Orchestrator and the developer tooling layer at Composio. If working on self-improving AI systems sounds like your kind of problem — we're hiring across SF and Bangalore:
