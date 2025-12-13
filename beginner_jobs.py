"""
Beginner Jobs Finder with AI Assistant
Find easy starter projects and learn how AI can help you complete them
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


def create_job_finder_agents():
    """Create specialized agents for finding beginner jobs"""
    
    # Beginner Jobs Scout
    job_scout = LlamaAgent(
        name="Beginner Jobs Scout",
        role="Entry-Level Opportunity Finder",
        goal="Find easy starter projects perfect for beginners with no experience",
        backstory="""You specialize in finding beginner-friendly freelance jobs and 
        projects that require minimal experience. You know which platforms have the 
        easiest entry points, what clients are willing to hire beginners for, and 
        which types of projects are simple enough to complete with AI assistance.""",
        model_name="qwen2.5:3b",
        temperature=0.6
    )
    
    # AI Tools Expert
    ai_tools_expert = LlamaAgent(
        name="AI Tools Specialist",
        role="AI-Assisted Work Expert",
        goal="Show how to use AI tools to complete projects easily",
        backstory="""You are an expert at using AI tools like ChatGPT, Claude, GitHub 
        Copilot, and other AI assistants to help beginners complete professional work. 
        You know exactly which AI tools to use for each task and how to use them 
        effectively to deliver quality results.""",
        model_name="qwen2.5:3b",
        temperature=0.7
    )
    
    # Quick Win Strategist
    quick_win_strategist = LlamaAgent(
        name="Quick Win Strategist",
        role="First Project Success Coach",
        goal="Create strategies for landing and completing your first paid project",
        backstory="""You specialize in helping complete beginners get their first 
        client and successfully complete their first project. You focus on quick wins, 
        confidence building, and creating momentum for new freelancers.""",
        model_name="qwen2.5:3b",
        temperature=0.6
    )
    
    return {
        'scout': job_scout,
        'ai_expert': ai_tools_expert,
        'strategist': quick_win_strategist
    }


def find_beginner_jobs():
    """Find beginner-friendly jobs that can be done with AI help"""
    
    print("\n" + "=" * 80)
    print("🚀 BEGINNER-FRIENDLY JOBS FINDER")
    print("No Experience Needed - AI Will Help You!")
    print("=" * 80)
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    
    agents = create_job_finder_agents()
    
    # Phase 1: Find Easy Starter Jobs
    print("=" * 80)
    print("PHASE 1: BEGINNER-FRIENDLY JOBS & PROJECTS")
    print("=" * 80)
    print("🔍 Beginner Jobs Scout searching for opportunities...\n")
    
    jobs_task = """Find and list 10 beginner-friendly jobs/projects that someone with 
NO experience can start doing TODAY with AI assistance:

For each job type, provide:

1. JOB/PROJECT TYPE
2. DIFFICULTY LEVEL (Super Easy / Easy / Moderate)
3. WHAT YOU'LL DO (simple description)
4. SKILLS NEEDED (be honest - very minimal)
5. WHERE TO FIND JOBS (specific platforms)
6. TYPICAL PAY (realistic for beginners)
7. TIME TO COMPLETE (estimated hours)
8. WHY IT'S BEGINNER-FRIENDLY

Focus on:
- Jobs that don't require portfolio
- Tasks that AI can help with significantly
- Quick turnaround projects
- Low barrier to entry
- Real demand in market

Categories to consider:
- Data entry & web research
- Simple website edits
- Content writing/blog posts
- Social media posts
- Basic graphic design
- Excel/spreadsheet work
- Email management
- Product descriptions
- Simple WordPress tasks
- Virtual assistant tasks

Make it practical and actionable for someone starting TODAY."""

    jobs_result = agents['scout'].execute(jobs_task)
    
    if jobs_result['status'] == 'completed':
        print(jobs_result['output'])
        print("\n✅ Job opportunities identified\n")
    
    # Phase 2: AI Tools for Each Job Type
    print("=" * 80)
    print("PHASE 2: AI TOOLS TO HELP YOU SUCCEED")
    print("=" * 80)
    print("🤖 AI Tools Specialist showing you how to use AI...\n")
    
    ai_tools_task = f"""Based on the beginner jobs identified, explain HOW TO USE AI 
to complete each type of project:

Create a practical guide for using AI tools:

1. CONTENT WRITING JOBS
   - Which AI: ChatGPT, Claude, Gemini
   - Exact prompts to use
   - How to edit AI output to make it sound human
   - Quality check steps

2. WEB RESEARCH & DATA ENTRY
   - AI tools for research (Perplexity, ChatGPT)
   - How to organize data with AI help
   - Automation tricks

3. SOCIAL MEDIA CONTENT
   - AI tools for posts (ChatGPT, Jasper)
   - Image creation (DALL-E, Midjourney, Canva AI)
   - Hashtag generation

4. SIMPLE DESIGN WORK
   - Canva with AI features
   - Remove.bg for backgrounds
   - AI image editors

5. WEBSITE EDITS
   - ChatGPT for code help
   - How to ask for HTML/CSS help
   - Testing and debugging with AI

6. EMAIL & ADMIN TASKS
   - AI email writing
   - Template creation
   - Automation ideas

For EACH category provide:
- Specific AI tool names (free ones prioritized)
- Step-by-step workflow
- Example prompts to use
- Pro tips for best results
- Common mistakes to avoid

Make it a complete "cheat sheet" for using AI to do professional work.

Previous research context:
{jobs_result['output'][:500]}..."""

    ai_tools_result = agents['ai_expert'].execute(ai_tools_task)
    
    if ai_tools_result['status'] == 'completed':
        print(ai_tools_result['output'])
        print("\n✅ AI tools guide complete\n")
    
    # Phase 3: Quick Win Strategy
    print("=" * 80)
    print("PHASE 3: YOUR FIRST PROJECT ACTION PLAN")
    print("=" * 80)
    print("🎯 Quick Win Strategist creating your roadmap...\n")
    
    strategy_task = """Create a detailed action plan for landing and completing the 
FIRST paid project within 7 days:

DAY 1-2: SETUP & PREPARATION
- Which platform to join first (and why)
- How to create a basic profile (even with no experience)
- What to say in your bio/description
- How to find your first project to bid on

DAY 3-4: APPLYING FOR JOBS
- How to write proposals that get responses (templates)
- Which jobs to apply for (specific criteria)
- How many applications to send
- What to charge (specific numbers for beginners)
- How to handle "no experience" objection

DAY 5-6: LANDING THE JOB
- How to communicate with potential clients
- What questions to ask
- How to negotiate (or not)
- Setting expectations
- Getting the contract

DAY 7+: COMPLETING THE PROJECT
- Step-by-step workflow with AI assistance
- Quality checklist before delivery
- How to ask for revisions if needed
- Delivery best practices
- Getting testimonials/reviews

EMERGENCY TIPS:
- What if no one responds to proposals?
- What if you get stuck on the work?
- How to handle difficult clients
- When to use AI and when not to

CONFIDENCE BOOSTERS:
- Remember: Everyone starts somewhere
- First project is about learning
- You have AI as your assistant
- Start small, build from there

Include specific examples and actual numbers/prices."""

    strategy_result = agents['strategist'].execute(strategy_task)
    
    if strategy_result['status'] == 'completed':
        print(strategy_result['output'])
        print("\n✅ Action plan complete\n")
    
    # Save Complete Guide
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = f"beginner_jobs_guide_{timestamp}.txt"
    
    try:
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("BEGINNER JOBS GUIDE - START EARNING WITH AI HELP\n")
            f.write("=" * 80 + "\n\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("Perfect for: Complete beginners with NO experience\n")
            f.write("Goal: Land your first paid project within 7 days\n\n")
            
            f.write("=" * 80 + "\n")
            f.write("PART 1: BEGINNER-FRIENDLY JOB OPPORTUNITIES\n")
            f.write("=" * 80 + "\n\n")
            f.write(jobs_result['output'] + "\n\n")
            
            f.write("=" * 80 + "\n")
            f.write("PART 2: AI TOOLS CHEAT SHEET\n")
            f.write("=" * 80 + "\n\n")
            f.write(ai_tools_result['output'] + "\n\n")
            
            f.write("=" * 80 + "\n")
            f.write("PART 3: 7-DAY ACTION PLAN\n")
            f.write("=" * 80 + "\n\n")
            f.write(strategy_result['output'] + "\n\n")
            
            f.write("=" * 80 + "\n")
            f.write("QUICK START CHECKLIST\n")
            f.write("=" * 80 + "\n\n")
            f.write("""
TODAY (Next 2 Hours):
□ Sign up on Fiverr or Upwork
□ Create basic profile (use AI to help write it)
□ Set up ChatGPT free account
□ Read through Part 1 of this guide
□ Pick ONE job type to focus on

TOMORROW:
□ Complete your profile
□ Practice with AI tools for your chosen job type
□ Write 3 proposal templates with AI help
□ Find 5 jobs you could apply for
□ Apply to your first 2-3 jobs

DAY 3-4:
□ Apply to 5-10 more jobs
□ Respond to any messages quickly
□ Lower price if needed for first client
□ Keep practicing with AI tools

DAY 5-7:
□ Land your first client
□ Complete the work with AI assistance
□ Deliver high quality results
□ Ask for review/testimonial
□ Apply lessons learned

REMEMBER:
✅ You don't need to be an expert
✅ AI is your co-pilot
✅ Start small and simple
✅ First project builds confidence
✅ Everyone started where you are

FREE AI TOOLS TO USE RIGHT NOW:
- ChatGPT (chatgpt.com) - FREE
- Claude (claude.ai) - FREE
- Gemini (gemini.google.com) - FREE
- Canva (canva.com) - FREE tier
- Grammarly - FREE basic

MINDSET:
"I may be a beginner, but I have AI tools that make me capable.
I can learn as I earn. I will start small and grow from there.
My first project is just the beginning."

NOW GO APPLY FOR YOUR FIRST JOB! 🚀
""")
        
        print(f"✅ Complete guide saved to: {report_file}\n")
    
    except Exception as e:
        print(f"⚠️  Could not save report: {e}\n")
    
    # Print Final Summary
    print("=" * 80)
    print("RESEARCH COMPLETE - YOU'RE READY TO START!")
    print("=" * 80)
    print("""
Your AI agents have created a complete beginner's guide:

✅ 10 beginner-friendly job types identified
✅ AI tools cheat sheet created
✅ 7-day action plan ready
✅ All saved to your guide file

EASIEST JOBS TO START WITH TODAY:
1. Content writing (blog posts, articles)
2. Data entry and web research  
3. Social media post creation
4. Product descriptions
5. Simple email management

BEST PLATFORMS FOR BEGINNERS:
- Fiverr (easiest to start)
- Upwork (more opportunities)
- Freelancer (good for data entry)

YOUR NEXT STEPS:
1. Read the complete guide
2. Sign up on ONE platform today
3. Set up ChatGPT (free)
4. Create your profile
5. Apply for 3 jobs tomorrow

YOU CAN DO THIS! 💪

Remember: AI is your secret weapon. Use it wisely, edit the output,
and deliver quality work. Your first $50-100 is just days away!

""")
    print("=" * 80 + "\n")
    
    return {
        'jobs': jobs_result,
        'ai_tools': ai_tools_result,
        'strategy': strategy_result
    }


def main():
    """Run beginner jobs finder"""
    find_beginner_jobs()


if __name__ == "__main__":
    main()
