# GitNexus：将任何 GitHub 仓库转化为交互式知识图谱

URL: https://x.com/MillieMarconnni/status/2028436636841996451

🚨 突发：GitHub 上的一位开发者刚刚构建了一个工具，能将任何 GitHub 仓库转变为交互式的知识图谱，并且免费开源了。

它叫 GitNexus。你可以把它看作是你代码库的可视化 X 光片，但它还自带一个你可以真正与其对话的 AI 智能体。

无需服务器。无需订阅。没有企业销售推销电话。

以下是它在你的浏览器中能做的事情：
→ 在几秒钟内解析你的整个 GitHub 仓库或 ZIP 文件
→ 使用 D3.js 构建实时的交互式知识图谱
→ 映射每一个函数、类、导入和调用关系
→ 运行一个 4 遍 (4-pass) 的 AST 管道：结构 → 解析 → 导入 → 调用图
→ 将所有内容存储在一个内嵌的 KuzuDB 图数据库中
→ 让你使用纯英语通过一个 AI 智能体查询你的代码库

这里最疯狂的部分是：它使用 Web Workers 跨线程并行解析，所以即使是庞大的单体仓库 (monorepo) 也不会让你的浏览器标签页卡死。

它的 Graph RAG 智能体使用 Cypher 查询语句来遍历真正的图关系，不是词嵌入 (embeddings)，也不是向量搜索 (vector search)。而是真正的图逻辑。

你可以问它类似这样的问题：“哪些函数调用了这个模块？” 或者 “找出所有继承自 X 的类”，它会通过图谱追踪出答案。

这就是那种企业团队每个月要花几千美元购买的代码智能工具。而它完全在你的浏览器中运行。

支持 TypeScript、JavaScript 和 Python。100% 开源。MIT 许可证。

代码仓库：[github.com/abhigyanpatwar/gitnexus](https://github.com/abhigyanpatwar/gitnexus)

![Image 1](./assets/gitnexus-interactive-knowledge-graph/image-01.jpg)
