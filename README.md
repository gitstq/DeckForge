# 🃏 DeckForge - Lightweight AI-Powered PPT Intelligent Generation CLI Engine

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-orange.svg)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg)]()

> ⚡ Transform any content into professional, natively editable PowerPoint presentations — entirely from your terminal. No AI IDE required.

**[简体中文](README_zh.md)** | **[繁體中文](README_zh_TW.md)** | **English**

---

## 🎉 About

**DeckForge** is a lightweight CLI engine that leverages Large Language Models (LLMs) to generate professional, natively editable `.pptx` files directly from your terminal. Unlike other AI presentation tools that require AI IDEs like Claude Code or Cursor, DeckForge works as a **standalone command-line tool** — just provide your content and get a beautiful presentation.

### 💡 Inspiration

Inspired by the growing trend of AI-powered presentation tools on GitHub, DeckForge was born from the need for a **zero-dependency, no-IDE-required** solution. Most existing tools lock you into specific AI IDEs or cloud platforms. DeckForge breaks free from these constraints — pure CLI, pure freedom.

### 🌟 What Makes DeckForge Different?

| Feature | DeckForge | Other Tools |
|---------|-----------|-------------|
| 🖥️ AI IDE Required | ❌ No | ✅ Yes (Claude Code, Cursor, etc.) |
| ⌨️ Standalone CLI | ✅ Yes | ❌ No |
| 🤖 Multi-LLM Support | ✅ OpenAI, Claude, DeepSeek, Ollama | Limited |
| 📦 Core Dependencies | **1** (python-pptx) | Many |
| 🎨 Built-in Themes | ✅ **11 professional themes** | External only |
| 🔒 Offline Mode | ✅ Template-only mode | ❌ No |
| 🌍 Multi-language | ✅ Content auto-detection | Limited |
| 💰 Cost | Free & Open Source | Often paid |

---

## ✨ Core Features

- 🚀 **One-Command Generation** — Generate presentations with a single CLI command
- 🤖 **Multi-LLM Backend** — Supports OpenAI, Claude, DeepSeek, and Ollama (local)
- 🎨 **11 Built-in Themes** — Modern, Dark, Academic, Minimal, Ocean, Nature, Sunset, Tech, Business, Creative, Emerald
- 📝 **Smart Content Parsing** — Automatically parses Markdown and plain text into slide structures
- 🔧 **Template-Only Mode** — Generate beautiful presentations without any API key (`--no-ai`)
- 📊 **Native PPTX Output** — Real PowerPoint shapes, text boxes, and layouts (not images)
- 🌐 **Multi-language Support** — Auto-detect content language, supports EN/ZH/JA/KO and more
- 🧩 **Modular Architecture** — Pluggable parsers, renderers, and LLM backends
- 🧪 **Well-Tested** — 25+ unit tests covering all core modules
- 📦 **Zero Core Dependencies** — Only requires `python-pptx` as runtime dependency

---

## 🚀 Quick Start

### 📋 Prerequisites

- **Python 3.10+** — The only requirement
- **python-pptx** — Installed automatically via requirements.txt

### 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/gitstq/DeckForge.git
cd DeckForge

# Install dependencies
pip install -r requirements.txt

# Or install as a CLI tool
pip install -e .
```

### ⚡ Basic Usage

```bash
# Generate from inline text
deckforge create --input "Introduction to Machine Learning" --output slides.pptx

# Generate from markdown file
deckforge create --input content.md --output presentation.pptx

# Generate with a specific theme
deckforge create --input content.md --theme dark --output dark_slides.pptx

# Generate without AI (template-only mode)
deckforge create --input content.md --no-ai --output template.pptx

# List all available themes
deckforge themes

# Show detailed theme info
deckforge themes --detail

# Check environment and API keys
deckforge info
```

### 🔑 LLM Configuration

```bash
# Set your preferred LLM API key
export OPENAI_API_KEY="sk-your-key-here"
# or
export ANTHROPIC_API_KEY="sk-ant-your-key-here"
# or
export DEEPSEEK_API_KEY="sk-your-key-here"

# For Ollama (local), just make sure it's running:
ollama serve
```

---

## 📖 Detailed Usage Guide

### 🎨 Themes

DeckForge includes 11 professionally designed themes:

| Theme | Style | Best For |
|-------|-------|----------|
| 🃏 `modern` | Clean blue accents | General purpose |
| 🌙 `dark` | Elegant dark background | Tech presentations |
| 🎓 `academic` | Formal serif fonts | Research & lectures |
| ⬜ `minimal` | Ultra-clean whitespace | Design-focused |
| 🌊 `ocean` | Deep sea blues | Tech & startup |
| 🌿 `nature` | Warm earthy tones | Environmental & wellness |
| 🌅 `sunset` | Warm gradient feel | Creative showcases |
| 💻 `tech` | Futuristic dark theme | Startup pitches |
| 💼 `business` | Corporate professional | Business meetings |
| 🎨 `creative` | Bold artistic colors | Creative portfolios |
| 💚 `emerald` | Rich green palette | Sophisticated events |

### 📝 Input Formats

#### Markdown Input (Recommended)

```markdown
# Presentation Title

## Introduction

Your introduction content here.

## Key Features

- Feature one with **bold text**
- Feature two with *italic text*
- Feature three

## Code Example

\`\`\`python
def hello():
    print("Hello, World!")
\`\`\`
```

#### Plain Text Input

```
Machine Learning Overview

Machine learning is transforming industries worldwide.

Key applications include:
- Natural language processing
- Computer vision
- Autonomous vehicles
```

### 🤖 LLM Enhancement

When an LLM backend is configured, DeckForge automatically enhances your content:

1. **Title Optimization** — Makes titles more compelling and specific
2. **Bullet Refinement** — Improves conciseness and impact of bullet points
3. **Speaker Notes** — Generates helpful notes for each slide
4. **Flow Optimization** — Ensures logical progression between slides

### ⌨️ CLI Reference

```
deckforge create [OPTIONS]

Options:
  -i, --input TEXT     Input content: text string or file path  [required]
  -o, --output TEXT    Output PPTX file path  [default: output.pptx]
  -t, --theme TEXT     Theme name  [default: modern]
  --llm TEXT           LLM backend: openai|claude|deepseek|ollama|none  [default: openai]
  --model TEXT         Specific model name override
  --slides INTEGER     Target number of slides
  --lang TEXT          Language: en|zh|ja|ko|auto  [default: auto]
  --title TEXT         Custom presentation title
  --no-ai             Generate without LLM (template-only mode)
```

---

## 💡 Design Philosophy & Roadmap

### 🎯 Design Principles

1. **Simplicity First** — One command to generate, zero configuration needed
2. **No Lock-in** — No AI IDE dependency, no cloud platform lock-in
3. **Modular Architecture** — Every component is pluggable and replaceable
4. **Offline Capable** — Template-only mode works without any API
5. **Native Output** — Real PowerPoint elements, not flattened images

### 🗺️ Roadmap

- [ ] **v1.1** — Template customization (custom colors, fonts, layouts)
- [ ] **v1.2** — Image insertion support (local files and AI-generated)
- [ ] **v1.3** — Chart and graph generation (bar, pie, line charts)
- [ ] **v1.4** — Interactive slide transitions and animations
- [ ] **v2.0** — Web UI for visual editing
- [ ] **v2.1** — Plugin system for community themes and renderers

---

## 📦 Installation & Deployment

### From Source

```bash
git clone https://github.com/gitstq/DeckForge.git
cd DeckForge
pip install -r requirements.txt
```

### As Python Package

```bash
pip install git+https://github.com/gitstq/DeckForge.git
```

### Development Mode

```bash
git clone https://github.com/gitstq/DeckForge.git
cd DeckForge
pip install -e ".[dev]"
pytest  # Run tests
```

### 🖥️ Compatible Environments

| Platform | Python 3.10 | Python 3.11 | Python 3.12 | Python 3.13 |
|----------|:-----------:|:-----------:|:-----------:|:-----------:|
| 🪟 Windows | ✅ | ✅ | ✅ | ✅ |
| 🍎 macOS | ✅ | ✅ | ✅ | ✅ |
| 🐧 Linux | ✅ | ✅ | ✅ | ✅ |

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. 📤 Push to the branch (`git push origin feature/amazing-feature`)
5. 🎉 Open a Pull Request

### Commit Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation updates
- `refactor:` Code refactoring
- `test:` Test additions/updates
- `chore:` Maintenance tasks

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Made with ❤️ by DeckForge Team<br>
  <sub>Transform your ideas into presentations, one command at a time.</sub>
</p>
