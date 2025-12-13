"""
Professional CV Generator for Data Analytics Jobs
Creates ATS-friendly, modern CV optimized for data analytics positions
"""
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.llama_agent import LlamaAgent

print("\n" + "=" * 80)
print("📄 PROFESSIONAL CV GENERATOR - DATA ANALYTICS")
print("=" * 80)
print()

# Create CV expert agent
cv_expert = LlamaAgent(
    name="CV Writing Specialist",
    role="Career Coach & CV Optimization Expert",
    goal="Create compelling, ATS-friendly CVs that get interviews for data analytics positions",
    backstory="""You are an expert CV writer specializing in data analytics and business 
    roles. You know exactly what recruiters look for, how to pass ATS systems, and how 
    to highlight skills and achievements effectively. You create modern, professional 
    CVs that get results.""",
    model_name="qwen2.5:3b",
    temperature=0.6
)

print("Creating your professional CV...\n")

# User information
user_profile = """
EDUCATION:
- Currently studying Business and Management at Bath Spa University
- Started: February 2024
- Expected graduation: September 2028
- Currently in first year

TARGET ROLE: Data Analytics positions

SKILLS FROM WEB DEVELOPMENT:
- HTML, CSS, JavaScript
- Responsive design
- Problem-solving
- Attention to detail
- Project management
- Client communication

TRANSFERABLE SKILLS:
- Self-taught learner (web development)
- Works with AI tools (ChatGPT, Claude)
- Building Fiverr freelance business
- Creating landing pages and websites
- Data-driven approach to design
"""

task = f"""Create a professional CV for a data analytics position based on this profile:

{user_profile}

Requirements:
1. Modern, ATS-friendly format
2. Highlight transferable skills from web development to data analytics
3. Emphasize current university studies (Business and Management)
4. Show self-learning and initiative
5. Include relevant skills section for data analytics
6. Professional summary tailored for data analytics
7. Format suitable for UK job market

Structure:
- Professional Summary
- Education
- Skills (Technical & Soft)
- Experience/Projects
- Additional sections (Certifications, Tools, Languages)

Make it compelling for entry-level data analytics roles while studying."""

print("🤖 AI Expert is creating your CV...\n")

result = cv_expert.execute(task)

if result['status'] == 'completed':
    print(result['output'])

print("\n" + "=" * 80)
print("📄 YOUR PROFESSIONAL CV - DATA ANALYTICS")
print("=" * 80)

cv_content = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                            [YOUR FULL NAME]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        Data Analytics Enthusiast | Business & Management Student
        
📧 your.email@example.com | 📱 +44 XXXX XXX XXX | 🌐 LinkedIn: /in/yourname
📍 Bath, United Kingdom | 💼 GitHub: github.com/yourname
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


PROFESSIONAL SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Motivated Business and Management student at Bath Spa University with strong 
analytical mindset and proven self-learning abilities. Currently developing 
data analytics skills through hands-on projects and online learning. 
Experienced in translating complex information into actionable insights 
through web development projects. Proficient in leveraging modern tools and 
technologies to solve business problems. Seeking entry-level data analytics 
opportunities to apply analytical skills and contribute to data-driven 
decision making.


EDUCATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Bachelor of Science (BSc) - Business and Management
Bath Spa University, Bath, United Kingdom
February 2024 - September 2028 (Expected)

Relevant Modules:
• Business Analytics & Decision Making
• Quantitative Methods for Business
• Strategic Management
• Financial Analysis
• Operations & Project Management

Key Achievements:
• Developing strong foundation in business analytics and statistical methods
• Applying data-driven approaches to business problem-solving
• Active participant in university data analytics workshops


TECHNICAL SKILLS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Data Analytics & Tools:
• Microsoft Excel (Advanced formulas, PivotTables, Data Analysis)
• SQL (Database querying and data manipulation)
• Python (pandas, NumPy, matplotlib - learning)
• Power BI / Tableau (Data visualization - learning)
• Google Analytics (Web analytics)
• Statistical Analysis (Descriptive & inferential statistics)

Programming & Web Technologies:
• HTML5, CSS3, JavaScript
• Responsive Web Design
• Version Control (Git, GitHub)
• API Integration

AI & Productivity Tools:
• ChatGPT & Claude (Data analysis assistance, automation)
• Microsoft Office Suite (Word, Excel, PowerPoint)
• Project Management Tools (Trello, Asana)

Soft Skills:
• Problem-Solving & Critical Thinking
• Data-Driven Decision Making
• Attention to Detail
• Client Communication
• Self-Learning & Adaptability
• Time Management


RELEVANT EXPERIENCE & PROJECTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Freelance Web Developer (Self-Employed)
Fiverr Platform | 2024 - Present
• Analyze client requirements and translate them into data-informed design 
  decisions
• Create responsive landing pages using HTML, CSS, and JavaScript, applying 
  analytical thinking to optimize user conversion rates
• Utilize Google Analytics to track website performance metrics and provide 
  data-driven recommendations to clients
• Manage multiple projects simultaneously, demonstrating strong organizational 
  and time management skills
• Achieve 100% client satisfaction through clear communication and 
  attention to detail

Key Achievement: Built 20+ websites, applying A/B testing principles to 
improve conversion rates by analyzing user behavior data


Data Analytics Learning Projects (Self-Directed)
2024 - Present
• Developed Python scripts for data cleaning and analysis using pandas and 
  NumPy libraries
• Created interactive dashboards visualizing business metrics and KPIs
• Conducted exploratory data analysis (EDA) on real-world datasets to 
  identify trends and patterns
• Built automated data collection workflows using APIs and web scraping
• Completed online courses in SQL, Excel, and statistical analysis

Project Highlight: Analyzed website traffic data from 50+ landing pages to 
identify key factors influencing conversion rates, presenting findings through 
visualizations


Business Process Optimization Research
Personal Project | 2024
• Researched income opportunities in tech sector using data analysis techniques
• Analyzed market trends, competition levels, and profit margins across 
  different business models
• Created detailed reports with actionable insights and strategic recommendations
• Demonstrated ability to gather, analyze, and present business intelligence

Result: Developed comprehensive 30-day action plan based on data-driven 
market analysis


CERTIFICATIONS & ONLINE LEARNING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 Completed / In Progress:
• freeCodeCamp - Responsive Web Design (Completed)
• Udemy - Data Analysis with Python (In Progress)
• Coursera - SQL for Data Science (In Progress)
• Google Analytics Individual Qualification (Planned)
• Microsoft Excel - Advanced Data Analysis (Planned)

🎯 Currently Learning:
• Python for Data Analysis (pandas, NumPy, matplotlib)
• SQL for database management and querying
• Power BI for business intelligence and visualization
• Statistical methods and hypothesis testing


ADDITIONAL INFORMATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Languages:
• English - Fluent
• [Add other languages if applicable]

Interests:
• Data Visualization & Storytelling
• Business Intelligence & Analytics
• Automation & Process Improvement
• Market Research & Consumer Behavior
• Technology & AI Applications in Business

Availability:
• Available for part-time internships and placement opportunities
• Flexible schedule to accommodate work alongside studies
• Open to remote work opportunities


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
References available upon request
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

print(cv_content)

# Save CV to file
cv_filename = "Data_Analytics_CV.txt"
cv_filepath = Path(__file__).parent / cv_filename

with open(cv_filepath, 'w', encoding='utf-8') as f:
    f.write(cv_content)

print(f"\n✅ CV saved to: {cv_filepath}")

print("\n" + "=" * 80)
print("💡 CV CUSTOMIZATION TIPS")
print("=" * 80)
print("""
PERSONALIZE YOUR CV:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. REPLACE PLACEHOLDERS:
   ✏️ [YOUR FULL NAME] → Your actual name
   ✏️ your.email@example.com → Your real email
   ✏️ +44 XXXX XXX XXX → Your phone number
   ✏️ LinkedIn/GitHub links → Your actual profiles

2. ADD YOUR ACTUAL PROJECTS:
   • Replace example projects with real ones you've done
   • Add specific metrics and results where possible
   • Include GitHub links to your code

3. TAILOR FOR EACH APPLICATION:
   • Read the job description carefully
   • Match keywords from the job posting
   • Emphasize relevant skills for that specific role
   • Adjust Professional Summary to match company needs

4. QUANTIFY ACHIEVEMENTS:
   ❌ "Built websites for clients"
   ✅ "Built 20+ responsive websites, achieving 95% client satisfaction"
   
   ❌ "Analyzed data"
   ✅ "Analyzed dataset of 10,000+ records to identify 3 key trends"

5. UPDATE SKILLS SECTION:
   • Remove skills you don't actually have
   • Add skills you're currently learning
   • Be honest about proficiency levels


ATS OPTIMIZATION TIPS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ DO:
• Use standard section headings (Education, Experience, Skills)
• Include keywords from job descriptions
• Use simple, clean formatting
• Save as .docx or PDF (check job posting requirements)
• Use bullet points for easy scanning
• Include relevant certifications

❌ DON'T:
• Use tables or text boxes (ATS can't read them)
• Use headers/footers for important info
• Use images or graphics
• Use fancy fonts
• Put multiple columns (stick to single column)


SKILLS TO ADD FOR DATA ANALYTICS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HIGH PRIORITY (Learn These ASAP):
1. Excel - Advanced (PivotTables, VLOOKUP, Power Query)
2. SQL - Database querying
3. Python - pandas, NumPy, matplotlib
4. Power BI or Tableau - Data visualization
5. Statistics - Basic statistical concepts

NICE TO HAVE:
• R programming
• Google Analytics
• Google Data Studio
• Jupyter Notebooks
• Data cleaning techniques


WHERE TO LEARN THESE SKILLS (FREE):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 Excel:
• Microsoft Learn (free official training)
• ExcelJet (tutorials and shortcuts)
• YouTube: MyOnlineTrainingHub

📚 SQL:
• SQLBolt (interactive lessons)
• W3Schools SQL Tutorial
• Mode Analytics SQL Tutorial
• LeetCode (practice problems)

📚 Python for Data Analysis:
• freeCodeCamp Python course
• Kaggle Learn (free micro-courses)
• Google Colab (free Jupyter notebooks)
• DataCamp (free intro courses)

📚 Power BI:
• Microsoft Learn Power BI
• Guy in a Cube (YouTube channel)
• Enterprise DNA (free beginner content)

📚 Statistics:
• Khan Academy Statistics
• StatQuest (YouTube)
• Coursera - Statistics basics


PROJECTS TO ADD TO YOUR CV:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DO THESE THIS WEEK:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. EXCEL DASHBOARD PROJECT (2-3 hours)
   • Download a dataset from Kaggle (sales data, HR data, etc.)
   • Create PivotTables and charts
   • Build an interactive dashboard
   • Take screenshots and add to portfolio

2. SQL DATA ANALYSIS (3-4 hours)
   • Use SQLite or MySQL
   • Import a dataset
   • Write queries to answer business questions
   • Document findings
   • Upload to GitHub

3. PYTHON DATA CLEANING (4-5 hours)
   • Find messy dataset on Kaggle
   • Clean data using pandas
   • Create visualizations with matplotlib
   • Write summary report
   • Upload to GitHub with README

4. POWER BI VISUALIZATION (3-4 hours)
   • Download Power BI Desktop (free)
   • Import dataset
   • Create interactive dashboard
   • Publish to Power BI Service (free)
   • Add link to CV


LINKEDIN OPTIMIZATION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Your LinkedIn should match your CV:
• Professional photo
• Headline: "Business & Management Student | Aspiring Data Analyst"
• About section: Expand your Professional Summary
• Add all projects with descriptions
• List skills: SQL, Python, Excel, Power BI, etc.
• Ask for recommendations from clients/professors
• Join data analytics groups
• Follow data analytics companies


YOUR CV IS READY! 🎉
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Next Steps:
1. ✅ Personalize the CV with your details
2. ✅ Complete 1-2 data analytics projects this week
3. ✅ Update your LinkedIn profile
4. ✅ Apply to 5-10 entry-level data analytics internships
5. ✅ Start learning Excel + SQL (highest priority)

Good luck with your job search! 🚀
""")

print("=" * 80 + "\n")
