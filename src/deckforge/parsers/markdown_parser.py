"""
Markdown Parser - Parse markdown content into slide structures
Markdown解析器 - 将Markdown内容解析为幻灯片结构
"""

import re
from typing import List, Dict, Any, Optional


class MarkdownParser:
    """Parse markdown content into structured slide data."""
    
    # Slide type mapping from markdown patterns
    HEADING_SLIDE_TYPES = {
        1: 'section',      # H1 = section divider
        2: 'content',      # H2 = content slide
        3: 'bullets',      # H3 = sub-section with bullets
    }
    
    def parse(self, content: str) -> List[Dict[str, Any]]:
        """Parse markdown content into slides.
        
        Args:
            content: Markdown formatted content
            
        Returns:
            List of slide dictionaries
        """
        content = content.strip()
        if not content:
            return self._empty_presentation()
        
        # Remove YAML front matter if present
        content = self._remove_front_matter(content)
        
        # Split into sections by headings
        sections = self._split_by_headings(content)
        
        if not sections:
            return self._empty_presentation()
        
        slides = []
        
        # Process first section as title slide
        first = sections[0]
        title = self._extract_md_title(first)
        subtitle = self._extract_md_subtitle(first)
        
        slides.append({
            'type': 'title',
            'title': title,
            'subtitle': subtitle,
            'notes': ''
        })
        
        # Process remaining sections
        for section in sections[1:]:
            slide = self._process_section(section)
            if slide:
                slides.append(slide)
        
        # Ensure we have a closing slide
        if slides and slides[-1]['type'] != 'closing':
            slides.append({
                'type': 'closing',
                'title': 'Thank You',
                'subtitle': 'Questions & Discussion',
                'notes': ''
            })
        
        return slides
    
    def _remove_front_matter(self, content: str) -> str:
        """Remove YAML front matter from markdown.
        
        Args:
            content: Raw markdown content
            
        Returns:
            Content without front matter
        """
        if content.startswith('---'):
            end = content.find('---', 3)
            if end != -1:
                return content[end + 3:].strip()
        return content
    
    def _split_by_headings(self, content: str) -> List[Dict[str, Any]]:
        """Split markdown content by headings into sections.
        
        Args:
            content: Markdown content
            
        Returns:
            List of section dictionaries
        """
        sections = []
        current_section = {
            'level': 0,
            'title': '',
            'content': '',
            'lines': []
        }
        
        for line in content.split('\n'):
            heading_match = re.match(r'^(#{1,6})\s+(.+)$', line)
            
            if heading_match:
                # Save previous section
                if current_section['lines']:
                    current_section['content'] = '\n'.join(current_section['lines']).strip()
                    sections.append(current_section)
                
                # Start new section
                level = len(heading_match.group(1))
                title = heading_match.group(2).strip()
                current_section = {
                    'level': level,
                    'title': title,
                    'content': '',
                    'lines': []
                }
            else:
                current_section['lines'].append(line)
        
        # Don't forget the last section
        if current_section['lines']:
            current_section['content'] = '\n'.join(current_section['lines']).strip()
            sections.append(current_section)
        
        return sections
    
    def _extract_md_title(self, section: Dict[str, Any]) -> str:
        """Extract title from the first section.
        
        Args:
            section: First section dictionary
            
        Returns:
            Title string
        """
        if section['title']:
            return section['title']
        
        # Try first non-empty line
        lines = section['content'].split('\n')
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#') and not line.startswith('!'):
                # Remove bold/italic markers
                line = re.sub(r'[*_]{1,3}([^*_]+)[*_]{1,3}', r'\1', line)
                return line[:100]
        
        return "Untitled Presentation"
    
    def _extract_md_subtitle(self, section: Dict[str, Any]) -> str:
        """Extract subtitle from the first section.
        
        Args:
            section: First section dictionary
            
        Returns:
            Subtitle string
        """
        lines = [l.strip() for l in section['content'].split('\n') if l.strip()]
        
        # Skip the title line if it was used
        start = 1 if section['title'] else 0
        
        for line in lines[start:]:
            # Skip images, links, horizontal rules
            if line.startswith('!') or line.startswith('---') or line.startswith('==='):
                continue
            # Remove markdown formatting
            clean = re.sub(r'[*_`#\[\]()]{1,3}', '', line).strip()
            if clean and len(clean) <= 150:
                return clean
        
        return ""
    
    def _process_section(self, section: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Process a section into a slide dictionary.
        
        Args:
            section: Section dictionary
            
        Returns:
            Slide dictionary or None if section is empty
        """
        title = section['title']
        content = section['content']
        level = section['level']
        
        if not title and not content:
            return None
        
        # Clean title
        title = re.sub(r'[*_`]{1,3}', '', title).strip()
        
        # Determine slide type
        slide_type = self.HEADING_SLIDE_TYPES.get(level, 'content')
        
        # Override type based on content analysis
        if self._has_code_block(content):
            slide_type = 'code'
        elif self._has_table(content):
            slide_type = 'table'
        elif self._has_image(content):
            slide_type = 'image'
        elif self._is_two_column(content):
            slide_type = 'two_column'
        
        # Extract bullets
        bullets = self._extract_md_bullets(content)
        
        # Extract notes (content after <!-- notes: -->)
        notes = ''
        notes_match = re.search(r'<!--\s*notes?:\s*(.+?)\s*-->', content, re.DOTALL)
        if notes_match:
            notes = notes_match.group(1).strip()
        
        # Clean content for display
        clean_content = self._clean_markdown(content)
        
        slide = {
            'type': slide_type,
            'title': title or 'Untitled',
            'content': clean_content,
            'bullets': bullets,
            'notes': notes,
            'raw_content': content
        }
        
        return slide
    
    def _extract_md_bullets(self, content: str) -> List[str]:
        """Extract bullet points from markdown content.
        
        Args:
            content: Markdown content
            
        Returns:
            List of bullet strings
        """
        bullets = []
        
        for line in content.split('\n'):
            line = line.strip()
            
            # Match list items
            match = re.match(r'^[-*+]\s+(.+)$', line)
            if match:
                clean = re.sub(r'[*_`]{1,3}', '', match.group(1)).strip()
                bullets.append(clean)
                continue
            
            match = re.match(r'^\d+[.)]\s+(.+)$', line)
            if match:
                clean = re.sub(r'[*_`]{1,3}', '', match.group(1)).strip()
                bullets.append(clean)
        
        return bullets
    
    def _has_code_block(self, content: str) -> bool:
        """Check if content contains a code block."""
        return '```' in content
    
    def _has_table(self, content: str) -> bool:
        """Check if content contains a markdown table."""
        lines = content.split('\n')
        table_lines = 0
        for line in lines:
            if re.match(r'^\|', line.strip()):
                table_lines += 1
            elif table_lines > 0:
                break
        return table_lines >= 2
    
    def _has_image(self, content: str) -> bool:
        """Check if content contains an image reference."""
        return bool(re.search(r'!\[.*?\]\(.*?\)', content))
    
    def _is_two_column(self, content: str) -> bool:
        """Check if content suggests a two-column layout."""
        # Check for side-by-side patterns
        patterns = [
            r'\|.*\|.*\|',      # Table-like
            r'left:.*right:',    # Explicit columns
            r'column.*column',   # Column mentions
        ]
        for pattern in patterns:
            if re.search(pattern, content, re.IGNORECASE):
                return True
        return False
    
    def _clean_markdown(self, content: str) -> str:
        """Remove markdown formatting for plain text display.
        
        Args:
            content: Markdown content
            
        Returns:
            Clean plain text
        """
        # Remove code blocks
        text = re.sub(r'```[\s\S]*?```', '[Code Block]', content)
        # Remove inline code
        text = re.sub(r'`([^`]+)`', r'\1', text)
        # Remove images
        text = re.sub(r'!\[([^\]]*)\]\([^)]+\)', r'\1', text)
        # Remove links but keep text
        text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
        # Remove bold/italic
        text = re.sub(r'[*_]{1,3}([^*_]+)[*_]{1,3}', r'\1', text)
        # Remove horizontal rules
        text = re.sub(r'^[-=_*]{3,}$', '', text, flags=re.MULTILINE)
        # Remove HTML comments
        text = re.sub(r'<!--[\s\S]*?-->', '', text)
        # Remove blockquotes marker
        text = re.sub(r'^>\s?', '', text, flags=re.MULTILINE)
        # Clean up whitespace
        text = re.sub(r'\n{3,}', '\n\n', text)
        
        return text.strip()
    
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
