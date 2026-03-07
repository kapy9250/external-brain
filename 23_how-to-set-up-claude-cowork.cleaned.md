# How to set up Claude Cowork (to level up from ChatGPT)
*Author: Ruben Hassid*
*URL: https://x.com/rubenhassid/status/2029514946640322593*

You just switched from ChatGPT to Claude. But you’re still not using Cowork.

When Claude released it, software stocks lost $830 billion in 6 days because of it.

And since I published my guide, people keep asking me:

> “I installed Claude. But how do I actually start using Claude Cowork?”

If you don’t code, you must master Claude Cowork now.

First, you might be lost between different Claude modes. So here’s a quick recap:

[![Image 1: Image](./assets/how-to-set-up-claude-cowork/image-01.jpg)](https://x.com/rubenhassid/article/2029514946640322593/media/2029488576522506240)

Claude Cowork is (by far) what you must focus on right now.

And that’s not it.

Here’s the entire Claude product line, in short:

1. Claude “Chat” → it’s like ChatGPT. Probably the only one you know.
2. Claude “Project” → it’s still Claude Chat, but separated as individual Projects.
3. Claude “Code” → massive revolution for developers to code (much) faster.
4. Claude “Cowork” → like Claude Code but for us, knowledge workers.
5. Claude “Skills” → teach Claude repeatable workflows. Like better Projects.
6. Claude “Connectors” → plug Claude directly into apps like Slack, Google Calendar, Gmail, etc. It reads, writes, and acts inside the tools you already use.
7. Claude “Plugins” → like Connectors, but you do it (you don’t want that). Connectors = download from the App Store, Plugins = you upload your app.

This newsletter is the full playbook of Cowork. How to set it up. How I use it every single week to write this newsletter, deliver consulting work, and research faster than I ever could alone. Also, where it falls short (I keep promising honesty).

Two things before we start:

1. Save this guide and spend 30 minutes this weekend to explore Cowork.
2. Send it to anyone who still hasn’t tried Cowork (or Claude).

You read my guide. So you installed it correctly.

Just a quick reminder for those who didn’t read it:

1. Go to Claude.ai. Download the app. 
2. You need a Pro account ($20/month). It’s very much worth it.
3. Open the app. Click on the Cowork tab at the top between Chat & Code.
4. Select a folder from your computer. More about it right after this set up.
5. Make sure to always select “Opus 4.6” and “Extended thinking”.

[![Image 2: Image](./assets/how-to-set-up-claude-cowork/image-02.jpg)](https://x.com/rubenhassid/article/2029514946640322593/media/2029488732966182912)

This is the Claude app (installed on your computer). Make sure to go to the Cowork tab > Select Opus 4.6 + Extended thinking > Work in a folder.

ChatGPT trained you to write better prompts. Longer prompts. Forget that.

With Cowork, the game is text files. Take everything you know (your writing style, your company’s rules, your best examples, your past work) and put it in text files. Drop them in a folder. Point Claude to that folder.

It’s kind of like having an SOP for an employee. But here, Claude is your employee. And the SOP is your “Claude Cowork” folder.

The more context you give it as files, the less prompting you need. The output goes from “generic AI” to “this actually sounds like a full-time employee.”

Here’s how to create your folder:

Create a dedicated folder for Cowork on your computer.

It needs a clean, intentional space. Here’s mine:

> ABOUT ME → a folder with 1/ “about me”, 2/ “anti AI writing style”. PROJECTS → live work. The projects you're building right now. The brief, the drafts, the reference material for that specific job. one subfolder per project. TEMPLATES → finished work so good you want to reuse it as a pattern. It’s not the content itself, but the “perfect” structure, as templates. CLAUDE OUTPUTS → where Claude Cowork delivers finished work for you.

[![Image 3: Image](./assets/how-to-set-up-claude-cowork/image-03.jpg)](https://x.com/rubenhassid/article/2029514946640322593/media/2029488843196375040)

Parent folder: CLAUDE COWORK. Inside, there are 4x folders (1-2-3-4).

This keeps things organized and limits what Claude can see. Cowork has real read/write access to whatever folder you share. If something goes wrong, you want the damage contained. You must keep it tight.

Now here’s how to create your own core files:

You now have 4 folders within your mega “Claude Cowork” folder.

Let’s create the “About me” files now:

File 1: about-me.md — Who you are. What you do. Your current priorities. What matters to you right now. 

File 2: anti-ai-writing-style.md — Because I hate the AI style. So I made a text file on how to NEVER write like an AI.

[![Image 4: Image](./assets/how-to-set-up-claude-cowork/image-04.jpg)](https://x.com/rubenhassid/article/2029514946640322593/media/2029488933122523136)

Quick note: a markdown file is just a plain text file with an .md extension. Open any text editor (even a Google Doc works), write your content, and save it as about-me.md instead of about-me.txt. Claude reads them better.

[![Image 5: Image](./assets/how-to-set-up-claude-cowork/image-05.jpg)](https://x.com/rubenhassid/article/2029514946640322593/media/2029489025644425216)

“.md” is just a type of text file AI loves to read.

One great markdown file is worth more than 50 random uploads. Don’t dump everything into the folder. Be intentional about what you include.

Go to: Settings → Cowork → Edit Global Instructions.

[![Image 6: Image](./assets/how-to-set-up-claude-cowork/image-06.jpg)](https://x.com/rubenhassid/article/2029514946640322593/media/2029489110944210944)

It’s like a persistent prompt Claude Cowork always read before.

Global Instructions handle how Claude must (always) behave.

Paste this:

> # GLOBAL INSTRUCTIONS ## BEFORE EVERY TASK 1. Read `ABOUT ME/`. No task starts without reading both. 2. If the task relates to a project, read everything in the matching `PROJECTS/` subfolder before proceeding. 3. If the task involves a content type that has a matching pattern in `TEMPLATES/`, study that template's structure first. Use the structure. Don't copy the content. ## FOLDER PROTOCOL You have three read-only folders and one write folder. ### Read-only — never create, edit, or delete anything here: - `ABOUT ME/` → My identity and writing rules. - `TEMPLATES/` → Proven structures to reuse as patterns. - `PROJECTS/` → My briefs, references, and finished work organized by project. ### Write folder — the only place you deliver work: - `CLAUDE OUTPUTS/` → Everything you create goes here. Organize with one subfolder per project, mirroring the structure of `PROJECTS/`. Create the subfolder if it doesn't exist yet. ## NAMING CONVENTION All files you create must follow this format: `project_content-type_v1.ext` Content types: Newsletter, LinkedIn Post, Brief, Deck, Report. Examples: - `How-To-AI_Newsletter_v1.md` - `EasyGen_Deck_v1.pptx` - `GPC_Report_v2.docx` Increment the version number if a file with the same name already exists. ## OPERATING RULES - If the brief is unclear or incomplete, use the `AskUserQuestion` tool. Don't fill gaps with generic filler. - Don't over-explain. Deliver the work. Save the commentary unless I ask for it. - Never delete files anywhere.

You set this once. It runs every time. You never type it again.

Combined with your context files, this means your prompts can be 10 words long and still produce work that sounds like you. With the same level of quality.

Here’s a prompt example:

> I want to write a cold DM on Linkedin to a Chief of Staff who needs an AI workshop. I will DM her on Linkedin, and I need to have a clear strategy to make her open the message and book a call. Start by using AskUserQuestion. Develop 5x completely different strategies.

[![Image 7: Image](./assets/how-to-set-up-claude-cowork/image-07.jpg)](https://x.com/rubenhassid/article/2029514946640322593/media/2029489349025226752)

1. Use Cowork 2. Select your Claude folder 3. Select the right model 4. Straightforward prompt with the task + success critera + steps.

[![Image 8: Image](./assets/how-to-set-up-claude-cowork/image-08.jpg)](https://x.com/rubenhassid/article/2029514946640322593/media/2029489434517749760)

Claude Cowork asked me clarifying questions, and I clicked on my answers.

[![Image 9: Image](./assets/how-to-set-up-claude-cowork/image-09.jpg)](https://x.com/rubenhassid/article/2029514946640322593/media/2029489506936885248)

It works like an employee to complete the task.

[![Image 10: Image](./assets/how-to-set-up-claude-cowork/image-10.jpg)](https://x.com/rubenhassid/article/2029514946640322593/media/2029489586498359296)

It takes 1-7 minutes, but I usually work somewhere else (or spin up more sessions on my browser with Claude Chat - welcome to the new world).

![Image 11](./assets/how-to-set-up-claude-cowork/image-11.jpg)

This level of output is literally what a good employee would do.

Now extrapolate to legal work, creative agencies, academic research.

You might think it was “too simple of a benchmark”.

Alright, let’s do another example. A heavy Excel file together:

> I want to create a spreadsheet that maps out a potential exit for my socials (if I could sell them). Start by using AskUserQuestion to be up to date with my numbers. Then and only then, create a spreadsheet with Wall Street financial model style.

[![Image 12: Image](./assets/how-to-set-up-claude-cowork/image-12.jpg)](https://x.com/rubenhassid/article/2029514946640322593/media/2029490688057102337)

It plans itself. It finds error itself. It fixes itself… while I work on something else. This is the revolution I was mentioning earlier.

[![Image 13: Image](./assets/how-to-set-up-claude-cowork/image-13.jpg)](https://x.com/rubenhassid/article/2029514946640322593/media/2029490765605322752)

Few question, 2 minutes. And I have a perfect start to an Excel file.

This is the feature that changed how I work. And I haven’t seen a single Cowork guide explain it properly.

Always add this to your prompt:

> Start by using the AskUserQuestion tool before answering to gather enough context.

When you do this, Cowork generates an interactive form. Actual buttons. Clickable options. Multi-select choices. Rankings you can drag and reorder.

AI is finally prompt you.

[![Image 14: Image](./assets/how-to-set-up-claude-cowork/image-14.jpg)](https://x.com/rubenhassid/article/2029514946640322593/media/2029490976075485184)

Here, my prompt is literally 2 lines + my Claude Cowork folder. That’s it.

[![Image 15: Image](./assets/how-to-set-up-claude-cowork/image-15.jpg)](https://x.com/rubenhassid/article/2029514946640322593/media/2029491128496455680)

I often times write the answer myself. But the options give me a direction.

[![Image 16: Image](./assets/how-to-set-up-claude-cowork/image-16.jpg)](https://x.com/rubenhassid/article/2029514946640322593/media/2029491203310321664)

“Nobody followed you because of your breakfast” is taken from my “about me” file. I can now build up from here.

This is called AskUserQuestion. It’s a tool built into Cowork. Claude forces you to be clear. It asks the right questions so it can give you the right output.

The one prompt I use for everything.

80% of my chats with Cowork starts like this:

> I want to [TASK] to [SUCCESS CRITERIA]. First, explore my CLAUDE COWORK folder. Then, ask me questions using the AskUserQuestion tool. I want to refine the approach with you before you execute.

What happens: Claude reads your context files, generates a clickable form asking about your audience, your goals, your preferences. You click through in under a minute. Claude shows a plan. You approve. It executes — creating real files in your folder. If something’s off midway, you interrupt. Claude recalibrates with a new form. Picks up where it left off.

The entire process feels like directing someone smart instead of wrestling with a text box. I’m obsessed with this feature.

(Yes, I stopped writing prompts. My prompt folder is collecting dust.)

I even added a “Text Replacement” on my Mac so that whenever I am typing the command “/prompt” it pastes this one prompt:

![Image 17](./assets/how-to-set-up-claude-cowork/image-17.jpg)

If you use a Mac, search for “Text replacement”. Click on the “+” and simply add a command (I like /prompt) and paste my prompt template.

Remember that $830 billion stock crash I opened with?

Anthropic released 11 official plugins. Sales. Marketing. Legal. Finance. Data analysis. Product management. Customer support. Each one gives Claude specific skills, workflows, and slash commands for that function.

Legal software lost so much value because Claude can do the work. And the plugins sitting in your Cowork sidebar are a big part of what triggered that reaction.

You don’t need to be technical to install it. I promise.

1. Open Cowork.
2. Click Customize in the left sidebar → Browse plugins.
3. Pick one that matches your work. Install.
4. Type / in the chat to see available slash commands.

[![Image 18: Image](./assets/how-to-set-up-claude-cowork/image-18.jpg)](https://x.com/rubenhassid/article/2029514946640322593/media/2029491767507099649)

On the homepage, click on “Customize”.

[![Image 19: Image](./assets/how-to-set-up-claude-cowork/image-19.jpg)](https://x.com/rubenhassid/article/2029514946640322593/media/2029492304621289472)

Can’t make it clearer for you, my friend :)

[![Image 20: Image](./assets/how-to-set-up-claude-cowork/image-20.jpg)](https://x.com/rubenhassid/article/2029514946640322593/media/2029492192167735297)

Browse, and click “Install” on the ones you want to try. It’s free.

[![Image 21: Image](./assets/how-to-set-up-claude-cowork/image-21.jpg)](https://x.com/rubenhassid/article/2029514946640322593/media/2029492366566977536)

Now click on the “+”, go to Plugins > [Name of the plugin] > Subtask.

[![Image 22: Image](./assets/how-to-set-up-claude-cowork/image-22.jpg)](https://x.com/rubenhassid/article/2029514946640322593/media/2029492472544481280)

Or you just learn the /command (here /onboarding).

[![Image 23: Image](./assets/how-to-set-up-claude-cowork/image-23.jpg)](https://x.com/rubenhassid/article/2029514946640322593/media/2029492576714440704)

You can even customize each plugins based on your company (Claude will ask you questions, and it will remember the answers).

Marketing plugin
The prompt: /marketing:draft-content → “Write a LinkedIn post about [topic]. Use my voice profile. Target [audience].”
What happens: Claude reads your about-me.md, drafts a post that actually sounds like you, and suggests hook variations. You pick one, edit, post. Five minutes instead of thirty.

Data plugin
The prompt: /data:explore → Drop a CSV into the folder.
What happens: Claude summarizes every column, flags anomalies, suggests analyses, and can build an interactive dashboard. It writes SQL in plain English. You don’t touch a formula.

Legal plugin
The prompt: “Review the NDA in this folder. Flag anything unusual or one-sided.”
What happens: Claude reads the contract, highlights risky clauses, explains each one in plain English, and suggests alternative language. This is what wiped $285 billion off the stock market.

Cowork can also connect to your existing tools. Slack, Google Drive, Notion, Figma, and 50+ others. They’re called Connectors.

Go to Settings → Connectors. Browse the directory. Click “Add.” Done.

Once connected, it reads your tools. Claude can search your Slack messages, pull from your Google Docs, or reference your Notion pages mid-conversation.

![Image 24](./assets/how-to-set-up-claude-cowork/image-24.jpg)

Here’s an example with Gamma.

Oh, and I forgot - connectors are free.

I don’t use anything else these days.

The setup: My folder has my about-me.md, my anti-AI-writing-guide.md, past newsletters that performed well, reference guides from other creators, and official documentation from companies (like OpenAI/Anthropic/Google).

The prompt:
> I want to write my next newsletter on using Gemini to grow on Linkedin with infographics using the new Nano Banana 2. First, explore my CLAUDE COWORK folder. Then, ask me questions using the AskUserQuestion tool. I want to refine the approach with you before you execute.

What happens: Claude reads every file. Generates a form asking about my audience, my tone, what length, what angles the other guides missed. I click answers. It produces an outline. I push back on weak sections. It adjusts. Then it writes — and because it has my voice profile and anti-AI writing guide, the output actually sounds like me.

I edit. But the heavy lifting is done. This newsletter you’re reading right now was outlined by Cowork and written by me. But you don’t care and you keep reading :)

The setup: Client sends a brief. I drop it in the folder next to my templates and past deliverables.

The prompt:
> A client just sent a brief for a 2026 AI adoption strategy. The brief is in /projects/client-x/. Read the brief, my deliverable template, and my past examples. Create a first draft as a .docx. Ask me questions first (AskUserQuestion).

What happens: Claude reads the brief. Compares it to my template format. Then it asks me things I didn't think of — "Should this include a timeline or just recommendations?" and "Do you want competitor examples or keep it internal?" I click answers. It creates a .docx file directly in my folder.

The setup: I drop 3-5 competitor articles or reports into a subfolder.

The prompt:
> I uploaded 4 newsletters from other creators covering Claude Cowork. Read all of them. Create a comparison table: what each one covered, what they missed, and where I can be the only one saying something new. Ask me questions first.

What happens: That used to be a junior job in my company. Now it’s a prompt.

This one is different. Cowork works without you even being there.

The setup: You create a folder called /weekly-briefings/.

The prompt (with /schedule, it’s a plugin):
> Every Monday at 7 am, research [competitor names] for news, product updates, or pricing changes. Save a summary to /weekly-briefings/ as a markdown file. Only include items from the past 7 days.

What happens: Cowork runs automatically every Monday, as long as your computer is awake and the app is open. You wake up to a briefing doc ready to read. That’s the endgame.

Across all four use cases, the pattern is the same. I never write a long prompt. I write a short task, point to my folder, and say “ask me questions.”

The workflow is always the same. Only the context changes.

It eats your usage fast. A single Cowork session can burn through what would normally be dozens of regular chat conversations. On the Pro plan ($20/month), you’ll feel it within a week if you use it daily. If Cowork becomes your main workflow, consider Max ($100/month). I’m being direct about this because I don’t want you surprised.

It’s still a research preview. Anthropic says this explicitly. It can make mistakes. It can misread files. It sometimes takes an odd approach to a task when a simpler one would work. You need to review what it produces. Don’t send a client deliverable without reading it first.

It needs the app open. Close the Claude Desktop app, and the session dies. There’s no mobile version. No web version. Cowork only runs inside the desktop app on macOS or Windows.

It’s not for quick questions. If you want to ask “what’s the capital of France,” use Chat. Cowork is for tasks, not trivia. It’s designed for multi-step work.

Agents can be hit or miss. For complex tasks, Cowork breaks the work into parts and runs them in parallel using multiple agents. Most of the time, it’s fast and accurate. Sometimes one agent goes in a weird direction, and the final output has a section that doesn’t match the rest. Keep an eye on it. Happens 10% of the time.

Cowork is not the best at everything. But it’s getting better every week.

And if this is Claude Opus 4.6 + Cowork, I can’t imagine Claude 5, Claude 6…

Open your calendar. Book 30 minutes with yourself, this newsletter, and Claude.

→ Go to Claude.ai. Download the desktop app.
→ Sign in with your Pro account ($20/month. Or $17/month if you pay annually).
→ Open the app. Click the Cowork tab at the top.
→ You’re in.
→ Create a folder on your computer called “Claude-Cowork.” Inside it, create four subfolders: ABOUT ME, TEMPLATES, PROJECTS, CLAUDE OUTPUTS.
→ In the context folder, create your first file: about-me.md. Write three things: (1) What you do for work. (2) How you like to communicate. (3) One example of writing you’re proud of. Paste it in.
→ No time to write it yourself? Let Cowork create it for you.

Pro tip: Instead of typing, use voice to talk. It’s 4x faster.

→ In Cowork, click Add Folder and select your Claude-Cowork folder.
→ Make sure to select Opus 4.6 + Extended thinking for the smartest AI.
→ Type: “I want [task] for [success criteria]. Go through my folder first, and use AskUserQuestion tool so you gather enough content before executing.”
→ Watch what happens. A form appears. Click answers. Let it create your context files.
→ Click Customize in the sidebar → Browse plugins.
→ Pick one that fits your work. Good starters: Productivity (tasks and workflows), Marketing (content drafting), or Sales (prospect research).
→ Click to install. Start a new conversation with the plugin active.
→ Type / to see what slash commands are available. Try one.
→ Give Cowork a task you’d actually need for work this week.
→ Type: “Create a [report / deck / document] based on the files in this folder. Ask me questions first.”
→ Watch it create a real file. Open it. Edit it. Use it.
→ Optional: be amazed.
