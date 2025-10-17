---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
---

# 高级经济理论

本讲座涵盖经济理论中更高级的主题。

## 动态规划

值迭代的贝尔曼方程：

$$
V(s) = \max_{a \in A(s)} \left\{ r(s,a) + \beta \sum_{s' \in S} P(s'|s,a) V(s') \right\}
$$

其中：
- $V(s)$ 是值函数
- $s$ 是当前状态
- $a$ 是行动
- $r(s,a)$ 是奖励函数
- $\beta$ 是折现因子
- $P(s'|s,a)$ 是转移概率

## 实现

```python
import numpy as np

def value_iteration(reward, transition, beta=0.95, tol=1e-6, max_iter=1000):
    """
    使用值迭代求解动态规划问题
    
    参数：
    -----------
    reward : ndarray
        奖励矩阵 (n_states x n_actions)
    transition : ndarray  
        转移概率矩阵 (n_states x n_actions x n_states)
    beta : float
        折现因子（默认：0.95）
    tol : float
        收敛容忍度（默认：1e-6）
    max_iter : int
        最大迭代次数（默认：1000）
        
    返回：
    --------
    V : ndarray
        最优值函数
    policy : ndarray
        最优策略
    """
    n_states, n_actions = reward.shape
    V = np.zeros(n_states)
    
    for iteration in range(max_iter):
        V_new = np.zeros(n_states)
        
        for s in range(n_states):
            q_values = reward[s] + beta * np.dot(transition[s], V)
            V_new[s] = np.max(q_values)
        
        if np.max(np.abs(V_new - V)) < tol:
            print(f"在 {iteration} 次迭代后收敛")
            break
            
        V = V_new
    
    # 提取最优策略
    policy = np.zeros(n_states, dtype=int)
    for s in range(n_states):
        q_values = reward[s] + beta * np.dot(transition[s], V)
        policy[s] = np.argmax(q_values)
    
    return V, policy
```

## 应用

动态规划是以下领域的基础：

1. **最优增长模型** - 确定最优储蓄和消费
2. **工作搜索理论** - 寻找最优保留工资
3. **资产定价** - 评估金融工具价值
4. **库存管理** - 优化库存水平

```{admonition} 关键见解
:class: important

动态规划将复杂的序列决策问题分解为更简单的子问题。
这种"最优性原理"是使DP如此强大的原因。
```

## 计算考虑

```{note}
值迭代以速率 $\beta$ 几何收敛。可以通过以下方法实现更快的收敛：
- 策略迭代
- 修改策略迭代
- 线性规划方法
```
