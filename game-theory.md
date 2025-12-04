---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 博弈论基础

本讲座介绍博弈论的基本概念及其在经济决策中的应用。我们将探讨策略互动、纳什均衡和常见的博弈结构。

## 策略思维导论

博弈论为分析多个决策者进行策略互动的情境提供了一个框架。每个参与者的最优选择取决于其他人的选择，从而产生复杂的相互依赖关系。

在经济市场中，企业在价格或数量上竞争时进行策略博弈。理解这些互动有助于预测市场结果并设计更好的机制。

## 囚徒困境

经典的囚徒困境说明了为什么理性的个体可能不会合作，即使合作对每个人都有利。两个嫌疑人被分别审讯，必须决定是认罪还是保持沉默。

收益矩阵捕获了策略结构：

|                | 合作        | 背叛        |
|----------------|-------------|-------------|
| **合作**       | (-1, -1)    | (-3, 0)     |
| **背叛**       | (0, -3)     | (-2, -2)    |

每个参与者都有占优策略选择背叛，导致对双方都次优的结果。

### 现实世界的应用

囚徒困境结构出现在许多经济背景中：
- 企业之间的价格竞争
- 公共物品供给
- 环境保护协议
- 军备竞赛和军事支出

理解这个博弈有助于解释市场失灵以及对监管或合作机制的需求。

## 纳什均衡

纳什均衡是一种策略组合，其中没有参与者可以通过单方面改变策略来改善其收益。它代表了一个稳定的结果，其中每个参与者的策略在给定其他人策略的情况下是最优的。

在数学上，对于参与者 $i = 1, \ldots, n$，具有策略集 $S_i$ 和收益函数 $u_i$，策略组合 $(s_1^*, \ldots, s_n^*)$ 是纳什均衡，如果：

$$
u_i(s_i^*, s_{-i}^*) \geq u_i(s_i, s_{-i}^*) \quad \forall s_i \in S_i, \forall i
$$

让我们用 Python 计算一个简单博弈的纳什均衡：

```{code-cell} python
import numpy as np
import nashpy as nash

# Define a simple 2x2 game
# Player 1's payoff matrix
A = np.array([[3, 0],
              [5, 1]])

# Player 2's payoff matrix  
B = np.array([[3, 5],
              [0, 1]])

# Create game
game = nash.Game(A, B)

# Find Nash equilibria
equilibria = list(game.support_enumeration())

print("Nash Equilibria:")
for eq in equilibria:
    print(f"Player 1: {eq[0]}, Player 2: {eq[1]}")
    print(f"Payoffs: ({np.dot(eq[0], A @ eq[1])}, {np.dot(eq[0], B.T @ eq[1])})")
    print()
```

### 混合策略

当不存在纯策略纳什均衡时，参与者可能会对策略进行随机化。这些混合策略均衡需要无差异条件，即参与者愿意进行随机化。

混合策略均衡概率可以通过求解以下方程计算：

```{math}
\begin{align}
p \cdot u_1(\text{Strategy 1}) &= p \cdot u_1(\text{Strategy 2}) \\
q \cdot u_2(\text{Strategy 1}) &= q \cdot u_2(\text{Strategy 2})
\end{align}
```

## 序贯博弈

在序贯博弈中，参与者按特定顺序行动并观察之前的行动。这些博弈使用逆向归纳法进行分析，从博弈树的末端向开始处理。

关键洞见是子博弈完美：在每个决策节点，参与者在给定未来博弈的情况下做出最优选择。这消除了理性参与者不会执行的不可信威胁。

### 斯塔克尔伯格竞争

一个经典应用是斯塔克尔伯格竞争，其中一家企业（领导者）首先选择数量，另一家企业（追随者）在观察到这一选择后再做决定。

领导者预期追随者的反应函数并做出最优选择：

$$
\max_{q_L} \pi_L(q_L, R(q_L))
$$

其中 $R(q_L)$ 是追随者对领导者数量 $q_L$ 的最佳反应。

让我们数值求解一个斯塔克尔伯格博弈：

```{code-cell} python
from scipy.optimize import minimize_scalar

# Market parameters
a = 100  # Demand intercept
c = 10   # Marginal cost

# Follower's reaction function: q_F = (a - c - q_L) / 2
def follower_response(q_L):
    return (a - c - q_L) / 2

# Leader's profit given follower's response
def leader_profit(q_L):
    q_F = follower_response(q_L)
    price = a - q_L - q_F
    return -(price - c) * q_L  # Negative for minimization

# Find leader's optimal quantity
result = minimize_scalar(leader_profit, bounds=(0, a-c), method='bounded')
q_L_optimal = result.x
q_F_optimal = follower_response(q_L_optimal)

print(f"Leader quantity: {q_L_optimal:.2f}")
print(f"Follower quantity: {q_F_optimal:.2f}")
print(f"Market price: {a - q_L_optimal - q_F_optimal:.2f}")
print(f"Leader profit: {-result.fun:.2f}")
```

## 重复博弈

当博弈重复进行时，通过声誉和惩罚机制出现新的均衡。无名氏定理表明，当参与者足够有耐心时，许多结果都可以作为均衡来维持。

关键机制是如果有人偏离合作路径，就会威胁恢复到非合作博弈。这需要：

1. 参与者重视未来收益（贴现因子 $\delta < 1$）
2. 偏离是可观察的
3. 惩罚威胁是可信的

### 触发策略

一个常见的执行机制是冷酷策略：合作直到有人背叛，然后永远背叛。当以下条件满足时，这种策略可以维持合作：

$$
\frac{1}{1-\delta} \cdot \pi_{\text{coop}} \geq \pi_{\text{deviate}} + \frac{\delta}{1-\delta} \cdot \pi_{\text{punish}}
$$

左边是永久合作的收益，右边是偏离的收益加上永久惩罚的收益。

## 练习

1. **计算均衡**：找出以下博弈的所有纳什均衡（纯策略和混合策略）：
   
   |           | 左    | 右    |
   |-----------|-------|-------|
   | **上**    | (3,2) | (1,3) |
   | **下**    | (0,1) | (2,4) |

2. **重复博弈**：计算在使用冷酷策略的无限重复囚徒困境中维持合作所需的最小贴现因子。

3. **序贯博弈**：求解一个三阶段进入博弈的子博弈完美均衡，其中企业按顺序决定是否进入市场。

4. **混合策略**：验证您为练习 1 计算的混合策略均衡使两个参与者在其纯策略之间无差异。