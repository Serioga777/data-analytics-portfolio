# AI Screen Assistant - GUI Version Guide

## 🎯 What This Is

A **graphical user interface** for the AI Screen Assistant that runs in the background.

**Features:**
✅ Big friendly GUI window
✅ One-click screen capture and analysis
✅ Shows AI answers in the window
✅ Runs in background (optional system tray)
✅ 100% local AI - no cloud, no API keys
✅ Multi-agent AI system

## 🚀 Quick Start

### Step 1: Make sure Ollama is running

The AI models need Ollama to work.

### Step 2: Run the GUI

```powershell
python ai_screen_gui_simple.py
```

### Step 3: Wait for AI to load

The first time, it will download AI models (~5-10 GB).
This only happens once!

### Step 4: Click "CAPTURE & ANALYZE"

1. Open your question/quiz in browser
2. Click the big green button
3. Window minimizes for 1 second
4. AI captures and analyzes
5. See answer in the results area!

## 🎮 How to Use

### Main Window:

```
┌─────────────────────────────────────────┐
│    🤖 AI Screen Assistant               │
│    Local AI • 100% Private              │
├─────────────────────────────────────────┤
│ ✅ AI READY!                            │
├─────────────────────────────────────────┤
│                                         │
│   ┌───────────────────────────────┐    │
│   │  📸 CAPTURE & ANALYZE SCREEN  │    │
│   └───────────────────────────────┘    │
│                                         │
│   [🗑️ Clear]  [📁 Open Folder]         │
│                                         │
│   📋 AI Analysis Results:               │
│   ┌───────────────────────────────┐    │
│   │                               │    │
│   │  Results show here...         │    │
│   │                               │    │
│   └───────────────────────────────┘    │
└─────────────────────────────────────────┘
```

### Workflow:

1. **Open your question** - In browser or any app
2. **Click green button** - "CAPTURE & ANALYZE SCREEN"
3. **Window minimizes** - For 1 second to capture
4. **AI works** - Vision AI reads (10-30 sec), Solver AI answers (10-30 sec)
5. **See results** - Answer appears in the results box
6. **Repeat** - Click again for more questions!

## 📋 Files Created

```
ai_screen_gui.py           ← Full version with system tray
ai_screen_gui_simple.py    ← Simple version (recommended)
requirements_gui.txt       ← GUI dependencies
```

## 🎨 GUI Features

### Status Bar:
Shows what AI is doing:
- ⏳ Initializing...
- ✅ AI Ready!
- 📸 Capturing...
- 👁️ Vision AI analyzing...
- 🧠 Solver AI working...
- ✅ Done!

### Big Capture Button:
- Green when ready
- Gray when processing
- Can't double-click (prevents errors)

### Results Area:
- Shows full AI analysis
- Scrollable for long answers
- Can be cleared
- Auto-saves to files

### Buttons:
- **Capture & Analyze** - Main action
- **Clear Results** - Empty results area
- **Open Folder** - See all captures

## 💡 Tips

### For Best Results:

1. **Make text big** - Zoom in on questions
2. **Good contrast** - Dark text on light background
3. **Full question visible** - Don't cut off text
4. **Wait for ready** - Let AI models load first
5. **One at a time** - Process one question, wait for result

### Performance:

**First run:**
- Downloads models (5-10 GB)
- Takes 5-10 minutes
- Only happens once!

**After first run:**
- Models already downloaded
- Starts in 10-20 seconds
- Each capture takes 20-60 seconds

**With GPU:**
- 10x faster (3-5 seconds per capture)
- Automatic if you have NVIDIA GPU

## 🔧 Troubleshooting

### Issue: "Ollama not running"

**Solution:**
1. Install Ollama from https://ollama.ai/download
2. Ollama should start automatically
3. Check system tray for Ollama icon

### Issue: GUI window is blank

**Solution:**
- Wait for models to load
- Check terminal for errors
- Try restarting the app

### Issue: Capture button disabled

**Solution:**
- AI models still loading
- Wait for "✅ AI READY!" status
- Check Ollama is running

### Issue: Takes too long

**Causes:**
- Using CPU instead of GPU (normal)
- Large models on limited RAM
- First analysis (models loading into memory)

**Solutions:**
- Be patient (20-60 seconds is normal)
- Use smaller models in code
- Upgrade to GPU for 10x speed

### Issue: Inaccurate answers

**Solutions:**
- Make sure question is fully visible
- Increase text size
- Use clearer screenshots
- Try capturing again

## ⚙️ Customization

### Change AI Models

Edit `ai_screen_gui_simple.py`:

```python
# Faster but less accurate
self.vision_model = "llava:7b"
self.solver_model = "mistral:latest"

# Slower but more accurate
self.vision_model = "llava:34b"
self.solver_model = "llama3.1:70b"
```

### Change Window Size

```python
self.root.geometry("900x700")  # Width x Height
```

### Change Colors

```python
# Header background
header = tk.Frame(self.root, bg="#2c3e50")  # Dark blue

# Button color
bg="#27ae60"  # Green
bg="#e74c3c"  # Red
bg="#3498db"  # Blue
```

## 🆚 GUI vs Terminal

### GUI Version (This):
✅ Easy to use - just click button
✅ Visual feedback - see status
✅ Organized results - nice formatting
✅ Beginner friendly
✅ Runs in background
❌ Requires GUI display

### Terminal Version:
✅ Lightweight - no GUI overhead
✅ Can run headless/remotely
✅ Faster startup
❌ Less user-friendly
❌ Have to read terminal output

## 🎯 Use Cases

### Perfect For:

✅ **Study sessions** - Quick answers while learning
✅ **Homework help** - Understanding concepts
✅ **Practice problems** - Checking your work
✅ **Research** - Extracting information
✅ **Note-taking** - Capturing content

### NOT For:

❌ **Real exams** - Academic dishonesty
❌ **Graded tests** - Cheating
❌ **Certifications** - Fraud
❌ **Proctored assessments** - Get you expelled

## 📊 System Requirements

### Minimum:
- Windows 10/11
- 16 GB RAM
- 20 GB free disk
- Python 3.8+
- Ollama installed

### Recommended:
- 32 GB RAM
- NVIDIA GPU (RTX 3060+)
- SSD storage
- Dual monitors (one for GUI, one for questions)

## 🚀 Advanced: System Tray Version

For the system tray version (`ai_screen_gui.py`):

**Features:**
- Runs completely in background
- Icon in system tray
- Right-click to capture
- Minimizes to tray instead of taskbar

**To enable:**
Uncomment lines in `ai_screen_gui.py`:
```python
tray_icon = create_system_tray_icon(app)
threading.Thread(target=tray_icon.run, daemon=True).start()
```

## ✅ Quick Start Checklist

- [ ] Ollama installed and running
- [ ] Models downloaded (or will auto-download)
- [ ] Python packages installed
- [ ] Understand ethical usage
- [ ] Ready to learn!

## 🎉 Ready to Use!

```powershell
python ai_screen_gui_simple.py
```

**Click the big green button and let AI help you learn! 🤖📚**
