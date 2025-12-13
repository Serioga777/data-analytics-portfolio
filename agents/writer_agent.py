"""
Writer Agent - Specialized in content creation and writing
"""
from typing import Dict, Any, Optional
import logging
from .base_agent import BaseAgent

logger = logging.getLogger(__name__)


class WriterAgent(BaseAgent):
    """Agent specialized in creating high-quality written content"""
    
    def __init__(
        self,
        name: str = "Content Writer",
        model: str = "gpt-4-turbo-preview",
        temperature: float = 0.8,
        verbose: bool = True
    ):
        """Initialize writer agent"""
        super().__init__(
            name=name,
            role="Senior Content Writer",
            goal="Create engaging, well-structured, and informative content",
            backstory="""You are a skilled content writer with years of experience 
            in creating compelling articles, reports, and documentation. You excel 
            at transforming complex information into clear, engaging narratives that 
            resonate with the target audience.""",
            model=model,
            temperature=temperature,
            verbose=verbose
        )
    
    def execute(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Execute writing task
        
        Args:
            task: Writing task description
            context: Optional context including research, tone, format, etc.
            
        Returns:
            Written content with metadata
        """
        if self.verbose:
            logger.info(f"{self.name} executing writing task: {task[:100]}...")
        
        # Store task in memory
        self.add_to_memory({
            'type': 'task',
            'task': task,
            'context': context
        })
        
        # Extract context parameters
        tone = context.get('tone', 'professional') if context else 'professional'
        format_type = context.get('format', 'article') if context else 'article'
        research_input = context.get('research', '') if context else ''
        
        # Convert research input to string if it's not already
        if isinstance(research_input, dict):
            research_input = str(research_input)
        
        # In a real implementation, this would:
        # 1. Analyze the research input
        # 2. Generate content using LLM
        # 3. Apply formatting and style
        # 4. Perform quality checks
        
        result = {
            'agent': self.name,
            'task': task,
            'status': 'completed',
            'output': f"""Written content for: {task}
            
            Tone: {tone}
            Format: {format_type}
            
            [This is a placeholder. In production, integrate with:
            - OpenAI/Anthropic/Google AI APIs
            - Template systems
            - Grammar/style checkers]
            
            Based on research: {research_input[:200] if research_input else 'N/A'}...
            """,
            'metadata': {
                'model': self.model,
                'temperature': self.temperature,
                'tone': tone,
                'format': format_type,
                'word_count': 0  # Would be calculated in production
            }
        }
        
        # Store result in memory
        self.add_to_memory({
            'type': 'result',
            'result': result
        })
        
        return result
    
    def revise(self, content: str, feedback: str) -> Dict[str, Any]:
        """
        Revise existing content based on feedback
        
        Args:
            content: Original content
            feedback: Feedback for revision
            
        Returns:
            Revised content
        """
        logger.info(f"{self.name} revising content based on feedback")
        
        return self.execute(
            task=f"Revise content: {feedback}",
            context={
                'original_content': content,
                'feedback': feedback,
                'operation': 'revision'
            }
        )
