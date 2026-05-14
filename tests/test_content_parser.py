"""Tests for DeckForge content parser."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from deckforge.parsers.content_parser import ContentParser


def test_parse_plain_text():
    """Test parsing plain text content."""
    parser = ContentParser()
    content = """Machine Learning Overview

Machine learning is a subset of artificial intelligence that enables systems to learn from data.

Key concepts include supervised learning, unsupervised learning, and reinforcement learning.

Applications range from image recognition to natural language processing."""
    
    slides = parser.parse(content)
    
    assert len(slides) >= 3
    assert slides[0]['type'] == 'title'
    assert 'Machine Learning' in slides[0]['title']
    assert slides[-1]['type'] == 'closing'


def test_parse_empty_content():
    """Test parsing empty content."""
    parser = ContentParser()
    slides = parser.parse("")
    
    assert len(slides) == 1
    assert slides[0]['type'] == 'title'


def test_parse_bullet_content():
    """Test detection of bullet-style content."""
    parser = ContentParser()
    content = """Benefits of Exercise

- Improved cardiovascular health
- Better mental health
- Increased energy levels
- Better sleep quality"""
    
    slides = parser.parse(content)
    
    # Should detect bullets
    content_slides = [s for s in slides if s['type'] == 'bullets']
    assert len(content_slides) >= 1


def test_extract_title():
    """Test title extraction."""
    parser = ContentParser()
    
    content = "My Presentation Title\n\nSome content here."
    title = parser._extract_title(content)
    assert title == "My Presentation Title"


def test_detect_slide_type():
    """Test slide type detection."""
    parser = ContentParser()
    
    # Bullet content
    bullet_content = "- Item 1\n- Item 2\n- Item 3"
    assert parser._detect_slide_type(bullet_content) == 'bullets'
    
    # Short content = section
    short = "Quick section"
    assert parser._detect_slide_type(short) == 'section'
    
    # Comparison content (needs to be longer than section threshold)
    compare = "Python vs Java: while Python is dynamic and interpreted, Java is static and compiled. Python offers rapid development, whereas Java provides strong typing and enterprise scalability."
    slide_type = parser._detect_slide_type(compare)
    assert slide_type in ('comparison', 'content')


if __name__ == '__main__':
    test_parse_plain_text()
    test_parse_empty_content()
    test_parse_bullet_content()
    test_extract_title()
    test_detect_slide_type()
    print("✅ All content parser tests passed!")
