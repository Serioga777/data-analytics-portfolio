"""
Fiverr Skills Suggestion Generator
Suggests best skills to add to your Fiverr profile
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.llama_agent import LlamaAgent

print("\n" + "=" * 80)
print("🎯 FIVERR SKILLS OPTIMIZER")
print("=" * 80)
print()

# Create skills expert agent
skills_expert = LlamaAgent(
    name="Skills Optimization Expert",
    role="Fiverr SEO & Skills Specialist",
    goal="Recommend the best skills to maximize Fiverr profile visibility and client attraction",
    backstory="""You are an expert in Fiverr optimization and know exactly which skills 
    get the most searches, which ones help profiles rank higher, and which combinations 
    attract the best clients. You understand both technical skills and soft skills that 
    matter to clients.""",
    model_name="qwen2.5:3b",
    temperature=0.6
)

print("Analyzing best skills for web development on Fiverr...\n")

task = """Suggest the BEST skills to add to a Fiverr web development profile in December 2025.

Provide skills in these categories:

1. CORE TECHNICAL SKILLS (Must-Have)
   - Programming languages
   - Frameworks
   - Essential tools

2. POPULAR IN-DEMAND SKILLS (High Search Volume)
   - What clients are actively searching for
   - Skills that get you found

3. PLATFORM-SPECIFIC SKILLS
   - CMS platforms
   - E-commerce platforms
   - Popular builders

4. SPECIALIZED SKILLS (Stand Out)
   - Advanced techniques
   - Niche specializations

5. SOFT SKILLS (Build Trust)
   - Communication
   - Process-related
   - Client management

For each skill, indicate:
- Priority (🔥 Must Add / ⭐ Important / 💡 Good to Have)
- Why it matters
- Client search volume (High/Medium/Low)

Also provide:
- BEGINNER PACKAGE: Essential 8-10 skills to add first
- INTERMEDIATE PACKAGE: Additional 10 skills to add later
- ADVANCED PACKAGE: Specialized skills for experts

Focus on 2025 market trends and what actually gets profile views and orders."""

print("🤖 AI Expert is analyzing Fiverr skills data...\n")

result = skills_expert.execute(task)

if result['status'] == 'completed':
    print(result['output'])
    print("\n" + "=" * 80)

print("\n" + "=" * 80)
print("QUICK REFERENCE: TOP SKILLS TO ADD NOW")
print("=" * 80)
print("""
🔥 ESSENTIAL SKILLS (Add These First):

LANGUAGES & CORE:
□ HTML5
□ CSS3
□ JavaScript
□ Responsive Design
□ Web Development

POPULAR PLATFORMS:
□ WordPress
□ Shopify
□ Wix
□ Squarespace
□ Bootstrap

DESIGN & UX:
□ UI/UX Design
□ Landing Page Design
□ Mobile Design
□ Figma
□ Canva

E-COMMERCE:
□ WooCommerce
□ E-commerce
□ Online Store
□ Product Pages

SEO & PERFORMANCE:
□ SEO
□ Website Optimization
□ Fast Loading
□ Mobile-First

MODERN SKILLS:
□ React (if you know it)
□ Tailwind CSS
□ Git/GitHub
□ API Integration
□ Elementor
""")

print("\n" + "=" * 80)
print("SOFT SKILLS THAT CONVERT:")
print("=" * 80)
print("""
Add these to build trust:

□ Fast Delivery
□ Responsive Communication
□ Unlimited Revisions
□ 24/7 Support
□ Customer Satisfaction
□ Quality Assurance
□ Project Management
□ Problem Solving
""")

print("\n" + "=" * 80)
print("SKILLS BY EXPERIENCE LEVEL")
print("=" * 80)
print("""
👶 BEGINNER (Start Here):
   HTML5, CSS3, JavaScript, Responsive Design, WordPress,
   Bootstrap, Mobile Design, Landing Pages, SEO Basics

📊 INTERMEDIATE (Add Next):
   React, Tailwind CSS, WooCommerce, Shopify, Figma,
   API Integration, Git, Performance Optimization

🚀 ADVANCED (Expert Level):
   Node.js, Full Stack, Custom CMS, Advanced JavaScript,
   Database Design, Cloud Hosting, DevOps
""")

print("\n" + "=" * 80)
print("FIVERR SKILL TAGS STRATEGY")
print("=" * 80)
print("""
📌 HOW MANY SKILLS TO ADD:
   - Minimum: 8-10 skills
   - Optimal: 15-20 skills  
   - Maximum: Don't overdo it (quality > quantity)

📌 SKILL SELECTION TIPS:
   ✅ Mix technical + soft skills
   ✅ Include what you actually know
   ✅ Add trending technologies
   ✅ Include your niche (e.g., "Landing Pages")
   ✅ Add platform names (WordPress, Shopify)

📌 AVOID:
   ❌ Skills you don't actually have
   ❌ Too generic (just "design")
   ❌ Outdated tech (Flash, old jQuery)
   ❌ Unrelated skills

📌 SKILL ORDER MATTERS:
   1. Most important/strongest first
   2. Client searches (WordPress, Shopify)
   3. Your specialization
   4. Supporting skills
   5. Soft skills last
""")

print("\n" + "=" * 80)
print("2025 TRENDING SKILLS (Add If You Know):")
print("=" * 80)
print("""
🔥 HOT RIGHT NOW:
   • AI Integration (ChatGPT, AI tools)
   • Responsive Design (mobile-first)
   • Shopify Development
   • Landing Page Optimization
   • Website Speed Optimization
   • Accessibility (WCAG)
   • Tailwind CSS
   • React/Next.js
   • Headless CMS
   • Web3 (if specialized)
""")

print("\n" + "=" * 80)
print("COPY-PASTE SKILL LISTS")
print("=" * 80)
print("""
FOR BEGINNERS (Copy this list):
HTML5, CSS3, JavaScript, Responsive Design, WordPress, 
Bootstrap, Mobile Design, Landing Pages, Web Development,
SEO Basics, UI Design, Fast Delivery, Customer Service

FOR WORDPRESS FOCUS:
WordPress, WooCommerce, Elementor, Theme Customization,
Plugin Integration, WordPress Design, WordPress Development,
Responsive Design, SEO, Mobile Optimization

FOR SHOPIFY FOCUS:
Shopify, E-commerce, Online Store, Product Pages,
Shopify Theme, WooCommerce, Payment Integration,
Responsive Design, SEO, Mobile Shopping

FOR MODERN STACK:
React, JavaScript, HTML5, CSS3, Tailwind CSS, Next.js,
Responsive Design, API Integration, Git, Web Development,
Modern UI, Performance Optimization
""")

print("\n" + "=" * 80)
print("ACTION STEPS:")
print("=" * 80)
print("""
1. Go to Fiverr → Edit Profile → Skills
2. Start typing skills from the lists above
3. Select from Fiverr's suggested skills
4. Add 10-15 skills to start
5. Prioritize skills you're confident in
6. Include popular search terms
7. Save your profile

✅ TIP: Fiverr auto-suggests skills. Start typing and pick 
   from their list - these are SEO-optimized!

Your skills are ready to add! 🎯
""")
print("=" * 80 + "\n")
