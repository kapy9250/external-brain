# 如果明天我要重新开始，我会如何成为一名量化交易员

URL: https://x.com/gemchange_ltd/status/2028904166895112617

2025年，顶级公司的入门级量化交易员（quants）的总薪酬达到了 30万-50万美元。

金融领域的 AI/ML 招聘同比增长了 88%。

如果有人在我刚开始走这条路时能把这篇文章交给我该多好——这里按照你应该学习的确切顺序，规划好了完整的路径。

这条路径就像电子游戏中的关卡，你不能跳级。

每一个概念都建立在前一个概念之上。但如果你投入真正的努力（解决实际问题），而不是去看那些浪费时间的无聊金融 YouTube 视频——你可以在大约 18 个月内从一无所知变成行业里的专家。免责声明：并非财务建议，请自己做研究，市场有风险。

大多数人认为量化交易就是关于选股、对特斯拉发表意见、预测财报。

量化交易是关于**数学**。

你主要是在处理统计关系、定价低效和结构性优势，这些之所以存在，是因为市场是由那些会犯系统性错误的人类所驱动的复杂系统。

量化金融中的一切在某种程度上都可以归结为 1 个问题：

赔率是多少，赔率对我有利吗？

这就是概率。如果你没有在很深的层面上理解概率，这篇文章里的其他任何内容对你来说都不重要。

## 条件思维 (Conditional thinking)

大多数人以绝对的方式思考。某件事要么是真的，要么不是。而量化交易员以条件的方式思考：基于我所知的信息，这件事发生的可能性有多大？

[![Image 1: Image](./assets/how-id-become-a-quant-if-i-had-to-start-over-tomorrow/image-01.jpg)](https://x.com/gemchange_ltd/article/2028904166895112617/media/2028769373503057920)

在 B 发生的条件下 A 发生的概率，等于两者同时发生的概率除以 B 发生的概率。这有着深远的影响。

一只股票在 60% 的交易日里会上涨——这是基础概率。但在交易量高于平均水平的日子里，它有 75% 的时间会上涨。

这个条件概率才是“非废话 (NOT BS)”。原始的 60% 只是“充满噪音的废话 (NOISY BS)”。

## 贝叶斯定理 (Bayes' theorem)

[![Image 2: Image](./assets/how-id-become-a-quant-if-i-had-to-start-over-tomorrow/image-02.jpg)](https://x.com/gemchange_ltd/article/2028904166895112617/media/2028769593448431616)

你更新后的信念等于：

(如果你的假设为真，你看到这些数据的可能性) * (你的先验信念) / (在任何假设下看到这些数据的总概率)。

分母是对所有假设的求和。

在实践中，你可以通过蒙特卡洛抽样来计算。

但逻辑是一样的。贝叶斯定理是你如何在实时中更新你的确信度的方法。

一个模型说某只股票应该值 $50。财报公布了，收入比预期高 3%。贝叶斯后验概率向上移动。更新最快且最准确的交易员就能赚到钱。

## 期望值与方差：你最好的两个朋友

[![Image 3: Image](./assets/how-id-become-a-quant-if-i-had-to-start-over-tomorrow/image-03.jpg)](https://x.com/gemchange_ltd/article/2028904166895112617/media/2028770153844944896)

[![Image 4: Image](./assets/how-id-become-a-quant-if-i-had-to-start-over-tomorrow/image-04.jpg)](https://x.com/gemchange_ltd/article/2028904166895112617/media/2028770199046922240)

期望值 (Expected value) 代表你的确信度。方差 (Variance) 代表你的风险。

如果你的策略有正的期望值，并且你能熬过方差的波动，你很可能就会赚钱。

**Level 1 作业** (3-4 周，每天 2 小时):
1. 阅读 Blitzstein & Hwang 的《Introduction to Probability》(哈佛大学的免费 PDF)。做完第 1-6 章的所有习题。
2. 写代码：模拟 10,000 次抛硬币，视觉上验证大数定律。
3. 写代码 2：实现一个贝叶斯更新器，接受先验和似然度，返回后验。

```python
import numpy as np
import matplotlib.pyplot as plt

# 大数定律：运行平均值收敛于真实概率
np.random.seed(42)
flips = np.random.choice([0, 1], size=10000, p=[0.5, 0.5])
running_avg = np.cumsum(flips) / np.arange(1, 10001)

plt.figure(figsize=(10, 4))
plt.plot(running_avg, linewidth=0.7)
plt.axhline(y=0.5, color='r', linestyle='--', label='True probability')
plt.xlabel('Number of flips')
plt.ylabel('Running average')
plt.title('Law of Large Numbers in Action')
plt.legend()
plt.savefig('lln.png', dpi=150)
print(f"After 10,000 flips: {running_avg[-1]:.4f} (true: 0.5000)")
```

一旦你懂得了概率的语言，你需要学会倾听数据。

[![Image 5: Image](./assets/how-id-become-a-quant-if-i-had-to-start-over-tomorrow/image-05.jpg)](https://x.com/gemchange_ltd/article/2028904166895112617/media/2028889248573644801)

这就是统计学。统计学教给我们的第一课是：“大多数看起来像真理的东西，实际上都是充满噪音的废话 (NOISY BS)”。

## 假设检验是“废话探测器”

你构建了一个模型。它回测出 15% 的年化回报。这是真的吗？

设定原假设 H_0：“该策略预期回报为零”。计算检验统计量。计算 p 值——即如果 H_0 为真，看到这么好的结果的概率。

但是，如果你测试了 1,000 个随机策略，纯粹出于偶然，其中会有 50 个显示 p 值低于 0.05。

这就是多重比较问题 (multiple comparisons problem)。你的解决办法是邦费罗尼校正 (Bonferroni correction)：将你的显著性阈值除以测试次数。或者使用 Benjamini-Hochberg 过程来控制错误发现率。

每一个初学者都极大地高估了他们发现的“真理”。你的前 10 个策略全都会是充满噪音的废话。现在就接受这一点，可以为你省下很多钱。

## 回归分析：分解回报

线性回归 y=Xβ+ϵ 是主力工具。在金融中，你将策略的回报针对已知的风险因子进行回归：

[![Image 6: Image](./assets/how-id-become-a-quant-if-i-had-to-start-over-tomorrow/image-06.jpg)](https://x.com/gemchange_ltd/article/2028904166895112617/media/2028874982357602305)

截距 α 是你的 alpha——无法用已知因子解释的回报。如果在剔除因子影响后 α 为零，那么你的“优势”不过是伪装的市场敞口。

OLS 估计量：

[![Image 7: Image](./assets/how-id-become-a-quant-if-i-had-to-start-over-tomorrow/image-07.jpg)](https://x.com/gemchange_ltd/article/2028904166895112617/media/2028875150184095744)

最重要的数字是 α。使用 Newey-West 标准误——金融数据具有自相关性和异方差性，因此默认的 OLS 标准误是错误的。使用它们就像开着挡风玻璃碎裂的车一样危险。

## 最大似然估计 (MLE)

给定来自具有参数 θ 的模型的数据 x_1,…,x_n：

[![Image 8: Image](./assets/how-id-become-a-quant-if-i-had-to-start-over-tomorrow/image-08.jpg)](https://x.com/gemchange_ltd/article/2028904166895112617/media/2028890232339255296)

将导数设为零并求解。（或者说完了）

MLE 是你如何校准金融中的每一个模型的方法：将 GARCH 模型拟合到波动率，估计跳跃-扩散 (jump-diffusion) 参数，校准期权定价以符合市场报价。

它是渐近有效的：对于大样本，没有任何其他一致估计量具有更低的方差（克拉美-罗下界，Cramér-Rao lower bound）。

当某家公司的人说他们在“校准”模型时，他们几乎总是指 MLE。

**Level 2 作业** (4-5 周):
1. 阅读 Wasserman 的《All of Statistics》第 1-13 章。
2. 写代码：使用 yfinance 下载真实的股票回报率。测试正态性（它们会失败）。通过 MLE 拟合一个 t 分布。进行比较。
3. 写代码：使用 statsmodels 对股票投资组合运行 Fama-French 三因子回归。
4. 写代码：实现一个排列检验 (permutation test)——洗牌日期 10,000 次，比较洗牌后的表现与实际表现。

```python
import numpy as np
from scipy import optimize, stats

# 演示肥尾效应：将 Student-t 的 MLE 拟合到回报数据
np.random.seed(42)

# 模拟“现实”回报（肥尾，轻微正漂移）
true_df = 4
returns = stats.t.rvs(df=true_df, loc=0.0005, scale=0.015, size=1000)

def neg_log_likelihood(params, data):
    df, loc, scale = params
    if df <= 2 or scale <= 0:
        return 1e10
    return -np.sum(stats.t.logpdf(data, df=df, loc=loc, scale=scale))

result = optimize.minimize(
    neg_log_likelihood, x0=[5, 0, 0.01], args=(returns,),
    method='Nelder-Mead'
)
fitted_df, fitted_loc, fitted_scale = result.x

print(f"MLE 自由度: {fitted_df:.2f} (真实值: {true_df})")
print(f"MLE 位置参数:           {fitted_loc:.6f}")
print(f"MLE 尺度参数:              {fitted_scale:.6f}")

# 正态性测试
_, p_normal = stats.normaltest(returns)
print(f"\n正态性测试 p-value: {p_normal:.2e}")
print(f"拒绝正态性吗？ {'是的  肥尾被证实' if p_normal < 0.05 else '不'}")
```

## 线性代数 (Linear Algebra)

线性代数听起来很无聊。但它是运行一切的机器：投资组合构建、PCA（主成分分析）、神经网络、协方差估计、因子模型。如果不精通矩阵，你就不可能成为一名量化分析师。

[![Image 9: Image](./assets/how-id-become-a-quant-if-i-had-to-start-over-tomorrow/image-09.jpg)](https://x.com/gemchange_ltd/article/2028904166895112617/media/2028891478500753413)

(如果你在学校里跳过了代数，那你就完了)

### 在矩阵中思考

协方差矩阵 Σ 捕捉了每一项资产相对于其他各项资产的移动情况。对于 500 只股票，Σ 是 500×500 的，包含 125,250 个唯一的条目。投资组合方差坍缩成一个单一的表达式：

[![Image 10: Image](./assets/how-id-become-a-quant-if-i-had-to-start-over-tomorrow/image-10.jpg)](https://x.com/gemchange_ltd/article/2028904166895112617/media/2028876049396699138)

这种二次型 (quadratic form) 是马科维茨 (Markowitz) 投资组合理论、风险管理以及一切的核心。

### 特征值是在股票宇宙中真正重要的东西

观察一个包含 500 只股票的宇宙，前 5 个特征向量解释了所有方差的 70%。其余的都是充满噪音的废话 (NOISY BS)。

当你第一次使用特征分解 (eigendecomposition) 时，整个世界都变了。这就是降维，也是因子投资的基础。

**Level 3 作业** (4-6 周):
1. 观看 Gilbert Strang 的 MIT 18.06 讲座——看全部。没商量。
2. 阅读 Strang 的《Introduction to Linear Algebra》。做课后习题。
3. 写代码：对标普 500 回报率进行 PCA 分解。绘制特征值谱。识别前 3 个主成分。
4. 写代码：从头实现马科维茨均值-方差优化。

```python
import numpy as np
import cvxpy as cp

# ============================================
# 使用 cvxpy 进行 Markowitz 优化
# ============================================
np.random.seed(42)
n_assets = 10
mu = np.random.uniform(0.04, 0.15, n_assets)
A = np.random.randn(n_assets, n_assets) * 0.1
cov = A @ A.T + np.eye(n_assets) * 0.01

w = cp.Variable(n_assets)
objective = cp.Minimize(cp.quad_form(w, cov))
constraints = [
    mu @ w >= 0.08,      # 最低回报
    cp.sum(w) == 1,       # 满仓投资
    w >= -0.1,            # 最多 10% 做空
    w <= 0.3              # 最多 30% 做多
]

prob = cp.Problem(objective, constraints)
prob.solve()

ret = mu @ w.value
vol = np.sqrt(w.value @ cov @ w.value)
sharpe = (ret - 0.03) / vol

print(f"投资组合回报:  {ret:.4f}")
print(f"投资组合波动率:     {vol:.4f}")
print(f"夏普比率:      {sharpe:.4f}")
print(f"权重: {np.round(w.value, 4)}")
```

## 微积分 (Calculus)

微积分是描述变化的语言。在金融中，一切都在变：价格、波动率、相关性，整个概率分布每秒都在发生改变。微积分描述并利用了这些变化。

导数 (数学上的)：出现在每一次神经网络的反向传播和每一次希腊字母 (Greek) 的计算中。

泰勒展开 (Taylor expansion)：

[![Image 11: Image](./assets/how-id-become-a-quant-if-i-had-to-start-over-tomorrow/image-11.jpg)](https://x.com/gemchange_ltd/article/2028904166895112617/media/2028877036509700096)

Delta 对冲是一阶近似。Gamma 对冲增加了二阶修正。而伊藤微积分 (Itô calculus) 之所以不同于普通微积分，正是因为对于随机过程来说，二阶泰勒项不会消失。记住这一点。

**Level 4 作业** (4-5 周):
1. 阅读 Boyd & Vandenberghe 的《Convex Optimization》(斯坦福的免费 PDF) 第 1-5 章。
2. 写代码：从头实现梯度下降。最小化 Rosenbrock 函数。
3. 写代码：使用 cvxpy 解决包含交易成本约束的投资组合优化问题。

在学习随机微积分之前，你只是一个喜欢金融的数据科学家。

学完之后，你才是一名量化交易员。QUANTATIVE FINANCE EXPERT，听懂了吗？

[![Image 12: Image](./assets/how-id-become-a-quant-if-i-had-to-start-over-tomorrow/image-12.jpg)](https://x.com/gemchange_ltd/article/2028904166895112617/media/2028894683586293760)

那就是你

在这里，你要学习在连续时间中对随机性进行建模，从第一性原理推导出布莱克-斯科尔斯 (Black-Scholes) 方程，并理解万亿美元的衍生品市场为什么是这样运作的。

### 布朗运动 (Brownian motion)：形式化的纯粹随机性

布朗运动（维纳过程）W_t 是一个连续时间的随机游走：

*   W_0 = 0
*   增量 W_t - W_s ~ N(0, t - s)，对于 t > s
*   非重叠的增量是独立的
*   路径是连续的但在任何地方都不可导

一切都依赖的关键洞见是：dW_t 的“大小”是 dt，这意味着 (dW_t)^2 = dt。这听起来像是一个技术细节，但它是量化金融中最重要的一条事实。

几何布朗运动 (Geometric Brownian Motion) 模拟股票价格：

[![Image 13: Image](./assets/how-id-become-a-quant-if-i-had-to-start-over-tomorrow/image-13.jpg)](https://x.com/gemchange_ltd/article/2028904166895112617/media/2028879892264132608)

### 伊藤引理 (Itô's lemma)

在普通微积分中，df = f'(x)dx。你进行泰勒展开，因为 (dx)^2 项极小，你把它舍弃了。

但是当 x 是一个随机过程时，(dW_t)^2 = dt 是一阶项。你不能舍弃它。

伊藤引理：

[![Image 14: Image](./assets/how-id-become-a-quant-if-i-had-to-start-over-tomorrow/image-14.jpg)](https://x.com/gemchange_ltd/article/2028904166895112617/media/2028880174767587329)

把它应用到一个期权价格上，你就得到了 Black-Scholes。这个公式是整个衍生品行业背后的引擎。

### 从头推导布莱克-斯科尔斯方程 (Deriving Black-Scholes from scratch)

准备好纸笔跟着来。

步骤 1：设 V(S,t) 为期权价格。应用伊藤引理：

[![Image 15: Image](./assets/how-id-become-a-quant-if-i-had-to-start-over-tomorrow/image-15.jpg)](https://x.com/gemchange_ltd/article/2028904166895112617/media/2028880303385669632)

步骤 2：构建一个 Delta 对冲的投资组合 Π=V−∂V/∂S​⋅S。计算 dΠ：

[![Image 16: Image](./assets/how-id-become-a-quant-if-i-had-to-start-over-tomorrow/image-16.jpg)](https://x.com/gemchange_ltd/article/2028904166895112617/media/2028880486072819712)

dW_t​ 项被完美抵消了。这个投资组合在局部是无风险的。

步骤 3：一个无风险投资组合必须赚取无风险利率：dΠ = rΠ dt。

步骤 4：代入并重新排列：

[![Image 17: Image](./assets/how-id-become-a-quant-if-i-had-to-start-over-tomorrow/image-17.jpg)](https://x.com/gemchange_ltd/article/2028904166895112617/media/2028880968610635777)

这就是布莱克-斯科尔斯偏微分方程 (Black-Scholes PDE)。

注意发生了一件神奇的事——漂移项 μ 消失了。期权价格并不依赖于股票的预期回报。风险偏好并不重要。你可以假设每个人都是风险中性的来为期权定价。当你第一次真正理解这一点时，绝对是震撼大脑的。

求解这个针对具有执行价 K 和到期日 T 的欧式看涨期权的 PDE，可得：

[![Image 18: Image](./assets/how-id-become-a-quant-if-i-had-to-start-over-tomorrow/image-18.jpg)](https://x.com/gemchange_ltd/article/2028904166895112617/media/2028881164254289920)

[![Image 19: Image](./assets/how-id-become-a-quant-if-i-had-to-start-over-tomorrow/image-19.jpg)](https://x.com/gemchange_ltd/article/2028904166895112617/media/2028881299759611904)

其中 d_1=

[![Image 20: Image](./assets/how-id-become-a-quant-if-i-had-to-start-over-tomorrow/image-20.jpg)](https://x.com/gemchange_ltd/article/2028904166895112617/media/2028881391610404864)

d_2 = d_1 - σ√T

### 希腊字母 (The Greeks)

*   **Delta Δ**: 股票每波动 $1 时期权波动的金额。你的对冲比率。
*   **Gamma Γ​**: Delta 变化的速度。你的凸性敞口。
*   **Theta Θ**: 时间衰减。对于多头期权来说通常是负的。
*   **Vega V**: 对波动率的敏感度。大多数衍生品交易台赚钱的来源。
*   **Rho ρ**: 对利率的敏感度。

Delta 告诉你对冲比率。Gamma 告诉你需要多频繁地进行重新对冲。Theta 是持有的成本。Vega 是波动率交易台的面包和黄油。

**Level 5 作业** (6-8 周 - 最难的一关):
1. 阅读 Shreve 的《Stochastic Calculus for Finance II》。黄金标准。
2. 替代读物：Arguin 的《A First Course in Stochastic Calculus》(更新，更易读)。
3. 推导：当 S 遵循 GBM 时，将伊藤引理应用于 f(S)=ln⁡(S)。得出 −σ^2/2。
4. 推导：从 Delta 对冲论证中得出完整的 Black-Scholes 方程。
5. 写代码：从头实现 Black-Scholes。与蒙特卡洛模拟比较。验证收敛性。

```python
import numpy as np
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    if option_type == 'call':
        return S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
    else:
        return K*np.exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1)

def monte_carlo_option(S0, K, T, r, sigma, n_sims=500_000):
    """通过风险中性模拟定价 (漂移 = r, 不是 mu)"""
    Z = np.random.standard_normal(n_sims)
    ST = S0 * np.exp((r - sigma**2/2)*T + sigma*np.sqrt(T)*Z)
    payoffs = np.maximum(ST - K, 0)
    price = np.exp(-r*T) * np.mean(payoffs)
    stderr = np.exp(-r*T) * np.std(payoffs) / np.sqrt(n_sims)
    return price, stderr

def greeks(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    return {
        'delta': norm.cdf(d1),
        'gamma': norm.pdf(d1) / (S * sigma * np.sqrt(T)),
        'theta': -(S*norm.pdf(d1)*sigma)/(2*np.sqrt(T)) - r*K*np.exp(-r*T)*norm.cdf(d2),
        'vega':  S * np.sqrt(T) * norm.pdf(d1),
        'rho':   K * T * np.exp(-r*T) * norm.cdf(d2),
    }

# 验证：蒙特卡洛模拟收敛于 Black-Scholes
S, K, T, r, sigma = 100, 105, 1.0, 0.05, 0.2

bs = black_scholes(S, K, T, r, sigma)
mc, err = monte_carlo_option(S, K, T, r, sigma)
g = greeks(S, K, T, r, sigma)

print(f"Black-Scholes: ${bs:.4f}")
print(f"Monte Carlo:   ${mc:.4f} ± {err:.4f}")
print(f"Difference:    ${abs(bs - mc):.4f}\n")
for name, val in g.items():
    print(f"  {name:>6}: {val:.6f}")
```

这是目前世界上最有趣的市场，其背后的数学连接了本文中的一切：概率、信息论、凸优化、整数规划。

### LMSR 如何为信念定价

对数市场评分规则 (LMSR, Logarithmic Market Scoring Rule)，由 Robin Hanson 发明，驱动着自动预测市场。对于 n 个结果的成本函数：

[![Image 21: Image](./assets/how-id-become-a-quant-if-i-had-to-start-over-tomorrow/image-21.jpg)](https://x.com/gemchange_ltd/article/2028904166895112617/media/2028883538553065472)

其中 q_i​ 追踪结果 i 的未平仓份额，b 是流动性参数。结果 i 的价格为：

[![Image 22: Image](./assets/how-id-become-a-quant-if-i-had-to-start-over-tomorrow/image-22.jpg)](https://x.com/gemchange_ltd/article/2028904166895112617/media/2028883637823823873)

那是 softmax 函数——驱动着每一个神经网络分类器的函数。

价格总和始终为 1，始终位于 (0,1) 区间内，并且由于提供了无限流动性而始终存在。做市商的最大损失被限制在 b * ln(n)。

### 4 种职业原型：

1. **量化研究员 (Quant Researcher)**：极度聪明的家伙，在拍字节级别的数据中寻找模式，建立预测模型，设计策略。需要博士级别的数学/统计/机器学习背景，或极为优异的本科学业成绩。在像 Jane Street 这样的公司，研究员会使用成千上万的 GPU。
2. **量化开发员/工程师 (Quant Developer/Engineer)**：中等聪明的家伙，主要是构建者。开发交易平台、执行引擎、实时数据管道。使研究员的模型能够实际交易。需要精通生产级 C++/Rust/Python、低延迟系统。
3. **量化交易员 (Quant Trader)**：要么是最大的赌徒，要么是极度聪明的家伙，主要是决策者。运作资金，管理风险，做实时决策。薪酬方差最大——在特别好的年份可以拿到八位数。
4. **风险量化 (Risk Quant)**：极度聪明的家伙或者就是经验极其丰富的企业人员，主要是守护者。模型验证、VaR（在险价值）、压力测试、合规监管。职业更稳定，天花板较低。新兴的 AI/ML 量化角色（使用深度学习生成信号）增长最快，2025 年招聘量同比增长了 88%。

### 薪酬情况：

**顶级梯队 (Jane Street, Citadel, HRT)**
- 应届毕业生: $300K-$500K+ 总包
- 职业中期 (3-7年): $550K-$950K
- 资深 (8+年): $1M-$3M+
- 明星交易员/PM: $3M-$30M+

**中级梯队 (Two Sigma, DE Shaw)**
- 应届毕业生: $250K–$350K
- 职业中期 (3-7年): $350K–$625K
- 资深 (8+年): $575K–$1.2M

据报道，Jane Street 在 2025 年上半年的平均员工薪酬为每年 140 万美元。不过那是平均水平。

### 面试挑战

简历筛选 -> 在线评估（通过 Zetamac 进行心算——目标 50+，逻辑谜题） -> 电话面试（概率问题、博弈游戏） -> Superday（3-5 场背靠背面试、模拟交易、编码、白板推导）。

Jane Street 会故意出一些难到无法独自解决的问题——他们想测试你如何使用提示并与人合作。

在他们最近的实习生中，超过三分之二学的是计算机科学 (CS)；超过三分之一学的是数学。通常不要求具备金融知识。

排名第一的备考资源：周新锋 (Xinfeng Zhou) 的《A Practical Guide to Quantitative Finance Interviews》(绿皮书)——包含 200 多个真实问题。补充资料：Brainstellar（“量化界的 LeetCode”）和 Jane Street 的 Figgie 纸牌游戏。

### 技术栈

**Python 栈**
- 数据: pandas, polars（Polars 在处理大数据集时快 10-50 倍）
- 数值计算: numpy, scipy
- 机器学习 (表格型): xgboost, lightgbm, catboost
- 机器学习 (深度): pytorch
- 优化: cvxpy
- 衍生品: QuantLib（工业级，C++ 后端）
- 统计: statsmodels
- 回测: NautilusTrader
- 回测 (更简单): backtrader, vectorbt（更容易上手的起点）
- 量化研究: Microsoft Qlib（17K+ stars，面向 AI）
- 交易强化学习: FinRL（10K+ stars）

**C++ 和 Rust**
老实说，我对这些一无所知。以下是我找到的信息：
- C++ 库: QuantLib, Eigen, Boost。
- Rust: 用于期权定价的 RustQuant，NautilusTrader 作为 Rust+Python 范例（Rust 核心为了速度，Python API 用于研究）。

**数据源**
- 免费: yfinance, Finnhub（60 次调用/分钟）, Alpha Vantage。
- 中档: Polygon ($199/月, 延迟低于 20 毫秒), Tiingo。
- 企业级: Bloomberg Terminal (~$32K/年), Refinitiv, FactSet。
- 区块链: Alchemy（带有归档访问权限的免费额度）。

**求解器 (Solvers)**
- Gurobi: 最快的商业 MIP 求解器，提供免费学术许可。对于组合套利必不可少。
- Google OR-Tools: 最强的免费求解器。
- PuLP/Pyomo: Python 建模接口。

### 学习资源

**数学**
1. Blitzstein & Hwang - Introduction to Probability (哈佛免费 PDF)
2. Strang - Introduction to Linear Algebra + MIT 18.06 讲座
3. Wasserman - All of Statistics
4. Boyd & Vandenberghe - Convex Optimization (斯坦福免费 PDF)
5. Shreve - Stochastic Calculus for Finance I & II

**量化金融**
1. Hull - Options, Futures, and Other Derivatives (期权、期货及其他衍生产品)
2. Natenberg - Option Volatility and Pricing
3. López de Prado - Advances in Financial Machine Learning
4. Ernest Chan - Quantitative Trading
5. Zuckerman - The Man Who Solved the Market

**面试准备**
1. Zhou - Practical Guide to Quantitative Finance Interviews (绿皮书 #1)
2. Crack - Heard on the Street
3. Joshi - Quant Job Interview Questions

**比赛**
*   Jane Street Kaggle ($100K 奖金)
*   WorldQuant BRAIN (100K+ 用户，为 Alpha 信号付费)
*   Citadel Datathon (通向就业的快车道)
*   Jane Street 月度谜题 (难度高于面试)

估计误差 (Estimation error) 才是真正的敌人。满仓凯利下注 (Full Kelly betting)、无约束的马科维茨模型、特征过多的机器学习模型——它们都因为同一个原因而失败：过度拟合了参数估计中充满噪音的废话 (NOISY BS)。

如果使用真实参数，这些数学是完美运作的。但你永远不可能拥有真实的参数。理论与实践之间的差距总是来源于估计误差，而最优秀的量化分析师就是那些尊重误差的人。

工具已经民主化了。但定力 (Conviction) 没有。任何人都可以使用 QuantLib 和 PyTorch。技术是必要但不充分的。护城河 (Edge) 存在于独特的数据、独特的模型或独特的执行中——而不是更好的 pip 安装包。

数学才是护城河。AI 可以写代码、提建议。但如果你能够推导伊藤引理为什么多出一个项、证明贴现价格在风险中性测度下是鞅 (martingales)、知道在组合市场中凸松弛 (convex relaxation) 何时是紧的何时是松的，这种数学的流畅度就区分了“构建优势”的 quant 和“借用优势”的 quant。而借来的优势是会过期的。

第 2 部分将涵盖：奇异衍生品（障碍期权、亚洲期权、回望期权）、随机波动率（Heston 模型校准）、跳跃扩散（Merton）、高级测度论（鞅表示定理、可选停止定理）、最优执行的随机控制（Almgren-Chriss）、用于做市的强化学习、用于金融时间序列的 Transformer 架构、FPGA 交易基础设施、WebSocket 馈送、并行执行、结合 Gurobi 使用 Frank-Wolfe 算法在数千种条件下进行组合套利。

数学越难，支票越长。