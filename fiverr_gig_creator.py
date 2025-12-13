"""
Fiverr Gig Creator
Creates optimized gig titles, descriptions, tags, and keywords for web development services
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.llama_agent import LlamaAgent

print("\n" + "=" * 80)
print("🚀 FIVERR GIG CREATOR - WEB DEVELOPMENT")
print("=" * 80)
print()

# Create gig optimization expert
gig_expert = LlamaAgent(
    name="Fiverr Gig Optimization Expert",
    role="Fiverr SEO & Gig Creation Specialist",
    goal="Create high-converting gig titles, descriptions, tags, and keywords that get found and get orders",
    backstory="""You are an expert in Fiverr marketplace optimization. You know exactly 
    what keywords buyers search for, what gig titles get clicks, and what descriptions 
    convert browsers into buyers. You understand Fiverr's algorithm and how to rank 
    gigs on the first page.""",
    model_name="qwen2.5:3b",
    temperature=0.7
)

print("Creating your optimized Fiverr gig...\n")

task = """Create a complete Fiverr gig for a web development service.

The seller's profile:
- Web developer specializing in HTML, CSS, JavaScript, WordPress
- Focus on responsive, mobile-friendly websites
- Beginner-friendly, fast delivery
- Uses AI tools to speed up work
- Target clients: small businesses, portfolios, landing pages

Provide:

1. GIG TITLES (5 options, max 80 characters each)
   - Include keywords buyers search for
   - Make them specific and compelling
   - Format: "I will [do something specific] for [target audience]"

2. CATEGORY & SUBCATEGORY
   - Best category for web development gigs
   - Most profitable subcategory

3. SEARCH TAGS (5 tags, optimized for SEO)
   - High search volume keywords
   - Low competition where possible
   - Mix of broad and specific

4. POSITIVE KEYWORDS (for search boost)
   - 5 keywords buyers use when searching
   - Relevant to web development

5. GIG DESCRIPTION (Complete, ready to paste)
   - Attention-grabbing intro
   - What you offer (3-5 services)
   - Why choose you (3-5 benefits)
   - What's included in packages
   - Clear call-to-action
   - SEO-optimized with keywords

6. PRICING STRATEGY
   - Basic, Standard, Premium package ideas
   - Competitive pricing for beginners

Make everything beginner-friendly, SEO-optimized, and conversion-focused for December 2025."""

print("🤖 AI Expert is creating your gig...\n")

result = gig_expert.execute(task)

if result['status'] == 'completed':
    print(result['output'])

print("\n" + "=" * 80)
print("📋 QUICK COPY-PASTE GIG ELEMENTS")
print("=" * 80)

print("""
═══════════════════════════════════════════════════════════════
1️⃣ GIG TITLE OPTIONS (Pick One - 80 chars max)
═══════════════════════════════════════════════════════════════

Option 1: ⭐ RECOMMENDED
"I will create a responsive modern website for your business"
(66 characters)

Option 2: For Landing Pages
"I will design a professional landing page that converts visitors"
(67 characters)

Option 3: For WordPress
"I will build a custom WordPress website with responsive design"
(63 characters)

Option 4: For Portfolios
"I will develop a stunning portfolio website to showcase your work"
(67 characters)

Option 5: Speed Focus
"I will create a fast loading responsive website in 24 hours"
(60 characters)

💡 TIP: Use Option 1 for beginners - broad appeal, good SEO

═══════════════════════════════════════════════════════════════
2️⃣ CATEGORY & SUBCATEGORY
═══════════════════════════════════════════════════════════════

Category: Programming & Tech
Subcategory: Website Development → Website Builders & CMS

Alternative:
Category: Programming & Tech
Subcategory: Full Website Creation

═══════════════════════════════════════════════════════════════
3️⃣ SEARCH TAGS (Use All 5 - Copy Exactly)
═══════════════════════════════════════════════════════════════

1. responsive website
2. wordpress website
3. landing page
4. html css
5. web development

Alternative Tags (If above are taken):
- website design
- mobile website
- business website
- portfolio website
- website builder

💡 TIP: Type these EXACTLY as shown. Fiverr auto-suggests matching tags.

═══════════════════════════════════════════════════════════════
4️⃣ POSITIVE KEYWORDS (Paste These)
═══════════════════════════════════════════════════════════════

website development, responsive design, WordPress, landing page, HTML CSS

Alternative:
modern website, mobile friendly, business website, portfolio site, fast delivery

═══════════════════════════════════════════════════════════════
5️⃣ GIG DESCRIPTION (Ready to Paste)
═══════════════════════════════════════════════════════════════

🌟 NEED A PROFESSIONAL WEBSITE THAT LOOKS AMAZING ON ANY DEVICE?

I create modern, responsive websites that help your business stand out online!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ WHAT I OFFER:

• Responsive Website Design (mobile, tablet, desktop perfect)
• WordPress Website Development
• Landing Page Creation
• Portfolio & Business Websites
• HTML, CSS, JavaScript Custom Coding
• Fast Loading & SEO Optimized

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 WHY CHOOSE ME:

✓ Fast Delivery (24-48 hours available)
✓ Modern, Clean Designs
✓ Mobile-Friendly & Responsive
✓ SEO Optimized for Google
✓ Unlimited Revisions
✓ 24/7 Communication
✓ Professional Quality at Affordable Prices

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📦 WHAT'S INCLUDED:

→ Fully Responsive Design
→ Cross-Browser Compatible
→ Clean, Professional Code
→ Fast Loading Speed
→ Mobile Optimization
→ Free Minor Revisions

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💼 PERFECT FOR:

• Small Businesses
• Personal Portfolios
• Landing Pages
• Startup Websites
• Online Presence

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 READY TO GET STARTED?

Click "Continue" to discuss your project!
Let's bring your vision to life with a stunning website.

Order now and get your professional website delivered fast! 💻✨

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 TAGS: Responsive Website | WordPress | Landing Page | HTML CSS | 
Web Development | Mobile Friendly | Business Website | Professional

═══════════════════════════════════════════════════════════════
6️⃣ PRICING PACKAGES
═══════════════════════════════════════════════════════════════

💰 BASIC PACKAGE - $25 (Starter)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Simple Landing Page"
• 1 Page Website
• Responsive Design
• Mobile Friendly
• Fast Loading
• 2 Revisions
Delivery: 2 days

💰 STANDARD PACKAGE - $50 (Most Popular) ⭐
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Professional Website"
• Up to 5 Pages
• Responsive Design
• WordPress Integration
• SEO Optimized
• 4 Revisions
• Contact Form
Delivery: 3 days

💰 PREMIUM PACKAGE - $100 (Best Value)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"Complete Business Website"
• Up to 10 Pages
• Full WordPress Site
• Advanced Features
• E-commerce Ready
• SEO Optimization
• Unlimited Revisions
• Free 1 Month Support
Delivery: 5 days

💡 PRICING TIPS FOR BEGINNERS:
- Start low to get first reviews (Basic: $20-30)
- Increase prices after 5-10 positive reviews
- Most sales come from STANDARD package
- Premium shows you're professional

═══════════════════════════════════════════════════════════════
7️⃣ REQUIREMENTS (What to ask buyers)
═══════════════════════════════════════════════════════════════

When a buyer orders, ask for:

1. Website purpose? (business, portfolio, landing page, etc.)
2. Do you have content ready? (text, images, logo)
3. Any design preferences? (colors, style, reference sites)
4. Special features needed? (contact form, gallery, etc.)
5. Domain name? (if they want you to deploy)

═══════════════════════════════════════════════════════════════
8️⃣ FAQ (Add to Your Gig)
═══════════════════════════════════════════════════════════════

Q: Do I need to provide content?
A: Yes, please provide text and images. I can help with layout!

Q: Will my website work on mobile?
A: Absolutely! All websites are fully responsive and mobile-friendly.

Q: Can you help with hosting?
A: I deliver the website files. I can guide you on hosting setup!

Q: Do you offer revisions?
A: Yes! Revisions included based on your package.

Q: How fast can you deliver?
A: Basic pages: 1-2 days. Full sites: 3-5 days. Rush available!

""")

print("\n" + "=" * 80)
print("🎯 ACTION STEPS - CREATE YOUR GIG")
print("=" * 80)
print("""
1. ✅ Go to Fiverr → Selling → Gigs → Create New Gig

2. ✅ Fill in GIG OVERVIEW:
   - Gig Title: Copy from "Option 1" above
   - Category: Programming & Tech → Website Development
   - Search Tags: Copy the 5 tags exactly

3. ✅ Fill in PRICING:
   - Add 3 packages (Basic, Standard, Premium)
   - Copy pricing structure above
   - Add what's included for each

4. ✅ Fill in DESCRIPTION & FAQ:
   - Paste the full description from above
   - Add the FAQ section

5. ✅ Add REQUIREMENTS:
   - Copy the 5 questions above

6. ✅ Upload GIG IMAGES/VIDEO (Important!):
   - Image 1: "Responsive Website Design" mockup
   - Image 2: "Mobile Friendly" showcase
   - Image 3: Portfolio samples
   - Use Canva.com to create these FREE!

7. ✅ PUBLISH your gig!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 BONUS TIPS:

✓ Add a video (gigs with videos get 200% more orders!)
✓ Use all 3 pricing tiers (most buyers choose middle)
✓ Update gig regularly (boosts search ranking)
✓ Respond to messages within 1 hour
✓ First 5 orders: Overdeliver to get 5-star reviews!

Your gig is ready to publish! 🎉
""")

print("=" * 80 + "\n")
