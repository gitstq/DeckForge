"""
Theme Manager - Manage presentation themes
主题管理器 - 管理演示文稿主题
"""

import os
import json
from typing import Dict, Any, List, Optional


class ThemeManager:
    """Manage and provide presentation themes."""
    
    def __init__(self):
        """Initialize theme manager with built-in themes."""
        self._themes = self._load_builtin_themes()
    
    def _load_builtin_themes(self) -> Dict[str, Dict[str, Any]]:
        """Load all built-in themes.
        
        Returns:
            Dictionary of theme configurations
        """
        themes = {}
        
        # Modern theme - clean and professional
        themes['modern'] = {
            'name': 'Modern',
            'description': 'Clean and professional design with blue accents',
            'colors': {
                'background': '#FFFFFF',
                'title': '#1a1a2e',
                'subtitle': '#666666',
                'text': '#333333',
                'accent': '#4A90D9',
                'surface': '#F5F7FA',
                'muted': '#999999',
                'code_bg': '#1e1e1e',
            },
            'fonts': {
                'title': 'Arial',
                'body': 'Arial',
                'code': 'Consolas',
            },
            'layouts': {
                'title': 'centered',
                'content': 'header_bar',
            }
        }
        
        # Academic theme - formal and structured
        themes['academic'] = {
            'name': 'Academic',
            'description': 'Formal design for academic and research presentations',
            'colors': {
                'background': '#FFFFFF',
                'title': '#2C3E50',
                'subtitle': '#7F8C8D',
                'text': '#2C3E50',
                'accent': '#2980B9',
                'surface': '#ECF0F1',
                'muted': '#BDC3C7',
                'code_bg': '#2C3E50',
            },
            'fonts': {
                'title': 'Georgia',
                'body': 'Arial',
                'code': 'Courier New',
            },
            'layouts': {
                'title': 'centered',
                'content': 'header_bar',
            }
        }
        
        # Dark theme - elegant dark background
        themes['dark'] = {
            'name': 'Dark',
            'description': 'Elegant dark theme with vibrant accents',
            'colors': {
                'background': '#1a1a2e',
                'title': '#EAEAEA',
                'subtitle': '#AAAAAA',
                'text': '#D0D0D0',
                'accent': '#E94560',
                'surface': '#16213e',
                'muted': '#888888',
                'code_bg': '#0f3460',
            },
            'fonts': {
                'title': 'Arial',
                'body': 'Arial',
                'code': 'Consolas',
            },
            'layouts': {
                'title': 'centered',
                'content': 'header_bar',
            }
        }
        
        # Minimal theme - ultra clean
        themes['minimal'] = {
            'name': 'Minimal',
            'description': 'Ultra-clean minimalist design with maximum whitespace',
            'colors': {
                'background': '#FFFFFF',
                'title': '#000000',
                'subtitle': '#888888',
                'text': '#333333',
                'accent': '#000000',
                'surface': '#FAFAFA',
                'muted': '#CCCCCC',
                'code_bg': '#F5F5F5',
            },
            'fonts': {
                'title': 'Helvetica',
                'body': 'Helvetica',
                'code': 'Menlo',
            },
            'layouts': {
                'title': 'centered',
                'content': 'simple',
            }
        }
        
        # Nature theme - earthy and organic
        themes['nature'] = {
            'name': 'Nature',
            'description': 'Warm earthy tones inspired by nature',
            'colors': {
                'background': '#FFF8F0',
                'title': '#2D5016',
                'subtitle': '#6B8E23',
                'text': '#3E3E3E',
                'accent': '#8FBC8F',
                'surface': '#F0F8E8',
                'muted': '#A0A0A0',
                'code_bg': '#2D3B2D',
            },
            'fonts': {
                'title': 'Georgia',
                'body': 'Arial',
                'code': 'Consolas',
            },
            'layouts': {
                'title': 'centered',
                'content': 'header_bar',
            }
        }
        
        # Ocean theme - deep sea blues
        themes['ocean'] = {
            'name': 'Ocean',
            'description': 'Deep ocean blue palette for tech presentations',
            'colors': {
                'background': '#FFFFFF',
                'title': '#0C2340',
                'subtitle': '#4682B4',
                'text': '#2C3E50',
                'accent': '#1E90FF',
                'surface': '#E8F4FD',
                'muted': '#87CEEB',
                'code_bg': '#0C2340',
            },
            'fonts': {
                'title': 'Arial',
                'body': 'Arial',
                'code': 'Consolas',
            },
            'layouts': {
                'title': 'centered',
                'content': 'header_bar',
            }
        }
        
        # Sunset theme - warm gradient feel
        themes['sunset'] = {
            'name': 'Sunset',
            'description': 'Warm sunset-inspired palette for creative presentations',
            'colors': {
                'background': '#FFF5EE',
                'title': '#FF6347',
                'subtitle': '#FF8C69',
                'text': '#4A3728',
                'accent': '#FF4500',
                'surface': '#FFEFD5',
                'muted': '#D2B48C',
                'code_bg': '#3D2B1F',
            },
            'fonts': {
                'title': 'Arial',
                'body': 'Georgia',
                'code': 'Consolas',
            },
            'layouts': {
                'title': 'centered',
                'content': 'header_bar',
            }
        }
        
        # Tech theme - futuristic tech feel
        themes['tech'] = {
            'name': 'Tech',
            'description': 'Futuristic tech-inspired design for startup pitches',
            'colors': {
                'background': '#0D1117',
                'title': '#58A6FF',
                'subtitle': '#8B949E',
                'text': '#C9D1D9',
                'accent': '#7C3AED',
                'surface': '#161B22',
                'muted': '#484F58',
                'code_bg': '#0D1117',
            },
            'fonts': {
                'title': 'Arial',
                'body': 'Arial',
                'code': 'Fira Code',
            },
            'layouts': {
                'title': 'centered',
                'content': 'header_bar',
            }
        }
        
        # Business theme - corporate professional
        themes['business'] = {
            'name': 'Business',
            'description': 'Corporate professional design for business presentations',
            'colors': {
                'background': '#FFFFFF',
                'title': '#1B2A4A',
                'subtitle': '#5D6D7E',
                'text': '#2C3E50',
                'accent': '#C0392B',
                'surface': '#F2F3F4',
                'muted': '#ABB2B9',
                'code_bg': '#1B2A4A',
            },
            'fonts': {
                'title': 'Arial',
                'body': 'Arial',
                'code': 'Consolas',
            },
            'layouts': {
                'title': 'centered',
                'content': 'header_bar',
            }
        }
        
        # Creative theme - bold and artistic
        themes['creative'] = {
            'name': 'Creative',
            'description': 'Bold and artistic design for creative showcases',
            'colors': {
                'background': '#FFFFFF',
                'title': '#E91E63',
                'subtitle': '#9C27B0',
                'text': '#333333',
                'accent': '#FF5722',
                'surface': '#FCE4EC',
                'muted': '#CE93D8',
                'code_bg': '#263238',
            },
            'fonts': {
                'title': 'Arial',
                'body': 'Arial',
                'code': 'Consolas',
            },
            'layouts': {
                'title': 'centered',
                'content': 'header_bar',
            }
        }
        
        # Emerald theme - green professional
        themes['emerald'] = {
            'name': 'Emerald',
            'description': 'Rich emerald green for sophisticated presentations',
            'colors': {
                'background': '#FFFFFF',
                'title': '#064E3B',
                'subtitle': '#059669',
                'text': '#374151',
                'accent': '#10B981',
                'surface': '#ECFDF5',
                'muted': '#6EE7B7',
                'code_bg': '#064E3B',
            },
            'fonts': {
                'title': 'Georgia',
                'body': 'Arial',
                'code': 'Consolas',
            },
            'layouts': {
                'title': 'centered',
                'content': 'header_bar',
            }
        }
        
        return themes
    
    def list_themes(self) -> List[str]:
        """List all available theme names.
        
        Returns:
            List of theme name strings
        """
        return sorted(self._themes.keys())
    
    def has_theme(self, name: str) -> bool:
        """Check if a theme exists.
        
        Args:
            name: Theme name
            
        Returns:
            True if theme exists
        """
        return name.lower() in self._themes
    
    def get_theme(self, name: str) -> Dict[str, Any]:
        """Get a theme configuration by name.
        
        Args:
            name: Theme name
            
        Returns:
            Theme configuration dictionary
        """
        key = name.lower()
        if key not in self._themes:
            raise KeyError(f"Theme '{name}' not found. Available: {', '.join(self.list_themes())}")
        return self._themes[key]
    
    def get_theme_info(self, name: str) -> Dict[str, Any]:
        """Get detailed theme information.
        
        Args:
            name: Theme name
            
        Returns:
            Theme info dictionary
        """
        theme = self.get_theme(name)
        return {
            'name': theme.get('name', name),
            'description': theme.get('description', ''),
            'colors': theme.get('colors', {}),
            'fonts': theme.get('fonts', {}),
        }
