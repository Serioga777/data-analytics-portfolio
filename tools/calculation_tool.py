"""
Calculation Tool for Agents
"""
from typing import Dict, Any, Union
import logging
import math

logger = logging.getLogger(__name__)


class CalculationTool:
    """Tool for performing calculations and mathematical operations"""
    
    def __init__(self):
        """Initialize calculation tool"""
        self.name = "calculator"
        self.description = "Perform mathematical calculations and operations"
    
    def calculate(self, expression: str) -> Dict[str, Any]:
        """
        Evaluate a mathematical expression
        
        Args:
            expression: Mathematical expression to evaluate
            
        Returns:
            Calculation result
        """
        try:
            # Safe evaluation with limited scope
            allowed_names = {
                'abs': abs, 'round': round, 'min': min, 'max': max,
                'sum': sum, 'pow': pow,
                'sqrt': math.sqrt, 'sin': math.sin, 'cos': math.cos,
                'tan': math.tan, 'log': math.log, 'exp': math.exp,
                'pi': math.pi, 'e': math.e
            }
            
            result = eval(expression, {"__builtins__": {}}, allowed_names)
            
            logger.info(f"Calculated: {expression} = {result}")
            return {
                'success': True,
                'expression': expression,
                'result': result
            }
        except Exception as e:
            logger.error(f"Error calculating {expression}: {e}")
            return {
                'success': False,
                'expression': expression,
                'error': str(e)
            }
    
    def statistics(self, numbers: list) -> Dict[str, Any]:
        """
        Calculate basic statistics for a list of numbers
        
        Args:
            numbers: List of numbers
            
        Returns:
            Statistical measures
        """
        try:
            if not numbers:
                return {'success': False, 'error': 'Empty list provided'}
            
            n = len(numbers)
            mean = sum(numbers) / n
            sorted_nums = sorted(numbers)
            median = sorted_nums[n // 2] if n % 2 == 1 else (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
            
            variance = sum((x - mean) ** 2 for x in numbers) / n
            std_dev = math.sqrt(variance)
            
            logger.info(f"Calculated statistics for {n} numbers")
            return {
                'success': True,
                'count': n,
                'mean': mean,
                'median': median,
                'std_dev': std_dev,
                'min': min(numbers),
                'max': max(numbers),
                'sum': sum(numbers)
            }
        except Exception as e:
            logger.error(f"Error calculating statistics: {e}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def __call__(self, expression: str) -> Dict[str, Any]:
        """Make the tool callable"""
        return self.calculate(expression)
