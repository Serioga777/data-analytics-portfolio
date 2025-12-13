"""
Base Agent Class for Multi-Agent Framework
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class BaseAgent(ABC):
    """Base class for all agents in the framework"""
    
    def __init__(
        self,
        name: str,
        role: str,
        goal: str,
        backstory: str,
        model: str = "gpt-4-turbo-preview",
        temperature: float = 0.7,
        verbose: bool = True
    ):
        """
        Initialize base agent
        
        Args:
            name: Agent's name
            role: Agent's role/specialty
            goal: Agent's primary goal
            backstory: Agent's background context
            model: LLM model to use
            temperature: Model temperature setting
            verbose: Enable verbose logging
        """
        self.name = name
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.model = model
        self.temperature = temperature
        self.verbose = verbose
        self.memory: List[Dict[str, Any]] = []
        self.created_at = datetime.now()
        
        if self.verbose:
            logger.info(f"Initialized agent: {self.name} ({self.role})")
    
    @abstractmethod
    def execute(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Execute a task - must be implemented by subclasses
        
        Args:
            task: The task description
            context: Optional context for the task
            
        Returns:
            Result dictionary with output and metadata
        """
        pass
    
    def add_to_memory(self, item: Dict[str, Any]) -> None:
        """Add an item to agent's memory"""
        item['timestamp'] = datetime.now().isoformat()
        self.memory.append(item)
        
        if self.verbose:
            logger.debug(f"{self.name} added to memory: {item.get('type', 'unknown')}")
    
    def get_memory(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """
        Retrieve agent's memory
        
        Args:
            limit: Maximum number of items to return (most recent)
            
        Returns:
            List of memory items
        """
        if limit:
            return self.memory[-limit:]
        return self.memory
    
    def clear_memory(self) -> None:
        """Clear agent's memory"""
        self.memory = []
        if self.verbose:
            logger.info(f"{self.name} memory cleared")
    
    def get_info(self) -> Dict[str, Any]:
        """Get agent information"""
        return {
            "name": self.name,
            "role": self.role,
            "goal": self.goal,
            "backstory": self.backstory,
            "model": self.model,
            "memory_size": len(self.memory),
            "created_at": self.created_at.isoformat()
        }
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(name='{self.name}', role='{self.role}')>"
