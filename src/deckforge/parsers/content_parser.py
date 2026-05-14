"""
Content Parser - Parse plain text content into slide structures
内容解析器 - 将纯文本内容解析为幻灯片结构
"""

import re
from typing import List, Dict, Any


class ContentParser:
    """Parse plain text content into structured slide data."""
    
    def parse(self, content: str) -> List[Dict[str, Any]]:
        """Parse plain text content into slides.
        
        Args:
            content: Plain text content
            
        Returns:
            List of slide dictionaries with title, content, and type
        """
        # Clean and normalize content
        content = content.strip()
        if not content:
            return self._empty_presentation()
        
        # Split into paragraphs/sections
        paragraphs = self._split_paragraphs(content)
        
        # Build slides
        slides = []
        
        # First slide: title slide
        title = self._extract_title(content)
        slides.append({
            'type': 'title',
            'title': title,
            'subtitle': self._extract_first_sentence(content, title),
            'notes': ''
        })
        
        # Content slides
        for i, para in enumerate(paragraphs):
            if not para.strip():
                continue
            
            # Try to extract a heading from the paragraph
            heading, body = self._split_heading_body(para)
            
            slide_type = self._detect_slide_type(body)
            
            slide = {
                'type': slide_type,
                'title': heading or f"Slide {i + 2}",
                'content': body,
                'bullets': self._extract_bullets(body),
                'notes': ''
            }
            slides.append(slide)
        
        # Add closing slide
        slides.append({
            'type': 'closing',
            'title': 'Thank You',
            'subtitle': 'Questions & Discussion',
            'notes': ''
        })
        
        return slides
    
    def _split_paragraphs(self, content: str) -> List[str]:
        """Split content into logical paragraphs.
        
        Args:
            content: Input content
            
        Returns:
            List of paragraph strings
        """
        # Split by double newlines or significant separators
        paragraphs = re.split(r'\n\s*\n|\n---+\n|\n===+\n', content)
        return [p.strip() for p in paragraphs if p.strip()]
    
    def _extract_title(self, content: str) -> str:
        """Extract a title from the content.
        
        Args:
            content: Input content
            
        Returns:
            Extracted title string
        """
        lines = content.strip().split('\n')
        
        # First non-empty line is usually the title
        for line in lines:
            line = line.strip()
            if line and len(line) <= 100:
                # Remove common prefixes
                line = re.sub(r'^(title|heading|#)+[:\s]*', '', line, flags=re.IGNORECASE)
                return line.strip()
        
        return "Presentation"
    
    def _extract_first_sentence(self, content: str, title: str) -> str:
        """Extract the first meaningful sentence as subtitle.
        
        Args:
            content: Input content
            title: Already extracted title
            
        Returns:
            First sentence string
        """
        # Remove title from content
        remaining = content.replace(title, '', 1).strip()
        
        # Find first sentence
        match = re.search(r'([^.!?]+[.!?])', remaining)
        if match:
            sentence = match.group(1).strip()
            if len(sentence) <= 120:
                return sentence
        
        return ""
    
    def _split_heading_body(self, paragraph: str) -> tuple:
        """Split a paragraph into heading and body.
        
        Args:
            paragraph: Input paragraph
            
        Returns:
            Tuple of (heading, body)
        """
        lines = paragraph.split('\n')
        
        if len(lines) <= 1:
            # Single line - use as title with empty body
            return lines[0].strip(), lines[0].strip()
        
        # First line as heading, rest as body
        heading = lines[0].strip()
        body = '\n'.join(lines[1:]).strip()
        
        return heading, body
    
    def _detect_slide_type(self, content: str) -> str:
        """Detect the best slide layout type for the content.
        
        Args:
            content: Slide content
            
        Returns:
            Slide type string
        """
        lines = [l.strip() for l in content.split('\n') if l.strip()]
        
        # Check for list-like content
        bullet_count = sum(1 for l in lines if re.match(r'^[-*•]\s+|^\d+[.)]\s+', l))
        if bullet_count >= 2:
            return 'bullets'
        
        # Check for short content (section divider)
        if len(content) < 80 and len(lines) <= 2:
            return 'section'
        
        # Check for comparison patterns
        if re.search(r'\b(vs|versus|compared?|compared|while|whereas|on the other hand)\b', content, re.IGNORECASE):
            return 'comparison'
        
        # Default to content
        return 'content'
    
    def _extract_bullets(self, content: str) -> List[str]:
        """Extract bullet points from content.
        
        Args:
            content: Slide content
            
        Returns:
            List of bullet point strings
        """
        bullets = []
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Match bullet patterns
            match = re.match(r'^[-*•]\s+(.+)$', line)
            if match:
                bullets.append(match.group(1))
                continue
            
            match = re.match(r'^\d+[.)]\s+(.+)$', line)
            if match:
                bullets.append(match.group(1))
                continue
            
            # If no bullet pattern, treat each line as a bullet if content is short
            if len(lines) <= 6:
                bullets.append(line)
        
        return bullets
    
    def _empty_presentation(self) -> List[Dict[str, Any]]:
        """Return a minimal empty presentation structure.
        
        Returns:
            List with a single title slide
        """
        return [
            {
                'type': 'title',
                'title': 'Untitled Presentation',
                'subtitle': 'Created with DeckForge',
                'notes': ''
            }
        ]
