# DeckForge - Lightweight AI-Powered PPT Intelligent Generation CLI Engine
# 轻量级AI驱动PPT智能生成CLI引擎

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-orange.svg)]()

> ⚡ Transform any content into professional, natively editable PowerPoint presentations — entirely from your terminal. No AI IDE required.

## 🎉 About

DeckForge is a lightweight CLI engine that leverages Large Language Models (LLMs) to generate professional, natively editable `.pptx` files directly from your terminal. Unlike other AI presentation tools that require AI IDEs like Claude Code or Cursor, DeckForge works as a standalone command-line tool — just provide your content and get a beautiful presentation.

### ✨ Key Differentiators

| Feature | DeckForge | Other Tools |
|---------|-----------|-------------|
| AI IDE Required | ❌ No | ✅ Yes (Claude Code, Cursor, etc.) |
| Standalone CLI | ✅ Yes | ❌ No |
| Multi-LLM Support | ✅ OpenAI, Claude, DeepSeek, Ollama | Limited |
| Core Dependencies | 1 (python-pptx) | Many |
| Template System | ✅ Built-in themes | External only |
| Offline Mode | ✅ Template-only mode | ❌ No |

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/gitstq/DeckForge.git
cd DeckForge

# Install dependencies
pip install -r requirements.txt

# Or install in development mode
pip install -e .
```

### Basic Usage

```bash
# Generate from text content
deckforge create --input "Introduction to Machine Learning" --output presentation.pptx

# Generate from markdown file
deckforge create --input slides.md --output presentation.pptx

# Generate with specific theme
deckforge create --input content.md --theme academic --output academic_talk.pptx

# Use specific LLM backend
deckforge create --input report.md --llm openai --output report.pptx

# List available themes
deckforge themes

# Show help
deckforge --help
```

### Environment Configuration

```bash
# Set your LLM API key
export OPENAI_API_KEY="your-key-here"
# or
export ANTHROPIC_API_KEY="your-key-here"
# or
export DEEPSEEK_API_KEY="your-key-here"
```

## 📖 Documentation

For detailed usage instructions, please refer to the following documentation:

- [简体中文文档](README_zh.md)
- [繁體中文文檔](README_zh_TW.md)
- [English Documentation](README.md)

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
