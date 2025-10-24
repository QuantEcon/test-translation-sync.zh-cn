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
  Vector Spaces: 向量空间
  Basic Properties: 基本性质
  Eigenvalues and Eigenvectors: 特征值和特征向量
---

# 线性代数基础

本讲座介绍了对数量经济学至关重要的线性代数基本概念。我们将探讨向量空间、矩阵及其在经济问题中的应用。

## 向量空间

向量空间是由称为向量的对象组成的集合,这些对象可以相加并与标量相乘。理解向量空间对于现代经济分析至关重要。

从数学上讲,向量 $\mathbf{v} \in \mathbb{R}^n$ 可以表示为:

$$
\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix}
$$

让我们在Python中创建并可视化一些向量:

```{code-cell} python
import numpy as np
import matplotlib.pyplot as plt

# Create two vectors
v1 = np.array([2, 3])
v2 = np.array([1, 4])

# Visualize vectors
fig, ax = plt.subplots(figsize=(8, 6))
ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='blue', label='v1')
ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='red', label='v2')
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 5)
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_title('Vector Representation in 2D Space')
ax.legend()
ax.grid(True)
plt.show()
```

### 基本性质

向量空间满足几个关键性质:
- 在加法和标量乘法下的封闭性
- 加法单位元(零向量)的存在性
- 加法逆元的存在性

这些性质确保向量空间在数学运算下表现可预测。

两个向量 $\mathbf{u}$ 和 $\mathbf{v}$ 的和按分量定义为:

```{math}
\mathbf{u} + \mathbf{v} = \begin{bmatrix} u_1 + v_1 \\ u_2 + v_2 \\ \vdots \\ u_n + v_n \end{bmatrix}
```

## 特征值和特征向量

特征值和特征向量揭示了线性变换的重要性质。矩阵 $A$ 的特征向量 $v$ 满足:

```{math}
:label: eigenvalue-equation
Av = \lambda v
```

其中 $\lambda$ 是特征值。这个基本方程在整个经济学中都有出现,从增长理论到稳定性分析。

对于 $n \times n$ 矩阵 $A$,特征多项式为:

$$
\det(A - \lambda I) = 0
$$

求解此方程得到特征值。让我们计算一个转移矩阵的特征值:

```{code-cell} python
# Create a transition matrix for a simple Markov chain
# States: Employed, Unemployed
transition_matrix = np.array([
    [0.95, 0.05],  # Employed -> (Employed, Unemployed)
    [0.20, 0.80]   # Unemployed -> (Employed, Unemployed)
])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(transition_matrix)

print("Transition Matrix:")
print(transition_matrix)
print("\nEigenvalues:")
print(np.round(eigenvalues, 4))
print("\nEigenvectors:")
print(np.round(eigenvectors, 4))

# The eigenvector corresponding to eigenvalue 1 gives steady-state distribution
steady_state_index = np.argmax(eigenvalues)
steady_state = eigenvectors[:, steady_state_index]
steady_state = steady_state / steady_state.sum()  # Normalize

print("\nSteady-State Distribution:")
print(f"Employed: {steady_state[0]:.2%}")
print(f"Unemployed: {steady_state[1]:.2%}")
```

这些概念对于分析动态经济系统(如增长模型和稳定性分析)至关重要。

幂迭代法可用于找到主特征值:

$$
\lambda_1 = \lim_{k \to \infty} \frac{\|A^k \mathbf{v}_0\|}{\|A^{k-1} \mathbf{v}_0\|}
$$
