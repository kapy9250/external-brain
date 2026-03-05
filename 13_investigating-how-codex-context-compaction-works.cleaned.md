# Investigating how Codex context compaction works

URL: https://x.com/kangwook_lee/status/2028955292025962534

For non-codex models, the open-source Codex CLI compacts context locally: an LLM summarizes the conversation using a compaction prompt. When the compacted context is later used, responses.create() receives it with a handoff prompt that frames the summary. Both prompts are visible in the source code.

For codex models, the CLI instead calls the compact() API, which returns an encrypted blob. We don't know if it uses an LLM internally, what prompts it uses, or whether there is a handoff prompt at all.

Below, I show how a simple prompt injection (2 API calls, 35 lines of Python) reveals that the API compaction path does use an LLM to summarize the context, with its own compaction prompt and a handoff prompt prepended to the summary. The prompts are nearly identical to the open-source versions.

I call compact() with a crafted user message. On the server side, a compactor LLM processes our input using its own hidden system prompt (which I have never seen and want to figure out).

The server seems to assemble the compactor's context like this:

[![Image 1: Image](./assets/investigating-how-codex-context-compaction-works/image-01.jpg)](https://x.com/Kangwook_Lee/article/2028955292025962534/media/2028952813783662592)

The compactor LLM reads its system prompt + our input together. Because our input contains an injection payload (red text above), the compactor is tricked into including its own system prompt in its output. This plaintext summary exists only on OpenAI's server. We only see the encrypted blob:

[![Image 2: Image](./assets/investigating-how-codex-context-compaction-works/image-02.jpg)](https://x.com/Kangwook_Lee/article/2028955292025962534/media/2028952997011832833)

At this point we have no way to read what's inside the blob. It is AES-encrypted and the key lives on OpenAI's servers. We only hope the compactor obeyed the injection and wrote its prompt into the summary. The only way to find out is Step 2.

I pass the encrypted blob + a second user message to responses.create(). The server decrypts the blob and assembles the model's context.

I send:

[![Image 3: Image](./assets/investigating-how-codex-context-compaction-works/image-03.jpg)](https://x.com/Kangwook_Lee/article/2028955292025962534/media/2028953128410988546)

The model seems to see something like this:

[![Image 4: Image](./assets/investigating-how-codex-context-compaction-works/image-04.jpg)](https://x.com/Kangwook_Lee/article/2028955292025962534/media/2028953263085920256)

If Step 1 worked, the decrypted blob should contain the compaction prompt (leaked by our injection). The server also prepends a handoff prompt to the blob. So if our probe successfully gets the model to repeat what it sees, the output should reveal all three: the system prompt, the handoff prompt, and the compaction prompt.

Below is the complete, unedited output from one run of extract_prompts.py. Yellow = system prompt, green = handoff prompt, pink = compaction prompt.

[![Image 5: Image](./assets/investigating-how-codex-context-compaction-works/image-05.jpg)](https://x.com/Kangwook_Lee/article/2028955292025962534/media/2028953470850744320)

How do we know these are the real prompts and not just hallucinated text? The extracted compaction prompt and handoff prompt closely match the known prompts used for non-codex models in the open-source Codex CLI, which makes it unlikely that the model invented them from scratch. Results vary across runs.

Putting it all together, here is our best guess for what compact() does on the server side, based on what the extraction revealed.

[![Image 6: Image](./assets/investigating-how-codex-context-compaction-works/image-06.jpg)](https://x.com/Kangwook_Lee/article/2028955292025962534/media/2028953557664399360)

[![Image 7: Image](./assets/investigating-how-codex-context-compaction-works/image-07.jpg)](https://x.com/Kangwook_Lee/article/2028955292025962534/media/2028953642322313216)

Why does the Codex CLI use two entirely different compaction paths (local LLM for non-codex models, encrypted API for codex models) when the underlying prompts are nearly identical? And why encrypt the summary at all?

Hard to say. Maybe the encrypted blob carries something more than what this simple experiment can reveal, e.g. something specific about how tool results are compacted and restored. But I didn't bother to test further.