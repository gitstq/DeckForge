"""Tests for DeckForge engine integration."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from deckforge.engine import DeckForgeEngine


def test_create_no_ai_mode():
    """Test creating presentation without AI (template-only mode)."""
    engine = DeckForgeEngine(
        theme='modern',
        llm_backend='none'
    )
    
    content = """# My Presentation

## Introduction

This is an introduction to the topic.

## Key Features

- Feature one
- Feature two
- Feature three

## Conclusion

Thank you for your attention."""
    
    output_path = '/tmp/test_output.pptx'
    result = engine.create(content, output_path)
    
    assert os.path.exists(output_path)
    assert engine.slide_count > 0
    
    # Clean up
    os.remove(output_path)
    print(f"  ✅ Generated {engine.slide_count} slides")


def test_create_plain_text_no_ai():
    """Test creating from plain text without AI."""
    engine = DeckForgeEngine(
        theme='dark',
        llm_backend='none'
    )
    
    content = "Artificial Intelligence in Modern Healthcare\n\nAI is transforming healthcare with improved diagnostics, personalized treatment, and drug discovery. Key applications include medical imaging analysis, electronic health records processing, and predictive analytics for patient outcomes."
    
    output_path = '/tmp/test_plain.pptx'
    result = engine.create(content, output_path)
    
    assert os.path.exists(output_path)
    assert engine.slide_count > 0
    
    os.remove(output_path)
    print(f"  ✅ Generated {engine.slide_count} slides from plain text")


def test_create_with_different_themes():
    """Test creating presentations with different themes."""
    themes = ['modern', 'dark', 'academic', 'minimal', 'ocean']
    content = "# Test\n\n## Section\n\n- Point 1\n- Point 2"
    
    for theme in themes:
        engine = DeckForgeEngine(theme=theme, llm_backend='none')
        output_path = f'/tmp/test_{theme}.pptx'
        engine.create(content, output_path)
        assert os.path.exists(output_path)
        os.remove(output_path)
    
    print(f"  ✅ All {len(themes)} themes rendered successfully")


def test_invalid_theme():
    """Test error handling for invalid theme."""
    try:
        engine = DeckForgeEngine(theme='nonexistent_theme')
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "not found" in str(e)
        print("  ✅ Invalid theme error handled correctly")


if __name__ == '__main__':
    test_create_no_ai_mode()
    test_create_plain_text_no_ai()
    test_create_with_different_themes()
    test_invalid_theme()
    print("\n✅ All engine integration tests passed!")
