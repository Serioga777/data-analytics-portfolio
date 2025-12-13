"""
Llama-Powered Agent - Uses local Llama model via Ollama
"""
from typing import Dict, Any, Optional, List
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.base_agent import BaseAgent
from llm_integration import LocalLlamaLLM

logger = logging.getLogger(__name__)


class LlamaAgent(BaseAgent):
    """Agent powered by local Llama model"""
    
    def __init__(
        self,
        name: str = "Llama Assistant",
        role: str = "AI Assistant",
        goal: str = "Help users with tasks using local Llama model",
        backstory: str = "An AI assistant powered by local Llama",
        model_name: str = "llama2",
        temperature: float = 0.7,
        verbose: bool = True
    ):
        """
        Initialize Llama-powered agent
        
        Args:
            name: Agent name
            role: Agent role
            goal: Agent goal
            backstory: Agent backstory
            model_name: Ollama model name (llama2, llama3, mistral, etc.)
            temperature: Model temperature
            verbose: Enable verbose logging
        """
        super().__init__(
            name=name,
            role=role,
            goal=goal,
            backstory=backstory,
            model=model_name,
            temperature=temperature,
            verbose=verbose
        )
        
        # Initialize local LLM
        self.llm = LocalLlamaLLM(
            model_name=model_name,
            temperature=temperature
        )
        
        # Check connection
        if self.llm.check_connection():
            logger.info(f"✓ Connected to local Llama model: {model_name}")
        else:
            logger.warning("⚠️  Ollama not detected. Make sure it's running: ollama serve")
    
    def execute(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Execute task using local Llama model
        
        Args:
            task: Task description
            context: Optional context
            
        Returns:
            Result dictionary with LLM output
        """
        if self.verbose:
            logger.info(f"{self.name} executing task with local Llama: {task[:100]}...")
        
        # Store task in memory
        self.add_to_memory({
            'type': 'task',
            'task': task,
            'context': context
        })
        
        # Build prompt with agent context
        system_prompt = f"""You are {self.name}, a {self.role}.

Your goal: {self.goal}

Background: {self.backstory}

Respond to the following task professionally and helpfully."""
        
        # Add context if provided
        if context:
            context_str = "\n\nContext:\n"
            for key, value in context.items():
                if isinstance(value, str) and len(value) < 500:
                    context_str += f"- {key}: {value}\n"
            task = task + context_str
        
        # Generate response using local Llama
        response = self.llm.generate(
            prompt=task,
            system_prompt=system_prompt,
            temperature=self.temperature
        )
        
        if response['success']:
            result = {
                'agent': self.name,
                'task': task,
                'status': 'completed',
                'output': response['content'],
                'metadata': {
                    'model': self.model,
                    'temperature': self.temperature,
                    'llm_type': 'local_llama'
                }
            }
        else:
            result = {
                'agent': self.name,
                'task': task,
                'status': 'error',
                'output': f"Error: {response.get('error', 'Unknown error')}",
                'metadata': {
                    'model': self.model,
                    'error': response.get('error', 'Unknown error')
                }
            }
        
        # Store result in memory
        self.add_to_memory({
            'type': 'result',
            'result': result
        })
        
        return result
    
    def chat(self, message: str, history: Optional[List[Dict[str, str]]] = None) -> str:
        """
        Chat with the agent
        
        Args:
            message: User message
            history: Optional chat history
            
        Returns:
            Agent response
        """
        messages = history or []
        
        # Add system message if first message
        if not messages:
            messages.append({
                "role": "system",
                "content": f"You are {self.name}, a {self.role}. {self.backstory}"
            })
        
        # Add user message
        messages.append({
            "role": "user",
            "content": message
        })
        
        # Get response
        response = self.llm.chat(messages, temperature=self.temperature)
        
        if response['success']:
            return response['content']
        else:
            return f"Error: {response.get('error', 'Could not get response')}"
