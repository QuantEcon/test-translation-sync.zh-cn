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
  Setup: 设置
  The Model: 模型
  Steady State: 稳态
  Numerical Example: 数值示例
  Comparative Statics: 比较静态
  Exercises: 练习
---

# 索洛增长模型

本讲座介绍[索洛增长模型](https://en.wikipedia.org/wiki/Solow%E2%80%93Swan_model)，这是宏观经济学中理解长期经济增长的基础模型之一。

我们将探讨资本积累、劳动力增长和技术进步如何决定人均产出的稳态水平。

## 设置

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager
fontP = font_manager.FontProperties()
fontP.set_family('SimHei')
fontP.set_size(14)
```

## 模型

考虑一个具有生产函数的经济体

$$
Y_t = A K_t^{\alpha} L_t^{1-\alpha}
$$

其中：

* $Y_t$ 是时间 $t$ 的总产出
* $K_t$ 是资本存量
* $L_t$ 是劳动力
* $A$ 是技术参数
* $\alpha \in (0,1)$ 是资本份额

资本积累方程为

$$
K_{t+1} = s Y_t + (1 - \delta) K_t
$$ (eq:capital-accum)

其中 $s \in (0,1)$ 是储蓄率，$\delta \in (0,1)$ 是折旧率。

## 稳态

定义 $k_t = K_t / L_t$ 为人均资本，我们可以证明稳态人均资本为

$$
k^* = \left(\frac{s A}{\delta + n}\right)^{\frac{1}{1-\alpha}}
$$ (eq:steady-state)

其中 $n$ 是人口增长率。

使稳态消费最大化的[黄金法则](https://en.wikipedia.org/wiki/Golden_Rule_savings_rate)储蓄率为 $s^* = \alpha$。

## 数值示例

让我们计算并绘制转移动态。

```{code-cell} ipython3
# 参数
A = 1.0      # 技术水平
α = 0.33     # 资本份额
s = 0.25     # 储蓄率
δ = 0.05     # 折旧率
n = 0.02     # 人口增长率
T = 100      # 时间期数

# 稳态
k_star = (s * A / (δ + n)) ** (1 / (1 - α))
y_star = A * k_star ** α
print(f"稳态 k* = {k_star:.4f}")
print(f"稳态 y* = {y_star:.4f}")
```

```{code-cell} ipython3
# 转移动态
k = np.zeros(T)
k[0] = 1.0  # 初始人均资本

for t in range(T - 1):
    k[t+1] = (s * A * k[t]**α + (1 - δ) * k[t]) / (1 + n)
```

```{code-cell} ipython3
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 人均资本
axes[0].plot(k, linewidth=2)
axes[0].axhline(k_star, color='r', linestyle='--', label='稳态 $k^*$')
axes[0].set_xlabel('时间', fontproperties=fontP)
axes[0].set_ylabel('人均资本 $k_t$', fontproperties=fontP)
axes[0].set_title('向稳态的过渡', fontproperties=fontP)
axes[0].legend(prop=fontP)

# 人均产出
y = A * k ** α
axes[1].plot(y, linewidth=2, color='green')
axes[1].axhline(y_star, color='r', linestyle='--', label='稳态 $y^*$')
axes[1].set_xlabel('时间', fontproperties=fontP)
axes[1].set_ylabel('人均产出 $y_t$', fontproperties=fontP)
axes[1].set_title('产出动态', fontproperties=fontP)
axes[1].legend(prop=fontP)

plt.tight_layout()
plt.show()
```

## 比较静态

我们可以研究储蓄率的变化如何影响稳态。

```{code-cell} ipython3
s_values = np.linspace(0.05, 0.50, 100)
k_stars = (s_values * A / (δ + n)) ** (1 / (1 - α))
y_stars = A * k_stars ** α
c_stars = (1 - s_values) * y_stars

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(s_values, c_stars, linewidth=2, label='消费 $c^*$')
ax.axvline(α, color='r', linestyle='--', label=f'黄金法则 $s^* = \\alpha = {α}$')
ax.set_xlabel('储蓄率 $s$', fontproperties=fontP)
ax.set_ylabel('稳态人均消费', fontproperties=fontP)
ax.set_title('资本积累的黄金法则', fontproperties=fontP)
ax.legend(prop=fontP)
plt.show()
```

## 练习

```{exercise}
:label: solow_ex_a
```

考虑两个经济体 A 和 B，参数如下：
- 经济体 A：$s = 0.20$，$\delta = 0.05$，$n = 0.01$，$\alpha = 0.33$
- 经济体 B：$s = 0.35$，$\delta = 0.08$，$n = 0.03$，$\alpha = 0.33$

1. 计算每个经济体的稳态人均资本和产出。
2. 哪个经济体有更高的稳态人均消费？
3. 从 $k_0 = 1$ 出发，绘制两个经济体的转移动态。

```{exercise-end}
```

```{solution-start} solow_ex_a
:class: dropdown
```

```{code-cell} ipython3
for name, params in [('A', (0.20, 0.05, 0.01)), ('B', (0.35, 0.08, 0.03))]:
    s_i, δ_i, n_i = params
    k_i = (s_i * A / (δ_i + n_i)) ** (1 / (1 - α))
    y_i = A * k_i ** α
    c_i = (1 - s_i) * y_i
    print(f"经济体 {name}: k* = {k_i:.4f}, y* = {y_i:.4f}, c* = {c_i:.4f}")
```

经济体 A 尽管储蓄率较低，但有更高的稳态人均消费。

```{solution-end}
```