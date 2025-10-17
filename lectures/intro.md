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

# 经济学导论

这是一个用于测试翻译同步操作的讲座。

## 基本概念

经济学是研究社会如何配置稀缺资源的学科。

## 经济模型

经济模型是经济过程的简化表示。它们通过关注关键关系来帮助我们理解复杂系统。

我们使用理论和经验方法来构建和检验这些模型。

## 数学示例

生产函数：

$$
Y = A K^{\alpha} L^{1-\alpha}
$$

其中：
- $Y$ 是产出
- $K$ 是资本
- $L$ 是劳动力
- $A$ 是全要素生产率

## 代码示例

```python
def calculate_gdp(capital, labor, productivity=1.0, alpha=0.3):
    """
    使用柯布-道格拉斯生产函数计算GDP
    
    参数：
    -----------
    capital : float
        资本存量
    labor : float
        劳动力
    productivity : float
        全要素生产率（默认：1.0）
    alpha : float
        资本份额（默认：0.3）
        
    返回：
    --------
    float : 计算的GDP
    """
    return productivity * (capital ** alpha) * (labor ** (1 - alpha))

# 使用示例
gdp = calculate_gdp(capital=100, labor=50)
print(f"GDP: {gdp:.2f}")
```

## MyST 指令

```{note}
这是关于经济理论的重要说明。
```

```{warning}
小心经济模型中的假设！
```

```{tip}
始终根据实际数据验证模型的预测。
```

## 总结

本讲座涵盖：
1. 基本经济概念
2. 生产函数
3. 计算方法

## 参考文献

- Smith, Adam. "The Wealth of Nations" (1776)
- Keynes, John Maynard. "The General Theory of Employment, Interest and Money" (1936)
- Solow, Robert M. "A Contribution to the Theory of Economic Growth" (1956)
