"""
DeckForge Engine - Core presentation generation engine
DeckForge 引擎 - 核心演示文稿生成引擎
"""

import os
import json
import re
from typing import Optional, List, Dict, Any

from .themes.manager import ThemeManager
from .renderers.pptx_renderer import PPTXRenderer
from .parsers.content_parser import ContentParser
from .parsers.markdown_parser import MarkdownParser


class DeckForgeEngine:
    """Main engine for generating PPTX presentations."""
    
    def __init__(
        self,
        theme: str = 'modern',
        llm_backend: str = 'openai',
        model: Optional[str] = None,
        lang: str = 'auto',
        title: Optional[str] = None,
        target_slides: Optional[int] = None
    ):
        """Initialize the DeckForge engine.
        
        Args:
            theme: Presentation theme name
            llm_backend: LLM backend ('openai', 'claude', 'deepseek', 'ollama', 'none')
            model: Specific model name override
            lang: Presentation language code
            title: Custom presentation title
            target_slides: Target number of slides
        """
        self.theme_name = theme
        self.llm_backend = llm_backend
        self.model = model
        self.lang = lang
        self.custom_title = title
        self.target_slides = target_slides
        self.slide_count = 0
        
        # Initialize components
        self.theme_manager = ThemeManager()
        self.content_parser = ContentParser()
        self.markdown_parser = MarkdownParser()
        
        # Validate theme
        if not self.theme_manager.has_theme(theme):
            available = ', '.join(self.theme_manager.list_themes())
            raise ValueError(f"Theme '{theme}' not found. Available: {available}")
    
    def create(self, content: str, output_path: str) -> str:
        """Generate a PPTX presentation from content.
        
        Args:
            content: Input content (text or markdown)
            output_path: Output PPTX file path
            
        Returns:
            Path to the generated PPTX file
        """
        # Step 1: Parse content into structured data
        slide_data = self._parse_content(content)
        
        # Step 2: Enhance with LLM if available
        if self.llm_backend != 'none':
            slide_data = self._enhance_with_llm(slide_data, content)
        
        # Step 3: Render to PPTX
        self._render_pptx(slide_data, output_path)
        
        return os.path.abspath(output_path)
    
    def _parse_content(self, content: str) -> List[Dict[str, Any]]:
        """Parse raw content into structured slide data.
        
        Args:
            content: Raw input content
            
        Returns:
            List of slide dictionaries
        """
        # Detect if content is markdown
        is_markdown = self._is_markdown(content)
        
        if is_markdown:
            slides = self.markdown_parser.parse(content)
        else:
            slides = self.content_parser.parse(content)
        
        # Apply custom title if provided
        if self.custom_title and slides:
            slides[0]['title'] = self.custom_title
        
        # Limit slides if target specified
        if self.target_slides and len(slides) > self.target_slides:
            slides = slides[:self.target_slides]
        
        return slides
    
    def _is_markdown(self, content: str) -> bool:
        """Detect if content is markdown format.
        
        Args:
            content: Input content
            
        Returns:
            True if content appears to be markdown
        """
        markdown_indicators = [
            r'^#{1,6}\s+',      # Headers
            r'^\*{3,}$',         # Horizontal rules
            r'^-\s+',            # Unordered lists
            r'^\d+\.\s+',        # Ordered lists
            r'\[.*\]\(.*\)',     # Links
            r'```',              # Code blocks
            r'^>\s+',            # Blockquotes
        ]
        
        score = 0
        lines = content.split('\n')[:20]  # Check first 20 lines
        
        for line in lines:
            for pattern in markdown_indicators:
                if re.search(pattern, line):
                    score += 1
                    break
        
        return score >= 2
    
    def _enhance_with_llm(
        self, slide_data: List[Dict[str, Any]], raw_content: str
    ) -> List[Dict[str, Any]]:
        """Enhance slide data using LLM.
        
        Args:
            slide_data: Parsed slide data
            raw_content: Original raw content
            
        Returns:
            Enhanced slide data
        """
        try:
            if self.llm_backend == 'openai':
                from .llm.openai_backend import OpenAIBackend
                backend = OpenAIBackend(model=self.model)
            elif self.llm_backend == 'claude':
                from .llm.claude_backend import ClaudeBackend
                backend = ClaudeBackend(model=self.model)
            elif self.llm_backend == 'deepseek':
                from .llm.deepseek_backend import DeepSeekBackend
                backend = DeepSeekBackend(model=self.model)
            elif self.llm_backend == 'ollama':
                from .llm.ollama_backend import OllamaBackend
                backend = OllamaBackend(model=self.model)
            else:
                return slide_data
            
            enhanced = backend.enhance_slides(slide_data, raw_content, self.lang)
            return enhanced if enhanced else slide_data
            
        except ImportError as e:
            print(f"⚠️  LLM backend '{self.llm_backend}' not available: {e}")
            print(f"   Falling back to template-only mode.")
            return slide_data
        except Exception as e:
            print(f"⚠️  LLM enhancement failed: {e}")
            print(f"   Using parsed content directly.")
            return slide_data
    
    def _render_pptx(
        self, slide_data: List[Dict[str, Any]], output_path: str
    ) -> None:
        """Render slide data to PPTX file.
        
        Args:
            slide_data: Structured slide data
            output_path: Output file path
        """
        theme = self.theme_manager.get_theme(self.theme_name)
        renderer = PPTXRenderer(theme)
        
        # Ensure output directory exists
        output_dir = os.path.dirname(output_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        
        # Render
        prs = renderer.render(slide_data)
        prs.save(output_path)
        self.slide_count = len(slide_data)
