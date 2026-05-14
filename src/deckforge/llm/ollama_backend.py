"""
Ollama LLM Backend - Local LLM inference
Ollama LLM后端 - 本地大模型推理
"""

import json
import subprocess
from typing import List, Dict, Any, Optional

from .base import LLMBackend


class OllamaBackend(LLMBackend):
    """Ollama local LLM backend."""
    
    @property
    def default_model(self) -> str:
        return 'llama3'
    
    @property
    def backend_name(self) -> str:
        return 'ollama'
    
    def _call_api(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """Call Ollama API (local inference).
        
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
            raise ImportError("urllib is required for Ollama API calls")
        
        url = "http://localhost:11434/api/chat"
        
        payload = {
            'model': self.model,
            'messages': messages,
            'stream': False,
            'options': {
                'temperature': 0.7,
                'num_predict': 4096,
            }
        }
        
        headers = {
            'Content-Type': 'application/json',
        }
        
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(url, data=data, headers=headers, method='POST')
        
        try:
            with urllib.request.urlopen(req, timeout=300) as resp:
                result = json.loads(resp.read().decode('utf-8'))
                return result.get('message', {}).get('content', '')
        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8')
            raise RuntimeError(f"Ollama API error {e.code}: {error_body}")
        except urllib.error.URLError as e:
            raise RuntimeError(
                f"Ollama connection error: {e.reason}. "
                "Make sure Ollama is running (start with 'ollama serve')"
            )
    
    @staticmethod
    def list_models() -> List[str]:
        """List available Ollama models.
        
        Returns:
            List of model name strings
        """
        try:
            import urllib.request
            url = "http://localhost:11434/api/tags"
            req = urllib.request.Request(url, method='GET')
            with urllib.request.urlopen(req, timeout=10) as resp:
                result = json.loads(resp.read().decode('utf-8'))
                return [m['name'] for m in result.get('models', [])]
        except Exception:
            return []
    
    @staticmethod
    def is_running() -> bool:
        """Check if Ollama server is running.
        
        Returns:
            True if Ollama is accessible
        """
        try:
            import urllib.request
            url = "http://localhost:11434/api/tags"
            req = urllib.request.Request(url, method='GET')
            with urllib.request.urlopen(req, timeout=5) as resp:
                return resp.status == 200
        except Exception:
            return False
