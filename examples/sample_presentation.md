# Example: Generate from Markdown

# Introduction to DeckForge

## What is DeckForge?

DeckForge is a lightweight CLI engine that generates professional PPTX presentations from your terminal.

## Key Features

- **No AI IDE Required**: Works as a standalone CLI tool
- **Multi-LLM Support**: OpenAI, Claude, DeepSeek, Ollama
- **10+ Built-in Themes**: Modern, Dark, Academic, and more
- **Zero Core Dependencies**: Only requires python-pptx
- **Template-Only Mode**: Generate without any LLM API

## Quick Start

1. Install: `pip install -r requirements.txt`
2. Run: `deckforge create --input content.md --output slides.pptx`
3. Done!

## Architecture

DeckForge uses a modular pipeline:
- Content Parser → LLM Enhancer → PPTX Renderer

Each stage is independent and replaceable.

## Use Cases

- Conference talks
- Business presentations
- Academic lectures
- Project updates
- Team meetings
