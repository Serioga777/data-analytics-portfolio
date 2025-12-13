"""
Example: Qwen Local LLM Integration
Demonstrates using your local Qwen models
"""
import logging
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.llama_agent import LlamaAgent
from llm_integration import LocalLlamaLLM

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def main():
    """Test Qwen integration"""
    print("\n" + "=" * 80)
    print("Multi-Agent Framework - Qwen Local LLM Integration")
    print("=" * 80)
    
    # Use your Qwen model
    model_name = "qwen2.5:3b"  # Faster and more reliable, use "qwen2.5:7b" for more complex tasks
    
    print(f"\n✓ Using local model: {model_name}")
    
    # Test 1: Basic LLM
    print("\n" + "=" * 80)
    print("Test 1: Basic LLM Generation")
    print("=" * 80)
    
    llm = LocalLlamaLLM(model_name=model_name, temperature=0.7)
    
    prompt = "Explain what a multi-agent AI system is in 2-3 sentences."
    print(f"\nPrompt: {prompt}")
    print("\nGenerating response with Qwen...")
    
    response = llm.generate(prompt)
    
    if response['success']:
        print("\n" + "-" * 80)
        print("Qwen Response:")
        print("-" * 80)
        print(response['content'])
        print("-" * 80)
    else:
        print(f"\n❌ Error: {response.get('error', 'Unknown error')}")
        return
    
    # Test 2: Qwen-powered Agent
    print("\n" + "=" * 80)
    print("Test 2: Qwen-Powered Agent")
    print("=" * 80)
    
    agent = LlamaAgent(
        name="Qwen Research Assistant",
        role="AI Research Specialist",
        goal="Help with AI research and provide insights",
        backstory="An AI assistant powered by Qwen, specializing in multi-agent systems",
        model_name=model_name,
        temperature=0.7
    )
    
    print(f"\n✓ Created agent: {agent.name}")
    print(f"  Role: {agent.role}")
    print(f"  Model: {agent.model}")
    
    task = "What are the top 3 benefits of using multi-agent systems?"
    print(f"\nTask: {task}")
    print("\nExecuting with Qwen...")
    
    result = agent.execute(task)
    
    if result['status'] == 'completed':
        print("\n" + "-" * 80)
        print("Agent Response:")
        print("-" * 80)
        print(result['output'])
        print("-" * 80)
        print(f"\n✓ Task completed successfully")
        print(f"  Memory items: {len(agent.get_memory())}")
    else:
        print(f"\n❌ Task failed: {result.get('output', 'Unknown error')}")
        return
    
    # Test 3: Multi-Agent Workflow
    print("\n" + "=" * 80)
    print("Test 3: Multi-Agent Workflow with Qwen")
    print("=" * 80)
    
    # Create two agents with different roles
    researcher = LlamaAgent(
        name="AI Researcher",
        role="Research Analyst",
        goal="Research AI topics thoroughly",
        model_name=model_name,
        temperature=0.5  # More focused
    )
    
    writer = LlamaAgent(
        name="Content Writer",
        role="Technical Writer",
        goal="Create clear, engaging content",
        model_name=model_name,  # Use same model
        temperature=0.8  # More creative
    )
    
    print(f"\n✓ Created 2 agents:")
    print(f"  - {researcher.name} (using {researcher.model})")
    print(f"  - {writer.name} (using {writer.model})")
    
    # Step 1: Research
    print("\n" + "-" * 80)
    print("Phase 1: Research")
    print("-" * 80)
    
    research_task = "List the main challenges in building multi-agent AI systems"
    print(f"Task: {research_task}\n")
    
    research_result = researcher.execute(research_task)
    
    if research_result['status'] == 'completed':
        print("✓ Research completed")
        print(f"Output preview: {research_result['output'][:200]}...")
    else:
        print("❌ Research failed")
        return
    
    # Step 2: Write Summary
    print("\n" + "-" * 80)
    print("Phase 2: Write Summary")
    print("-" * 80)
    
    write_task = "Write a brief summary of the research findings"
    print(f"Task: {write_task}\n")
    
    write_result = writer.execute(
        write_task,
        context={'research_findings': research_result['output']}
    )
    
    if write_result['status'] == 'completed':
        print("Summary:")
        print("-" * 80)
        print(write_result['output'])
        print("-" * 80)
    else:
        print("❌ Writing failed")
        return
    
    # Final Summary
    print("\n" + "=" * 80)
    print("✓ Multi-Agent Workflow Completed Successfully!")
    print("=" * 80)
    print(f"\nWorkflow Summary:")
    print(f"  - Researcher used {researcher.model} (temp={researcher.temperature})")
    print(f"  - Writer used {writer.model} (temp={writer.temperature})")
    print(f"  - Total memory items: {len(researcher.get_memory()) + len(writer.get_memory())}")
    
    print("\n" + "=" * 80)
    print("Next Steps:")
    print("=" * 80)
    print("✓ Your local Qwen models are integrated!")
    print("\nYou can now:")
    print("- Use qwen2.5:7b for complex reasoning tasks")
    print("- Use qwen2.5:3b for faster responses")
    print("- Create custom agents with different Qwen configurations")
    print("- Build multi-agent workflows without API costs")
    print("- Combine Qwen with other agents in your framework")
    print("\nModify this example in: examples/qwen_example.py")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
