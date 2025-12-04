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
  Linear Algebra Foundations: 线性代数基础
  Vector Spaces: 向量空间
  Vector Spaces::Basic Properties: 基本性质
  Matrix Operations: 矩阵运算
  Matrix Operations::Eigenvalues and Eigenvectors: 特征值和特征向量
---

# 线性代数基础

本讲座介绍了对定量经济学和数据科学至关重要的线性代数基本概念。我们将探讨向量空间、矩阵、特征值及其在经济问题中的应用。

## 向量空间

向量空间是称为向量的对象的集合，这些对象可以相加并与标量相乘。理解向量空间对现代经济分析和机器学习应用至关重要。

数学上，向量 $\mathbf{v} \in \mathbb{R}^n$ 可以表示为：

$$
\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix}
$$

让我们用 Python 创建并可视化一些向量：

```{code-cell} python
import numpy as np
import matplotlib.pyplot as plt

# 创建两个向量
v1 = np.array([2, 3])
v2 = np.array([1, 4])

# 可视化向量
fig, ax = plt.subplots(figsize=(8, 6))
ax.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='blue', label='v1')
ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='red', label='v2')
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 5)
ax.set_xlabel('x轴')
ax.set_ylabel('y轴')
ax.set_title('二维空间中的向量表示')
ax.legend()
ax.grid(True)
plt.show()
```

### 基本性质

向量空间满足几个关键性质：
- 加法和标量乘法下的封闭性
- 加法单位元（零向量）的存在
- 加法逆元的存在

这些性质确保向量空间在数学运算下表现可预测。

## 矩阵运算

矩阵是表示线性变换的数字矩形数组。它们是经济建模、数据分析和优化问题的基本工具。

一般的 $m \times n$ 矩阵具有以下形式：

$$
A = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}
$$

### 特征值和特征向量

特征值和特征向量揭示了线性变换的重要结构性质。对于方阵 $A$，特征向量 $\mathbf{v}$ 及其对应的特征值 $\lambda$ 满足：

$$
A\mathbf{v} = \lambda \mathbf{v}
$$

这些概念对于理解动态系统、稳定性分析以及降维技术（如 PCA）至关重要。
