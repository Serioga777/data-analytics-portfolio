"""
Example 1: Basic Multi-Agent Collaboration
Demonstrates simple agent interactions
"""
import logging
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from agents import ResearcherAgent, WriterAgent, AnalyzerAgent

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def main():
    """Demonstrate basic multi-agent collaboration"""
    print("=" * 80)
    print("Multi-Agent Framework - Basic Example")
    print("=" * 80)
    print()
    
    # Initialize agents
    print("Initializing agents...")
    researcher = ResearcherAgent(name="AI Researcher")
    writer = WriterAgent(name="Tech Writer")
    analyzer = AnalyzerAgent(name="Data Analyst")
    
    print(f"✓ {researcher.name}: {researcher.role}")
    print(f"✓ {writer.name}: {writer.role}")
    print(f"✓ {analyzer.name}: {analyzer.role}")
    print()
    
    # Task 1: Research
    print("-" * 80)
    print("Task 1: Research Phase")
    print("-" * 80)
    research_task = "Research the latest developments in multi-agent AI systems"
    research_result = researcher.execute(research_task)
    print(f"Research completed by {research_result['agent']}")
    print(f"Status: {research_result['status']}")
    print()
    
    # Task 2: Writing
    print("-" * 80)
    print("Task 2: Writing Phase")
    print("-" * 80)
    writing_task = "Write a summary article about multi-agent AI systems"
    writing_result = writer.execute(
        writing_task,
        context={
            'research': research_result['output'],
            'tone': 'professional',
            'format': 'article'
        }
    )
    print(f"Writing completed by {writing_result['agent']}")
    print(f"Status: {writing_result['status']}")
    print()
    
    # Task 3: Analysis
    print("-" * 80)
    print("Task 3: Analysis Phase")
    print("-" * 80)
    analysis_task = "Analyze the effectiveness of the research and writing"
    analysis_result = analyzer.execute(
        analysis_task,
        context={
            'data': [research_result, writing_result],
            'metrics': ['completeness', 'clarity', 'accuracy']
        }
    )
    print(f"Analysis completed by {analysis_result['agent']}")
    print(f"Status: {analysis_result['status']}")
    print()
    
    # Summary
    print("=" * 80)
    print("Workflow Summary")
    print("=" * 80)
    print(f"1. {researcher.name} conducted research")
    print(f"   Memory items: {len(researcher.get_memory())}")
    print(f"2. {writer.name} created content")
    print(f"   Memory items: {len(writer.get_memory())}")
    print(f"3. {analyzer.name} analyzed results")
    print(f"   Memory items: {len(analyzer.get_memory())}")
    print()
    
    print("✓ Multi-agent workflow completed successfully!")
    print()
    print("Next steps:")
    print("1. Configure your API keys in .env file")
    print("2. Install dependencies: pip install -r requirements.txt")
    print("3. Explore other examples in the examples/ directory")
    print("4. Customize agents for your specific use case")


if __name__ == "__main__":
    main()
