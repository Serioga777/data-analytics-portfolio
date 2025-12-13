"""
Example: Local Llama Integration
Demonstrates using local Llama models via Ollama
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


def check_ollama_setup():
    """Check if Ollama is running and has models"""
    print("=" * 80)
    print("Checking Ollama Setup")
    print("=" * 80)
    
    llm = LocalLlamaLLM()
    
    # Check connection
    if llm.check_connection():
        print("✓ Ollama is running")
        
        # List available models
        models = llm.list_models()
        if models:
            print(f"✓ Available models: {', '.join(models)}")
            return True, models[0]
        else:
            print("⚠️  No models found. Pull a model with: ollama pull llama2")
            return False, None
    else:
        print("❌ Ollama is not running")
        print("\nTo start Ollama:")
        print("1. Make sure Ollama is installed")
        print("2. Run: ollama serve")
        print("3. Pull a model: ollama pull llama2")
        return False, None


def test_basic_llm():
    """Test basic LLM functionality"""
    print("\n" + "=" * 80)
    print("Test 1: Basic LLM Generation")
    print("=" * 80)
    
    llm = LocalLlamaLLM(model_name="llama2")
    
    prompt = "Explain what a multi-agent AI system is in 2-3 sentences."
    print(f"\nPrompt: {prompt}")
    print("\nGenerating response...")
    
    response = llm.generate(prompt)
    
    if response['success']:
        print("\n" + "-" * 80)
        print("Response:")
        print("-" * 80)
        print(response['content'])
        print("-" * 80)
        return True
    else:
        print(f"\n❌ Error: {response.get('error', 'Unknown error')}")
        return False


def test_llama_agent():
    """Test Llama-powered agent"""
    print("\n" + "=" * 80)
    print("Test 2: Llama-Powered Agent")
    print("=" * 80)
    
    # Create Llama agent
    agent = LlamaAgent(
        name="Research Assistant",
        role="AI Research Specialist",
        goal="Help with AI research and provide insights",
        backstory="An AI assistant specializing in multi-agent systems research",
        model_name="llama2"
    )
    
    print(f"\n✓ Created agent: {agent.name}")
    print(f"  Role: {agent.role}")
    print(f"  Model: {agent.model}")
    
    # Execute task
    task = "What are the key benefits of using multi-agent systems in AI?"
    print(f"\nTask: {task}")
    print("\nExecuting with local Llama...")
    
    result = agent.execute(task)
    
    if result['status'] == 'completed':
        print("\n" + "-" * 80)
        print("Agent Response:")
        print("-" * 80)
        print(result['output'])
        print("-" * 80)
        print(f"\n✓ Task completed successfully")
        print(f"  Memory items: {len(agent.get_memory())}")
        return True
    else:
        print(f"\n❌ Task failed: {result.get('output', 'Unknown error')}")
        return False


def test_multi_agent_workflow():
    """Test multiple Llama agents working together"""
    print("\n" + "=" * 80)
    print("Test 3: Multi-Agent Workflow with Local Llama")
    print("=" * 80)
    
    # Create multiple agents
    researcher = LlamaAgent(
        name="AI Researcher",
        role="Research Analyst",
        goal="Research and gather information about AI topics",
        model_name="llama2",
        temperature=0.5
    )
    
    summarizer = LlamaAgent(
        name="Summarizer",
        role="Content Summarizer",
        goal="Create concise summaries of complex information",
        model_name="llama2",
        temperature=0.3
    )
    
    print("\n✓ Created 2 agents:")
    print(f"  - {researcher.name} (Research)")
    print(f"  - {summarizer.name} (Summarization)")
    
    # Step 1: Research
    print("\n" + "-" * 80)
    print("Step 1: Research Phase")
    print("-" * 80)
    research_task = "List 3 key challenges in multi-agent AI systems"
    print(f"Task: {research_task}")
    
    research_result = researcher.execute(research_task)
    
    if research_result['status'] != 'completed':
        print(f"❌ Research failed: {research_result.get('output', 'Unknown error')}")
        return False
    
    print("\nResearch Output:")
    print(research_result['output'][:300] + "...")
    
    # Step 2: Summarize
    print("\n" + "-" * 80)
    print("Step 2: Summarization Phase")
    print("-" * 80)
    summary_task = "Summarize the key points from the research"
    print(f"Task: {summary_task}")
    
    summary_result = summarizer.execute(
        summary_task,
        context={'research': research_result['output']}
    )
    
    if summary_result['status'] != 'completed':
        print(f"❌ Summarization failed")
        return False
    
    print("\nSummary Output:")
    print(summary_result['output'])
    
    print("\n" + "=" * 80)
    print("✓ Multi-agent workflow completed successfully!")
    print("=" * 80)
    
    return True


def main():
    """Main function"""
    print("\n" + "=" * 80)
    print("Multi-Agent Framework - Local Llama Integration")
    print("=" * 80)
    
    # Check Ollama setup
    is_ready, model_name = check_ollama_setup()
    
    if not is_ready:
        print("\n" + "=" * 80)
        print("Setup Instructions")
        print("=" * 80)
        print("\n1. Install Ollama:")
        print("   - Windows: Download from https://ollama.ai")
        print("   - Install and restart your terminal")
        print("\n2. Start Ollama:")
        print("   ollama serve")
        print("\n3. Pull a model (in a new terminal):")
        print("   ollama pull llama2")
        print("   # Or try: llama3, mistral, codellama")
        print("\n4. Run this script again")
        print("=" * 80)
        return
    
    print("\n✓ Ollama is ready! Running tests...\n")
    
    # Run tests
    test1_passed = test_basic_llm()
    
    if test1_passed:
        test2_passed = test_llama_agent()
        
        if test2_passed:
            test_multi_agent_workflow()
    
    print("\n" + "=" * 80)
    print("Testing Complete")
    print("=" * 80)
    print("\nYour local Llama integration is working!")
    print("\nNext steps:")
    print("- Modify agent prompts in agents/llama_agent.py")
    print("- Try different Ollama models (llama3, mistral, codellama)")
    print("- Build custom workflows with multiple Llama agents")
    print("- Integrate with your existing agents")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
