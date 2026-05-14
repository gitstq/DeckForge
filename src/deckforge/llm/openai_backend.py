"""
OpenAI LLM Backend
OpenAI LLM后端
"""

import os
import json
from typing import List, Dict, Any, Optional

from .base import LLMBackend


class OpenAIBackend(LLMBackend):
    """OpenAI API backend for LLM calls."""
    
    @property
    def default_model(self) -> str:
        return 'gpt-4o-mini'
    
    @property
    def backend_name(self) -> str:
        return 'openai'
    
    def _call_api(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """Call OpenAI API.
        
        Args:
            messages: List of message dictionaries
            **kwargs: Additional parameters
            
        Returns:
            Response text string
        """
        try:
            import urllib.request
            import urllib.error
        except ImportError:
            raise ImportError("urllib is required for OpenAI API calls")
        
        api_key = os.environ.get('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
        
        url = "https://api.openai.com/v1/chat/completions"
        
        payload = {
            'model': self.model,
            'messages': messages,
            'temperature': 0.7,
            'max_tokens': 4096,
        }
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}',
        }
        
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(url, data=data, headers=headers, method='POST')
        
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                result = json.loads(resp.read().decode('utf-8'))
                return result['choices'][0]['message']['content']
        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8')
            raise RuntimeError(f"OpenAI API error {e.code}: {error_body}")
        except urllib.error.URLError as e:
            raise RuntimeError(f"OpenAI API connection error: {e.reason}")
