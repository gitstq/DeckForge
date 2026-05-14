"""Tests for DeckForge PPTX renderer."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from deckforge.themes.manager import ThemeManager
from deckforge.renderers.pptx_renderer import PPTXRenderer


def test_render_title_slide():
    """Test rendering a title slide."""
    manager = ThemeManager()
    theme = manager.get_theme('modern')
    renderer = PPTXRenderer(theme)
    
    slides = [{
        'type': 'title',
        'title': 'Test Presentation',
        'subtitle': 'A subtitle here',
        'notes': 'Speaker notes'
    }]
    
    prs = renderer.render(slides)
    assert len(prs.slides) == 1
    
    # Verify slide dimensions
    assert prs.slide_width == renderer.SLIDE_WIDTH
    assert prs.slide_height == renderer.SLIDE_HEIGHT


def test_render_multiple_slides():
    """Test rendering multiple slides."""
    manager = ThemeManager()
    theme = manager.get_theme('dark')
    renderer = PPTXRenderer(theme)
    
    slides = [
        {'type': 'title', 'title': 'Title', 'subtitle': 'Sub', 'notes': ''},
        {'type': 'section', 'title': 'Section 1', 'content': '', 'bullets': [], 'notes': ''},
        {'type': 'bullets', 'title': 'Key Points', 'content': '', 'bullets': ['Point 1', 'Point 2'], 'notes': ''},
        {'type': 'content', 'title': 'Details', 'content': 'Some detailed content here.', 'bullets': [], 'notes': ''},
        {'type': 'closing', 'title': 'Thank You', 'subtitle': 'Q&A', 'notes': ''},
    ]
    
    prs = renderer.render(slides)
    assert len(prs.slides) == 5


def test_render_all_themes():
    """Test rendering with all available themes."""
    manager = ThemeManager()
    
    slides = [
        {'type': 'title', 'title': 'Theme Test', 'subtitle': 'Testing all themes', 'notes': ''},
        {'type': 'bullets', 'title': 'Points', 'content': '', 'bullets': ['A', 'B', 'C'], 'notes': ''},
        {'type': 'closing', 'title': 'Done', 'subtitle': '', 'notes': ''},
    ]
    
    for theme_name in manager.list_themes():
        theme = manager.get_theme(theme_name)
        renderer = PPTXRenderer(theme)
        prs = renderer.render(slides)
        assert len(prs.slides) == 3, f"Theme {theme_name} failed to render"


def test_render_empty_slides():
    """Test rendering with minimal slide data."""
    manager = ThemeManager()
    theme = manager.get_theme('modern')
    renderer = PPTXRenderer(theme)
    
    slides = [{'type': 'title', 'title': 'Only Slide', 'subtitle': '', 'notes': ''}]
    prs = renderer.render(slides)
    assert len(prs.slides) == 1


if __name__ == '__main__':
    test_render_title_slide()
    test_render_multiple_slides()
    test_render_all_themes()
    test_render_empty_slides()
    print("✅ All PPTX renderer tests passed!")
