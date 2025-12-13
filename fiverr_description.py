"""
Fiverr Profile Description Generator
Creates compelling profile descriptions for web developers
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.llama_agent import LlamaAgent

print("\n" + "=" * 80)
print("✍️ FIVERR PROFILE DESCRIPTION GENERATOR")
print("=" * 80)
print()

# Create specialized agent
description_writer = LlamaAgent(
    name="Fiverr Profile Writer",
    role="Freelance Profile Copywriter",
    goal="Write compelling Fiverr descriptions that attract clients",
    backstory="""You are an expert at writing Fiverr profile descriptions that convert 
    visitors into clients. You know how to highlight skills, show value, build trust, 
    and include keywords that help profiles rank in searches. You write in a confident, 
    professional yet approachable tone.""",
    model_name="qwen2.5:3b",
    temperature=0.7
)

print("Let's create your Fiverr profile description!\n")
print("Answer a few quick questions (or press Enter to skip):\n")

# Gather info
experience = input("Your experience level (beginner/intermediate/expert) [beginner]: ").strip() or "beginner"
skills = input("Main skills (e.g., HTML, CSS, JavaScript, WordPress) [web development]: ").strip() or "HTML, CSS, JavaScript, responsive design"
speciality = input("What you specialize in (e.g., landing pages, e-commerce) [websites]: ").strip() or "modern, responsive websites"
ai_tools = input("Do you use AI tools? (yes/no) [yes]: ").strip().lower() or "yes"

print("\n" + "=" * 80)
print("GENERATING YOUR DESCRIPTION...")
print("=" * 80)
print()

# Create the task
task = f"""Write a compelling Fiverr profile description for a web developer with these details:

Experience Level: {experience}
Skills: {skills}
Specialization: {speciality}
Uses AI tools: {ai_tools}

Requirements:
- Minimum 150 characters
- Maximum 600 characters (Fiverr limit)
- Confident and professional tone
- Focus on VALUE to clients (what they get)
- Include relevant keywords for SEO
- Mention quick turnaround and quality
- Build trust even if beginner
- End with a call-to-action

If beginner, emphasize:
- Dedication to quality
- Modern tools and practices
- Competitive pricing
- Fast communication
- Willing to revise until perfect

Write 3 different versions:
1. SHORT VERSION (150-200 characters) - Punchy and direct
2. MEDIUM VERSION (300-400 characters) - Balanced
3. LONG VERSION (500-600 characters) - Detailed

Make them ready to copy-paste directly into Fiverr!"""

print("🤖 AI Agent is writing your descriptions...\n")

result = description_writer.execute(task)

if result['status'] == 'completed':
    print(result['output'])
    print("\n" + "=" * 80)

print("\n" + "=" * 80)
print("BONUS: PROFILE OPTIMIZATION TIPS")
print("=" * 80)
print("""
✅ KEYWORDS TO INCLUDE (for SEO):
   - Web developer, web design, responsive
   - HTML, CSS, JavaScript
   - WordPress, landing page, website
   - Fast turnaround, professional
   - Modern, clean, mobile-friendly

✅ POWER WORDS THAT WORK:
   - Professional, modern, responsive
   - Fast, reliable, dedicated
   - Custom, tailored, quality
   - Affordable, competitive
   - Guaranteed, committed

✅ AVOID:
   ❌ "New to Fiverr" (say "new seller" if anything)
   ❌ "Cheap" (say "affordable" or "competitive")
   ❌ "Please give me a chance"
   ❌ Spelling/grammar errors
   ❌ ALL CAPS or excessive emojis

✅ CALL-TO-ACTION EXAMPLES:
   - "Let's bring your vision to life!"
   - "Message me to get started!"
   - "Ready to create something amazing?"
   - "Contact me before ordering to discuss your project!"

✅ STRUCTURE TIPS:
   [Hook] → [Skills/Value] → [What You Offer] → [CTA]
   
   Example:
   "Hi! I create modern, responsive websites that look great on any device. 
   [Skills] With expertise in HTML, CSS, JavaScript, and WordPress, 
   [Value] I deliver professional results quickly. 
   [Offer] Whether you need a landing page, portfolio, or business site, 
   [CTA] let's bring your vision to life!"
""")

print("\n" + "=" * 80)
print("NEXT STEPS:")
print("=" * 80)
print("""
1. ✅ Choose your favorite version (or mix the best parts)
2. ✅ Copy it to Fiverr profile description
3. ✅ Add relevant keywords from the list above
4. ✅ Make sure it's 150+ characters
5. ✅ Proofread for typos
6. ✅ Save and publish your profile!

QUICK CHECKS:
□ Does it sound confident (not desperate)?
□ Does it focus on what CLIENT gets (not what you need)?
□ Does it include your main skills?
□ Is it free of typos?
□ Does it end with action?

Your profile description is ready! 🚀
""")
print("=" * 80 + "\n")
