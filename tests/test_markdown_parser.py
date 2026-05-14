"""Tests for DeckForge markdown parser."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from deckforge.parsers.markdown_parser import MarkdownParser


def test_parse_markdown_basic():
    """Test basic markdown parsing."""
    parser = MarkdownParser()
    content = """# Introduction to Python

Python is a high-level programming language.

## Features

- Easy to learn
- Powerful standard library
- Cross-platform

## Applications

Web development, data science, AI, automation."""
    
    slides = parser.parse(content)
    
    assert len(slides) >= 4
    assert slides[0]['type'] == 'title'
    assert 'Python' in slides[0]['title']
    assert slides[-1]['type'] == 'closing'


def test_parse_markdown_with_front_matter():
    """Test markdown with YAML front matter."""
    parser = MarkdownParser()
    content = """---
title: Test Presentation
author: John Doe
---

# Main Title

Content here."""
    
    slides = parser.parse(content)
    assert len(slides) >= 1
    assert '---' not in slides[0].get('title', '')


def test_parse_markdown_code_blocks():
    """Test detection of code blocks in content."""
    parser = MarkdownParser()
    content = """# Code Example

Some intro text.

## Code Slide

```python
def hello():
    print("Hello, World!")
```

This is a code example."""
    
    slides = parser.parse(content)
    # Check that code content is preserved in slides
    code_found = any('hello' in str(s.get('raw_content', s.get('content', ''))) for s in slides)
    assert code_found, "Code block content should be preserved in slides"


def test_extract_bullets():
    """Test bullet extraction."""
    parser = MarkdownParser()
    content = """## Key Points

- First point
- Second point
* Third point
+ Fourth point
1. Numbered item"""
    
    bullets = parser._extract_md_bullets(content)
    assert len(bullets) >= 4


def test_clean_markdown():
    """Test markdown cleaning."""
    parser = MarkdownParser()
    content = """**Bold** and *italic* text with `code` and [links](https://example.com).

![Image](img.png)

<!-- notes: hidden notes -->

> Blockquote"""
    
    cleaned = parser._clean_markdown(content)
    assert '**' not in cleaned
    assert '*' not in cleaned or cleaned.count('*') == 0
    assert '`' not in cleaned
    assert 'https://example.com' not in cleaned
    assert 'hidden notes' not in cleaned


def test_empty_markdown():
    """Test empty markdown."""
    parser = MarkdownParser()
    slides = parser.parse("")
    assert len(slides) == 1
    assert slides[0]['type'] == 'title'


if __name__ == '__main__':
    test_parse_markdown_basic()
    test_parse_markdown_with_front_matter()
    test_parse_markdown_code_blocks()
    test_extract_bullets()
    test_clean_markdown()
    test_empty_markdown()
    print("✅ All markdown parser tests passed!")
