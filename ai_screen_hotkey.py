"""
AI Screen Assistant - Hotkey Version with System Tray
Press Ctrl+Shift+R to read screen and get AI answer
"""

import pyautogui
from PIL import Image
import base64
import io
import os
from datetime import datetime
import keyboard
from openai import OpenAI
import threading
import queue

class HotkeyScreenAssistant:
    def __init__(self, api_key):
        self.output_folder = "screen_captures"
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
        
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4o"
        self.is_processing = False
        self.task_queue = queue.Queue()
    
    def capture_screen(self):
        """Capture current screen"""
        return pyautogui.screenshot()
    
    def image_to_base64(self, image):
        """Convert image to base64"""
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()
    
    def save_screenshot(self, image):
        """Save screenshot"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.output_folder}/screen_{timestamp}.png"
        image.save(filename)
        return filename
    
    def ask_ai(self, image, prompt):
        """Send to AI for analysis"""
        img_base64 = self.image_to_base64(image)
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{img_base64}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=2000
        )
        return response.choices[0].message.content
    
    def process_screen(self):
        """Process screen capture and get AI answer"""
        if self.is_processing:
            print("⏳ Already processing... please wait")
            return
        
        self.is_processing = True
        
        try:
            print("\n" + "="*70)
            print(f"📸 READING SCREEN - {datetime.now().strftime('%H:%M:%S')}")
            print("="*70)
            
            # Capture
            print("📸 Capturing screen...")
            image = self.capture_screen()
            filename = self.save_screenshot(image)
            print(f"✓ Saved: {filename}")
            
            # AI Analysis
            print("🤖 Analyzing with AI...")
            prompt = """Analyze this screenshot and help with any questions or assignments shown.

Provide:
1. What the question/assignment is asking
2. The correct answer or solution
3. Step-by-step explanation
4. If multiple choice, identify the right option

Be thorough and accurate."""
            
            answer = self.ask_ai(image, prompt)
            
            # Display
            print("\n" + "="*70)
            print("🎯 AI ANSWER")
            print("="*70)
            print(answer)
            print("="*70 + "\n")
            
            # Save response
            response_file = filename.replace(".png", "_answer.txt")
            with open(response_file, 'w', encoding='utf-8') as f:
                f.write(answer)
            print(f"✓ Answer saved: {response_file}\n")
            
        except Exception as e:
            print(f"❌ Error: {e}")
        finally:
            self.is_processing = False
    
    def on_hotkey(self):
        """Hotkey callback - run in separate thread"""
        thread = threading.Thread(target=self.process_screen)
        thread.daemon = True
        thread.start()
    
    def run(self):
        """Start hotkey listener"""
        print("\n" + "="*70)
        print("🤖 AI SCREEN ASSISTANT - HOTKEY MODE")
        print("="*70)
        print(f"\nModel: {self.model}")
        print("\n📌 HOTKEYS:")
        print("  Ctrl+Shift+R - Read screen and get AI answer")
        print("  Ctrl+Shift+Q - Quit assistant")
        print("\n⏳ Listening for hotkeys...")
        print("="*70 + "\n")
        
        # Register hotkeys
        keyboard.add_hotkey('ctrl+shift+r', self.on_hotkey)
        keyboard.add_hotkey('ctrl+shift+q', self.stop)
        
        # Wait
        keyboard.wait('ctrl+shift+q')
    
    def stop(self):
        """Stop assistant"""
        print("\n🛑 Stopping AI Screen Assistant...")
        keyboard.unhook_all()


def main():
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║         AI SCREEN ASSISTANT - HOTKEY VERSION                 ║
    ║         Press Ctrl+Shift+R to read screen                    ║
    ╚══════════════════════════════════════════════════════════════╝
    
    ⚠️  For legitimate personal use only!
    """)
    
    # Get API key
    api_key = input("Enter your OpenAI API key: ").strip()
    if not api_key:
        api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("❌ No API key provided!")
        return
    
    print("\n🚀 Starting assistant...")
    print("TIP: Run as Administrator for hotkeys to work globally\n")
    
    assistant = HotkeyScreenAssistant(api_key)
    
    try:
        assistant.run()
    except KeyboardInterrupt:
        print("\n🛑 Interrupted")
    finally:
        print("✓ Assistant stopped")


if __name__ == "__main__":
    main()
