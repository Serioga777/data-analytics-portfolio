"""
AI Screen Reading Assistant
Real-time screen monitoring with AI-powered question answering

Features:
- Click to capture screen
- AI analyzes screenshot
- Answers questions and solves assignments
- System tray integration
"""

import pyautogui
import pytesseract
from PIL import Image
import base64
import io
import os
from datetime import datetime
import threading
import time
from openai import OpenAI
# Alternative: from anthropic import Anthropic

# Configure paths
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class AIScreenAssistant:
    def __init__(self, api_key=None, ai_provider="openai"):
        """
        Initialize AI Screen Assistant
        
        Args:
            api_key: Your OpenAI or Anthropic API key
            ai_provider: "openai" or "anthropic"
        """
        self.output_folder = "screen_captures"
        self.create_output_folder()
        
        self.ai_provider = ai_provider
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        
        if not self.api_key:
            print("⚠️  WARNING: No API key found!")
            print("Set environment variable: OPENAI_API_KEY")
            print("Or pass api_key parameter")
        
        # Initialize AI client
        if self.ai_provider == "openai":
            self.client = OpenAI(api_key=self.api_key)
            self.model = "gpt-4o"  # GPT-4 Vision model
        elif self.ai_provider == "anthropic":
            from anthropic import Anthropic
            self.client = Anthropic(api_key=self.api_key)
            self.model = "claude-3-5-sonnet-20241022"
    
    def create_output_folder(self):
        """Create folder for saving screenshots"""
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
    
    def capture_screen(self, region=None):
        """Capture screenshot of entire screen or specific region"""
        try:
            if region:
                screenshot = pyautogui.screenshot(region=region)
            else:
                screenshot = pyautogui.screenshot()
            return screenshot
        except Exception as e:
            print(f"❌ Capture error: {e}")
            return None
    
    def image_to_base64(self, image):
        """Convert PIL Image to base64 string"""
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        return img_str
    
    def save_screenshot(self, image, prefix="screen"):
        """Save screenshot with timestamp"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.output_folder}/{prefix}_{timestamp}.png"
        image.save(filename)
        return filename
    
    def extract_text_ocr(self, image):
        """Extract text using OCR (fallback method)"""
        try:
            text = pytesseract.image_to_string(image)
            return text.strip()
        except Exception as e:
            print(f"❌ OCR error: {e}")
            return ""
    
    def analyze_with_ai(self, image, prompt="What do you see in this image?"):
        """
        Send screenshot to AI for analysis
        
        Args:
            image: PIL Image object
            prompt: Question or instruction for AI
        
        Returns:
            AI's response text
        """
        try:
            # Convert image to base64
            img_base64 = self.image_to_base64(image)
            
            if self.ai_provider == "openai":
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": prompt
                                },
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
            
            elif self.ai_provider == "anthropic":
                message = self.client.messages.create(
                    model=self.model,
                    max_tokens=2000,
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "image",
                                    "source": {
                                        "type": "base64",
                                        "media_type": "image/png",
                                        "data": img_base64
                                    }
                                },
                                {
                                    "type": "text",
                                    "text": prompt
                                }
                            ]
                        }
                    ]
                )
                return message.content[0].text
        
        except Exception as e:
            print(f"❌ AI Error: {e}")
            return f"Error: {str(e)}"
    
    def answer_question(self, image):
        """AI answers questions about the screenshot"""
        prompt = """Analyze this screenshot and help me with any questions, assignments, or tasks shown.

Please:
1. Describe what you see (question, assignment, test, etc.)
2. Provide the answer or solution
3. Explain your reasoning step-by-step
4. If it's multiple choice, identify the correct answer
5. If it's a problem to solve, show your work

Be thorough and accurate."""
        
        return self.analyze_with_ai(image, prompt)
    
    def read_and_answer(self):
        """Main function: Capture screen and get AI answer"""
        print("\n" + "="*70)
        print(f"📸 CAPTURING SCREEN at {datetime.now().strftime('%H:%M:%S')}")
        print("="*70)
        
        # Capture screen
        print("⏳ Taking screenshot...")
        image = self.capture_screen()
        
        if not image:
            print("❌ Failed to capture screen")
            return
        
        # Save screenshot
        filename = self.save_screenshot(image)
        print(f"✓ Screenshot saved: {filename}")
        
        # Get AI analysis
        print("\n🤖 Sending to AI for analysis...")
        print("⏳ Please wait (this may take 10-30 seconds)...\n")
        
        answer = self.answer_question(image)
        
        # Display result
        print("="*70)
        print("🎯 AI ASSISTANT RESPONSE")
        print("="*70)
        print(answer)
        print("="*70)
        
        # Save response
        response_file = filename.replace(".png", "_response.txt")
        with open(response_file, 'w', encoding='utf-8') as f:
            f.write(answer)
        print(f"\n✓ Response saved: {response_file}")
        
        return answer
    
    def run_interactive(self):
        """Interactive mode - press ENTER to capture and analyze"""
        print("\n" + "="*70)
        print("🤖 AI SCREEN READING ASSISTANT")
        print("="*70)
        print(f"\nAI Provider: {self.ai_provider.upper()}")
        print(f"Model: {self.model}")
        print("\n📌 HOW TO USE:")
        print("1. Navigate to the question/assignment on your screen")
        print("2. Press ENTER in this terminal")
        print("3. AI will capture, read, and answer")
        print("\nType 'quit' to exit\n")
        print("="*70)
        
        while True:
            user_input = input("\n👉 Press ENTER to READ SCREEN (or 'quit'): ").strip().lower()
            
            if user_input == 'quit':
                print("\n✓ Exiting AI Screen Assistant...")
                break
            
            # Give user time to switch windows
            print("\n⏳ Capturing in 2 seconds... (switch to your content now!)")
            time.sleep(2)
            
            # Capture and analyze
            self.read_and_answer()


def main():
    """Main entry point"""
    print("""
    ╔══════════════════════════════════════════════════════════════════╗
    ║              AI SCREEN READING ASSISTANT                         ║
    ║              Powered by GPT-4 Vision / Claude 3.5                ║
    ╚══════════════════════════════════════════════════════════════════╝
    
    ⚠️  ETHICAL USE ONLY:
    This tool is for legitimate purposes:
    ✅ Personal learning and study assistance
    ✅ Understanding difficult concepts
    ✅ Research and information extraction
    ✅ Accessibility support
    
    ❌ DO NOT use for:
    • Taking actual exams or tests
    • Academic dishonesty
    • Bypassing security measures
    • Violating terms of service
    
    By using this tool, you agree to use it ethically and responsibly.
    """)
    
    # Get user confirmation
    confirm = input("I understand and will use this ethically (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("❌ Exiting. Ethical use not confirmed.")
        return
    
    # Get API key
    print("\n" + "="*70)
    print("🔑 API KEY SETUP")
    print("="*70)
    print("\nYou need an API key from OpenAI or Anthropic:")
    print("• OpenAI: https://platform.openai.com/api-keys")
    print("• Anthropic: https://console.anthropic.com/")
    
    api_key = input("\nEnter your API key (or press ENTER to use env variable): ").strip()
    
    if not api_key:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("\n⚠️  No API key provided!")
            print("Set environment variable: OPENAI_API_KEY")
            print("Or enter it manually when prompted")
            return
    
    # Choose provider
    provider = input("\nChoose AI provider (openai/anthropic) [openai]: ").strip().lower() or "openai"
    
    # Create assistant
    print("\n🚀 Starting AI Screen Assistant...")
    assistant = AIScreenAssistant(api_key=api_key, ai_provider=provider)
    
    try:
        assistant.run_interactive()
    except KeyboardInterrupt:
        print("\n\n🛑 Interrupted by user")
    finally:
        print("\n✓ AI Screen Assistant stopped")
        print(f"📁 All captures saved in: {assistant.output_folder}/")


if __name__ == "__main__":
    main()
