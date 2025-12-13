"""
Local AI Screen Assistant - Multi-Agent System
No API keys needed - runs completely on your local machine!

Agents:
1. Screen Capture Agent - Captures and processes screenshots
2. Vision Agent - Reads and understands images (LLaVA model)
3. Question Solver Agent - Solves problems and assignments
4. Answer Formatter Agent - Formats and presents answers
"""

import pyautogui
from PIL import Image
import base64
import io
import os
from datetime import datetime
import json
import ollama

class ScreenCaptureAgent:
    """Agent responsible for capturing and managing screenshots"""
    
    def __init__(self, output_folder="screen_captures"):
        self.output_folder = output_folder
        self.create_output_folder()
        self.capture_history = []
    
    def create_output_folder(self):
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
            print(f"✓ Created capture folder: {self.output_folder}")
    
    def capture_screen(self, region=None):
        """Capture screenshot"""
        try:
            screenshot = pyautogui.screenshot(region=region)
            timestamp = datetime.now()
            
            capture_info = {
                'timestamp': timestamp,
                'image': screenshot,
                'region': region
            }
            self.capture_history.append(capture_info)
            
            print(f"📸 Screen captured at {timestamp.strftime('%H:%M:%S')}")
            return capture_info
        except Exception as e:
            print(f"❌ Capture error: {e}")
            return None
    
    def save_capture(self, capture_info, prefix="screen"):
        """Save screenshot to file"""
        timestamp = capture_info['timestamp'].strftime("%Y%m%d_%H%M%S")
        filename = f"{self.output_folder}/{prefix}_{timestamp}.png"
        capture_info['image'].save(filename)
        capture_info['filename'] = filename
        print(f"✓ Saved: {filename}")
        return filename
    
    def get_latest_capture(self):
        """Get most recent capture"""
        return self.capture_history[-1] if self.capture_history else None


class VisionAgent:
    """Agent that reads and understands images using local LLaVA model"""
    
    def __init__(self, model="llava:13b"):
        """
        Initialize Vision Agent with local model
        
        Models to try:
        - llava:7b (faster, less accurate)
        - llava:13b (balanced, recommended)
        - llava:34b (slower, more accurate)
        - bakllava (optimized version)
        """
        self.model = model
        self.check_model()
    
    def check_model(self):
        """Check if model is available locally"""
        try:
            models_response = ollama.list()
            # Handle both dict and object responses
            if hasattr(models_response, 'models'):
                models_list = models_response.models
            elif isinstance(models_response, dict) and 'models' in models_response:
                models_list = models_response['models']
            else:
                models_list = []
            
            # Extract model names
            model_names = []
            for m in models_list:
                if hasattr(m, 'name'):
                    model_names.append(m.name)
                elif isinstance(m, dict) and 'name' in m:
                    model_names.append(m['name'])
            
            if not any(self.model in name for name in model_names):
                print(f"⚠️  Model '{self.model}' not found locally")
                print(f"📥 Downloading {self.model}... (this may take a while)")
                print("💡 TIP: This only happens once!")
                ollama.pull(self.model)
                print(f"✓ Model {self.model} ready!")
            else:
                print(f"✓ Vision model loaded: {self.model}")
        except Exception as e:
            print(f"⚠️  Error checking model: {e}")
            print("Make sure Ollama is installed and running!")
    
    def analyze_image(self, image, prompt="Describe what you see in detail."):
        """Use local AI to analyze image"""
        try:
            # Convert PIL Image to bytes
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='PNG')
            img_bytes = img_byte_arr.getvalue()
            
            # Send to local LLaVA model
            response = ollama.chat(
                model=self.model,
                messages=[{
                    'role': 'user',
                    'content': prompt,
                    'images': [img_bytes]
                }]
            )
            
            return response['message']['content']
        except Exception as e:
            print(f"❌ Vision analysis error: {e}")
            return None
    
    def read_screen(self, image):
        """Read and describe everything on screen"""
        prompt = """You are a screen reader AI. Analyze this screenshot carefully.

Describe:
1. What type of content is shown (question, quiz, assignment, document, etc.)
2. All text visible on screen
3. Any questions or problems that need to be answered
4. Important details, numbers, or options
5. The format (multiple choice, essay, math problem, etc.)

Be thorough and extract ALL text."""
        
        return self.analyze_image(image, prompt)


class QuestionSolverAgent:
    """Agent specialized in solving questions, quizzes, and assignments"""
    
    def __init__(self, model="llama3.2:latest"):
        """
        Initialize Solver Agent
        
        Recommended models:
        - llama3.2:latest (general purpose)
        - codellama:13b (for coding problems)
        - mistral:latest (fast and good)
        - deepseek-coder (for programming)
        """
        self.model = model
        self.check_model()
    
    def check_model(self):
        """Ensure model is available"""
        try:
            models_response = ollama.list()
            # Handle both dict and object responses
            if hasattr(models_response, 'models'):
                models_list = models_response.models
            elif isinstance(models_response, dict) and 'models' in models_response:
                models_list = models_response['models']
            else:
                models_list = []
            
            # Extract model names
            model_names = []
            for m in models_list:
                if hasattr(m, 'name'):
                    model_names.append(m.name)
                elif isinstance(m, dict) and 'name' in m:
                    model_names.append(m['name'])
            
            if not any(self.model in name for name in model_names):
                print(f"📥 Downloading solver model {self.model}...")
                ollama.pull(self.model)
                print(f"✓ Solver model ready!")
            else:
                print(f"✓ Solver model loaded: {self.model}")
        except Exception as e:
            print(f"⚠️  Error: {e}")
    
    def solve_question(self, screen_description):
        """Solve the question/problem based on screen description"""
        prompt = f"""You are an expert problem solver and tutor.

Based on this screen content:
{screen_description}

Your task:
1. Identify what question or problem needs to be solved
2. Provide the correct answer or solution
3. Explain your reasoning step-by-step
4. If it's multiple choice, clearly state which option is correct
5. Show all work and calculations if applicable

Be accurate, thorough, and educational in your response."""
        
        try:
            response = ollama.chat(
                model=self.model,
                messages=[{
                    'role': 'system',
                    'content': 'You are an expert tutor and problem solver. Always provide accurate, detailed answers with clear explanations.'
                }, {
                    'role': 'user',
                    'content': prompt
                }]
            )
            
            return response['message']['content']
        except Exception as e:
            print(f"❌ Solver error: {e}")
            return None
    
    def verify_answer(self, question, proposed_answer):
        """Double-check the answer for accuracy"""
        prompt = f"""Question: {question}

Proposed Answer: {proposed_answer}

Verify if this answer is correct. If not, provide the correct answer."""
        
        try:
            response = ollama.chat(
                model=self.model,
                messages=[{'role': 'user', 'content': prompt}]
            )
            return response['message']['content']
        except Exception as e:
            return None


class AnswerFormatterAgent:
    """Agent that formats and presents answers clearly"""
    
    def format_answer(self, screen_description, solution):
        """Format the final answer for display"""
        formatted = f"""
{'='*70}
🎯 AI ASSISTANT RESPONSE
{'='*70}

📋 WHAT I SEE:
{screen_description}

{'='*70}

💡 ANSWER & SOLUTION:
{solution}

{'='*70}
"""
        return formatted
    
    def save_answer(self, formatted_answer, filename):
        """Save formatted answer to file"""
        answer_file = filename.replace('.png', '_answer.txt')
        with open(answer_file, 'w', encoding='utf-8') as f:
            f.write(formatted_answer)
        print(f"✓ Answer saved: {answer_file}")
        return answer_file


class LocalAIScreenAssistant:
    """Main orchestrator - coordinates all agents"""
    
    def __init__(self):
        print("\n🚀 Initializing Local AI Screen Assistant...")
        print("💻 All processing happens on YOUR computer - no cloud!")
        
        # Initialize all agents
        self.capture_agent = ScreenCaptureAgent()
        self.vision_agent = VisionAgent(model="llava:13b")
        self.solver_agent = QuestionSolverAgent(model="llama3.2:latest")
        self.formatter_agent = AnswerFormatterAgent()
        
        print("\n✓ All agents initialized!\n")
    
    def process_screen(self):
        """Main workflow: capture → read → solve → format"""
        print("\n" + "="*70)
        print(f"📸 PROCESSING SCREEN - {datetime.now().strftime('%H:%M:%S')}")
        print("="*70)
        
        # Step 1: Capture screen
        print("\n[STEP 1/4] 📸 Capturing screen...")
        capture_info = self.capture_agent.capture_screen()
        if not capture_info:
            print("❌ Failed to capture screen")
            return
        
        filename = self.capture_agent.save_capture(capture_info)
        
        # Step 2: Vision agent reads the screen
        print("\n[STEP 2/4] 👁️  Vision Agent analyzing screenshot...")
        print("⏳ This may take 10-30 seconds...")
        screen_description = self.vision_agent.read_screen(capture_info['image'])
        
        if not screen_description:
            print("❌ Failed to read screen")
            return
        
        print("✓ Screen content extracted")
        
        # Step 3: Solver agent finds the answer
        print("\n[STEP 3/4] 🧠 Solver Agent working on solution...")
        print("⏳ Analyzing and solving...")
        solution = self.solver_agent.solve_question(screen_description)
        
        if not solution:
            print("❌ Failed to generate solution")
            return
        
        print("✓ Solution generated")
        
        # Step 4: Format and display
        print("\n[STEP 4/4] 📝 Formatting answer...")
        formatted_answer = self.formatter_agent.format_answer(
            screen_description, 
            solution
        )
        
        # Display result
        print(formatted_answer)
        
        # Save to file
        self.formatter_agent.save_answer(formatted_answer, filename)
        
        return formatted_answer
    
    def run_interactive(self):
        """Interactive mode - press ENTER to process screen"""
        print("\n" + "="*70)
        print("🤖 LOCAL AI SCREEN ASSISTANT - MULTI-AGENT SYSTEM")
        print("="*70)
        print("\n💻 Running completely offline on your machine!")
        print("\n📌 HOW TO USE:")
        print("1. Open your question/quiz/assignment")
        print("2. Press ENTER in this terminal")
        print("3. Wait 2 seconds to switch windows")
        print("4. AI agents will capture, read, and solve")
        print("\nType 'quit' to exit\n")
        print("="*70)
        
        while True:
            user_input = input("\n👉 Press ENTER to READ & SOLVE (or 'quit'): ").strip().lower()
            
            if user_input == 'quit':
                print("\n✓ Shutting down AI agents...")
                break
            
            # Give user time to switch windows
            print("\n⏳ Starting in 2 seconds... (switch to your content now!)")
            import time
            time.sleep(2)
            
            # Process the screen
            self.process_screen()


def main():
    """Main entry point"""
    print("""
    ╔══════════════════════════════════════════════════════════════════╗
    ║         LOCAL AI SCREEN ASSISTANT                                ║
    ║         Multi-Agent System - 100% Offline                        ║
    ║         Powered by Ollama (LLaVA + LLama)                        ║
    ╚══════════════════════════════════════════════════════════════════╝
    
    🎯 FEATURES:
    ✅ Runs completely on YOUR computer (no cloud, no API keys)
    ✅ Multi-agent architecture with specialized AI agents
    ✅ Vision Agent reads and understands screenshots
    ✅ Solver Agent answers questions and solves problems
    ✅ 100% private - your data never leaves your machine
    
    📋 REQUIREMENTS:
    • Ollama must be installed and running
    • Models will auto-download on first use (~7-13 GB)
    
    ⚠️  ETHICAL USE ONLY:
    This tool is for legitimate purposes:
    ✅ Personal learning and study
    ✅ Practice problems and homework
    ✅ Understanding concepts
    ✅ Research and information gathering
    
    ❌ DO NOT use for:
    • Taking actual exams or tests
    • Academic dishonesty
    • Graded assessments
    • Violating academic integrity
    """)
    
    # Check if Ollama is running
    try:
        ollama.list()
        print("✓ Ollama is running!")
    except Exception as e:
        print("\n❌ ERROR: Ollama not found or not running!")
        print("\n📥 To install Ollama:")
        print("1. Visit: https://ollama.ai/download")
        print("2. Download for Windows")
        print("3. Install and start Ollama")
        print("4. Run this script again")
        return
    
    # Confirm ethical use
    confirm = input("\nI will use this ethically for learning only (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("❌ Exiting. Ethical use not confirmed.")
        return
    
    # Start the assistant
    print("\n🚀 Starting Local AI Screen Assistant...\n")
    
    try:
        assistant = LocalAIScreenAssistant()
        assistant.run_interactive()
    except KeyboardInterrupt:
        print("\n\n🛑 Interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
    finally:
        print("\n✓ AI Screen Assistant stopped")
        print(f"📁 All captures in: screen_captures/")


if __name__ == "__main__":
    main()
