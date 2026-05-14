"""Tests for DeckForge theme manager."""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from deckforge.themes.manager import ThemeManager


def test_list_themes():
    """Test listing all themes."""
    manager = ThemeManager()
    themes = manager.list_themes()
    
    assert len(themes) >= 8
    assert 'modern' in themes
    assert 'dark' in themes
    assert 'academic' in themes


def test_get_theme():
    """Test getting a specific theme."""
    manager = ThemeManager()
    theme = manager.get_theme('modern')
    
    assert 'colors' in theme
    assert 'fonts' in theme
    assert 'background' in theme['colors']
    assert 'title' in theme['colors']
    assert 'accent' in theme['colors']


def test_has_theme():
    """Test theme existence check."""
    manager = ThemeManager()
    
    assert manager.has_theme('modern')
    assert manager.has_theme('Modern')  # Case insensitive
    assert not manager.has_theme('nonexistent')


def test_theme_info():
    """Test getting theme info."""
    manager = ThemeManager()
    info = manager.get_theme_info('dark')
    
    assert 'name' in info
    assert 'description' in info
    assert 'colors' in info
    assert info['name'] == 'Dark'


def test_all_themes_have_required_fields():
    """Test all themes have required configuration fields."""
    manager = ThemeManager()
    
    required_colors = ['background', 'title', 'subtitle', 'text', 'accent']
    required_fonts = ['title', 'body']
    
    for theme_name in manager.list_themes():
        theme = manager.get_theme(theme_name)
        
        for color in required_colors:
            assert color in theme['colors'], f"Theme {theme_name} missing color: {color}"
        
        for font in required_fonts:
            assert font in theme['fonts'], f"Theme {theme_name} missing font: {font}"


if __name__ == '__main__':
    test_list_themes()
    test_get_theme()
    test_has_theme()
    test_theme_info()
    test_all_themes_have_required_fields()
    print("✅ All theme manager tests passed!")
