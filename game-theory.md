---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
translation:
  title: 博弈论基础
  headings:
    Introduction to Strategic Thinking: 策略思维导论
    The Prisoner's Dilemma: 囚徒困境
    The Prisoner's Dilemma::Real-World Applications: 现实世界的应用
    Nash Equilibrium: 纳什均衡
    Nash Equilibrium::Mixed Strategies: 混合策略
    Sequential Games: 序贯博弈
    Sequential Games::Stackelberg Competition: 斯塔克尔伯格竞争
    Repeated Games: 重复博弈
    Repeated Games::Trigger Strategies: 触发策略
    Exercises: 练习
---

# 博弈论基础

本讲座介绍博弈论的基本概念及其在经济决策中的应用。我们将探讨策略互动、纳什均衡以及常见的博弈结构。

## 策略思维导论

博弈论提供了一个分析多个决策者进行策略互动情境的框架。每个参与者的最优选择都取决于其他人的选择，从而产生复杂的相互依存关系。

在经济市场中，就价格或数量展开竞争的企业进行的是策略博弈。理解这些互动有助于预测市场结果并设计更好的机制。

## 囚徒困境

经典的囚徒困境说明了为何理性个体即使在合作对所有人都有利的情况下也可能不选择合作。两名嫌疑人被分开审讯，各自必须决定是坦白还是保持沉默。

收益矩阵刻画了这一策略结构：

|                | 合作         | 背叛        |
|----------------|-------------|-------------|
| **合作**       | (-1, -1)    | (-3, 0)     |
| **背叛**       | (0, -3)     | (-2, -2)    |

每个参与者都有一个占优策略，即背叛，这导致了对双方而言均非最优的结果。

### 现实世界的应用

囚徒困境的结构出现在许多经济情境中：
- 企业间的价格竞争
- 公共产品的提供
- 环境保护协议
- 军备竞赛与军事支出

理解这一博弈有助于解释市场失灵以及监管或合作机制的必要性。

## 纳什均衡

纳什均衡是一种策略组合，在该组合下没有任何参与者能通过单方面改变策略来提高自己的收益。它代表了一种稳定的结果，即在给定他人策略的情况下，每个参与者的策略都是最优的。

用数学语言表述，对于参与者 $i = 1, \ldots, n$，其策略集合为 $S_i$，收益函数为 $u_i$，策略组合 $(s_1^*, \ldots, s_n^*)$ 是纳什均衡，当且仅当：

$$
u_i(s_i^*, s_{-i}^*) \geq u_i(s_i, s_{-i}^*) \quad \forall s_i \in S_i, \forall i
$$

让我们用 Python 来计算一个简单博弈的纳什均衡：

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

当不存在纯策略纳什均衡时，参与者可能会在策略上进行随机化。这类混合策略均衡要求满足使参与者愿意随机化的无差异条件。

混合策略均衡的概率可以通过求解以下方程来计算：

```{math}
\begin{align}
p \cdot u_1(\text{Strategy 1}) &= p \cdot u_1(\text{Strategy 2}) \\
q \cdot u_2(\text{Strategy 1}) &= q \cdot u_2(\text{Strategy 2})
\end{align}
```

## 序贯博弈

在序贯博弈中，参与者按特定顺序行动，并观察之前的行动。这类博弈通过逆向归纳法进行分析，即从博弈树的末端反推到开端。

其中的关键洞见是子博弈完美性：在每个决策节点上，参与者都会基于未来的博弈进程做出最优选择。这就排除了理性参与者不会真正执行的不可置信威胁。

### 斯塔克尔伯格竞争

一个经典应用是斯塔克尔伯格竞争，其中一家企业（领导者）先选择产量，另一家企业（跟随者）在观察到该选择后再做决策。

领导者会预见到跟随者的反应函数，并据此做出最优选择：

$$
\max_{q_L} \pi_L(q_L, R(q_L))
$$

其中 $R(q_L)$ 是跟随者对领导者产量 $q_L$ 的最优反应。

让我们通过数值方法求解一个斯塔克尔伯格博弈：

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

当博弈被反复进行时，通过声誉和惩罚机制会涌现出新的均衡。无名氏定理表明，当参与者足够有耐心时，许多结果都可以作为均衡得以维持。

其中的关键机制是：一旦有人偏离合作路径，就会威胁重新回到非合作博弈状态。这需要满足：

1. 参与者重视未来的收益（贴现因子 $\delta < 1$）
2. 偏离行为是可观察的
3. 惩罚威胁是可置信的

### 触发策略

一种常见的执行机制是冷酷策略：合作直到有人背叛，此后便永远背叛。当满足以下条件时，该策略可以维持合作：

$$
\frac{1}{1-\delta} \cdot \pi_{\text{coop}} \geq \pi_{\text{deviate}} + \frac{\delta}{1-\delta} \cdot \pi_{\text{punish}}
$$

左边是永久合作所带来的收益，而右边则是先偏离一次、随后遭受永久惩罚所带来的收益。

## 练习

1. **计算均衡**：请找出以下博弈的所有纳什均衡（纯策略与混合策略）：

   |           | 左     | 右    |
   |-----------|-------|-------|
   | **上**    | (3,2) | (1,3) |
   | **下**    | (0,1) | (2,4) |

2. **重复博弈**：计算在无限重复的囚徒困境中，使用冷酷策略维持合作所需的最小贴现因子。

3. **序贯博弈**：求解一个三阶段进入博弈的子博弈完美均衡，在该博弈中，各企业依次决定是否进入某一市场。

4. **混合策略**：验证你在练习 1 中计算出的混合策略均衡确实使双方参与者对自己的纯策略感到无差异。