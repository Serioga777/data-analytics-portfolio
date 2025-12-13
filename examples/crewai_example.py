"""
Example 3: CrewAI Integration
Demonstrates using CrewAI framework for advanced multi-agent workflows
"""
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


def create_crewai_workflow():
    """Create a CrewAI-based multi-agent workflow"""
    
    print("\n" + "=" * 80)
    print("Multi-Agent Framework - CrewAI Integration Example")
    print("=" * 80 + "\n")
    
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Warning: OPENAI_API_KEY not found in .env file")
        print("Please add your OpenAI API key to the .env file to run this example.")
        print("\nExample .env content:")
        print("OPENAI_API_KEY=sk-your-api-key-here")
        return
    
    print("✓ API key found. Initializing CrewAI agents...\n")
    
    # Define agents with specific roles
    researcher = Agent(
        role='Research Analyst',
        goal='Uncover cutting-edge developments in AI and machine learning',
        backstory="""You are an expert research analyst with a keen eye for detail.
        You excel at finding relevant information and identifying key trends in 
        the AI industry. Your analyses are thorough and well-documented.""",
        verbose=True,
        allow_delegation=False
    )
    
    writer = Agent(
        role='Tech Content Writer',
        goal='Create engaging and informative content about AI developments',
        backstory="""You are a skilled technical writer who can transform complex
        AI concepts into clear, accessible content. Your writing is engaging and
        informative, making technical topics approachable for all audiences.""",
        verbose=True,
        allow_delegation=False
    )
    
    editor = Agent(
        role='Content Editor',
        goal='Ensure content quality and accuracy',
        backstory="""You are a meticulous editor with expertise in technical content.
        You ensure that all content is accurate, well-structured, and free of errors.
        Your feedback helps improve the clarity and impact of technical writing.""",
        verbose=True,
        allow_delegation=False
    )
    
    # Define tasks
    research_task = Task(
        description="""Conduct comprehensive research on the latest multi-agent AI
        systems. Focus on:
        1. Recent breakthroughs and innovations
        2. Key players and frameworks (CrewAI, AutoGen, LangGraph)
        3. Real-world applications
        4. Future trends and challenges
        
        Provide a detailed research report with sources.""",
        agent=researcher,
        expected_output="A comprehensive research report with key findings and sources"
    )
    
    writing_task = Task(
        description="""Using the research findings, write an engaging article about
        multi-agent AI systems. The article should:
        1. Have a compelling introduction
        2. Explain key concepts clearly
        3. Highlight important developments
        4. Include real-world examples
        5. Conclude with future outlook
        
        Target audience: Tech-savvy professionals and developers.""",
        agent=writer,
        expected_output="A well-structured, engaging article (800-1000 words)"
    )
    
    editing_task = Task(
        description="""Review and edit the article for:
        1. Technical accuracy
        2. Clarity and readability
        3. Grammar and style
        4. Logical flow and structure
        5. Overall impact
        
        Provide the final polished version with any corrections noted.""",
        agent=editor,
        expected_output="Polished final article with editorial notes"
    )
    
    # Create crew with sequential process
    crew = Crew(
        agents=[researcher, writer, editor],
        tasks=[research_task, writing_task, editing_task],
        process=Process.sequential,
        verbose=True
    )
    
    print("\n" + "-" * 80)
    print("Starting CrewAI workflow...")
    print("-" * 80 + "\n")
    
    # Execute the workflow
    try:
        result = crew.kickoff()
        
        print("\n" + "=" * 80)
        print("WORKFLOW COMPLETED")
        print("=" * 80)
        print(f"\n{result}\n")
        
        return result
    
    except Exception as e:
        print(f"\n❌ Error executing workflow: {e}")
        print("\nTroubleshooting:")
        print("1. Ensure your OpenAI API key is valid")
        print("2. Check your internet connection")
        print("3. Verify all dependencies are installed")
        return None


def main():
    """Main function to run CrewAI example"""
    result = create_crewai_workflow()
    
    if result:
        print("\n✓ CrewAI multi-agent workflow completed successfully!")
    else:
        print("\n⚠️  Workflow did not complete. Please check the error messages above.")
    
    print("\nNext steps:")
    print("1. Explore the CrewAI documentation: https://docs.crewai.com")
    print("2. Try modifying agent roles and tasks")
    print("3. Add custom tools to your agents")
    print("4. Experiment with different process types (sequential, hierarchical)")


if __name__ == "__main__":
    main()
