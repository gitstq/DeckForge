# 🃏 DeckForge - 轻量级AI驱动PPT智能生成CLI引擎

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-orange.svg)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg)]()

> ⚡ 在终端中将任何内容转化为专业、原生可编辑的PowerPoint演示文稿——无需AI IDE。

**简体中文** | **[繁體中文](README_zh_TW.md)** | **[English](README.md)**

---

## 🎉 项目介绍

**DeckForge** 是一款轻量级CLI引擎，利用大语言模型（LLM）直接在终端中生成专业、原生可编辑的 `.pptx` 文件。与其他需要Claude Code或Cursor等AI IDE的演示文稿工具不同，DeckForge作为**独立的命令行工具**运行——只需提供内容，即可获得精美的演示文稿。

### 💡 灵感来源

受GitHub上AI驱动演示文稿工具热潮的启发，DeckForge诞生于对**零依赖、无需IDE**解决方案的需求。大多数现有工具将你锁定在特定的AI IDE或云平台上。DeckForge打破了这些限制——纯CLI，纯自由。

### 🌟 差异化亮点

| 特性 | DeckForge | 其他工具 |
|------|-----------|----------|
| 🖥️ 需要AI IDE | ❌ 不需要 | ✅ 需要（Claude Code、Cursor等） |
| ⌨️ 独立CLI | ✅ 支持 | ❌ 不支持 |
| 🤖 多LLM后端 | ✅ OpenAI、Claude、DeepSeek、Ollama | 有限 |
| 📦 核心依赖 | **1个**（python-pptx） | 很多 |
| 🎨 内置主题 | ✅ **11款专业主题** | 仅外部 |
| 🔒 离线模式 | ✅ 纯模板模式 | ❌ 不支持 |
| 🌍 多语言 | ✅ 内容自动检测 | 有限 |
| 💰 费用 | 免费开源 | 通常付费 |

---

## ✨ 核心特性

- 🚀 **一键生成** — 单条CLI命令即可生成演示文稿
- 🤖 **多LLM后端** — 支持OpenAI、Claude、DeepSeek和Ollama（本地）
- 🎨 **11款内置主题** — 现代、暗黑、学术、极简、海洋、自然、日落、科技、商务、创意、翡翠
- 📝 **智能内容解析** — 自动将Markdown和纯文本解析为幻灯片结构
- 🔧 **纯模板模式** — 无需任何API密钥即可生成精美演示文稿（`--no-ai`）
- 📊 **原生PPTX输出** — 真实的PowerPoint形状、文本框和布局（非图片）
- 🌐 **多语言支持** — 自动检测内容语言，支持中/英/日/韩等
- 🧩 **模块化架构** — 可插拔的解析器、渲染器和LLM后端
- 🧪 **充分测试** — 25+单元测试覆盖所有核心模块
- 📦 **零核心依赖** — 仅需 `python-pptx` 作为运行时依赖

---

## 🚀 快速开始

### 📋 环境要求

- **Python 3.10+** — 唯一必需条件
- **python-pptx** — 通过requirements.txt自动安装

### 🔧 安装

```bash
# 克隆仓库
git clone https://github.com/gitstq/DeckForge.git
cd DeckForge

# 安装依赖
pip install -r requirements.txt

# 或安装为CLI工具
pip install -e .
```

### ⚡ 基本用法

```bash
# 从内联文本生成
deckforge create --input "机器学习入门" --output slides.pptx

# 从Markdown文件生成
deckforge create --input content.md --output presentation.pptx

# 使用指定主题生成
deckforge create --input content.md --theme dark --output dark_slides.pptx

# 无AI模式生成（纯模板模式）
deckforge create --input content.md --no-ai --output template.pptx

# 列出所有可用主题
deckforge themes

# 显示详细主题信息
deckforge themes --detail

# 查看环境和API密钥状态
deckforge info
```

### 🔑 LLM配置

```bash
# 设置你偏好的LLM API密钥
export OPENAI_API_KEY="sk-your-key-here"
# 或
export ANTHROPIC_API_KEY="sk-ant-your-key-here"
# 或
export DEEPSEEK_API_KEY="sk-your-key-here"

# 对于Ollama（本地），确保它正在运行：
ollama serve
```

---

## 📖 详细使用指南

### 🎨 主题一览

DeckForge内置11款专业设计主题：

| 主题 | 风格 | 适用场景 |
|------|------|----------|
| 🃏 `modern` | 简洁蓝色调 | 通用场景 |
| 🌙 `dark` | 优雅暗色背景 | 技术演示 |
| 🎓 `academic` | 正式衬线字体 | 学术研究 |
| ⬜ `minimal` | 极致留白 | 设计导向 |
| 🌊 `ocean` | 深海蓝色调 | 科技创业 |
| 🌿 `nature` | 温暖大地色调 | 环保健康 |
| 🌅 `sunset` | 暖色渐变 | 创意展示 |
| 💻 `tech` | 未来科技感 | 创业路演 |
| 💼 `business` | 商务专业风 | 商务会议 |
| 🎨 `creative` | 大胆艺术色 | 创意作品集 |
| 💚 `emerald` | 翡翠绿色调 | 高端活动 |

### 📝 输入格式

#### Markdown输入（推荐）

```markdown
# 演示文稿标题

## 简介

这里是简介内容。

## 核心特性

- 特性一，支持**粗体文本**
- 特性二，支持*斜体文本*
- 特性三

## 代码示例

\`\`\`python
def hello():
    print("你好，世界！")
\`\`\`
```

#### 纯文本输入

```
机器学习概述

机器学习正在改变全球各行各业。

主要应用包括：
- 自然语言处理
- 计算机视觉
- 自动驾驶
```

### 🤖 LLM增强功能

配置LLM后端后，DeckForge会自动增强你的内容：

1. **标题优化** — 使标题更具吸引力和针对性
2. **要点精炼** — 提升要点的简洁性和影响力
3. **演讲备注** — 为每张幻灯片生成有用的备注
4. **流程优化** — 确保幻灯片之间的逻辑连贯性

### ⌨️ CLI参考

```
deckforge create [选项]

选项:
  -i, --input TEXT     输入内容：文本字符串或文件路径  [必需]
  -o, --output TEXT    输出PPTX文件路径  [默认: output.pptx]
  -t, --theme TEXT     主题名称  [默认: modern]
  --llm TEXT           LLM后端: openai|claude|deepseek|ollama|none  [默认: openai]
  --model TEXT         指定模型名称覆盖
  --slides INTEGER     目标幻灯片数量
  --lang TEXT          语言: en|zh|ja|ko|auto  [默认: auto]
  --title TEXT         自定义演示文稿标题
  --no-ai             无LLM生成（纯模板模式）
```

---

## 💡 设计思路与迭代规划

### 🎯 设计理念

1. **简洁优先** — 一条命令生成，零配置需求
2. **无锁定** — 无AI IDE依赖，无云平台锁定
3. **模块化架构** — 每个组件都可插拔和替换
4. **离线可用** — 纯模板模式无需任何API
5. **原生输出** — 真实的PowerPoint元素，非扁平化图片

### 🗺️ 迭代规划

- [ ] **v1.1** — 模板自定义（自定义颜色、字体、布局）
- [ ] **v1.2** — 图片插入支持（本地文件和AI生成）
- [ ] **v1.3** — 图表生成（柱状图、饼图、折线图）
- [ ] **v1.4** — 交互式幻灯片过渡和动画
- [ ] **v2.0** — Web UI可视化编辑
- [ ] **v2.1** — 插件系统，支持社区主题和渲染器

---

## 📦 打包与部署指南

### 从源码安装

```bash
git clone https://github.com/gitstq/DeckForge.git
cd DeckForge
pip install -r requirements.txt
```

### 作为Python包安装

```bash
pip install git+https://github.com/gitstq/DeckForge.git
```

### 开发模式

```bash
git clone https://github.com/gitstq/DeckForge.git
cd DeckForge
pip install -e ".[dev]"
pytest  # 运行测试
```

### 🖥️ 兼容环境

| 平台 | Python 3.10 | Python 3.11 | Python 3.12 | Python 3.13 |
|------|:-----------:|:-----------:|:-----------:|:-----------:|
| 🪟 Windows | ✅ | ✅ | ✅ | ✅ |
| 🍎 macOS | ✅ | ✅ | ✅ | ✅ |
| 🐧 Linux | ✅ | ✅ | ✅ | ✅ |

---

## 🤝 贡献指南

欢迎贡献！请遵循以下指南：

1. 🍴 Fork本仓库
2. 🌿 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 💾 提交更改 (`git commit -m 'feat: 添加新功能'`)
4. 📤 推送分支 (`git push origin feature/amazing-feature`)
5. 🎉 发起Pull Request

### 提交规范

我们遵循 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

- `feat:` 新功能
- `fix:` Bug修复
- `docs:` 文档更新
- `refactor:` 代码重构
- `test:` 测试添加/更新
- `chore:` 维护任务

---

## 📄 开源协议

本项目基于 **MIT协议** 开源——详见 [LICENSE](LICENSE) 文件。

---

<p align="center">
  由 DeckForge Team 用 ❤️ 打造<br>
  <sub>一条命令，将你的想法变为演示文稿。</sub>
</p>
