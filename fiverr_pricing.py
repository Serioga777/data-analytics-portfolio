"""
Fiverr Pricing Packages Generator
Creates optimized pricing packages for landing page services
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.llama_agent import LlamaAgent

print("\n" + "=" * 80)
print("💰 FIVERR PRICING PACKAGES OPTIMIZER")
print("=" * 80)
print()

# Create pricing expert agent
pricing_expert = LlamaAgent(
    name="Fiverr Pricing Strategy Expert",
    role="Freelance Pricing & Package Specialist",
    goal="Create profitable, competitive pricing packages that maximize conversions and order value",
    backstory="""You are an expert in Fiverr pricing psychology and package design. 
    You know exactly how to price services to attract buyers while maximizing profit. 
    You understand buyer behavior, perceived value, and how to structure packages 
    that encourage upgrades to higher tiers.""",
    model_name="qwen2.5:3b",
    temperature=0.6
)

print("Creating your optimized pricing packages...\n")

task = """Create pricing packages for a Fiverr landing page gig with these constraints:

REQUIREMENTS:
- Must offer "functional website"
- Minimum $80 for packages (Fiverr requirement)
- 3 packages: Basic, Standard, Premium
- Service: Landing page creation
- Skills: HTML, CSS, JavaScript, responsive design, Bootstrap
- Seller: Beginner (no reviews yet)
- Target: Small businesses, startups

PACKAGE ELEMENTS AVAILABLE:
- Number of pages
- Revisions
- Responsive design (must include)
- Content upload
- Plugins/extensions installation
- E-commerce functionality
- Number of products
- Payment Integration
- Opt-in form
- Autoresponder integration
- Speed optimization
- Hosting setup
- Social media icons

Provide:

1. THREE COMPLETE PACKAGES (Basic, Standard, Premium)
   For each package include:
   - Package name (catchy, value-focused)
   - Description (2-3 sentences)
   - All features/elements
   - Delivery time
   - Price (competitive for beginners)
   - Number of revisions

2. PACKAGE DIFFERENTIATION STRATEGY
   - What makes each package unique
   - Why buyers choose each tier
   - Upgrade path

3. EXTRA SERVICES (Upsells)
   - Additional pages price
   - Extra revisions price
   - Rush delivery pricing
   - Other profitable extras

4. PRICING PSYCHOLOGY
   - Why these prices work
   - How to position value
   - Common buyer objections

Focus on beginner-friendly pricing that gets orders while being profitable."""

print("🤖 AI Expert is creating your pricing strategy...\n")

result = pricing_expert.execute(task)

if result['status'] == 'completed':
    print(result['output'])

print("\n" + "=" * 80)
print("📋 COPY-PASTE READY PACKAGES")
print("=" * 80)

print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                          💼 BASIC PACKAGE - $80                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

PACKAGE NAME: "Essential Landing Page"

DESCRIPTION:
Perfect starter landing page for your business. Clean, professional design 
that looks great on all devices. Get online fast with a responsive, 
conversion-focused page.

✅ WHAT'S INCLUDED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Functional website (1 page)
✓ Responsive design (mobile, tablet, desktop)
✓ Up to 5 sections (header, about, services, testimonials, contact)
✓ Contact form with email integration
✓ Social media icons
✓ Speed optimized
✓ 2 revisions included
✓ Source code delivered

DELIVERY: 3 days
PRICE: $80
REVISIONS: 2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

╔══════════════════════════════════════════════════════════════════════════════╗
║                      ⭐ STANDARD PACKAGE - $150 (MOST POPULAR)               ║
╚══════════════════════════════════════════════════════════════════════════════╝

PACKAGE NAME: "Professional Landing Page"

DESCRIPTION:
Complete professional landing page with advanced features and custom design. 
Includes lead generation tools, animations, and everything you need to 
convert visitors into customers.

✅ WHAT'S INCLUDED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Functional website (1 page + thank you page)
✓ Responsive design (all devices)
✓ Up to 8 sections (unlimited design options)
✓ Custom graphics & design elements
✓ Advanced contact form
✓ Opt-in form (newsletter/email capture)
✓ Autoresponder integration (Mailchimp, etc.)
✓ Social media icons
✓ Smooth animations & effects
✓ Speed optimization
✓ SEO meta tags
✓ 4 revisions included
✓ Source code + documentation

DELIVERY: 5 days
PRICE: $150
REVISIONS: 4

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

╔══════════════════════════════════════════════════════════════════════════════╗
║                      🚀 PREMIUM PACKAGE - $250 (BEST VALUE)                  ║
╚══════════════════════════════════════════════════════════════════════════════╝

PACKAGE NAME: "Complete Marketing Suite"

DESCRIPTION:
Full-featured landing page system with multiple pages, advanced integrations, 
and premium features. Perfect for product launches and serious marketing 
campaigns. Includes everything + ongoing support.

✅ WHAT'S INCLUDED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Functional website (3 pages: main landing, thank you, privacy policy)
✓ Responsive design (perfect on all devices)
✓ Unlimited sections & custom design
✓ Premium custom graphics
✓ Advanced contact & opt-in forms
✓ Autoresponder integration (any platform)
✓ Payment integration (Stripe/PayPal for digital products)
✓ Social media icons & share buttons
✓ Advanced animations & interactive elements
✓ Speed optimization (90+ page speed)
✓ Full SEO optimization
✓ Hosting setup assistance
✓ Google Analytics integration
✓ Unlimited revisions
✓ 30-day post-delivery support
✓ Source code + full documentation

DELIVERY: 7 days
PRICE: $250
REVISIONS: Unlimited

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

print("\n" + "=" * 80)
print("💎 EXTRA SERVICES (UPSELLS)")
print("=" * 80)
print("""
Add these extras to increase your order value:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 EXTRA FAST DELIVERY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Basic: Deliver in 1 day (+$40)
Standard: Deliver in 2 days (+$60)
Premium: Deliver in 4 days (+$80)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
➕ ADDITIONAL PAGES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

+1 additional page: $30
+2 additional pages: $50
+3 additional pages: $70

Examples: About page, Services page, FAQ page

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔄 ADDITIONAL REVISIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

+2 extra revisions: $15
+5 extra revisions: $30
Unlimited revisions: $50

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📝 CONTENT UPLOAD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

I'll add your text & images to the page: $25

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛒 E-COMMERCE FUNCTIONALITY (Basic only)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Add simple buy button/payment: $40

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚡ SPEED OPTIMIZATION (Basic/Standard only)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Advanced speed optimization (90+ score): $35

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌐 HOSTING SETUP (Basic/Standard only)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

I'll upload & configure on your hosting: $30

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 ANALYTICS INTEGRATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Google Analytics + Facebook Pixel setup: $20

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎨 CUSTOM LOGO DESIGN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Simple logo for your landing page: $45
""")

print("\n" + "=" * 80)
print("🎯 PACKAGE COMPARISON")
print("=" * 80)
print("""
╔══════════════════╦═══════════╦═══════════╦═══════════╗
║ FEATURE          ║  BASIC    ║ STANDARD  ║  PREMIUM  ║
╠══════════════════╬═══════════╬═══════════╬═══════════╣
║ Price            ║   $80     ║   $150    ║   $250    ║
║ Pages            ║    1      ║    2      ║     3     ║
║ Delivery         ║  3 days   ║  5 days   ║   7 days  ║
║ Revisions        ║    2      ║    4      ║ Unlimited ║
║ Responsive       ║    ✅     ║    ✅     ║    ✅     ║
║ Contact Form     ║    ✅     ║    ✅     ║    ✅     ║
║ Opt-in Form      ║    ❌     ║    ✅     ║    ✅     ║
║ Autoresponder    ║    ❌     ║    ✅     ║    ✅     ║
║ Payment Gateway  ║    ❌     ║    ❌     ║    ✅     ║
║ Speed Optimized  ║    ✅     ║    ✅     ║    ✅     ║
║ SEO              ║   Basic   ║   Yes     ║  Advanced ║
║ Animations       ║    ❌     ║    ✅     ║    ✅     ║
║ Hosting Setup    ║    ❌     ║    ❌     ║    ✅     ║
║ Social Icons     ║    ✅     ║    ✅     ║    ✅     ║
║ Support          ║    ❌     ║    ❌     ║  30 days  ║
╚══════════════════╩═══════════╩═══════════╩═══════════╝

🎯 BUYER BEHAVIOR:
• 20% choose Basic (price-conscious, testing you out)
• 60% choose Standard (best value perception) ⭐ FOCUS HERE
• 20% choose Premium (serious buyers, urgent needs)
""")

print("\n" + "=" * 80)
print("💡 PRICING PSYCHOLOGY TIPS")
print("=" * 80)
print("""
WHY THESE PRICES WORK:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. $80 BASIC = "FOOT IN THE DOOR"
   ✅ Meets Fiverr's $80 minimum
   ✅ Low enough for first-time buyers
   ✅ Still profitable (8-10 hours work = $8-10/hour)
   ✅ Gets you reviews to raise prices later

2. $150 STANDARD = "SWEET SPOT" ⭐
   ✅ 2x Basic price (buyers see 2x value)
   ✅ Looks like best deal (anchoring effect)
   ✅ Most buyers default to middle option
   ✅ Higher profit margin

3. $250 PREMIUM = "ANCHOR PRICE"
   ✅ Makes Standard look affordable
   ✅ Attracts serious clients
   ✅ Shows you can deliver complex work
   ✅ Highest profit margin

VALUE POSITIONING:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Basic: "Fast & affordable way to get online"
Standard: "Everything you need to succeed" ← EMPHASIZE THIS
Premium: "Complete solution with ongoing support"

COMMON OBJECTIONS & ANSWERS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❓ "Why so expensive?"
💬 "You're not just buying a page, you're getting a conversion tool 
   that makes you money. One new customer pays for the entire page!"

❓ "Can you do it cheaper?"
💬 "Basic package is perfect for startups! It has everything essential 
   to get you online professionally."

❓ "What's the difference between packages?"
💬 "Basic gets you online. Standard helps you grow. Premium handles 
   everything including setup and support."

❓ "Do I really need Premium?"
💬 "If you're launching a product or serious marketing campaign, yes. 
   If you just need web presence, Standard is perfect!"
""")

print("\n" + "=" * 80)
print("🚀 PRICING STRATEGY")
print("=" * 80)
print("""
MONTH 1-2 (First 10 orders):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Basic: $80
Standard: $150
Premium: $250

Goal: Get 5-star reviews
Strategy: Overdeliver on every order

MONTH 3-4 (After 10-20 reviews):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Basic: $100 (+25%)
Standard: $200 (+33%)
Premium: $300 (+20%)

Goal: Increase profit margins
Strategy: You have social proof now

MONTH 5+ (Level 1 Seller):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Basic: $120
Standard: $250
Premium: $400

Goal: Premium positioning
Strategy: Target serious clients

MAXIMIZE REVENUE WITH EXTRAS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Average Order Value Strategy:
• Basic + 1-2 extras = $110-130
• Standard + 2-3 extras = $200-250
• Premium + extras = $300-400

Most Profitable Extras:
1. Extra Fast Delivery (high margin)
2. Additional Pages (easy to add)
3. Content Upload (quick work)
4. Hosting Setup (one-time, easy)

Your pricing is ready to implement! 💰
""")

print("=" * 80 + "\n")
