"""
Claude (Anthropic) LLM Backend
Claude (Anthropic) LLM后端
"""

import os
import json
from typing import List, Dict, Any, Optional

from .base import LLMBackend


class ClaudeBackend(LLMBackend):
    """Anthropic Claude API backend for LLM calls."""
    
    @property
    def default_model(self) -> str:
        return 'claude-sonnet-4-20250514'
    
    @property
    def backend_name(self) -> str:
        return 'claude'
    
    def _call_api(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """Call Anthropic Claude API.
        
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
            raise ImportError("urllib is required for Claude API calls")
        
        api_key = os.environ.get('ANTHROPIC_API_KEY')
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable not set")
        
        url = "https://api.anthropic.com/v1/messages"
        
        # Extract system message
        system_msg = ""
        user_messages = []
        for msg in messages:
            if msg['role'] == 'system':
                system_msg = msg['content']
            else:
                user_messages.append(msg)
        
        payload = {
            'model': self.model,
            'max_tokens': 4096,
            'system': system_msg,
            'messages': user_messages,
        }
        
        headers = {
            'Content-Type': 'application/json',
            'x-api-key': api_key,
            'anthropic-version': '2023-06-01',
        }
        
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(url, data=data, headers=headers, method='POST')
        
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                result = json.loads(resp.read().decode('utf-8'))
                # Claude returns content blocks
                for block in result.get('content', []):
                    if block.get('type') == 'text':
                        return block['text']
                return ""
        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8')
            raise RuntimeError(f"Claude API error {e.code}: {error_body}")
        except urllib.error.URLError as e:
            raise RuntimeError(f"Claude API connection error: {e.reason}")
