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
  title: 经济学导论
  headings:
    Supply and Demand: 供给与需求
    Economic Models: 经济模型
    Economic Models::Calibration in Practice: 实践中的校准
---

# 经济学导论

本文档提供了经济学原理的基本介绍。我们将探讨构成经济分析基础的基本概念。

## 供给与需求

供给和需求是经济学中最基本的概念。供给曲线显示生产者愿意以不同价格出售多少商品，而需求曲线显示消费者愿意购买多少商品。

当市场处于均衡状态时，供给量等于需求量。这个均衡价格平衡了买家和卖家的利益。

## 经济模型

经济模型是经济过程的简化表示。它们通过关注最重要的关系来帮助经济学家理解复杂系统。

模型做出假设以简化现实。虽然没有模型是完美的，但好的模型可以提供关于经济如何运作的宝贵见解。

模型的**校准**是指选择一组参数值，使模型的预测与观测数据相吻合。校准不是估计：它通过匹配少数几个目标矩来确定参数，而不是通过最大化似然函数。诸如 McCall 模型这样的搜寻模型通常就是这样校准的。统计学背景可参阅 [维基百科的校准条目](https://en.wikipedia.org/wiki/Calibration_(statistics))。

```{todo}
Add a worked calibration example once the data appendix is finalised.
```

(sec:calibration)=
### 实践中的校准

在实践中，建模者会选取一个接近$0.95$的贴现因子 $\beta$，然后检查由此隐含的资本产出比是否合理。

```{code-cell} python
# 一行式校准检查
beta = 0.95
print(f"annual discount rate: {1 / beta - 1:.2%}")
```
