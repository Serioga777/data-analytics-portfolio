"""
Screen Capture and OCR Assistant
Captures screen content and extracts text using OCR
For legitimate use: personal documents, accessibility, learning tools only
"""

import pyautogui
import pytesseract
from PIL import Image
import pygetwindow as gw
import time
import keyboard
import threading
from datetime import datetime
import os

# Configure Tesseract path (update this to your Tesseract installation)
# Download from: https://github.com/UB-Mannheim/tesseract/wiki
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class ScreenOCRAssistant:
    def __init__(self):
        self.is_running = False
        self.output_folder = "ocr_captures"
        self.create_output_folder()
        
    def create_output_folder(self):
        """Create folder for saving screenshots"""
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
            print(f"✓ Created output folder: {self.output_folder}")
    
    def capture_full_screen(self):
        """Capture entire screen"""
        screenshot = pyautogui.screenshot()
        return screenshot
    
    def capture_region(self, x, y, width, height):
        """Capture specific region of screen"""
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        return screenshot
    
    def capture_active_window(self):
        """Capture only the active window"""
        try:
            active_window = gw.getActiveWindow()
            if active_window:
                x, y, width, height = active_window.left, active_window.top, active_window.width, active_window.height
                screenshot = self.capture_region(x, y, width, height)
                return screenshot, active_window.title
            else:
                print("⚠ No active window found")
                return None, None
        except Exception as e:
            print(f"❌ Error capturing window: {e}")
            return None, None
    
    def capture_browser_window(self):
        """Capture browser window specifically (Chrome, Firefox, Edge, etc.)"""
        try:
            # Get all windows
            all_windows = gw.getAllWindows()
            
            # Common browser window title patterns
            browser_keywords = ['Chrome', 'Firefox', 'Edge', 'Safari', 'Opera', 'Brave']
            
            for window in all_windows:
                for browser in browser_keywords:
                    if browser.lower() in window.title.lower():
                        # Activate the browser window
                        window.activate()
                        time.sleep(0.5)  # Wait for window to come to front
                        
                        x, y, width, height = window.left, window.top, window.width, window.height
                        screenshot = self.capture_region(x, y, width, height)
                        return screenshot, window.title
            
            print("⚠ No browser window found")
            return None, None
            
        except Exception as e:
            print(f"❌ Error capturing browser: {e}")
            return None, None
    
    def extract_text_from_image(self, image):
        """Extract text from image using OCR"""
        try:
            # Use Tesseract OCR
            text = pytesseract.image_to_string(image)
            return text.strip()
        except Exception as e:
            print(f"❌ OCR Error: {e}")
            return None
    
    def save_screenshot(self, image, prefix="capture"):
        """Save screenshot with timestamp"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.output_folder}/{prefix}_{timestamp}.png"
        image.save(filename)
        print(f"✓ Screenshot saved: {filename}")
        return filename
    
    def save_extracted_text(self, text, prefix="text"):
        """Save extracted text to file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.output_folder}/{prefix}_{timestamp}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"✓ Text saved: {filename}")
        return filename
    
    def capture_and_extract(self, mode="browser"):
        """Main function: capture screen and extract text"""
        print(f"\n{'='*60}")
        print(f"🔍 Capturing {mode.upper()} at {datetime.now().strftime('%H:%M:%S')}")
        print(f"{'='*60}")
        
        # Capture based on mode
        if mode == "fullscreen":
            image = self.capture_full_screen()
            title = "Full Screen"
        elif mode == "browser":
            image, title = self.capture_browser_window()
        elif mode == "active":
            image, title = self.capture_active_window()
        else:
            image = self.capture_full_screen()
            title = "Full Screen"
        
        if image is None:
            print("❌ Failed to capture screen")
            return None, None
        
        print(f"📸 Captured: {title}")
        
        # Save screenshot
        screenshot_file = self.save_screenshot(image, prefix=mode)
        
        # Extract text
        print("🔤 Extracting text...")
        text = self.extract_text_from_image(image)
        
        if text:
            print(f"✓ Extracted {len(text)} characters")
            print(f"\n--- EXTRACTED TEXT ---\n{text[:500]}...")  # Show first 500 chars
            
            # Save text
            text_file = self.save_extracted_text(text, prefix=mode)
            
            return screenshot_file, text_file
        else:
            print("⚠ No text extracted")
            return screenshot_file, None
    
    def start_hotkey_listener(self):
        """Start listening for hotkeys"""
        print("\n" + "="*60)
        print("🚀 SCREEN OCR ASSISTANT - RUNNING")
        print("="*60)
        print("\n📌 HOTKEYS:")
        print("  F9  - Capture Browser Window + OCR")
        print("  F10 - Capture Active Window + OCR")
        print("  F11 - Capture Full Screen + OCR")
        print("  ESC - Stop Assistant")
        print("\n⏳ Waiting for hotkey press...")
        print("="*60 + "\n")
        
        self.is_running = True
        
        # Register hotkeys
        keyboard.add_hotkey('f9', lambda: self.capture_and_extract("browser"))
        keyboard.add_hotkey('f10', lambda: self.capture_and_extract("active"))
        keyboard.add_hotkey('f11', lambda: self.capture_and_extract("fullscreen"))
        keyboard.add_hotkey('esc', self.stop)
        
        # Keep running
        keyboard.wait('esc')
    
    def stop(self):
        """Stop the assistant"""
        print("\n🛑 Stopping Screen OCR Assistant...")
        self.is_running = False
        keyboard.unhook_all()


def main():
    """Main entry point"""
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║         SCREEN CAPTURE & OCR ASSISTANT                   ║
    ║         For legitimate personal use only                 ║
    ╚══════════════════════════════════════════════════════════╝
    
    ⚠️  IMPORTANT NOTICE:
    This tool is for legitimate purposes only:
    • Extracting text from your own documents
    • Accessibility assistance
    • Personal research and note-taking
    • Learning and development
    
    ❌ DO NOT use for:
    • Academic dishonesty or cheating
    • Bypassing security measures
    • Unauthorized data collection
    • Any unethical purposes
    """)
    
    # Ask for confirmation
    response = input("\n✓ I understand and will use this tool ethically (yes/no): ").strip().lower()
    
    if response != 'yes':
        print("❌ Exiting. Tool usage not confirmed.")
        return
    
    # Create and start assistant
    assistant = ScreenOCRAssistant()
    
    try:
        assistant.start_hotkey_listener()
    except KeyboardInterrupt:
        print("\n\n🛑 Interrupted by user")
    finally:
        print("\n✓ Screen OCR Assistant stopped")
        print(f"📁 Captures saved in: {assistant.output_folder}/")


if __name__ == "__main__":
    main()
