"""
LLM Base Backend - Abstract base class for LLM backends
LLM基础后端 - LLM后端抽象基类
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
import json


class LLMBackend(ABC):
    """Abstract base class for LLM backends."""
    
    def __init__(self, model: Optional[str] = None):
        """Initialize LLM backend.
        
        Args:
            model: Specific model name override
        """
        self.model = model or self.default_model
    
    @property
    @abstractmethod
    def default_model(self) -> str:
        """Default model for this backend."""
        pass
    
    @property
    @abstractmethod
    def backend_name(self) -> str:
        """Name of the LLM backend."""
        pass
    
    @abstractmethod
    def _call_api(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """Make an API call to the LLM.
        
        Args:
            messages: List of message dictionaries
            **kwargs: Additional API parameters
            
        Returns:
            Response text string
        """
        pass
    
    def enhance_slides(
        self,
        slide_data: List[Dict[str, Any]],
        raw_content: str,
        lang: str = 'auto'
    ) -> Optional[List[Dict[str, Any]]]:
        """Enhance slide data using LLM.
        
        Args:
            slide_data: Parsed slide data
            raw_content: Original raw content
            lang: Target language
            
        Returns:
            Enhanced slide data or None on failure
        """
        try:
            prompt = self._build_enhancement_prompt(slide_data, raw_content, lang)
            messages = [
                {'role': 'system', 'content': self._system_prompt()},
                {'role': 'user', 'content': prompt}
            ]
            
            response = self._call_api(messages)
            return self._parse_response(response, slide_data)
        except Exception:
            return None
    
    def _system_prompt(self) -> str:
        """Build system prompt for slide enhancement."""
        return (
            "You are a professional presentation designer and content strategist. "
            "Your task is to enhance presentation slide content for clarity, "
            "impact, and professional quality. Respond only with valid JSON."
        )
    
    def _build_enhancement_prompt(
        self,
        slide_data: List[Dict[str, Any]],
        raw_content: str,
        lang: str
    ) -> str:
        """Build the enhancement prompt.
        
        Args:
            slide_data: Current slide data
            raw_content: Original content
            lang: Target language
            
        Returns:
            Prompt string
        """
        lang_instruction = ""
        if lang and lang != 'auto':
            lang_map = {
                'en': 'English',
                'zh': 'Chinese (Simplified)',
                'ja': 'Japanese',
                'ko': 'Korean',
                'es': 'Spanish',
                'fr': 'French',
                'de': 'German',
            }
            lang_name = lang_map.get(lang, lang)
            lang_instruction = f"\nLanguage: Write all content in {lang_name}."
        
        # Simplify slide data for the prompt
        simplified = []
        for i, slide in enumerate(slide_data):
            s = {
                'index': i,
                'type': slide.get('type', 'content'),
                'title': slide.get('title', ''),
            }
            if slide.get('bullets'):
                s['bullets'] = slide['bullets']
            elif slide.get('content'):
                s['content'] = slide['content'][:200]
            simplified.append(s)
        
        return f"""Given the following presentation content and slide structure, enhance each slide for maximum clarity and impact.

Original content:
{raw_content[:2000]}

Current slide structure:
{json.dumps(simplified, ensure_ascii=False, indent=2)}
{lang_instruction}

Please enhance the slides by:
1. Improving titles to be more compelling and specific
2. Refining bullet points for conciseness and impact
3. Adding speaker notes for each slide
4. Ensuring logical flow between slides

Respond with a JSON array of enhanced slides. Each slide should have:
- "title": enhanced title
- "bullets": array of enhanced bullet points (or null)
- "content": enhanced body text (or null)
- "notes": speaker notes

Example format:
[
  {{"title": "Enhanced Title", "bullets": ["Point 1", "Point 2"], "content": null, "notes": "Speaker notes here"}},
  ...
]

Respond ONLY with the JSON array, no other text."""
    
    def _parse_response(
        self,
        response: str,
        original_slides: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Parse LLM response and merge with original slide data.
        
        Args:
            response: LLM response text
            original_slides: Original slide data
            
        Returns:
            Enhanced slide data
        """
        # Try to extract JSON from response
        json_str = response.strip()
        
        # Remove markdown code block markers if present
        if json_str.startswith('```'):
            lines = json_str.split('\n')
            lines = [l for l in lines if not l.strip().startswith('```')]
            json_str = '\n'.join(lines).strip()
        
        try:
            enhanced = json.loads(json_str)
        except json.JSONDecodeError:
            # Try to find JSON array in the response
            import re
            match = re.search(r'\[.*\]', json_str, re.DOTALL)
            if match:
                try:
                    enhanced = json.loads(match.group())
                except json.JSONDecodeError:
                    return original_slides
            else:
                return original_slides
        
        if not isinstance(enhanced, list):
            return original_slides
        
        # Merge enhanced data with original slides
        result = []
        for i, original in enumerate(original_slides):
            if i < len(enhanced):
                enhanced_slide = enhanced[i]
                merged = dict(original)
                
                if 'title' in enhanced_slide and enhanced_slide['title']:
                    merged['title'] = enhanced_slide['title']
                if 'bullets' in enhanced_slide and enhanced_slide['bullets']:
                    merged['bullets'] = enhanced_slide['bullets']
                if 'content' in enhanced_slide and enhanced_slide['content']:
                    merged['content'] = enhanced_slide['content']
                if 'notes' in enhanced_slide and enhanced_slide['notes']:
                    merged['notes'] = enhanced_slide['notes']
                
                result.append(merged)
            else:
                result.append(original)
        
        return result
