# How to turn your OpenClaw into the world's best assistant

I turned my OpenClaw into the most effective assistant and chief of staff I've ever worked with.

I've hired EAs in my previous companies and I'm absolutely blown away by how well this is working.

This post is a step-by-step guide to how I did it.

If you want to cheat, you can just tell your OpenClaw to follow this open source repo exactly:

Now let me show you how it works.

1. Schedule all my meetings like "Hey R2, can you please find a time that works for both of us?" (he can even parse Calendly links and pick times that work for me and book them).
2. Check my inbox every 15 minutes and tell me which emails actually need my attention
3. Proactively follow up on emails that didn't get a reply
4. Watch my calendar, flag conflicts, and warn me when I have something coming up soon
5. Run my day from one canonical markdown task list in `tasks/current.md`
6. Prep my task list before I wake up by promoting due items into `Today`
7. Keep my task list clean by avoiding duplicate tasks across backlog and today views
8. Spot replies from prospects or referral partners and update the outreach tracker in Google Sheets
9. Update my CRM when I send/receive emails
10. Research suppliers and reach out to them to setup meetings
11. Send me short, high-signal updates when something needs action, and stay quiet when nothing important is happening
12. Work from durable context in files, memory, Gmail, Calendar, and Sheets instead of pretending chat history is enough
13. Be customized around my business, my channels, my preferences, and my exact operating style instead of acting like a generic AI assistant

```bash
clawchief/
├── README.md
├── skills/
│   ├── business-development/
│   │   └── SKILL.md
│   ├── daily-task-manager/
│   │   └── SKILL.md
│   ├── daily-task-prep/
│   │   └── SKILL.md
│   └── executive-assistant/
│       └── SKILL.md
├── workspace/
│   ├── HEARTBEAT.md
│   ├── TOOLS.md
│   └── tasks/
│       └── current.md
└── cron/
    └── jobs.template.json
```

Before you do anything with clawchief, make sure OpenClaw itself is already installed and working.

clawchief is not a replacement for OpenClaw. It's a practical operating layer on top of it.

This setup expects gog to work for:
* Gmail message search
* Calendar list and event reads
* Google Sheets metadata reads

If those are broken, your assistant won't be able to do real executive-assistant work reliably. Talk to your claw about how to set it up and they'll help you.

Copy these skill directories into `~/.openclaw/skills/`:
* skills/executive-assistant
* skills/business-development
* skills/daily-task-manager
* skills/daily-task-prep

These are the behavioral building blocks. This is what teaches OpenClaw how to act like an executive assistant, how to manage a task list, and how to handle operational business-development workflows.

Copy these into `~/.openclaw/workspace/`:
* workspace/HEARTBEAT.md
* workspace/TOOLS.md
* workspace/tasks/current.md

If you already have files there, merge carefully.

This defines what the assistant should check proactively. For me, that includes things like:
* important new email
* upcoming calendar events
* scheduling issues
* task-list follow-up
* occasional marketing or relationship-building nudges

This is how you stop your assistant from being passive.

This is where I keep local, environment-specific notes. Not generic skill logic — actual setup details. For example:
* preferred email accounts
* Google Sheets usage notes
* local environment quirks
* browser-profile guidance
* small tactical rules I don't want buried in prompts

This is one of the most important files in the whole system. I keep one canonical markdown task list. That means when the assistant checks what matters today, it is looking at one live source of truth instead of guessing from stale conversation history.

Make sure these are highly customized to you and your OpenClaw:
* AGENTS.md
* SOUL.md
* USER.md
* IDENTITY.md
* MEMORY.md
* memory/

This is where OpenClaw becomes your assistant instead of mine. These files let you define:
* who the human is
* who the assistant is
* tone and boundaries
* personal and business preferences
* long-term memory
* continuity across sessions

If you skip this step, you'll have a decent template. If you do this step well, you'll have an assistant that feels personal, grounded, and increasingly excellent.

The repo includes placeholders for the obvious things:
* owner name
* assistant name
* assistant email
* primary work email
* personal email
* business name
* business URL
* timezone
* primary update channel
* primary update target
* Google Sheet ID
* target market
* target geography
* repo root

This is where the assistant starts to feel alive.

The repo includes a cron template. The recommended starting jobs are:
1. executive assistant sweep
2. daily task prep
3. daily business-development sourcing

You can add optional jobs later, like backups or self-update, but I would start with the core operational routines first.

The important point is this:
The assistant becomes dramatically more useful when it wakes itself up to do recurring work. That is what shifts it from reactive to proactive.

Use the checklist in the repo and make sure the whole system works end to end. A real install should mean the assistant can do things like:
* read the task file correctly
* route proactive updates to the right place
* use Gmail message-level search
* check all relevant calendars before booking
* treat Google Sheets as the live outreach source of truth
* promote due-today items into `## Today`
* prefer an agent-controlled browser profile where appropriate

If those behaviors are not working, you're not done.

My advice if you want this to be amazing:
Use clawchief as the starting point, not the finish line.

The best version of this setup will reflect your actual world:
* your inboxes
* your calendar setup
* your preferred channels
* your task habits
* your business workflows
* your memory model
* your tolerance for interruptions

The more you customize it, the more valuable it becomes.

Generic assistants are generic because they are under-configured. Great assistants are opinionated, specific, and deeply shaped around one person's operating reality.

I didn't get the world's best assistant by asking OpenClaw better questions. I got it by giving OpenClaw a better operating system.

That's what clawchief is.

If you want to shortcut the process, start here. If you want to do it properly, use the repo, customize it aggressively, and make your assistant responsible for real recurring work.

That's when things get interesting.