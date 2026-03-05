# 探究 Codex 上下文压缩的工作原理

URL: https://x.com/kangwook_lee/status/2028955292025962534

对于非 Codex 模型，开源的 Codex CLI 在本地压缩上下文：一个 LLM 使用压缩提示词（compaction prompt）来总结对话。当之后使用被压缩的上下文时，responses.create() 会接收它，并附带一个用于框定总结的交接提示词（handoff prompt）。这两个提示词在源代码中都是可见的。

对于 Codex 模型，CLI 转而调用 compact() API，它返回一个加密的 blob。我们不知道它内部是否使用了 LLM，使用了什么提示词，或者到底有没有交接提示词。

下面，我展示了一个简单的提示词注入（2 次 API 调用，35 行 Python 代码）是如何揭示 API 压缩路径确实使用了一个 LLM 来总结上下文的，而且有它自己的压缩提示词，并在总结前面添加了一个交接提示词。这些提示词与开源版本几乎完全相同。

我用精心构造的用户消息调用了 compact()。在服务器端，一个压缩器 LLM 使用它自己隐藏的系统提示词（我从未见过，而且想弄清楚）处理我们的输入。

服务器似乎是这样组装压缩器的上下文的：

[![Image 1: Image](./assets/investigating-how-codex-context-compaction-works/image-01.jpg)](https://x.com/Kangwook_Lee/article/2028955292025962534/media/2028952813783662592)

压缩器 LLM 将其系统提示词和我们的输入放在一起读取。因为我们的输入包含一个注入有效载荷（上图中的红色文本），压缩器被诱骗在其输出中包含了它自己的系统提示词。这个纯文本摘要只存在于 OpenAI 的服务器上。我们只看到了加密的 blob：

[![Image 2: Image](./assets/investigating-how-codex-context-compaction-works/image-02.jpg)](https://x.com/Kangwook_Lee/article/2028955292025962534/media/2028952997011832833)

此时我们无法读取 blob 内部的内容。它是用 AES 加密的，密钥保存在 OpenAI 的服务器上。我们只能希望压缩器服从了注入，并将其提示词写入了摘要中。唯一找出真相的方法是第二步。

我将加密的 blob + 第二条用户消息传递给 responses.create()。服务器解密 blob 并组装模型的上下文。

我发送：

[![Image 3: Image](./assets/investigating-how-codex-context-compaction-works/image-03.jpg)](https://x.com/Kangwook_Lee/article/2028955292025962534/media/2028953128410988546)

模型似乎看到了类似这样的内容：

[![Image 4: Image](./assets/investigating-how-codex-context-compaction-works/image-04.jpg)](https://x.com/Kangwook_Lee/article/2028955292025962534/media/2028953263085920256)

如果第 1 步成功了，解密后的 blob 应该包含压缩提示词（被我们的注入泄露）。服务器还会在 blob 前面预置一个交接提示词。所以，如果我们的探测成功让模型重复它看到的内容，输出应该会揭示全部三个：系统提示词、交接提示词和压缩提示词。

下面是 extract_prompts.py 一次运行的完整、未经编辑的输出。黄色 = 系统提示词，绿色 = 交接提示词，粉色 = 压缩提示词。

[![Image 5: Image](./assets/investigating-how-codex-context-compaction-works/image-05.jpg)](https://x.com/Kangwook_Lee/article/2028955292025962534/media/2028953470850744320)

我们如何知道这些是真实的提示词，而不是幻觉产生的文本？提取出的压缩提示词和交接提示词与开源 Codex CLI 中已知的非 Codex 模型使用的提示词非常匹配，这使得模型从头凭空捏造它们的可能性极小。多次运行的结果会有所不同。

综上所述，基于提取所揭示的内容，以下是我们对服务器端 compact() 功能的最佳猜测。

[![Image 6: Image](./assets/investigating-how-codex-context-compaction-works/image-06.jpg)](https://x.com/Kangwook_Lee/article/2028955292025962534/media/2028953557664399360)

[![Image 7: Image](./assets/investigating-how-codex-context-compaction-works/image-07.jpg)](https://x.com/Kangwook_Lee/article/2028955292025962534/media/2028953642322313216)

既然底层的提示词几乎完全相同，为什么 Codex CLI 要使用两条完全不同的压缩路径（针对非 Codex 模型使用本地 LLM，针对 Codex 模型使用加密的 API）？而且为什么要对总结进行加密？

很难说。也许加密的 blob 携带的信息比这个简单的实验能揭示的要多，比如一些关于工具结果如何被压缩和恢复的具体信息。但我没有费心去进一步测试。