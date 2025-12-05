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
  Programming for Economics: 编程与经济学
  Using `numpy` Arrays: 使用 `numpy` 数组
  Using `numpy` Arrays::Creating Arrays with `np.arange()` and `np.linspace()`: 使用 `np.arange()` 和 `np.linspace()` 创建数组
  Working with **Pandas DataFrames**: 使用 **Pandas DataFrames**
  'Working with **Pandas DataFrames**::Reading Data: `pd.read_csv()` vs `pd.read_excel()`': 读取数据：`pd.read_csv()` 与 `pd.read_excel()`
  '*Matplotlib* Visualization Basics': '*Matplotlib* 可视化基础'
  '*Matplotlib* Visualization Basics::The `plt.plot()` Function': '`plt.plot()` 函数'
  Using [QuantEcon](https://quantecon.org) Libraries: 使用 [QuantEcon](https://quantecon.org) 库
  Using [QuantEcon](https://quantecon.org) Libraries::Installing `quantecon` Package: 安装 `quantecon` 包
  'Special Cases: $\LaTeX$ in Headings': 特殊情况：标题中的 $\LaTeX$
  'Special Cases: $\LaTeX$ in Headings::The $\beta$-Coefficient in Regression': 回归中的 $\beta$-系数
  'Special Cases: $\LaTeX$ in Headings::Computing $\mathbb{E}[X]$ (Expected Values)': 计算 $\mathbb{E}[X]$（期望值）
  Questions & Answers: 问题与解答
  '"Edge Cases" and [Special] {Characters}': '"边界情况" 和 [特殊] {字符}'
  '"Edge Cases" and [Special] {Characters}::Using `matplotlib`''s `plt.subplot()` for Multiple Plots': 使用 `matplotlib` 的 `plt.subplot()` 创建多个图表
  Summary: 总结
---

# 编程与经济学

本讲座涵盖了现代经济分析所必需的编程概念和工具。

## 使用 `numpy` 数组

`numpy` 库为数值计算提供了高效的数组操作。数组是 Python 科学计算的基础。

NumPy 数组支持向量化操作，避免了缓慢的 Python 循环：

```python
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
result = arr ** 2  # Vectorized squaring
```

### 使用 `np.arange()` 和 `np.linspace()` 创建数组

不同的数组创建方法服务于不同的目的。`np.arange()` 函数创建具有指定步长的数组：

```python
x = np.arange(0, 10, 0.5)  # From 0 to 10, step 0.5
```

同时，`np.linspace()` 创建具有指定点数的数组：

```python
y = np.linspace(0, 1, 100)  # 100 points from 0 to 1
```

## 使用 **Pandas DataFrames**

**pandas** 库提供了强大的数据操作功能。DataFrames 是二维的带标签数据结构。

### 读取数据：`pd.read_csv()` 与 `pd.read_excel()`

不同的文件格式需要不同的读取函数：

- **CSV 文件**：使用 `pd.read_csv('data.csv')`
- **Excel 文件**：使用 `pd.read_excel('data.xlsx')`
- **JSON 文件**：使用 `pd.read_json('data.json')`

## *Matplotlib* 可视化基础

*Matplotlib* 是 Python 的基础绘图库。它提供了对图形外观的精细控制。

### `plt.plot()` 函数

基本的线图使用 `plt.plot(x, y)` 创建：

```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Simple Plot')
plt.show()
```

## 使用 [QuantEcon](https://quantecon.org) 库

[QuantEcon](https://quantecon.org) 项目提供了专门用于经济建模的工具。访问[文档](https://quanteconpy.readthedocs.io/)了解详情。

### 安装 `quantecon` 包

通过 pip 安装：

```bash
pip install quantecon
```

或使用 conda：

```bash
conda install -c conda-forge quantecon
```

## 特殊情况：标题中的 $\LaTeX$

数学符号以行内形式出现：$f(x) = x^2 + 2x + 1$。

### 回归中的 $\beta$-系数

回归系数 $\beta$ 衡量变量之间的关系：

$$
y = \alpha + \beta x + \epsilon
$$

### 计算 $\mathbb{E}[X]$（期望值）

期望值 $\mathbb{E}[X]$ 表示平均结果：

$$
\mathbb{E}[X] = \sum_{i} x_i P(X = x_i)
$$

## 问题与解答

关于Python在经济学中应用的常见问题：

- **问**：`numpy`和纯Python哪个更快？
- **答**：对于数值运算，`numpy`通常快10-100倍

- **问**：我可以用`pandas`处理大型数据集吗？
- **答**：可以，但对于超过内存大小的数据集请考虑使用`dask`

## "边界情况" 和 [特殊] {字符}

本节测试标题中的各种特殊字符。

### 使用 `matplotlib` 的 `plt.subplot()` 创建多个图表

subplot 函数在一个图形中创建多个图表：

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.plot(x, y1)
ax2.plot(x, y2)
```

## 总结

像 **numpy**、*pandas* 和 `matplotlib` 这样的编程工具对于现代经济学研究至关重要。掌握这些库以高效地分析数据和可视化结果。
