"""
AI Screen Assistant - GUI Version with System Tray
Runs in background, click to capture and get AI answers!

Features:
- System tray icon (runs in background)
- Click "Capture & Analyze" to process screen
- Shows AI answers in popup window
- Completely local - no API keys
- Multi-agent AI system
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
from pystray import Icon, Menu, MenuItem
from PIL import Image as PILImage
import sys

class AIScreenGUI:
    def __init__(self):
        self.output_folder = "screen_captures"
        self.create_output_folder()
        
        # AI Models
        self.vision_model = "llava:13b"
        self.solver_model = "llama3.2:latest"
        
        # Status
        self.is_processing = False
        self.models_ready = False
        
        # Create main window (hidden initially)
        self.root = tk.Tk()
        self.root.title("AI Screen Assistant")
        self.root.geometry("800x600")
        self.root.withdraw()  # Hide initially
        
        # Create UI
        self.create_ui()
        
        # Initialize AI in background
        threading.Thread(target=self.initialize_ai, daemon=True).start()
    
    def create_output_folder(self):
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
    
    def create_ui(self):
        """Create the main GUI window"""
        # Title
        title_frame = tk.Frame(self.root, bg="#2c3e50", pady=20)
        title_frame.pack(fill="x")
        
        title = tk.Label(
            title_frame,
            text="🤖 AI Screen Assistant",
            font=("Arial", 24, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        title.pack()
        
        subtitle = tk.Label(
            title_frame,
            text="Local AI • Multi-Agent System • 100% Private",
            font=("Arial", 10),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        subtitle.pack()
        
        # Status bar
        self.status_frame = tk.Frame(self.root, bg="#34495e", pady=10)
        self.status_frame.pack(fill="x")
        
        self.status_label = tk.Label(
            self.status_frame,
            text="⏳ Initializing AI models...",
            font=("Arial", 10),
            bg="#34495e",
            fg="white"
        )
        self.status_label.pack()
        
        # Control buttons
        button_frame = tk.Frame(self.root, pady=20)
        button_frame.pack()
        
        self.capture_btn = tk.Button(
            button_frame,
            text="📸 Capture & Analyze Screen",
            font=("Arial", 14, "bold"),
            bg="#27ae60",
            fg="white",
            padx=30,
            pady=15,
            command=self.capture_and_analyze,
            state="disabled"
        )
        self.capture_btn.pack(side="left", padx=10)
        
        self.clear_btn = tk.Button(
            button_frame,
            text="🗑️ Clear Results",
            font=("Arial", 12),
            bg="#95a5a6",
            fg="white",
            padx=20,
            pady=10,
            command=self.clear_results
        )
        self.clear_btn.pack(side="left", padx=10)
        
        # Results area
        results_frame = tk.Frame(self.root)
        results_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        tk.Label(
            results_frame,
            text="Results:",
            font=("Arial", 12, "bold")
        ).pack(anchor="w")
        
        self.results_text = scrolledtext.ScrolledText(
            results_frame,
            font=("Consolas", 10),
            wrap=tk.WORD,
            bg="#ecf0f1"
        )
        self.results_text.pack(fill="both", expand=True)
        
        # Footer
        footer = tk.Label(
            self.root,
            text="💡 Click 'Capture & Analyze' or use system tray icon • For educational use only",
            font=("Arial", 8),
            fg="#7f8c8d"
        )
        footer.pack(pady=5)
    
    def initialize_ai(self):
        """Initialize AI models in background"""
        try:
            self.update_status("⏳ Checking Ollama...")
            ollama.list()
            
            self.update_status("⏳ Loading Vision AI (LLaVA)...")
            self.check_and_pull_model(self.vision_model)
            
            self.update_status("⏳ Loading Solver AI (LLama)...")
            self.check_and_pull_model(self.solver_model)
            
            self.models_ready = True
            self.update_status("✅ AI Ready! Click 'Capture & Analyze' to start")
            self.capture_btn.config(state="normal", bg="#27ae60")
            
        except Exception as e:
            self.update_status(f"❌ Error: {e}")
            messagebox.showerror(
                "AI Initialization Error",
                f"Failed to initialize AI models:\n{e}\n\nMake sure Ollama is installed and running."
            )
    
    def check_and_pull_model(self, model):
        """Check if model exists, download if not"""
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
                self.update_status(f"📥 Downloading {model} (first time only)...")
                ollama.pull(model)
        except Exception as e:
            print(f"Error checking model: {e}")
    
    def update_status(self, message):
        """Update status label"""
        self.status_label.config(text=message)
    
    def capture_and_analyze(self):
        """Capture screen and analyze with AI"""
        if self.is_processing:
            messagebox.showinfo("Processing", "Already processing a capture. Please wait...")
            return
        
        if not self.models_ready:
            messagebox.showwarning("Not Ready", "AI models are still loading. Please wait...")
            return
        
        # Run in background thread
        threading.Thread(target=self._process_capture, daemon=True).start()
    
    def _process_capture(self):
        """Background processing"""
        self.is_processing = True
        
        try:
            # Update UI
            self.root.after(0, lambda: self.capture_btn.config(state="disabled", bg="#95a5a6"))
            self.root.after(0, lambda: self.update_status("⏳ Capturing screen..."))
            
            # Minimize window
            self.root.after(0, self.root.withdraw)
            
            # Wait a moment for window to minimize
            import time
            time.sleep(0.5)
            
            # Capture screen
            screenshot = pyautogui.screenshot()
            timestamp = datetime.now()
            
            # Save screenshot
            filename = f"{self.output_folder}/screen_{timestamp.strftime('%Y%m%d_%H%M%S')}.png"
            screenshot.save(filename)
            
            self.root.after(0, lambda: self.update_status("👁️ Vision AI reading screen..."))
            
            # Vision AI analyzes
            screen_description = self.analyze_with_vision(screenshot)
            
            self.root.after(0, lambda: self.update_status("🧠 Solver AI working on answer..."))
            
            # Solver AI answers
            solution = self.solve_with_ai(screen_description)
            
            # Format result
            result = f"""{'='*70}
🎯 AI ASSISTANT RESPONSE
{'='*70}
⏰ Time: {timestamp.strftime('%H:%M:%S')}
📁 Saved: {filename}

{'='*70}
📋 WHAT I SEE:
{'='*70}
{screen_description}

{'='*70}
💡 ANSWER & SOLUTION:
{'='*70}
{solution}

{'='*70}
"""
            
            # Save answer
            answer_file = filename.replace('.png', '_answer.txt')
            with open(answer_file, 'w', encoding='utf-8') as f:
                f.write(result)
            
            # Update UI
            self.root.after(0, lambda: self.display_result(result))
            self.root.after(0, lambda: self.update_status("✅ Analysis complete!"))
            self.root.after(0, self.root.deiconify)  # Show window
            
        except Exception as e:
            error_msg = f"❌ Error: {str(e)}"
            self.root.after(0, lambda: self.update_status(error_msg))
            self.root.after(0, lambda: messagebox.showerror("Error", f"Failed to process:\n{e}"))
        
        finally:
            self.is_processing = False
            self.root.after(0, lambda: self.capture_btn.config(state="normal", bg="#27ae60"))
    
    def analyze_with_vision(self, image):
        """Use Vision AI to read image"""
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_bytes = img_byte_arr.getvalue()
        
        prompt = """Analyze this screenshot carefully.

Describe:
1. What type of content (question, quiz, assignment, document)
2. ALL text visible on screen
3. Any questions or problems to solve
4. Important details, numbers, options
5. Format (multiple choice, essay, math, etc.)

Be thorough and extract ALL text."""
        
        response = ollama.chat(
            model=self.vision_model,
            messages=[{
                'role': 'user',
                'content': prompt,
                'images': [img_bytes]
            }]
        )
        
        return response['message']['content']
    
    def solve_with_ai(self, screen_description):
        """Use Solver AI to answer"""
        prompt = f"""Based on this screen content:
{screen_description}

Provide:
1. What the question/problem is asking
2. The correct answer or solution
3. Step-by-step explanation
4. If multiple choice, state which option is correct
5. Show all work if applicable

Be accurate and thorough."""
        
        response = ollama.chat(
            model=self.solver_model,
            messages=[{
                'role': 'system',
                'content': 'You are an expert tutor. Provide accurate, detailed answers with clear explanations.'
            }, {
                'role': 'user',
                'content': prompt
            }]
        )
        
        return response['message']['content']
    
    def display_result(self, result):
        """Display result in text area"""
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(1.0, result)
    
    def clear_results(self):
        """Clear results area"""
        self.results_text.delete(1.0, tk.END)
        self.update_status("✅ AI Ready! Click 'Capture & Analyze' to start")
    
    def show_window(self):
        """Show main window"""
        self.root.deiconify()
        self.root.lift()
        self.root.focus_force()
    
    def hide_window(self):
        """Hide window to system tray"""
        self.root.withdraw()
    
    def quit_app(self):
        """Quit application"""
        if messagebox.askyesno("Quit", "Are you sure you want to quit AI Screen Assistant?"):
            self.root.quit()
            sys.exit(0)
    
    def run(self):
        """Start the GUI"""
        self.root.protocol("WM_DELETE_WINDOW", self.hide_window)  # Hide instead of close
        self.root.mainloop()


def create_system_tray_icon(app):
    """Create system tray icon"""
    
    # Create icon image
    icon_image = PILImage.new('RGB', (64, 64), color='#27ae60')
    
    def on_capture(icon, item):
        """Capture from tray"""
        app.capture_and_analyze()
    
    def on_show(icon, item):
        """Show window from tray"""
        app.show_window()
    
    def on_quit(icon, item):
        """Quit from tray"""
        icon.stop()
        app.quit_app()
    
    # Create menu
    menu = Menu(
        MenuItem('📸 Capture & Analyze', on_capture),
        MenuItem('🖥️ Show Window', on_show),
        MenuItem('❌ Quit', on_quit)
    )
    
    # Create icon
    icon = Icon(
        "AI Screen Assistant",
        icon_image,
        "AI Screen Assistant - Click to capture",
        menu
    )
    
    return icon


def main():
    """Main entry point"""
    print("""
    ╔══════════════════════════════════════════════════════════════════╗
    ║         AI SCREEN ASSISTANT - GUI VERSION                        ║
    ║         Runs in background with system tray                      ║
    ╚══════════════════════════════════════════════════════════════════╝
    
    🎯 FEATURES:
    ✅ GUI interface with one-click capture
    ✅ Runs in system tray (background)
    ✅ Local AI - no cloud, no API keys
    ✅ Multi-agent system
    ✅ 100% private
    
    ⚠️  ETHICAL USE ONLY - For learning and study purposes
    
    🚀 Starting GUI...
    """)
    
    # Create app
    app = AIScreenGUI()
    
    # Create system tray icon (optional)
    # Uncomment to enable system tray:
    # tray_icon = create_system_tray_icon(app)
    # threading.Thread(target=tray_icon.run, daemon=True).start()
    
    # Show window
    app.show_window()
    
    # Run
    app.run()


if __name__ == "__main__":
    main()
