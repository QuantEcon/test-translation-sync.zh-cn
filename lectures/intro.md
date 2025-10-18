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
  Basic Concepts: 基本概念
  Key Terms: 关键术语
  Economic Systems: 经济体制
  Mathematical Framework: 数学框架
  Returns to Scale: 规模报酬
  Python Implementation: Python 实现
  Economic Applications: 经济应用
  Labor Market Analysis: 劳动力市场分析
  Capital Accumulation: 资本积累
  MyST Directives: MyST 指令
  Empirical Evidence: 经验证据
  Data Sources: 数据来源
  Summary: 总结
  References: 参考文献
---

# 经济学导论

这是一个用于测试翻译同步操作的综合讲座,演示了各种类型的变化。

## 基本概念

经济学是研究社会如何在竞争性用途之间配置稀缺资源的学科。它考察约束条件下的决策制定。

### 关键术语

- **稀缺性**:相对于无限欲望而言资源有限
- **机会成本**:放弃的次优选择的价值
- **供给与需求**:决定价格和数量的市场力量
- **边际分析**:考察成本和收益的增量变化

### 经济体制

不同社会以各种方式组织经济活动:
- 市场经济依赖价格信号
- 计划经济使用中央协调
- 混合经济结合两种方法

## 数学框架

生产函数表示投入与产出之间的关系:

$$
Y = A K^{\alpha} L^{1-\alpha}
$$

其中:
- $Y$ 是总产出
- $K$ 是资本存量
- $L$ 是劳动投入
- $A$ 是全要素生产率
- $\alpha \in (0,1)$ 是资本份额参数

### 规模报酬

科布-道格拉斯生产函数表现出规模报酬不变:

$$
F(\lambda K, \lambda L) = \lambda F(K, L)
$$

对于任意 $\lambda > 0$。

## Python 实现

这里是一个带有额外功能的改进实现:

```python
import numpy as np

def calculate_gdp(capital, labor, productivity=1.0, alpha=0.3):
    """
    Calculate GDP using Cobb-Douglas production function
    
    Parameters:
    -----------
    capital : float
        Capital stock (K)
    labor : float
        Labor force (L)
    productivity : float
        Total factor productivity (A), default: 1.0
    alpha : float
        Capital share parameter, default: 0.3
        
    Returns:
    --------
    float : Calculated GDP (Y)
    
    Examples:
    ---------
    >>> calculate_gdp(100, 50)
    31.62
    """
    if capital < 0 or labor < 0:
        raise ValueError("Inputs must be non-negative")
    
    return productivity * (capital ** alpha) * (labor ** (1 - alpha))

def marginal_product_capital(capital, labor, productivity=1.0, alpha=0.3):
    """Calculate marginal product of capital"""
    return alpha * productivity * (capital ** (alpha - 1)) * (labor ** (1 - alpha))

# Example usage with multiple scenarios
scenarios = [
    {'capital': 100, 'labor': 50},
    {'capital': 150, 'labor': 75},
    {'capital': 200, 'labor': 100}
]

for i, scenario in enumerate(scenarios, 1):
    gdp = calculate_gdp(**scenario)
    mpk = marginal_product_capital(**scenario)
    print(f"Scenario {i}: GDP = {gdp:.2f}, MPK = {mpk:.4f}")
```

## 经济应用

让我们探讨这些概念的一些实际应用。

### 劳动力市场分析

劳动力市场均衡发生在劳动力供给等于劳动力需求的地方。工资调整以实现市场出清。

### 资本积累

资本积累遵循运动规律：

$$
K_{t+1} = I_t + (1-\delta)K_t
$$

其中 $I_t$ 是投资，$\delta$ 是折旧率。

## MyST 指令

```{note}
这是关于经济理论及其在实际政策中应用的重要说明。
```

```{warning}
在经济模型中要小心假设!始终检查稳健性。
```

{tip}
在得出政策结论之前,始终根据真实数据验证模型的预测。
```

```{admonition} 关键见解
总生产函数框架是理解经济增长和发展的基础。
```

## 经验证据

最近的经验研究表明,全要素生产率占跨国收入差异的很大一部分。

### 数据来源

经验分析的常见数据来源包括:
- Penn World Tables
- World Bank Development Indicators
- OECD National Accounts

## 总结

本讲座涵盖了：
1. 基本经济概念和术语
2. 数学生产函数及其性质
3. 经济分析的计算方法
4. 劳动和资本市场的实际应用
5. 经验证据和数据来源

## 参考文献

- Smith, Adam. "The Wealth of Nations" (1776)
- Keynes, John Maynard. "The General Theory of Employment, Interest and Money" (1936)
- Solow, Robert M. "A Contribution to the Theory of Economic Growth" (1956)
- Romer, David. "Advanced Macroeconomics" (4th ed., 2019)
- Acemoglu, Daron and Robinson, James. "Why Nations Fail" (2012)
