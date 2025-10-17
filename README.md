# 测试翻译同步（目标）

**⚠️ 测试仓库 - 不用于生产环境**

此仓库用于测试 `quantecon/action-translation-sync` GitHub 操作。

## 目的

翻译同步操作开发和验证的测试平台。

## 结构

- `lectures/` - MyST Markdown 格式的测试讲座内容
  - `intro.md` - 基本概念与数学和代码
  - `advanced.md` - 动态规划等高级主题
  - `_toc.yml` - 目录
- `.github/workflows/` - 翻译同步工作流

## 源仓库

翻译从以下仓库同步：[`quantecon/test-translation-sync`](https://github.com/quantecon/test-translation-sync)

## 工作流程

1. 源仓库发生更改
2. 创建并合并拉取请求
3. 操作自动运行
4. 在此仓库中检查翻译PR

## 测试

有关测试指南，请参阅 [action-translation-sync 文档](https://github.com/quantecon/action-translation-sync/blob/main/docs/TEST-REPOSITORIES.md)。
