"""
Money-Making Research System
AI agents to help identify and research income opportunities
"""
import logging
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.llama_agent import LlamaAgent

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def create_money_research_agents():
    """Create specialized agents for income opportunity research"""
    
    # Opportunity Scout - Finds income opportunities
    opportunity_scout = LlamaAgent(
        name="Opportunity Scout",
        role="Income Opportunity Researcher",
        goal="Identify viable ways to earn money online and offline",
        backstory="""You are an expert at identifying income opportunities. 
        You research freelancing, online businesses, side hustles, passive income,
        and other money-making methods. You evaluate opportunities based on
        required skills, startup costs, time commitment, and earning potential.""",
        model_name="qwen2.5:3b",
        temperature=0.6
    )
    
    # Market Analyst - Analyzes market demand and competition
    market_analyst = LlamaAgent(
        name="Market Analyst",
        role="Market Research Specialist",
        goal="Analyze market demand, competition, and profitability",
        backstory="""You are a market research expert who evaluates business 
        opportunities. You analyze market trends, competition levels, pricing 
        strategies, and profit margins. You provide realistic assessments of 
        earning potential and market saturation.""",
        model_name="qwen2.5:3b",
        temperature=0.5
    )
    
    # Action Planner - Creates actionable plans
    action_planner = LlamaAgent(
        name="Action Planner",
        role="Strategic Action Planner",
        goal="Create step-by-step action plans to start earning",
        backstory="""You are a strategic planner who creates detailed, actionable 
        plans. You break down complex goals into simple steps, identify required 
        resources, set realistic timelines, and anticipate potential obstacles. 
        You focus on practical, achievable actions.""",
        model_name="qwen2.5:3b",
        temperature=0.7
    )
    
    return {
        'scout': opportunity_scout,
        'analyst': market_analyst,
        'planner': action_planner
    }


def research_money_making_opportunities(user_skills=None, available_time=None, budget=None):
    """
    Research income opportunities based on user's situation
    
    Args:
        user_skills: List of skills or "general"
        available_time: Time available (e.g., "2 hours/day", "weekends")
        budget: Starting budget (e.g., "$0", "$100", "$500")
    """
    print("\n" + "=" * 80)
    print("MONEY-MAKING RESEARCH SYSTEM")
    print("=" * 80)
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()
    
    # Get user input if not provided
    if user_skills is None:
        print("What skills do you have? (or type 'general' for any opportunity)")
        user_skills = input("> ").strip() or "general skills"
    
    if available_time is None:
        print("\nHow much time can you dedicate? (e.g., '2 hours/day', 'weekends')")
        available_time = input("> ").strip() or "flexible"
    
    if budget is None:
        print("\nWhat's your starting budget? (e.g., '$0', '$100', '$500')")
        budget = input("> ").strip() or "$0"
    
    print("\n" + "=" * 80)
    print(f"Researching opportunities for:")
    print(f"  Skills: {user_skills}")
    print(f"  Time: {available_time}")
    print(f"  Budget: {budget}")
    print("=" * 80)
    
    # Create agents
    agents = create_money_research_agents()
    
    # Phase 1: Opportunity Discovery
    print("\n" + "-" * 80)
    print("PHASE 1: OPPORTUNITY DISCOVERY")
    print("-" * 80)
    
    scout_task = f"""Based on these criteria, identify 5 realistic income opportunities:
    
    Skills: {user_skills}
    Available time: {available_time}
    Starting budget: {budget}
    
    For each opportunity, provide:
    1. Name and brief description
    2. Estimated earning potential (realistic range)
    3. Required skills/knowledge
    4. Startup costs
    5. Time to first income
    
    Focus on opportunities that are actually achievable and profitable in 2025."""
    
    print("\n🔍 Opportunity Scout is researching...\n")
    opportunities_result = agents['scout'].execute(scout_task)
    
    if opportunities_result['status'] != 'completed':
        print("❌ Opportunity discovery failed")
        return
    
    print(opportunities_result['output'])
    
    # Phase 2: Market Analysis
    print("\n" + "-" * 80)
    print("PHASE 2: MARKET ANALYSIS")
    print("-" * 80)
    
    analyst_task = f"""Analyze these income opportunities and provide insights:
    
    {opportunities_result['output'][:1000]}
    
    For the top 3 opportunities, analyze:
    1. Market demand (high/medium/low)
    2. Competition level
    3. Profit margins
    4. Scalability potential
    5. Risk factors
    
    Rank them by best overall potential for someone with these constraints:
    - Skills: {user_skills}
    - Time: {available_time}
    - Budget: {budget}"""
    
    print("\n📊 Market Analyst is evaluating...\n")
    analysis_result = agents['analyst'].execute(analyst_task)
    
    if analysis_result['status'] != 'completed':
        print("❌ Market analysis failed")
        return
    
    print(analysis_result['output'])
    
    # Phase 3: Action Planning
    print("\n" + "-" * 80)
    print("PHASE 3: ACTION PLAN")
    print("-" * 80)
    
    planner_task = f"""Create a detailed 30-day action plan for the #1 ranked opportunity.
    
    Market Analysis Results:
    {analysis_result['output'][:1000]}
    
    Create a week-by-week plan that includes:
    
    Week 1: Setup & Learning
    - Specific actions to take
    - Resources to gather
    - Skills to learn
    
    Week 2: Building & Preparing
    - What to create/build
    - How to get started
    
    Week 3: Launch & Marketing
    - How to find first customers/clients
    - Marketing strategies
    
    Week 4: Scaling & Optimization
    - How to increase income
    - Next steps
    
    Make it specific and actionable. Each task should be clear and doable."""
    
    print("\n📋 Action Planner is creating your roadmap...\n")
    plan_result = agents['planner'].execute(planner_task)
    
    if plan_result['status'] != 'completed':
        print("❌ Action planning failed")
        return
    
    print(plan_result['output'])
    
    # Generate Summary Report
    print("\n" + "=" * 80)
    print("RESEARCH COMPLETE - SUMMARY")
    print("=" * 80)
    
    summary = f"""
Research completed for: {user_skills} | {available_time} | {budget}

Agents deployed:
  ✓ Opportunity Scout - Identified income opportunities
  ✓ Market Analyst - Evaluated market potential
  ✓ Action Planner - Created 30-day plan

Next Steps:
1. Review the opportunities identified above
2. Focus on the #1 ranked opportunity
3. Follow the 30-day action plan
4. Start with Week 1 tasks immediately
5. Track progress and adjust as needed

💡 Pro Tips:
- Start small and test the market
- Focus on one opportunity at a time
- Take action within 24 hours
- Learn as you earn
- Reinvest profits to scale

Your AI research team has done the analysis.
Now it's time for YOU to take action! 🚀
"""
    
    print(summary)
    
    # Save report
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = f"money_research_report_{timestamp}.txt"
    
    try:
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("MONEY-MAKING RESEARCH REPORT\n")
            f.write("=" * 80 + "\n\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"Your Profile:\n")
            f.write(f"  Skills: {user_skills}\n")
            f.write(f"  Time: {available_time}\n")
            f.write(f"  Budget: {budget}\n\n")
            f.write("-" * 80 + "\n")
            f.write("OPPORTUNITIES DISCOVERED\n")
            f.write("-" * 80 + "\n\n")
            f.write(opportunities_result['output'] + "\n\n")
            f.write("-" * 80 + "\n")
            f.write("MARKET ANALYSIS\n")
            f.write("-" * 80 + "\n\n")
            f.write(analysis_result['output'] + "\n\n")
            f.write("-" * 80 + "\n")
            f.write("30-DAY ACTION PLAN\n")
            f.write("-" * 80 + "\n\n")
            f.write(plan_result['output'] + "\n\n")
            f.write("=" * 80 + "\n")
            f.write(summary)
        
        print(f"\n✅ Full report saved to: {report_file}")
    except Exception as e:
        print(f"\n⚠️  Could not save report: {e}")
    
    print("\n" + "=" * 80 + "\n")
    
    return {
        'opportunities': opportunities_result,
        'analysis': analysis_result,
        'plan': plan_result
    }


def quick_research_mode():
    """Quick mode with preset profiles"""
    print("\n" + "=" * 80)
    print("QUICK RESEARCH PROFILES")
    print("=" * 80)
    print("\nChoose a profile or enter 0 for custom:")
    print("\n1. Developer/Tech Skills")
    print("   Skills: Programming, web development")
    print("   Time: 2-3 hours/day after work")
    print("   Budget: $0")
    print("\n2. Creative/Design Skills")
    print("   Skills: Graphic design, writing, video editing")
    print("   Time: Weekends")
    print("   Budget: $100")
    print("\n3. No Special Skills")
    print("   Skills: General/willing to learn")
    print("   Time: Flexible")
    print("   Budget: $0")
    print("\n4. Business/Marketing Background")
    print("   Skills: Marketing, sales, business")
    print("   Time: 4-5 hours/day")
    print("   Budget: $500")
    
    choice = input("\nEnter choice (0-4): ").strip()
    
    profiles = {
        '1': ("Programming, web development, tech", "2-3 hours/day", "$0"),
        '2': ("Graphic design, writing, video editing", "Weekends", "$100"),
        '3': ("General skills, willing to learn anything", "Flexible schedule", "$0"),
        '4': ("Marketing, sales, business strategy", "4-5 hours/day", "$500")
    }
    
    if choice in profiles:
        skills, time, budget = profiles[choice]
        return research_money_making_opportunities(skills, time, budget)
    else:
        return research_money_making_opportunities()


def main():
    """Main function"""
    print("\n" + "=" * 80)
    print("💰 AI MONEY-MAKING RESEARCH SYSTEM 💰")
    print("=" * 80)
    print("\nYour personal AI team will research income opportunities for you!")
    print("\nMode options:")
    print("1. Quick Research (choose from preset profiles)")
    print("2. Custom Research (enter your specific details)")
    
    mode = input("\nSelect mode (1 or 2): ").strip()
    
    if mode == '1':
        quick_research_mode()
    else:
        research_money_making_opportunities()


if __name__ == "__main__":
    main()
