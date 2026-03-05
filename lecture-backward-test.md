---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
heading-map:
  Solow Growth Model: 索洛增长模型
  The Production Function: 生产函数
  Capital Accumulation: 资本积累
  Steady State: 稳态
  Convergence Dynamics: 收敛动态
---

# 索洛增长模型

索洛增长模型是宏观经济学中最重要的模型之一。它通过资本积累、劳动力增长和技术进步来解释长期经济增长。

## 生产函数

经济体使用生产函数来生产产出：

$$
Y = K^\alpha L^{1-\alpha}
$$

其中 $Y$ 是产出，$K$ 是资本，$L$ 是劳动力，$\alpha$ 是资本份额（通常在 $0 < \alpha < 1$ 范围内，实证估计约为 $\alpha \approx 0.3$）。

## 资本积累

资本随时间的演化方程为：

$$
K_{t+1} = sY_t + (1-\delta)K_t
$$

其中 $s$ 是储蓄率，$\delta$ 是折旧率。

在人均分析中，令 $k = K/L$，人均资本的运动方程为：

$$
k_{t+1} = \frac{s k_t^\alpha + (1-\delta)k_t}{1+n}
$$

其中 $n$ 是人口增长率。模型预测经济体会收敛到一个人均资本恒定的稳态。

## 稳态

在稳态中，人均产出为：

$$
y^* = \left(\frac{s}{n + \delta}\right)^{\frac{\alpha}{1-\alpha}}
$$

注意分母包含人口增长率 $n$。这意味着更高的储蓄率会提高稳态人均产出，而更高的人口增长率会降低稳态人均产出。

```{code-cell} python3
import numpy as np
import matplotlib.pyplot as plt

# Parameters
alpha = 0.3
s = 0.2
delta = 0.05
n = 0.02

# Corrected steady state (includes population growth)
k_star = (s / (n + delta)) ** (1 / (1 - alpha))
y_star = k_star ** alpha

print(f"Steady state capital per worker: {k_star:.2f}")
print(f"Steady state output per worker: {y_star:.2f}")

# Comparative statics: effect of savings rate
s_values = np.linspace(0.05, 0.5, 50)
y_star_values = (s_values / (n + delta)) ** (alpha / (1 - alpha))

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(s_values, y_star_values, 'b-', linewidth=2)
ax.set_xlabel('Savings rate (s)', fontsize=12)
ax.set_ylabel('Steady-state output per worker (y*)', fontsize=12)
ax.set_title('Effect of Savings Rate on Steady-State Output', fontsize=14)
ax.axvline(x=s, color='r', linestyle='--', label=f's = {s}')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

## 收敛动态

处于稳态以下的经济体增长速度快于处于稳态以上的经济体。对于资本份额 $\alpha < 1$，人均资本的增长率可以表示为：

$$
\frac{k_{t+1} - k_t}{k_t} \approx (1-\alpha)(n+\delta)\left(\frac{k^*}{k_t} - 1\right)
$$

收敛速度约为 $(1-\alpha)(n+\delta)$，当 $\alpha = 0.3$、$n = 0.02$、$\delta = 0.05$ 时，收敛速度约为每年 4.9%。这意味着经济体每年弥合约 4.9% 的产出差距，这与跨国实证数据中约 2% 的条件收敛率进行了有趣的对比。
