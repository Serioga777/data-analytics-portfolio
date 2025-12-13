"""
Example 2: Advanced Multi-Agent Workflow
Demonstrates complex agent orchestration with tools
"""
import logging
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from agents import ResearcherAgent, WriterAgent, AnalyzerAgent
from tools import WebSearchTool, FileOperationsTool, CalculationTool

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


class MultiAgentOrchestrator:
    """Orchestrator for managing multiple agents and workflows"""
    
    def __init__(self):
        """Initialize orchestrator with agents and tools"""
        self.agents = {
            'researcher': ResearcherAgent(name="Research Lead"),
            'writer': WriterAgent(name="Content Creator"),
            'analyzer': AnalyzerAgent(name="Insights Analyst")
        }
        
        self.tools = {
            'search': WebSearchTool(),
            'files': FileOperationsTool(),
            'calculator': CalculationTool()
        }
        
        logger.info("Orchestrator initialized with agents and tools")
    
    def execute_workflow(self, topic: str) -> dict:
        """
        Execute a complete multi-agent workflow
        
        Args:
            topic: Topic to research and analyze
            
        Returns:
            Workflow results
        """
        results = {}
        
        # Step 1: Deep Research
        print(f"\n{'='*80}")
        print(f"WORKFLOW: {topic}")
        print(f"{'='*80}\n")
        
        print("Phase 1: Deep Research")
        print("-" * 80)
        research_result = self.agents['researcher'].deep_research(topic, depth=2)
        results['research'] = research_result
        print(f"✓ Research completed: {len(research_result['results'])} levels analyzed\n")
        
        # Step 2: Content Creation
        print("Phase 2: Content Creation")
        print("-" * 80)
        writing_result = self.agents['writer'].execute(
            f"Create comprehensive guide about {topic}",
            context={
                'research': research_result,
                'tone': 'educational',
                'format': 'guide'
            }
        )
        results['content'] = writing_result
        print(f"✓ Content created by {writing_result['agent']}\n")
        
        # Step 3: Analysis & Insights
        print("Phase 3: Analysis & Insights")
        print("-" * 80)
        analysis_result = self.agents['analyzer'].execute(
            f"Analyze research quality and content effectiveness for {topic}",
            context={
                'data': [research_result, writing_result],
                'metrics': ['depth', 'clarity', 'completeness', 'actionability']
            }
        )
        results['analysis'] = analysis_result
        print(f"✓ Analysis completed by {analysis_result['agent']}\n")
        
        # Step 4: Generate Report
        print("Phase 4: Report Generation")
        print("-" * 80)
        report = self._generate_report(results)
        results['report'] = report
        print("✓ Final report generated\n")
        
        return results
    
    def _generate_report(self, results: dict) -> str:
        """Generate final workflow report"""
        report = f"""
MULTI-AGENT WORKFLOW REPORT
{'=' * 80}

Research Summary:
- Topic: {results['research']['topic']}
- Depth: {results['research']['depth']} levels
- Status: {results['research']['status']}

Content Summary:
- Agent: {results['content']['agent']}
- Status: {results['content']['status']}

Analysis Summary:
- Agent: {results['analysis']['agent']}
- Status: {results['analysis']['status']}

WORKFLOW COMPLETED SUCCESSFULLY
{'=' * 80}
"""
        return report
    
    def get_agent_status(self) -> dict:
        """Get status of all agents"""
        return {
            name: agent.get_info()
            for name, agent in self.agents.items()
        }


def main():
    """Run advanced multi-agent workflow"""
    print("\n" + "=" * 80)
    print("Multi-Agent Framework - Advanced Example")
    print("=" * 80)
    
    # Initialize orchestrator
    orchestrator = MultiAgentOrchestrator()
    
    # Execute workflow
    topic = "Multi-Agent Systems in Modern AI"
    results = orchestrator.execute_workflow(topic)
    
    # Display report
    print(results['report'])
    
    # Show agent status
    print("\nAgent Status:")
    print("-" * 80)
    for name, info in orchestrator.get_agent_status().items():
        print(f"{name.upper()}:")
        print(f"  Name: {info['name']}")
        print(f"  Role: {info['role']}")
        print(f"  Memory Size: {info['memory_size']}")
        print()
    
    print("✓ Advanced workflow demonstration completed!")
    print("\nTo integrate with real LLMs:")
    print("1. Add your API keys to .env file")
    print("2. Implement LLM calls in agent execute() methods")
    print("3. Connect tools to actual external APIs")


if __name__ == "__main__":
    main()
