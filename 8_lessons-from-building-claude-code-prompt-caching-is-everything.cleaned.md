It is often said in engineering that “Cache Rules Everything Around Me,” and the same rule holds for agents.

Long-running agent products like Claude Code are economically feasible because of prompt caching: reusing prior computation to reduce both latency and cost.

What is prompt caching, how does it work, and how do you implement it technically?

At Claude Code, the harness is designed around prompt caching. High cache-hit rates reduce costs and enable more generous subscription rate limits. Cache-hit rate is monitored with alerts, and low hit rates are treated as incidents.

These are often unintuitive lessons from optimizing prompt caching at scale.

[![Image 1: Image](./assets/lessons-from-building-claude-code-prompt-caching-is-everything/image-01.jpg)](https://x.com/trq212/article/2024574133011673516/media/2024553977430646784)

## 1) Prompt caching is prefix matching

The API caches from request start up to each `cache_control` breakpoint. Ordering is therefore critical: maximize shared prefixes across requests.

Best practice: **static content first, dynamic content last**. A common structure:

1. Static system prompt + tools (globally cached)
2. Project context (cached within project)
3. Session context (cached within session)
4. Conversation messages

This maximizes cross-session reuse.

### Fragility examples

Prefix stability can break from seemingly small changes:

- inserting detailed timestamps into static system prompts
- non-deterministic tool ordering
- changing tool parameters during a conversation (e.g., agent-call targets)

## 2) Prefer message updates over prefix edits

Some information changes over time (date/time, file state, etc.). Editing prompts directly may cause costly cache misses.

Instead, pass updates as **new messages** in later turns. In Claude Code, a `<system-reminder>` is inserted into the next user/tool message to provide updates while preserving the cached prefix.

## 3) Caches are model-specific

Prompt caches are unique per model, which creates unintuitive tradeoffs.

Example: deep in a 100k-token Opus conversation, switching to Haiku for a simple question may be **more expensive**, because Haiku’s cache must be rebuilt from scratch.

If model switching is needed, use **subagents/handoffs**: parent model prepares a concise handoff for the target model.

## 4) Don’t mutate toolsets mid-conversation

A common anti-pattern is adding/removing tools dynamically “based on current need.”

Because tools are in the cached prefix, toolset changes invalidate cache for the conversation.

### Plan Mode: design around cache constraints

Naive approach: entering plan mode swaps to read-only tools. This breaks cache.

Better approach:

- keep full toolset stable
- represent mode changes as tools/messages (`EnterPlanMode`, `ExitPlanMode`)
- apply behavior constraints through instructions/messages, not toolset mutation

Bonus: model can autonomously enter plan mode when useful, without cache break.

### Tool Search: defer loading instead of removing

With many MCP tools, sending all full schemas each turn is costly, but removing tools breaks cache.

Solution: send stable lightweight stubs (`defer_loading: true`) and let model discover/expand via ToolSearch when needed. Prefix remains stable while full schemas load only on demand.

## 5) Compaction has hidden cache pitfalls

Compaction summarizes long conversations after context-window pressure.

If compaction is implemented as a separate call with different system prompt/tools, parent-prefix cache is lost and full input cost is paid.

[![Image 2: Image](./assets/lessons-from-building-claude-code-prompt-caching-is-everything/image-02.jpg)](https://x.com/trq212/article/2024574133011673516/media/2024558324591841283)

### Cache-safe forking pattern

For compaction/forks, reuse parent request shape exactly:

- same system prompt
- same user/system context
- same tool definitions
- parent history prepended
- compaction instruction appended as latest user message

Then only the newly appended tokens are uncached.

This requires maintaining a **compaction buffer** to leave room for compaction instructions and summary output tokens.

## Practical rules

1. Prompt caching is prefix-match. Any prefix change invalidates following cache.
2. Use message-level state updates, avoid frequent system-prompt edits.
3. Don’t change tools/models mid-stream unless architected as cache-safe handoffs.
4. Monitor cache-hit rate like uptime; small drops can materially hurt cost/latency.
5. Forked operations (compaction/summarization/skill execution) should share parent prefix.

Claude Code was designed around prompt caching from day one; agent builders should do the same.
