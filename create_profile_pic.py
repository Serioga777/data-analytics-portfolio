"""
Professional Profile Picture Generator for Fiverr
Creates web development themed profile images
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.llama_agent import LlamaAgent

print("\n" + "=" * 80)
print("🎨 FIVERR PROFILE PICTURE CREATOR")
print("Web Development Professional Image")
print("=" * 80)
print()

# Get user input
print("Let's create your professional profile picture!\n")
print("Option 1: I'll give you AI prompts to generate an image")
print("Option 2: I'll suggest free tools and templates you can use NOW")
print()

choice = input("Choose option (1 or 2): ").strip()

if choice == "1":
    print("\n" + "=" * 80)
    print("AI IMAGE GENERATION PROMPTS")
    print("=" * 80)
    print()
    print("Use these prompts with FREE AI image generators:")
    print()
    
    prompts = [
        {
            "style": "Professional Avatar - Modern",
            "prompt": """Professional web developer avatar, modern minimalist style, 
tech-themed background with subtle code elements, blue and white color scheme, 
clean geometric shapes, professional headshot placeholder with laptop and monitor icons, 
modern flat design, high quality, 1:1 aspect ratio, professional business avatar""",
            "tools": "DALL-E 3 (Bing Image Creator - FREE), Leonardo.ai"
        },
        {
            "style": "Icon-Based Design",
            "prompt": """Circular profile picture for web developer, centered laptop icon with 
code brackets </>, gradient background blue to purple, minimalist modern design, 
professional tech logo style, clean and simple, 500x500px, flat design""",
            "tools": "Canva AI, Microsoft Designer (FREE)"
        },
        {
            "style": "Geometric Tech",
            "prompt": """Web development professional logo, geometric hexagon shape, 
coding symbols integrated (< / >), navy blue and cyan gradient, modern tech aesthetic, 
minimalist professional, suitable for profile picture, clean lines, 1:1 square format""",
            "tools": "Leonardo.ai (FREE tier), Ideogram.ai"
        },
        {
            "style": "Abstract Developer",
            "prompt": """Abstract profile picture for web developer freelancer, 
flowing lines of code in background, laptop silhouette, modern purple and blue gradient, 
professional tech aesthetic, minimalist, circular crop, suitable for Fiverr profile""",
            "tools": "Bing Image Creator (FREE), Playground AI"
        }
    ]
    
    for i, p in enumerate(prompts, 1):
        print(f"OPTION {i}: {p['style']}")
        print("-" * 80)
        print(f"Prompt to use:")
        print(f'"{p["prompt"]}"')
        print()
        print(f"Best tools: {p['tools']}")
        print()
        print()
    
    print("=" * 80)
    print("HOW TO GENERATE:")
    print("=" * 80)
    print("""
1. Go to one of these FREE tools:
   - Bing Image Creator: bing.com/create (FREE, powered by DALL-E 3)
   - Microsoft Designer: designer.microsoft.com (FREE)
   - Leonardo.ai: leonardo.ai (FREE tier - 150 images/day)
   - Playground AI: playgroundai.com (FREE tier)

2. Copy one of the prompts above
3. Paste it into the tool
4. Click Generate
5. Download your favorite result
6. Crop to square (1:1) if needed

RECOMMENDED: Start with Bing Image Creator (easiest and FREE!)
""")

elif choice == "2":
    print("\n" + "=" * 80)
    print("INSTANT SOLUTION - USE CANVA (FREE)")
    print("=" * 80)
    print("""
Quick Method (5 minutes):

1. GO TO: canva.com (FREE account)

2. SEARCH: "Profile Picture" or "Avatar"

3. FILTER: Tech, Developer, Professional

4. PICK A TEMPLATE with:
   - Code/tech elements
   - Professional colors (blue, purple, green)
   - Clean, modern design

5. CUSTOMIZE:
   - Change colors to your preference
   - Add text if you want (your initial, "WD", etc.)
   - Adjust icons/elements

6. DOWNLOAD:
   - Click "Share" → "Download"
   - Format: PNG
   - Size: 500x500px or 1000x1000px

DONE! Upload to Fiverr immediately.

SPECIFIC TEMPLATE IDEAS:
- Search: "Tech Logo"
- Search: "Developer Avatar"
- Search: "Coding Profile Picture"
- Search: "Web Developer Icon"
""")
    
    print("\n" + "=" * 80)
    print("ALTERNATIVE: USE AN ICON/LOGO MAKER")
    print("=" * 80)
    print("""
Even Faster Option:

1. HATCHFUL by Shopify (hatchful.shopify.com)
   - FREE logo maker
   - Choose "Technology" category
   - Pick icon-based design
   - Download and use as profile pic

2. LOOKA (looka.com)
   - Enter "Web Developer" as business name
   - Choose tech/coding icons
   - Get free low-res version
   - Perfect for profile picture

3. SIMPLE ICON METHOD:
   - Go to: flaticon.com
   - Search: "web development" or "coding"
   - Download FREE icon (PNG)
   - Use Canva to add colored background
   - 2 minutes total!
""")

else:
    print("\nNo problem! Here's both options:")

print("\n" + "=" * 80)
print("QUICK TIPS FOR FIVERR PROFILE PICTURES")
print("=" * 80)
print("""
DO's:
✅ Use professional colors (blue, green, purple for tech)
✅ Keep it simple and clean
✅ Make sure it's 500x500px minimum
✅ Use high contrast (stands out in search)
✅ Tech-related imagery (code, laptop, brackets)

DON'Ts:
❌ Don't use your face if camera-shy
❌ Don't use generic stock photos
❌ Don't make it too busy/complex
❌ Don't use low resolution images
❌ Don't use copyrighted images

BEST COLORS FOR WEB DEVELOPER:
- Blue (#0066FF) - Trust, professional
- Purple (#6B46C1) - Creative, tech
- Green (#10B981) - Growth, coding
- Dark (#1F2937) - Sleek, modern

FASTEST OPTION RIGHT NOW:
1. Go to Canva.com
2. Search "Profile Picture Tech"
3. Pick one, change color
4. Download
5. Upload to Fiverr
TIME: 3 minutes!
""")

print("\n" + "=" * 80)
print("YOUR PROFILE PICTURE IS 3 MINUTES AWAY!")
print("=" * 80)
print()
print("🚀 RECOMMENDED ACTION NOW:")
print("   1. Open canva.com in your browser")
print("   2. Search 'tech profile picture' or 'developer avatar'")
print("   3. Customize one you like")
print("   4. Download as PNG")
print("   5. Upload to Fiverr immediately!")
print()
print("Need a custom AI-generated one? Use Bing Image Creator with the prompts above!")
print()
print("=" * 80 + "\n")
