"""
Local Llama LLM Integration
Supports integration with locally installed Llama models via Ollama or llama.cpp
"""
from typing import Dict, Any, Optional, List
import requests
import json
import logging

logger = logging.getLogger(__name__)


class LocalLlamaLLM:
    """Interface for local Llama models via Ollama"""
    
    def __init__(
        self,
        model_name: str = "llama2",
        base_url: str = "http://localhost:11434",
        temperature: float = 0.7,
        max_tokens: int = 2000
    ):
        """
        Initialize local Llama LLM
        
        Args:
            model_name: Name of the Ollama model (e.g., 'llama2', 'llama3', 'mistral')
            base_url: Ollama API base URL
            temperature: Model temperature
            max_tokens: Maximum tokens to generate
        """
        self.model_name = model_name
        self.base_url = base_url
        self.temperature = temperature
        self.max_tokens = max_tokens
        
    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Generate text using local Llama model via Ollama
        
        Args:
            prompt: User prompt
            system_prompt: Optional system prompt
            temperature: Override default temperature
            max_tokens: Override default max tokens
            
        Returns:
            Response dictionary with generated text
        """
        try:
            url = f"{self.base_url}/api/generate"
            
            payload = {
                "model": self.model_name,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": temperature or self.temperature,
                    "num_predict": max_tokens or self.max_tokens
                }
            }
            
            if system_prompt:
                payload["system"] = system_prompt
            
            logger.info(f"Calling local Llama model: {self.model_name}")
            
            response = requests.post(url, json=payload, timeout=120)
            response.raise_for_status()
            
            result = response.json()
            
            return {
                "success": True,
                "content": result.get("response", ""),
                "model": self.model_name,
                "done": result.get("done", True)
            }
            
        except requests.exceptions.ConnectionError:
            logger.error("Could not connect to Ollama. Is it running?")
            return {
                "success": False,
                "error": "Ollama not running. Start with: ollama serve",
                "content": ""
            }
        except Exception as e:
            logger.error(f"Error calling local Llama: {e}")
            return {
                "success": False,
                "error": str(e),
                "content": ""
            }
    
    def chat(
        self,
        messages: List[Dict[str, str]],
        temperature: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Chat completion using local Llama via Ollama
        
        Args:
            messages: List of message dicts with 'role' and 'content'
            temperature: Override default temperature
            
        Returns:
            Response dictionary
        """
        try:
            url = f"{self.base_url}/api/chat"
            
            payload = {
                "model": self.model_name,
                "messages": messages,
                "stream": False,
                "options": {
                    "temperature": temperature or self.temperature
                }
            }
            
            logger.info(f"Chat with local Llama model: {self.model_name}")
            
            response = requests.post(url, json=payload, timeout=120)
            response.raise_for_status()
            
            result = response.json()
            
            return {
                "success": True,
                "content": result.get("message", {}).get("content", ""),
                "model": self.model_name,
                "done": result.get("done", True)
            }
            
        except requests.exceptions.ConnectionError:
            logger.error("Could not connect to Ollama. Is it running?")
            return {
                "success": False,
                "error": "Ollama not running. Start with: ollama serve",
                "content": ""
            }
        except Exception as e:
            logger.error(f"Error in chat: {e}")
            return {
                "success": False,
                "error": str(e),
                "content": ""
            }
    
    def check_connection(self) -> bool:
        """Check if Ollama is running and accessible"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def list_models(self) -> List[str]:
        """List available local models"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            if response.status_code == 200:
                data = response.json()
                return [model["name"] for model in data.get("models", [])]
            return []
        except:
            return []


def get_local_llm(model_name: str = "llama2") -> LocalLlamaLLM:
    """
    Factory function to get a local LLM instance
    
    Args:
        model_name: Name of the Ollama model
        
    Returns:
        LocalLlamaLLM instance
    """
    return LocalLlamaLLM(model_name=model_name)
