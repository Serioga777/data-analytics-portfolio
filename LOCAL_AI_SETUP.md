# Local AI Screen Assistant - Complete Setup Guide
## 100% Offline - No API Keys Needed!

## 🎯 What This Is

A **multi-agent AI system** that runs completely on YOUR computer:

**Agents:**
1. **Screen Capture Agent** - Captures screenshots
2. **Vision Agent** - Reads images using LLaVA (local vision AI)
3. **Question Solver Agent** - Solves problems using LLama (local text AI)
4. **Answer Formatter Agent** - Formats and presents answers

**Benefits:**
✅ 100% offline - no internet needed after setup
✅ Completely private - data never leaves your PC
✅ No API costs - totally free after initial download
✅ No API keys or accounts needed
✅ Works even without internet connection

## 📋 Prerequisites

### 1. Install Ollama (Required)

Ollama runs local AI models on your computer.

**Download & Install:**
1. Go to: https://ollama.ai/download
2. Download **Ollama for Windows**
3. Run the installer
4. Ollama will start automatically

**Verify Installation:**
Open PowerShell and run:
```powershell
ollama list
```

If it shows a list (even if empty), you're good!

### 2. Install Python Packages

```powershell
pip install -r requirements_local_ai.txt
```

This installs:
- `ollama` - Python client for Ollama
- `pyautogui` - Screen capture
- `Pillow` - Image processing

## 🚀 First-Time Setup

### Step 1: Download AI Models

The script will auto-download models on first run, but you can pre-download:

**Vision Model (reads images):**
```powershell
ollama pull llava:13b
```
Size: ~7.4 GB
Time: 5-15 minutes depending on internet

**Solver Model (answers questions):**
```powershell
ollama pull llama3.2:latest
```
Size: ~2 GB  
Time: 2-5 minutes

**Alternative Models:**

If you have limited disk space or want faster performance:

```powershell
# Smaller vision model (faster, less accurate)
ollama pull llava:7b  # ~4 GB

# Larger vision model (slower, more accurate)
ollama pull llava:34b  # ~20 GB

# Alternative solver models
ollama pull mistral:latest  # ~4 GB, very good
ollama pull codellama:13b   # Good for programming problems
```

### Step 2: Verify Models

```powershell
ollama list
```

You should see:
```
NAME                ID              SIZE
llava:13b          xxx...          7.4 GB
llama3.2:latest    xxx...          2.0 GB
```

### Step 3: Test Ollama

```powershell
ollama run llama3.2:latest
```

Type a question like "What is 2+2?" and hit ENTER.
If it responds, Ollama is working! Type `/bye` to exit.

## 🎮 How to Use

### Run the Assistant

```powershell
python local_ai_assistant.py
```

### Workflow:

1. **Start the script** - It initializes all AI agents
2. **Open your question/quiz** in browser
3. **Press ENTER** in the terminal
4. **Wait 2 seconds** - Switch to your question window
5. **AI captures screen** automatically
6. **Vision Agent reads** the screenshot (10-30 seconds)
7. **Solver Agent answers** the question (10-30 seconds)
8. **See result** in terminal + saved to file

### Example Session:

```
👉 Press ENTER to READ & SOLVE (or 'quit'): [ENTER]

⏳ Starting in 2 seconds... (switch to your content now!)

[STEP 1/4] 📸 Capturing screen...
✓ Saved: screen_captures/screen_20241208_153042.png

[STEP 2/4] 👁️  Vision Agent analyzing screenshot...
⏳ This may take 10-30 seconds...
✓ Screen content extracted

[STEP 3/4] 🧠 Solver Agent working on solution...
⏳ Analyzing and solving...
✓ Solution generated

[STEP 4/4] 📝 Formatting answer...

======================================================================
🎯 AI ASSISTANT RESPONSE
======================================================================

📋 WHAT I SEE:
This is a multiple choice CSS question asking about the text-shadow property...

======================================================================

💡 ANSWER & SOLUTION:
The correct answer is "css text-shadow"

Explanation:
The text-shadow property in CSS is used to add shadow effects to text...
[Full detailed answer with step-by-step explanation]

======================================================================

✓ Answer saved: screen_captures/screen_20241208_153042_answer.txt
```

## ⚙️ Configuration

### Change AI Models

Edit `local_ai_assistant.py`:

```python
# For faster processing (less accurate)
self.vision_agent = VisionAgent(model="llava:7b")
self.solver_agent = QuestionSolverAgent(model="mistral:latest")

# For better accuracy (slower)
self.vision_agent = VisionAgent(model="llava:34b")
self.solver_agent = QuestionSolverAgent(model="llama3.1:70b")
```

### Recommended Configurations

**For low-end PC (8GB RAM):**
```python
vision_model = "llava:7b"      # ~4 GB
solver_model = "llama3.2:1b"   # ~1 GB
```

**For mid-range PC (16GB RAM):** (Default)
```python
vision_model = "llava:13b"     # ~7 GB
solver_model = "llama3.2:latest"  # ~2 GB
```

**For high-end PC (32GB+ RAM):**
```python
vision_model = "llava:34b"     # ~20 GB
solver_model = "llama3.1:70b"  # ~40 GB
```

## 📊 System Requirements

### Minimum:
- **CPU:** Intel i5 or AMD Ryzen 5
- **RAM:** 16 GB
- **Disk:** 20 GB free space
- **GPU:** Not required (CPU only works)

### Recommended:
- **CPU:** Intel i7/i9 or AMD Ryzen 7/9
- **RAM:** 32 GB
- **Disk:** 50 GB free SSD
- **GPU:** NVIDIA RTX 3060 or better (optional, speeds up processing 10x)

### With GPU Acceleration:
If you have NVIDIA GPU, Ollama will automatically use it:
- Processing time: 3-5 seconds per image
- Without GPU: 10-30 seconds per image

## 🔧 Troubleshooting

### Issue: "Ollama not found"

**Solution:**
1. Install Ollama from https://ollama.ai/download
2. Restart your terminal
3. Run `ollama list` to verify

### Issue: "Model not found"

**Solution:**
```powershell
ollama pull llava:13b
ollama pull llama3.2:latest
```

### Issue: "Takes too long to process"

**Causes & Solutions:**
- **Using CPU instead of GPU:** Normal, just slower (10-30 sec vs 3-5 sec)
- **Large model on low RAM:** Use smaller models (llava:7b, llama3.2:1b)
- **First run:** Models are loading into memory, subsequent runs faster

### Issue: "Out of memory error"

**Solution:**
- Close other programs
- Use smaller models
- Upgrade RAM
- Process one question at a time

### Issue: "Inaccurate answers"

**Solution:**
- Use larger models (llava:34b, llama3.1:70b)
- Take clearer screenshots
- Ensure text is visible and large enough
- Try re-processing the same question

### Issue: "Can't capture browser window"

**Solution:**
- Manually switch to browser before 2-second countdown
- Make browser window visible (not minimized)
- Ensure question is fully visible on screen

## 💻 Performance Tips

### Speed Up Processing:

1. **Use GPU** if available (automatic with NVIDIA)
2. **Use smaller models** for faster responses
3. **Close other programs** while using
4. **Use SSD** instead of HDD
5. **Pre-load models:**
   ```powershell
   ollama run llava:13b  # Then exit with /bye
   ollama run llama3.2:latest  # Then exit
   ```

### Improve Accuracy:

1. **Use larger models** (llava:34b, llama3.1:70b)
2. **Take clear screenshots** with good contrast
3. **Ensure text is large** (zoom in if needed)
4. **Process one question at a time**
5. **Verify answers** for important questions

## 📁 Output Files

All files saved to `screen_captures/`:

```
screen_captures/
├── screen_20241208_153042.png        ← Screenshot
├── screen_20241208_153042_answer.txt ← AI's answer
├── screen_20241208_154123.png
└── screen_20241208_154123_answer.txt
```

## 🆚 Local vs Cloud AI

### Local AI (This Tool):
✅ **Free** - No ongoing costs
✅ **Private** - Data stays on your PC
✅ **Offline** - Works without internet
✅ **Unlimited** - Process as many as you want
❌ **Slower** - 10-30 seconds per question
❌ **Large download** - 10-20 GB models
❌ **Needs powerful PC** - Minimum 16GB RAM

### Cloud AI (OpenAI/Anthropic):
✅ **Fast** - 2-5 seconds per question
✅ **More accurate** - Better AI models
✅ **No local resources** - Works on any PC
❌ **Costs money** - $0.02-0.05 per question
❌ **Needs internet** - Constant connection
❌ **Privacy concerns** - Data sent to cloud
❌ **Rate limits** - Can be restricted

## 🎯 Use Cases

### What This Tool is Good For:

✅ **Study and review** - Practice problems
✅ **Homework help** - Understanding concepts
✅ **Self-learning** - Educational support
✅ **Research** - Information gathering
✅ **Offline studying** - No internet needed
✅ **Privacy-sensitive content** - Data stays local

### What It's Not For:

❌ **Real-time exams** - Ethical violation
❌ **Proctored tests** - Can get you expelled
❌ **Graded assessments** - Academic dishonesty
❌ **Professional certifications** - Fraud

## 🛡️ Privacy & Security

### Your Data:
- Screenshots stay on YOUR computer
- Never uploaded to any server
- No tracking or analytics
- 100% private and secure

### AI Models:
- Run entirely on your machine
- No internet connection needed (after download)
- Open source models (LLaVA, LLama)
- Vetted by community

## ⚠️ Responsible Use

**Use for:**
- Learning and understanding
- Practice and review
- Concept clarification
- Self-study

**Never use for:**
- Actual graded exams
- Assignments where AI help is prohibited
- Cheating on tests
- Academic dishonesty

**Consequences of misuse:**
- Academic expulsion
- Failed courses
- Permanent record
- Loss of degree/certification

## 🔄 Updates

### Update Ollama:
Download latest version from https://ollama.ai/download

### Update Models:
```powershell
ollama pull llava:13b
ollama pull llama3.2:latest
```

### Update Python Packages:
```powershell
pip install --upgrade -r requirements_local_ai.txt
```

## 🆘 Support

### Check Ollama Status:
```powershell
ollama list      # List installed models
ollama ps        # Show running models
ollama serve     # Start Ollama server (if not running)
```

### Test Components:

**Test Screen Capture:**
```python
import pyautogui
screenshot = pyautogui.screenshot()
screenshot.save("test.png")
```

**Test Vision AI:**
```powershell
ollama run llava:13b
>>> /show test.png
>>> Describe this image
```

**Test Solver AI:**
```powershell
ollama run llama3.2:latest
>>> What is 2 + 2?
```

## ✅ Quick Start Checklist

- [ ] Ollama installed and running
- [ ] Models downloaded (llava:13b, llama3.2:latest)
- [ ] Python packages installed
- [ ] Tested Ollama with `ollama list`
- [ ] Read ethical usage guidelines
- [ ] Understand when NOT to use this tool

## 🚀 Ready to Use!

```powershell
python local_ai_assistant.py
```

**Enjoy your completely offline, private AI assistant! 🤖**

No API keys. No cloud. No costs. Just AI on your machine.
