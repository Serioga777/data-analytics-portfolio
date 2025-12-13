"""
Fiverr Education Section Generator
Creates professional education entries for your Fiverr profile
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.llama_agent import LlamaAgent

print("\n" + "=" * 80)
print("🎓 FIVERR EDUCATION SECTION OPTIMIZER")
print("=" * 80)
print()

# Create education expert agent
education_expert = LlamaAgent(
    name="Education Section Expert",
    role="Fiverr Profile Education Specialist",
    goal="Create compelling education entries that build credibility without overselling",
    backstory="""You are an expert at crafting education sections for Fiverr profiles.
    You know how to present online learning, self-taught skills, college education,
    and work experience in a way that builds trust with clients. You understand
    that Fiverr clients care more about skills than fancy degrees.""",
    model_name="qwen2.5:3b",
    temperature=0.6
)

print("Creating professional education entries for your profile...\n")

task = """Create education entries for a Fiverr web development profile with this background:
- Finished college
- Learned programming through online courses
- Gained experience through actual work

Provide:

1. EXAMPLE EDUCATION ENTRIES (Copy-Paste Ready)
   - College/University format
   - Online learning platforms format
   - Certifications format
   - Self-taught/Work experience format

2. WHAT TO INCLUDE in each entry:
   - Title/Degree
   - Institution
   - Year of study
   - Country
   - Description (optional but recommended)

3. CREDIBILITY BOOSTERS:
   - How to phrase online learning professionally
   - How to frame work experience as education
   - What details matter most to clients

4. FIVERR EDUCATION TIPS:
   - What clients actually care about
   - How to stand out
   - Common mistakes to avoid

Make entries sound professional but honest. Focus on web development relevance."""

print("🤖 AI Expert is crafting your education entries...\n")

result = education_expert.execute(task)

if result['status'] == 'completed':
    print(result['output'])
    print("\n" + "=" * 80)

print("\n" + "=" * 80)
print("📋 COPY-PASTE READY EDUCATION EXAMPLES")
print("=" * 80)

print("""
OPTION 1: College + Online Learning (RECOMMENDED)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 Entry 1:
Title: Bachelor's Degree in Computer Science
       (or: College Degree / Associate Degree)
Institution: [Your College Name]
Year: 20XX - 20XX
Country: [Your Country]
Description: 
"Completed comprehensive studies in programming fundamentals, 
software development, and computer systems. Built strong foundation 
in problem-solving and technical skills."

💻 Entry 2:
Title: Web Development Certification
Institution: freeCodeCamp / Udemy / Coursera
Year: 2024 - 2025
Country: Online
Description:
"Completed intensive online courses in HTML, CSS, JavaScript, 
and responsive web design. Built 20+ projects including landing 
pages, portfolios, and business websites."

🚀 Entry 3:
Title: Professional Web Development Experience
Institution: Freelance / Self-Employed
Year: 2024 - Present
Country: [Your Country]
Description:
"Hands-on experience building real-world websites for clients. 
Specialized in responsive design, WordPress customization, and 
modern web technologies."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

print("""
OPTION 2: Online Learning Focus (If No Formal Degree)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💻 Entry 1:
Title: Full Stack Web Development Bootcamp
Institution: Udemy / The Odin Project / freeCodeCamp
Year: 2024 - 2025
Country: Online
Description:
"Intensive program covering HTML, CSS, JavaScript, responsive 
design, and modern frameworks. Completed 300+ hours of coding 
and built portfolio of real projects."

🎓 Entry 2:
Title: Responsive Web Design Certification
Institution: freeCodeCamp
Year: 2024
Country: Online
Description:
"Earned certification after completing projects in HTML5, CSS3, 
responsive design principles, and accessibility standards."

⚡ Entry 3:
Title: WordPress Development Specialist
Institution: WordPress.org / Udemy
Year: 2024 - 2025
Country: Online
Description:
"Comprehensive training in WordPress theme customization, 
plugin integration, and website optimization. Built 15+ 
WordPress sites."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

print("""
OPTION 3: College + Work Experience Focus
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎓 Entry 1:
Title: College Degree in [Your Field]
Institution: [College Name]
Year: 20XX - 20XX
Country: [Your Country]
Description:
"Developed analytical thinking, project management skills, 
and technical foundation that supports my web development work."

💼 Entry 2:
Title: Web Development Professional Training
Institution: On-the-Job Training / Self-Directed Learning
Year: 2024 - Present
Country: [Your Country]
Description:
"Advanced skills through real client projects, online courses 
(Udemy, freeCodeCamp), and continuous learning. Specialized in 
responsive design, WordPress, and modern web technologies."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

print("\n" + "=" * 80)
print("🎯 POPULAR ONLINE PLATFORMS TO LIST")
print("=" * 80)
print("""
Use these as "Institution" names (clients recognize them):

HIGH CREDIBILITY:
✅ freeCodeCamp (Free, well-known, has certifications)
✅ Udemy (Professional courses)
✅ Coursera (University-backed)
✅ The Odin Project (Respected bootcamp)
✅ Codecademy (Popular learning platform)

GOOD CREDIBILITY:
✅ LinkedIn Learning
✅ Pluralsight
✅ Udacity
✅ edX
✅ Scrimba

PLATFORM-SPECIFIC:
✅ WordPress.org (for WordPress skills)
✅ Meta Blueprint (for Facebook/social)
✅ Google Digital Garage (for SEO/marketing)

ALSO VALID:
✅ Self-Directed Learning
✅ Online Bootcamp
✅ Professional Development
✅ Freelance Projects
""")

print("\n" + "=" * 80)
print("✍️ HOW TO WRITE DESCRIPTIONS")
print("=" * 80)
print("""
GOOD DESCRIPTION FORMULA:

1. What you learned: "Completed intensive training in..."
2. What you built: "Created 20+ projects including..."
3. Your specialty: "Specialized in responsive design and..."

EXAMPLES:

❌ BAD: "Learned to code"
✅ GOOD: "Completed 300+ hours of hands-on coding projects in 
HTML, CSS, and JavaScript, building responsive websites."

❌ BAD: "Took online courses"
✅ GOOD: "Earned certifications in web development through 
freeCodeCamp and Udemy, completing 15+ real-world projects."

❌ BAD: "Self-taught"
✅ GOOD: "Self-directed learning through online platforms and 
real client work, specializing in modern responsive design."

POWER WORDS TO USE:
• Completed    • Earned        • Specialized
• Built        • Intensive     • Comprehensive
• Hands-on     • Professional  • Real-world
• Advanced     • Certified     • Trained
""")

print("\n" + "=" * 80)
print("⚠️ FIVERR EDUCATION TIPS")
print("=" * 80)
print("""
DO:
✅ Add 2-4 education entries (looks professional)
✅ Include online courses (clients don't care if it's online)
✅ Mention specific technologies you learned
✅ Add year ranges (shows you're current)
✅ Include descriptions (builds credibility)
✅ List certifications if you have them
✅ Frame work experience as learning

DON'T:
❌ Leave education blank (looks incomplete)
❌ Lie about degrees you don't have
❌ Add irrelevant education (high school, unrelated degrees)
❌ Use vague descriptions ("learned stuff")
❌ Add too many entries (5+ looks desperate)
❌ Skip the description field

WHAT CLIENTS ACTUALLY CARE ABOUT:
1. Can you do the work? (Skills matter most)
2. Are you current? (Recent learning = modern skills)
3. Are you professional? (Well-written = trustworthy)
4. Do you specialize? (Niche > generalist)

TRUTH: Most successful Fiverr sellers are self-taught!
Online learning is 100% legitimate and respected.
""")

print("\n" + "=" * 80)
print("🎓 EDUCATION BY YOUR SITUATION")
print("=" * 80)
print("""
IF YOU HAVE COLLEGE DEGREE:
→ List college first
→ Add online learning second  
→ Add work experience third
→ Total: 2-3 entries

IF YOU'RE SELF-TAUGHT:
→ List main online course/platform first
→ Add specific certifications second
→ Add work/project experience third
→ Total: 2-4 entries

IF YOU HAVE CERTIFICATIONS:
→ Put certified courses first
→ Add supporting courses second
→ Add practical experience third
→ Total: 3 entries

IF YOU LEARNED ON THE JOB:
→ Frame it as "Professional Development"
→ Mention platforms you used to learn
→ Emphasize real projects built
→ Total: 2-3 entries
""")

print("\n" + "=" * 80)
print("📝 FILL-IN-THE-BLANK TEMPLATES")
print("=" * 80)
print("""
TEMPLATE 1: College Graduate
────────────────────────────
Title: Bachelor's/Associate Degree in [Your Major]
Institution: [Your College Name]  
Year: [Start Year] - [End Year]
Country: [Your Country]
Description: "Completed degree program with focus on 
[relevant subjects]. Developed strong [skills] that support 
my web development work."

TEMPLATE 2: Online Learning
────────────────────────────
Title: [Course Name] Certification / [Topic] Bootcamp
Institution: freeCodeCamp / Udemy / Coursera
Year: 2024 - 2025 (or 2024 - Present)
Country: Online
Description: "Completed comprehensive training in [technologies]. 
Built [number]+ projects including [project types]. Specialized 
in [your focus area]."

TEMPLATE 3: Work Experience
────────────────────────────
Title: Professional Web Development Training
Institution: Self-Directed Learning / Freelance Work
Year: 2024 - Present
Country: [Your Country]
Description: "Advanced web development skills through real 
client projects and online platforms. Specialized in 
[your specialty]. Delivered [number]+ successful projects."
""")

print("\n" + "=" * 80)
print("🚀 ACTION STEPS")
print("=" * 80)
print("""
1. Go to Fiverr → Your Profile → Edit Profile
2. Scroll to "Education" section
3. Click "Add Education"
4. Fill in using templates above
5. Add 2-3 entries total
6. Save your profile

SUGGESTED ORDER:
1st: Your strongest credential (college OR main certification)
2nd: Online learning/courses
3rd: Work experience/practical training

✅ Your education section is ready to add!
""")

print("=" * 80 + "\n")
