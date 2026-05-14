"""
DeepSeek LLM Backend
DeepSeek LLM后端
"""

import os
import json
from typing import List, Dict, Any, Optional

from .base import LLMBackend


class DeepSeekBackend(LLMBackend):
    """DeepSeek API backend for LLM calls."""
    
    @property
    def default_model(self) -> str:
        return 'deepseek-chat'
    
    @property
    def backend_name(self) -> str:
        return 'deepseek'
    
    def _call_api(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """Call DeepSeek API.
        
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
            raise ImportError("urllib is required for DeepSeek API calls")
        
        api_key = os.environ.get('DEEPSEEK_API_KEY')
        if not api_key:
            raise ValueError("DEEPSEEK_API_KEY environment variable not set")
        
        url = "https://api.deepseek.com/chat/completions"
        
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
            raise RuntimeError(f"DeepSeek API error {e.code}: {error_body}")
        except urllib.error.URLError as e:
            raise RuntimeError(f"DeepSeek API connection error: {e.reason}")
