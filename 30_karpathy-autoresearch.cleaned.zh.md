# Andrej Karpathy on X: autoresearch

我把 "autoresearch" 项目打包成了一个全新的、自包含的极简仓库，大家如果想在周末玩一玩的话可以试试。它基本上就是把 nanochat LLM 训练核心精简成了一个单 GPU、单文件版本（约 630 行代码），然后：
- 人类迭代提示词（.md）
- AI Agent 迭代训练代码（.py）

我们的目标是，通过工程化设计你的 Agent，让它无限期地取得最快的研究进展，而无需你自己的任何参与。

在图片中，每一个点都代表一次完整的 LLM 训练运行，耗时正好 5 分钟。Agent 在一个 git 功能分支上以自主循环的方式工作，当它发现更好的设置（最终的验证集损失更低）时——包括神经网络架构、优化器以及所有超参数等——它会向训练脚本累积 git 提交。

你可以想象一下，比较不同提示词、不同 Agent 等等的研究进展。
[github.com/karpathy/autoresearch](https://github.com/karpathy/autoresearch)

一部分是代码，一部分是科幻，还有一点点“神经质” :)