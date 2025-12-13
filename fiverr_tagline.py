"""
Fiverr Tagline Generator
Creates attention-grabbing taglines for Fiverr gigs
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.llama_agent import LlamaAgent

print("\n" + "=" * 80)
print("✨ FIVERR TAGLINE GENERATOR")
print("=" * 80)
print()

# Create tagline expert agent
tagline_expert = LlamaAgent(
    name="Fiverr Tagline Copywriter",
    role="Conversion-Focused Copywriting Specialist",
    goal="Create compelling, click-worthy taglines that attract buyers and stand out in search",
    backstory="""You are an expert copywriter who specializes in creating powerful, 
    attention-grabbing taglines for Fiverr gigs. You understand buyer psychology, 
    what makes people click, and how to communicate value in just a few words. 
    You know the perfect balance of professionalism and personality.""",
    model_name="qwen2.5:3b",
    temperature=0.8
)

print("Creating attention-grabbing taglines for your gig...\n")

task = """Create taglines for a Fiverr landing page creation gig.

SERVICE: Landing page design and development
SKILLS: HTML, CSS, JavaScript, responsive design
TARGET AUDIENCE: Small businesses, startups, entrepreneurs
VALUE PROPOSITION: Fast, professional, conversion-focused landing pages

REQUIREMENTS:
- Short and punchy (max 80 characters)
- Describes what you do clearly
- Shows value/benefit
- Professional but friendly
- Makes buyer want to click
- SEO-friendly when possible

Provide:

1. TOP 10 TAGLINE OPTIONS (ranked best to worst)
2. TAGLINE FORMULAS (templates to create your own)
3. WHAT MAKES A GOOD TAGLINE (psychology)
4. TAGLINES TO AVOID (common mistakes)

Focus on conversion and click-through rate."""

print("🤖 AI Expert is crafting your taglines...\n")

result = tagline_expert.execute(task)

if result['status'] == 'completed':
    print(result['output'])

print("\n" + "=" * 80)
print("🏆 TOP 10 TAGLINE OPTIONS")
print("=" * 80)
print("""
Copy any of these directly into Fiverr:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1️⃣ "Converting visitors into customers with stunning landing pages" ⭐
   (65 chars) - BEST OVERALL
   ✅ Shows benefit (conversion)
   ✅ Describes what you do (landing pages)
   ✅ Professional tone

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2️⃣ "Fast, responsive landing pages that turn clicks into sales"
   (59 chars) - SALES FOCUSED
   ✅ Shows speed (fast)
   ✅ Shows outcome (sales)
   ✅ Action-oriented

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3️⃣ "Professional landing pages for startups and small businesses"
   (63 chars) - TARGET AUDIENCE FOCUS
   ✅ Identifies ideal clients
   ✅ Professional positioning
   ✅ Clear service

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4️⃣ "Modern, mobile-friendly landing pages delivered in 48 hours"
   (61 chars) - SPEED + QUALITY
   ✅ Modern (up-to-date)
   ✅ Mobile focus (important!)
   ✅ Fast delivery promise

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5️⃣ "I create landing pages that look great and convert better"
   (59 chars) - BENEFIT FOCUSED
   ✅ Design + performance
   ✅ Clear value proposition
   ✅ Confident tone

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6️⃣ "Affordable, high-converting landing pages for your business"
   (62 chars) - VALUE PROPOSITION
   ✅ Affordable (attracts budget buyers)
   ✅ High-converting (benefit)
   ✅ Business focus

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
7️⃣ "Custom landing pages built with HTML, CSS & modern design"
   (60 chars) - TECHNICAL + DESIGN
   ✅ Shows custom work
   ✅ Lists technologies
   ✅ Modern appeal

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
8️⃣ "Get your product online fast with a beautiful landing page"
   (62 chars) - URGENCY + BENEFIT
   ✅ Speed (fast)
   ✅ Design (beautiful)
   ✅ Action-oriented (get)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
9️⃣ "Responsive landing pages designed to capture leads & boost sales"
   (67 chars) - COMPREHENSIVE
   ✅ Responsive (SEO keyword)
   ✅ Two benefits (leads + sales)
   ✅ Active verbs

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔟 "Landing pages that work on any device and convert like crazy"
   (64 chars) - CASUAL + CONFIDENT
   ✅ Mobile-friendly message
   ✅ Personality ("like crazy")
   ✅ Performance focused
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

print("\n" + "=" * 80)
print("📝 TAGLINE FORMULAS (Create Your Own)")
print("=" * 80)
print("""
Use these proven formulas to craft custom taglines:

FORMULA 1: [Benefit] + [Service] + [Target Audience]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Example: "High-converting landing pages for ambitious startups"
Template: "[adjective] [service] for [target audience]"

FORMULA 2: [Action] + [Outcome/Benefit]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Example: "Building landing pages that turn visitors into buyers"
Template: "[verb] [service] that [benefit]"

FORMULA 3: [Feature] + [Feature] + [Promise]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Example: "Fast, mobile-friendly landing pages delivered in 48 hours"
Template: "[feature], [feature] [service] [time promise]"

FORMULA 4: [Problem Solved] + [Service]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Example: "Stop losing customers - get a landing page that converts"
Template: "Stop [problem] - [solution]"

FORMULA 5: [Value] + [Service] + [Promise]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Example: "Affordable landing pages with professional results guaranteed"
Template: "[value word] [service] with [promise]"
""")

print("\n" + "=" * 80)
print("🎯 WHAT MAKES A GREAT TAGLINE")
print("=" * 80)
print("""
PSYCHOLOGY OF CLICK-WORTHY TAGLINES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ DO INCLUDE:

1. CLEAR BENEFIT (What they get)
   ❌ "I build landing pages"
   ✅ "Landing pages that convert visitors into customers"
   
2. TARGET AUDIENCE (Who it's for)
   ❌ "Professional web design"
   ✅ "Professional landing pages for small businesses"

3. DIFFERENTIATOR (What makes you special)
   ❌ "I make websites"
   ✅ "Fast, modern landing pages delivered in 48 hours"

4. ACTION WORDS (Active verbs)
   Good words: Create, Build, Design, Deliver, Convert, Transform, Boost
   Avoid: Provide, Offer, Give (too passive)

5. SPECIFICITY (Concrete details)
   ❌ "Quality work"
   ✅ "90+ page speed score guaranteed"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

POWER WORDS THAT WORK:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• Converting/Conversion (implies ROI)
• Fast/Quick/Rapid (buyers love speed)
• Professional/Premium (quality signal)
• Modern/Contemporary (up-to-date)
• Custom/Tailored (personalized)
• Responsive/Mobile-friendly (essential)
• Stunning/Beautiful (visual appeal)
• High-converting (business outcome)
• Affordable/Budget-friendly (value)
• Guaranteed/Proven (reduces risk)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NUMBERS WORK GREAT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ "Delivered in 48 hours"
✅ "90+ page speed score"
✅ "5+ years experience"
✅ "100% responsive design"
""")

print("\n" + "=" * 80)
print("❌ TAGLINES TO AVOID")
print("=" * 80)
print("""
DON'T USE THESE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌ TOO VAGUE:
   "I make great websites" - What kind? For who? What's great?
   "Quality work guaranteed" - Everyone says this
   "Professional services" - Too generic

❌ TOO LONG:
   "I will create a beautiful, modern, responsive landing page with HTML, 
   CSS, JavaScript and Bootstrap framework for your business needs"
   (Way over 80 characters!)

❌ TOO SALESY:
   "The BEST landing pages on Fiverr!!!" - Sounds desperate
   "#1 Landing Page Expert - Hire Me Now!" - Too pushy

❌ TOO TECHNICAL (for general audience):
   "Full-stack JavaScript developer specializing in React hooks and Redux"
   Save technical details for description

❌ FOCUSING ON YOU (Instead of buyer):
   "I have 5 years experience" - They care about THEIR results
   "I graduated from..." - Not relevant to their needs
   
   ✅ BETTER: "5 years creating landing pages that convert"

❌ SPELLING/GRAMMAR ERRORS:
   "Landing pages that looks great" - Instant credibility loss
   "Fast delivery garanteed" - Check spelling!

❌ ALL CAPS OR EXCESSIVE PUNCTUATION:
   "AMAZING LANDING PAGES!!!" - Looks spammy
   "Landing Pages... The Best..." - Unprofessional

❌ OVERPROMISING:
   "I'll make you a millionaire" - Unrealistic
   "Guaranteed #1 on Google" - Can't promise that
   "Unlimited everything for $5" - Not believable
""")

print("\n" + "=" * 80)
print("🎨 TAGLINE STYLE GUIDE")
print("=" * 80)
print("""
CHOOSE YOUR TONE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROFESSIONAL & CORPORATE:
✅ "Professional landing pages for growing businesses"
✅ "Strategic web design that drives business results"
✅ "Enterprise-quality landing pages at startup prices"

FRIENDLY & APPROACHABLE:
✅ "Let me build a landing page that sells for you!"
✅ "Beautiful landing pages that make customers smile"
✅ "Your perfect landing page is just one click away"

CONFIDENT & RESULTS-FOCUSED:
✅ "Landing pages that actually convert (proven results)"
✅ "I turn visitors into paying customers"
✅ "More leads, more sales, better landing pages"

MODERN & TRENDY:
✅ "Next-gen landing pages for modern brands"
✅ "Landing pages designed for 2025 and beyond"
✅ "Cutting-edge web design that stands out"

VALUE & BUDGET-FOCUSED:
✅ "Premium landing pages without the premium price"
✅ "Affordable web design that looks expensive"
✅ "Professional results on a startup budget"
""")

print("\n" + "=" * 80)
print("✅ RECOMMENDED TAGLINE")
print("=" * 80)
print("""
Based on your service (landing pages) and target (small businesses/startups),
here's the BEST tagline to use:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏆 RECOMMENDED:

"Converting visitors into customers with stunning landing pages"

WHY IT WORKS:
✅ 65 characters (perfect length)
✅ Benefit-first (conversion = money)
✅ Clear service (landing pages)
✅ Power word (stunning = visual appeal)
✅ Professional tone
✅ No fluff or hype
✅ Easy to understand
✅ Appeals to business owners

ALTERNATIVE (If you want faster delivery focus):

"Fast, responsive landing pages that turn clicks into sales"

WHY IT WORKS:
✅ 59 characters
✅ Speed emphasized (fast)
✅ Technical term (responsive) for SEO
✅ Clear outcome (sales)
✅ Action-oriented
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 COPY THIS:
Converting visitors into customers with stunning landing pages

Your tagline is ready! 🎉
""")

print("=" * 80 + "\n")
