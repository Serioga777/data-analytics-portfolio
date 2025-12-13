# AI Screen Reading Assistant - Complete Setup Guide

## 🎯 What This Does

This AI assistant:
✅ Captures your screen when you click a button
✅ Sends screenshot to AI (GPT-4 Vision or Claude 3.5)
✅ AI reads and understands what's on screen
✅ Answers questions, solves problems, explains concepts
✅ Saves screenshots and answers for reference

## 📋 Prerequisites

### 1. Get an AI API Key

You need an API key from one of these providers:

**Option A: OpenAI (GPT-4 Vision)** - Recommended
- Go to: https://platform.openai.com/api-keys
- Create account and add payment method
- Click "Create new secret key"
- Copy the key (starts with `sk-...`)
- Cost: ~$0.01-0.03 per image analysis

**Option B: Anthropic (Claude 3.5)**
- Go to: https://console.anthropic.com/
- Create account and get API key
- Similar pricing

### 2. Install Python Packages

```powershell
pip install -r requirements_ai_screen.txt
```

This installs:
- `openai` - For GPT-4 Vision
- `anthropic` - For Claude (optional)
- `pyautogui` - Screen capture
- `PIL/Pillow` - Image processing
- `keyboard` - Hotkey support

## 🚀 Quick Start

### Method 1: Interactive Mode (Easiest)

Press ENTER to capture and analyze:

```powershell
python ai_screen_assistant.py
```

**How to use:**
1. Run the script
2. Enter your API key when prompted
3. Navigate to your question/assignment
4. Press ENTER in terminal
5. Wait 2 seconds (it will capture)
6. AI analyzes and provides answer
7. Check `screen_captures/` folder

### Method 2: Hotkey Mode (Most Convenient)

Press **Ctrl+Shift+R** anytime to read screen:

```powershell
# Run as Administrator for global hotkeys!
python ai_screen_hotkey.py
```

**Hotkeys:**
- **Ctrl+Shift+R** - Read screen and get AI answer
- **Ctrl+Shift+Q** - Quit assistant

## 🔑 Setting Up API Key

### Option 1: Environment Variable (Recommended)

**Windows PowerShell:**
```powershell
# Temporary (current session only)
$env:OPENAI_API_KEY = "sk-your-key-here"

# Permanent (system-wide)
[System.Environment]::SetEnvironmentVariable('OPENAI_API_KEY', 'sk-your-key-here', 'User')
```

**Then restart your terminal and run:**
```powershell
python ai_screen_assistant.py
```

### Option 2: Enter Manually

Just run the script and paste your key when prompted.

### Option 3: Create .env File

Create file `.env` in the same folder:
```
OPENAI_API_KEY=sk-your-key-here
```

Then modify script to load it:
```python
from dotenv import load_dotenv
load_dotenv()
```

## 📖 Usage Examples

### Example 1: Multiple Choice Question

1. Open your test/quiz in browser
2. Press Ctrl+Shift+R (or ENTER in terminal)
3. AI will:
   - Read the question
   - Analyze options
   - Identify correct answer
   - Explain reasoning

### Example 2: Math Problem

1. Display math problem on screen
2. Trigger capture
3. AI will:
   - Understand the problem
   - Show step-by-step solution
   - Provide final answer

### Example 3: Essay Question

1. Show essay prompt
2. Capture screen
3. AI will:
   - Analyze the prompt
   - Suggest outline
   - Provide key points
   - Offer writing tips

## 📁 Output Files

All captures save to `screen_captures/` folder:

```
screen_captures/
├── screen_20241208_143052.png       ← Screenshot
├── screen_20241208_143052_answer.txt ← AI's answer
├── screen_20241208_144123.png
└── screen_20241208_144123_answer.txt
```

## ⚙️ Advanced Configuration

### Change AI Model

Edit the script:

```python
# For GPT-4 Vision
self.model = "gpt-4o"  # Latest GPT-4 with vision

# For Claude
self.model = "claude-3-5-sonnet-20241022"
```

### Customize AI Prompt

Modify the `answer_question()` function:

```python
def answer_question(self, image):
    prompt = """Your custom instructions here.
    
    Example:
    - Focus on math problems
    - Provide code solutions
    - Explain in simple terms
    """
    return self.analyze_with_ai(image, prompt)
```

### Capture Specific Region

Instead of full screen, capture just part:

```python
# Capture coordinates: (x, y, width, height)
image = self.capture_screen(region=(100, 100, 800, 600))
```

## 🔧 Troubleshooting

### Issue: "No API key found"

**Solution:**
- Set environment variable: `$env:OPENAI_API_KEY = "your-key"`
- Or enter manually when prompted
- Check key starts with `sk-`

### Issue: "Hotkeys not working"

**Solution:**
- Run PowerShell as Administrator
- Right-click PowerShell → "Run as Administrator"
- Then run the script

### Issue: "Rate limit exceeded"

**Solution:**
- You're making too many requests
- Wait a few seconds between captures
- Check your OpenAI account billing
- Add payment method if needed

### Issue: "Invalid API key"

**Solution:**
- Verify key is correct
- Check it starts with `sk-proj-` or `sk-`
- Generate new key from OpenAI dashboard
- Ensure billing is set up

### Issue: "Connection error"

**Solution:**
- Check internet connection
- Verify firewall isn't blocking
- Try VPN if needed
- Check OpenAI status page

## 💰 Cost Estimates

**OpenAI GPT-4 Vision:**
- Input: ~$0.01 per image
- Output: ~$0.03 per 1K tokens
- Average per question: $0.02-0.05

**Usage scenarios:**
- 20 questions = ~$0.40-1.00
- 100 questions = ~$2.00-5.00
- Heavy use (500/day) = $10-25/day

**Tips to save money:**
- Use for difficult questions only
- Batch similar questions
- Set max_tokens limit lower
- Use GPT-3.5 for simple tasks (cheaper)

## 🛡️ Privacy & Security

**Important:**
- Screenshots are sent to OpenAI/Anthropic servers
- Don't capture sensitive personal information
- Review OpenAI's privacy policy
- Delete captures folder regularly
- Use secure API key storage
- Don't share your API key

## ⚠️ Ethical Usage

**Appropriate use:**
✅ Personal study and learning
✅ Understanding difficult concepts  
✅ Practice problems and homework
✅ Research and information gathering
✅ Accessibility support

**Inappropriate use:**
❌ Taking actual graded exams
❌ Certification tests
❌ Proctored assessments
❌ Academic dishonesty
❌ Violating honor codes

**Consequences of misuse:**
- Academic expulsion
- Credential revocation
- Legal action
- Permanent academic record

## 🎓 Using Responsibly

**Best practices:**
1. Use for learning, not cheating
2. Understand the AI's explanations
3. Practice problems yourself first
4. Use AI to check your work
5. Learn from the explanations
6. Don't just copy answers

**When to use:**
- Studying for future exams
- Practice problem sets
- Understanding concepts
- Homework help (where allowed)
- Self-study and review

**When NOT to use:**
- During actual exams
- Graded assessments
- Certification tests
- When explicitly prohibited

## 🔄 Updates & Improvements

**Planned features:**
- Voice command integration
- Auto-scroll and multi-page capture
- Answer history database
- Subject-specific modes
- Flashcard generation
- Study guide creation

## 📞 Support

**Common questions:**
1. **Does this work offline?**
   No, requires internet for AI analysis

2. **Can I use free tier?**
   OpenAI requires paid account for GPT-4

3. **Is my data private?**
   Screenshots are sent to AI provider

4. **Can it solve any problem?**
   Works best with text/images, may struggle with complex diagrams

5. **Will this get me caught?**
   Yes, if used during proctored exams (don't do it!)

## ✅ Final Checklist

Before using:
- [ ] OpenAI API key obtained
- [ ] Python packages installed
- [ ] Script runs without errors
- [ ] Test capture works
- [ ] Understand ethical usage
- [ ] Know when NOT to use
- [ ] Billing set up (if needed)
- [ ] Read privacy implications

## 🚀 Ready to Start!

```powershell
# Method 1: Interactive
python ai_screen_assistant.py

# Method 2: Hotkey (run as Admin)
python ai_screen_hotkey.py
```

**Happy learning! 📚🤖**
