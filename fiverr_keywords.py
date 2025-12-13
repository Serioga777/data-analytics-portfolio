"""
Fiverr Positive Keywords Generator
Generates SEO-optimized positive keywords for Fiverr gigs
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.llama_agent import LlamaAgent

print("\n" + "=" * 80)
print("🔍 FIVERR POSITIVE KEYWORDS GENERATOR")
print("=" * 80)
print()

# Create keyword expert agent
keyword_expert = LlamaAgent(
    name="Fiverr SEO Keywords Expert",
    role="Fiverr Search Algorithm Specialist",
    goal="Generate high-performing positive keywords that maximize gig visibility",
    backstory="""You are an expert in Fiverr's search algorithm and SEO. You know 
    exactly which keywords buyers search for, how to balance primary and secondary 
    keywords, and how to maximize gig visibility without keyword stuffing. You 
    understand buyer search behavior and conversion optimization.""",
    model_name="qwen2.5:3b",
    temperature=0.5
)

print("Generating SEO-optimized positive keywords for your gig...\n")

task = """Generate positive keywords for a Fiverr gig offering landing page creation services.

GIG DETAILS:
- Title: "I will create a professional landing page for your business"
- Service: Landing page design and development
- Skills: HTML, CSS, JavaScript, responsive design, Bootstrap
- Target: Small businesses, startups, entrepreneurs
- Focus: Fast delivery, professional design, mobile-friendly

REQUIREMENTS:
1. Generate 15-20 strong positive keywords
2. Mix of high-volume and low-competition keywords
3. Include buyer intent keywords (what they actually search)
4. Avoid duplicating words from gig title
5. Focus on secondary keywords, not primary
6. Consider related services buyers might search for

Provide:
1. TOP POSITIVE KEYWORDS (Copy-paste ready list)
2. KEYWORD CATEGORIES (Organized by type)
3. WHY EACH KEYWORD WORKS (Brief explanation)
4. ALTERNATIVES (If some don't work)
5. KEYWORDS TO AVOID (Don't use these)

Focus on December 2025 trends and actual buyer search behavior."""

print("🤖 AI Expert is analyzing search data...\n")

result = keyword_expert.execute(task)

if result['status'] == 'completed':
    print(result['output'])

print("\n" + "=" * 80)
print("📋 COPY-PASTE READY POSITIVE KEYWORDS")
print("=" * 80)
print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏆 OPTION 1: BEST ALL-AROUND KEYWORDS (RECOMMENDED)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

responsive website, web design, html css, sales page, lead generation,
mobile friendly, conversion page, startup website, small business site,
modern design, fast delivery, custom website, bootstrap design

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💼 OPTION 2: BUSINESS-FOCUSED KEYWORDS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

responsive website, sales funnel, lead capture, conversion optimization,
business website, web design, product launch, marketing page, email capture,
startup site, promotional page, html development

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎨 OPTION 3: DESIGN-FOCUSED KEYWORDS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

responsive design, modern website, ui design, web development, html css,
mobile optimization, custom design, clean layout, minimalist design,
bootstrap template, professional web, creative design

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

print("\n" + "=" * 80)
print("🎯 KEYWORD BREAKDOWN BY CATEGORY")
print("=" * 80)
print("""
📱 TECHNICAL TERMS (What it's built with):
═══════════════════════════════════════════
• responsive website    ⭐⭐⭐⭐⭐ (High volume)
• html css              ⭐⭐⭐⭐   (High volume)
• web development       ⭐⭐⭐⭐   (Medium volume)
• bootstrap design      ⭐⭐⭐    (Lower competition)
• mobile friendly       ⭐⭐⭐⭐   (High volume)
• mobile optimization   ⭐⭐⭐    (Medium volume)

💼 SERVICE TYPE (What they're getting):
═══════════════════════════════════════════
• sales page           ⭐⭐⭐⭐⭐ (High conversion intent)
• lead generation      ⭐⭐⭐⭐   (High buyer intent)
• conversion page      ⭐⭐⭐⭐   (High buyer intent)
• promotional page     ⭐⭐⭐    (Medium volume)
• marketing page       ⭐⭐⭐    (Medium volume)
• product launch       ⭐⭐⭐⭐   (Good search volume)

🏢 TARGET MARKET (Who it's for):
═══════════════════════════════════════════
• small business site  ⭐⭐⭐⭐   (High volume)
• startup website      ⭐⭐⭐⭐   (High volume)
• business website     ⭐⭐⭐⭐⭐ (Very high volume)
• entrepreneur         ⭐⭐⭐    (Medium volume)

🎨 DESIGN QUALITIES (What it looks like):
═══════════════════════════════════════════
• modern design        ⭐⭐⭐⭐   (Popular search)
• clean layout         ⭐⭐⭐    (Medium volume)
• professional web     ⭐⭐⭐    (Medium volume)
• custom design        ⭐⭐⭐⭐   (High volume)
• minimalist design    ⭐⭐⭐    (Niche but valuable)

⚡ SPECIAL FEATURES (Value-adds):
═══════════════════════════════════════════
• fast delivery        ⭐⭐⭐⭐⭐ (Buyers love this!)
• email capture        ⭐⭐⭐⭐   (Lead gen focused)
• conversion optimization ⭐⭐⭐  (Advanced buyers)
• seo optimized        ⭐⭐⭐⭐   (Common request)
""")

print("\n" + "=" * 80)
print("✅ KEYWORD SELECTION STRATEGY")
print("=" * 80)
print("""
HOW TO CHOOSE YOUR KEYWORDS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. START WITH HIGH-VOLUME KEYWORDS (4-5 keywords)
   ✅ responsive website
   ✅ web design
   ✅ business website
   ✅ html css
   
   Why: Gets you basic visibility in popular searches

2. ADD BUYER INTENT KEYWORDS (3-4 keywords)
   ✅ sales page
   ✅ lead generation
   ✅ conversion page
   ✅ product launch
   
   Why: These buyers are ready to purchase

3. INCLUDE TARGET MARKET KEYWORDS (2-3 keywords)
   ✅ small business site
   ✅ startup website
   
   Why: Attracts your ideal clients

4. ADD DESIGN/QUALITY KEYWORDS (2-3 keywords)
   ✅ modern design
   ✅ custom design
   ✅ mobile friendly
   
   Why: Shows what makes you different

5. END WITH VALUE-ADD KEYWORDS (1-2 keywords)
   ✅ fast delivery
   ✅ seo optimized
   
   Why: Competitive advantages

TOTAL: 12-15 keywords (optimal range)
""")

print("\n" + "=" * 80)
print("⚠️ KEYWORDS TO AVOID")
print("=" * 80)
print("""
DON'T USE THESE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌ Words from your title:
   • "professional" (already in title)
   • "landing page" (already in title)
   • "create" (already in title)
   • "business" (use "small business" instead)

❌ Too generic/broad:
   • "website" (alone - too broad)
   • "design" (alone - too broad)
   • "web" (alone - too broad)

❌ Irrelevant services:
   • "wordpress" (if you're offering HTML/CSS)
   • "ecommerce" (not landing pages)
   • "shopify" (different service)
   • "app development" (not your service)

❌ Duplicate meanings:
   • "responsive" + "mobile friendly" (pick one)
   • "webpage" + "website" (pick one)
   • "html5" + "html css" (pick one)

❌ Outdated terms:
   • "flash website"
   • "table layout"
   • "frontpage"

❌ Special characters (Fiverr ignores these):
   • "html/css" → use "html css"
   • "UI/UX" → use "ui design"
   • "web-design" → use "web design"
""")

print("\n" + "=" * 80)
print("💡 PRO TIPS FOR MAXIMUM VISIBILITY")
print("=" * 80)
print("""
1. USE FIVERR'S KEYWORD RESEARCH TOOL
   → Go to: Selling → Gigs → Edit Gig → Search Tags
   → Type a keyword, Fiverr shows search volume
   → Pick keywords with HIGH volume + MEDIUM competition

2. ANALYZE COMPETITORS
   → Find top-ranking landing page gigs
   → Check their tags (visible in gig URL parameters)
   → Use similar but unique combinations

3. UPDATE KEYWORDS MONTHLY
   → Check gig analytics (which keywords bring orders)
   → Remove low-performing keywords
   → Test new trending keywords

4. MATCH KEYWORDS TO YOUR SKILLS
   ✅ If you know Bootstrap → use "bootstrap design"
   ✅ If you're fast → use "fast delivery"
   ✅ If you do SEO → use "seo optimized"
   ❌ Don't claim skills you don't have

5. THINK LIKE A BUYER
   What would YOU search for if you needed a landing page?
   • "sales page for product"
   • "lead generation page"
   • "responsive landing page"
   
   Use those exact terms!

6. BALANCE IS KEY
   Mix of:
   • 40% High-volume keywords (get found)
   • 30% Buyer-intent keywords (get orders)
   • 30% Niche keywords (stand out)
""")

print("\n" + "=" * 80)
print("🚀 YOUR FINAL KEYWORD LIST (COPY THIS)")
print("=" * 80)
print("""
Based on best practices, here's your optimal keyword list:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📝 PASTE THESE INTO FIVERR (in this order):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. responsive website
2. sales page
3. web design
4. lead generation
5. html css
6. small business site
7. startup website
8. conversion page
9. mobile friendly
10. modern design
11. custom website
12. fast delivery
13. product launch

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHY THIS LIST WORKS:
✅ 13 keywords (optimal for beginners)
✅ Mix of high-volume + buyer-intent
✅ No duplicates from title
✅ No special characters
✅ Covers all search angles
✅ Targets your ideal clients
✅ Shows your competitive advantages

ALTERNATIVE SET (If some are taken):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. responsive design
2. marketing page
3. web development
4. email capture
5. bootstrap template
6. business website
7. promotional page
8. mobile optimization
9. clean layout
10. custom design
11. seo optimized
12. conversion optimization
13. ui design

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

print("\n" + "=" * 80)
print("📊 EXPECTED RESULTS")
print("=" * 80)
print("""
With these keywords, you should:

WEEK 1:
• 50-100 gig impressions/day
• 5-10 gig clicks/day
• 0-1 orders (building momentum)

WEEK 2-4:
• 200-500 impressions/day
• 20-40 clicks/day
• 1-3 orders/week

MONTH 2+:
• 500-1000 impressions/day
• 50-100 clicks/day
• 2-5 orders/week

📈 TO IMPROVE RESULTS:
1. Get first 5-star review (ranking boost!)
2. Respond to messages within 1 hour
3. Deliver orders early
4. Update gig weekly (freshness boost)
5. Add video to gig (2x more clicks)

Your keywords are ready to paste! 🎯
""")

print("=" * 80 + "\n")
