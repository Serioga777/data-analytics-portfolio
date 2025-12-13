"""
Example 4: AutoGen Integration
Demonstrates using Microsoft AutoGen for conversational multi-agent systems
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def create_autogen_workflow():
    """Create an AutoGen-based multi-agent workflow"""
    
    print("\n" + "=" * 80)
    print("Multi-Agent Framework - AutoGen Integration Example")
    print("=" * 80 + "\n")
    
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Warning: OPENAI_API_KEY not found in .env file")
        print("Please add your OpenAI API key to the .env file to run this example.")
        print("\nExample .env content:")
        print("OPENAI_API_KEY=sk-your-api-key-here")
        return
    
    try:
        from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
        
        print("✓ API key found. Initializing AutoGen agents...\n")
        
        # Configuration for LLM
        config_list = [{
            "model": "gpt-4-turbo-preview",
            "api_key": os.getenv("OPENAI_API_KEY")
        }]
        
        llm_config = {
            "config_list": config_list,
            "temperature": 0.7,
        }
        
        # Create assistant agent
        assistant = AssistantAgent(
            name="AI_Assistant",
            llm_config=llm_config,
            system_message="""You are a helpful AI assistant specializing in 
            multi-agent systems and AI research. You provide clear, accurate, and 
            well-structured information. When given a task, you break it down into 
            steps and execute them systematically."""
        )
        
        # Create user proxy agent (represents human user)
        user_proxy = UserProxyAgent(
            name="User",
            human_input_mode="NEVER",  # No human input for automation
            max_consecutive_auto_reply=10,
            is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
            code_execution_config={
                "work_dir": "coding",
                "use_docker": False,  # Set to True if Docker is available
            },
        )
        
        print("-" * 80)
        print("Starting AutoGen conversation...")
        print("-" * 80 + "\n")
        
        # Initiate conversation
        task = """Analyze the benefits and challenges of multi-agent AI systems.
        Provide:
        1. Three key benefits
        2. Three main challenges
        3. A brief recommendation for when to use multi-agent systems
        
        Format your response clearly with headers."""
        
        user_proxy.initiate_chat(
            assistant,
            message=task
        )
        
        print("\n" + "=" * 80)
        print("CONVERSATION COMPLETED")
        print("=" * 80)
        
        return True
        
    except ImportError:
        print("❌ Error: AutoGen not properly installed")
        print("\nTo fix this, run:")
        print("pip install pyautogen")
        return False
    
    except Exception as e:
        print(f"\n❌ Error executing workflow: {e}")
        print("\nTroubleshooting:")
        print("1. Ensure your OpenAI API key is valid")
        print("2. Check your internet connection")
        print("3. Verify AutoGen is installed: pip install pyautogen")
        return False


def main():
    """Main function to run AutoGen example"""
    result = create_autogen_workflow()
    
    if result:
        print("\n✓ AutoGen multi-agent workflow completed successfully!")
    else:
        print("\n⚠️  Workflow did not complete. Please check the error messages above.")
    
    print("\nNext steps:")
    print("1. Explore AutoGen documentation: https://microsoft.github.io/autogen/")
    print("2. Try group chat with multiple agents")
    print("3. Enable code execution capabilities")
    print("4. Experiment with different conversation patterns")


if __name__ == "__main__":
    main()
