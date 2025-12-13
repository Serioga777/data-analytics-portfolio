"""
AI Screen Assistant - Simple GUI Version
Easy-to-use interface for screen capture and AI analysis

Click button → Captures screen → AI analyzes → Shows answer
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import pyautogui
from PIL import Image, ImageTk
import io
import os
from datetime import datetime
import ollama
import time

class SimpleAIScreenGUI:
    def __init__(self):
        self.output_folder = "screen_captures"
        self.create_output_folder()
        
        # AI Models
        self.vision_model = "llava:13b"
        self.solver_model = "llama3.2:latest"
        
        # Status
        self.is_processing = False
        self.models_ready = False
        
        # Create window
        self.root = tk.Tk()
        self.root.title("🤖 AI Screen Assistant")
        self.root.geometry("900x700")
        self.root.configure(bg="#ecf0f1")
        
        # Create UI
        self.create_ui()
        
        # Initialize AI in background
        threading.Thread(target=self.initialize_ai, daemon=True).start()
    
    def create_output_folder(self):
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
    
    def create_ui(self):
        """Create the GUI"""
        # Header
        header = tk.Frame(self.root, bg="#2c3e50", height=100)
        header.pack(fill="x")
        header.pack_propagate(False)
        
        tk.Label(
            header,
            text="🤖 AI Screen Assistant",
            font=("Arial", 28, "bold"),
            bg="#2c3e50",
            fg="white"
        ).pack(pady=10)
        
        tk.Label(
            header,
            text="Local AI • Multi-Agent System • 100% Private • No API Keys",
            font=("Arial", 11),
            bg="#2c3e50",
            fg="#ecf0f1"
        ).pack()
        
        # Status bar
        status_frame = tk.Frame(self.root, bg="#34495e", height=50)
        status_frame.pack(fill="x")
        status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(
            status_frame,
            text="⏳ Initializing AI models... Please wait...",
            font=("Arial", 11, "bold"),
            bg="#34495e",
            fg="white"
        )
        self.status_label.pack(pady=12)
        
        # Main content
        content = tk.Frame(self.root, bg="#ecf0f1")
        content.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Capture button (BIG!)
        self.capture_btn = tk.Button(
            content,
            text="📸 CAPTURE & ANALYZE SCREEN",
            font=("Arial", 18, "bold"),
            bg="#27ae60",
            fg="white",
            activebackground="#229954",
            activeforeground="white",
            padx=40,
            pady=25,
            relief="raised",
            borderwidth=3,
            cursor="hand2",
            command=self.capture_and_analyze,
            state="disabled"
        )
        self.capture_btn.pack(pady=20)
        
        # Info label
        tk.Label(
            content,
            text="👆 Click to capture your screen and get AI-powered answers",
            font=("Arial", 10),
            bg="#ecf0f1",
            fg="#7f8c8d"
        ).pack()
        
        # Button frame
        btn_frame = tk.Frame(content, bg="#ecf0f1")
        btn_frame.pack(pady=15)
        
        tk.Button(
            btn_frame,
            text="🗑️ Clear Results",
            font=("Arial", 11),
            bg="#95a5a6",
            fg="white",
            padx=15,
            pady=8,
            command=self.clear_results
        ).pack(side="left", padx=5)
        
        tk.Button(
            btn_frame,
            text="📁 Open Captures Folder",
            font=("Arial", 11),
            bg="#3498db",
            fg="white",
            padx=15,
            pady=8,
            command=self.open_folder
        ).pack(side="left", padx=5)
        
        # Results area
        results_label_frame = tk.Frame(content, bg="#ecf0f1")
        results_label_frame.pack(fill="x", pady=(20, 5))
        
        tk.Label(
            results_label_frame,
            text="📋 AI Analysis Results:",
            font=("Arial", 13, "bold"),
            bg="#ecf0f1",
            anchor="w"
        ).pack(side="left")
        
        self.results_text = scrolledtext.ScrolledText(
            content,
            font=("Consolas", 10),
            wrap=tk.WORD,
            bg="white",
            relief="sunken",
            borderwidth=2
        )
        self.results_text.pack(fill="both", expand=True)
        
        # Initial message
        self.results_text.insert(1.0, """
╔══════════════════════════════════════════════════════════════════╗
║                  Welcome to AI Screen Assistant!                 ║
╚══════════════════════════════════════════════════════════════════╝

🎯 How to use:
1. Wait for AI models to load (first time takes a few minutes)
2. Open your question/quiz/assignment in another window
3. Click the green "CAPTURE & ANALYZE" button
4. Window will minimize for 1 second
5. AI will read your screen and provide answers
6. Results appear here!

💡 Tips:
• Make sure your question is visible on screen
• The bigger the text, the better AI can read it
• You can click "Capture" multiple times for different questions
• All captures are saved in the 'screen_captures' folder

⚠️  Ethical Use Only:
This tool is for learning, practice, and study purposes.
Do NOT use for actual graded exams or tests!

⏳ Please wait while AI models initialize...
        """)
        
        # Footer
        footer = tk.Label(
            self.root,
            text="💻 100% Local AI • Your data never leaves your computer • For educational use only",
            font=("Arial", 9),
            fg="#7f8c8d",
            bg="#ecf0f1"
        )
        footer.pack(pady=10)
    
    def initialize_ai(self):
        """Initialize AI models"""
        try:
            self.update_status("⏳ Step 1/3: Checking Ollama connection...")
            time.sleep(0.5)
            ollama.list()
            
            self.update_status("⏳ Step 2/3: Loading Vision AI (LLaVA) - This may take a few minutes...")
            self.check_and_pull_model(self.vision_model)
            
            self.update_status("⏳ Step 3/3: Loading Solver AI (LLama)...")
            self.check_and_pull_model(self.solver_model)
            
            self.models_ready = True
            self.update_status("✅ AI READY! Click the button to capture and analyze your screen!")
            
            # Enable button
            self.capture_btn.config(
                state="normal",
                bg="#27ae60",
                text="📸 CAPTURE & ANALYZE SCREEN"
            )
            
            # Show success message
            self.root.after(100, lambda: messagebox.showinfo(
                "AI Ready!",
                "✅ AI models loaded successfully!\n\n"
                "You can now click 'CAPTURE & ANALYZE' to start.\n\n"
                "The window will minimize briefly to capture your screen."
            ))
            
        except Exception as e:
            self.update_status(f"❌ ERROR: {str(e)}")
            messagebox.showerror(
                "Initialization Error",
                f"Failed to initialize AI:\n\n{e}\n\n"
                "Make sure Ollama is installed and running.\n"
                "Visit: https://ollama.ai/download"
            )
    
    def check_and_pull_model(self, model):
        """Check if model exists, download if needed"""
        try:
            models_response = ollama.list()
            if hasattr(models_response, 'models'):
                models_list = models_response.models
            elif isinstance(models_response, dict):
                models_list = models_response.get('models', [])
            else:
                models_list = []
            
            model_names = []
            for m in models_list:
                if hasattr(m, 'name'):
                    model_names.append(m.name)
                elif isinstance(m, dict):
                    model_names.append(m.get('name', ''))
            
            if not any(model in name for name in model_names):
                self.update_status(f"📥 Downloading {model}... (First time only, ~5-10 GB)")
                ollama.pull(model)
                self.update_status(f"✅ {model} downloaded!")
        except Exception as e:
            print(f"Error: {e}")
    
    def update_status(self, message):
        """Update status label"""
        self.status_label.config(text=message)
        self.root.update()
    
    def capture_and_analyze(self):
        """Main capture function"""
        if self.is_processing:
            messagebox.showinfo("Processing", "⏳ Already processing! Please wait...")
            return
        
        if not self.models_ready:
            messagebox.showwarning("Not Ready", "⏳ AI is still loading. Please wait...")
            return
        
        # Run in background
        threading.Thread(target=self._do_capture, daemon=True).start()
    
    def _do_capture(self):
        """Background processing"""
        self.is_processing = True
        
        try:
            # Update UI
            self.root.after(0, lambda: self.capture_btn.config(
                state="disabled",
                bg="#95a5a6",
                text="⏳ Processing..."
            ))
            self.root.after(0, lambda: self.update_status("📸 Capturing screen in 1 second..."))
            
            # Minimize window
            self.root.after(0, self.root.iconify)
            time.sleep(1)  # Give time to switch windows
            
            # Capture
            screenshot = pyautogui.screenshot()
            timestamp = datetime.now()
            
            # Save
            filename = f"{self.output_folder}/screen_{timestamp.strftime('%Y%m%d_%H%M%S')}.png"
            screenshot.save(filename)
            
            # Restore window
            self.root.after(0, self.root.deiconify)
            
            self.root.after(0, lambda: self.update_status("👁️ Vision AI analyzing screenshot... (10-30 seconds)"))
            
            # Vision analysis
            screen_text = self.analyze_image(screenshot)
            
            self.root.after(0, lambda: self.update_status("🧠 Solver AI generating answer... (10-30 seconds)"))
            
            # Get answer
            answer = self.solve_problem(screen_text)
            
            # Format
            result = f"""
╔══════════════════════════════════════════════════════════════════╗
║                    🎯 AI ANALYSIS COMPLETE                       ║
╚══════════════════════════════════════════════════════════════════╝

⏰ Time: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}
📁 Saved: {filename}

{'='*70}
📋 WHAT THE AI SEES ON YOUR SCREEN:
{'='*70}

{screen_text}

{'='*70}
💡 AI ANSWER & SOLUTION:
{'='*70}

{answer}

{'='*70}
✅ Analysis complete! Scroll up to see full details.
{'='*70}
"""
            
            # Save answer
            answer_file = filename.replace('.png', '_answer.txt')
            with open(answer_file, 'w', encoding='utf-8') as f:
                f.write(result)
            
            # Display
            self.root.after(0, lambda: self.display_result(result))
            self.root.after(0, lambda: self.update_status("✅ Done! Results shown below. Click 'Capture' again for another question."))
            
            # Success sound/notification
            self.root.bell()
            
        except Exception as e:
            error = f"❌ Error during processing:\n{str(e)}"
            self.root.after(0, lambda: self.update_status(f"❌ Error: {str(e)}"))
            self.root.after(0, lambda: messagebox.showerror("Error", error))
        
        finally:
            self.is_processing = False
            self.root.after(0, lambda: self.capture_btn.config(
                state="normal",
                bg="#27ae60",
                text="📸 CAPTURE & ANALYZE SCREEN"
            ))
    
    def analyze_image(self, image):
        """Vision AI analysis"""
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_bytes = img_byte_arr.getvalue()
        
        response = ollama.chat(
            model=self.vision_model,
            messages=[{
                'role': 'user',
                'content': 'Analyze this screenshot. Describe what you see including all text, questions, problems, and any important details. Be thorough.',
                'images': [img_bytes]
            }]
        )
        
        return response['message']['content']
    
    def solve_problem(self, description):
        """Solver AI"""
        prompt = f"""Based on this screen content:

{description}

Provide:
1. What question or problem needs to be solved
2. The correct answer or solution
3. Step-by-step explanation
4. If multiple choice, state which option
5. Show all work

Be accurate and educational."""
        
        response = ollama.chat(
            model=self.solver_model,
            messages=[{
                'role': 'system',
                'content': 'You are an expert tutor. Provide accurate, detailed answers.'
            }, {
                'role': 'user',
                'content': prompt
            }]
        )
        
        return response['message']['content']
    
    def display_result(self, result):
        """Show result"""
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(1.0, result)
        self.results_text.see(1.0)  # Scroll to top
    
    def clear_results(self):
        """Clear results"""
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(1.0, "\n✅ Results cleared. Ready for next capture!\n")
    
    def open_folder(self):
        """Open captures folder"""
        import subprocess
        subprocess.Popen(f'explorer "{os.path.abspath(self.output_folder)}"')
    
    def run(self):
        """Start GUI"""
        self.root.mainloop()


if __name__ == "__main__":
    print("🚀 Starting AI Screen Assistant GUI...")
    app = SimpleAIScreenGUI()
    app.run()
