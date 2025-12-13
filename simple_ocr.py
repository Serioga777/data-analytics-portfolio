"""
Simple Screen OCR - Manual Trigger Version
Press ENTER in the terminal to capture instead of using hotkeys
"""

import pyautogui
import pytesseract
from PIL import Image
import pygetwindow as gw
import time
from datetime import datetime
import os

# Configure Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class SimpleOCR:
    def __init__(self):
        self.output_folder = "ocr_captures"
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
    
    def capture_browser(self):
        """Capture browser window"""
        print("\n🔍 Looking for browser window...")
        all_windows = gw.getAllWindows()
        browser_keywords = ['Chrome', 'Firefox', 'Edge', 'Safari', 'Opera', 'Brave']
        
        for window in all_windows:
            for browser in browser_keywords:
                if browser.lower() in window.title.lower():
                    print(f"✓ Found browser: {window.title}")
                    window.activate()
                    time.sleep(0.5)
                    
                    x, y, width, height = window.left, window.top, window.width, window.height
                    screenshot = pyautogui.screenshot(region=(x, y, width, height))
                    return screenshot, window.title
        
        print("⚠ No browser found, capturing active window instead...")
        active = gw.getActiveWindow()
        if active:
            x, y, width, height = active.left, active.top, active.width, active.height
            screenshot = pyautogui.screenshot(region=(x, y, width, height))
            return screenshot, active.title
        
        return None, None
    
    def extract_text(self, image):
        """Extract text using OCR"""
        try:
            text = pytesseract.image_to_string(image)
            return text.strip()
        except Exception as e:
            print(f"❌ OCR Error: {e}")
            return None
    
    def save_files(self, image, text):
        """Save screenshot and text"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save image
        img_file = f"{self.output_folder}/capture_{timestamp}.png"
        image.save(img_file)
        print(f"✓ Screenshot: {img_file}")
        
        # Save text
        if text:
            txt_file = f"{self.output_folder}/text_{timestamp}.txt"
            with open(txt_file, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"✓ Text file: {txt_file}")
            print(f"\n--- EXTRACTED TEXT ({len(text)} chars) ---")
            print(text[:500] + "..." if len(text) > 500 else text)
    
    def run(self):
        """Main capture loop"""
        print("\n" + "="*60)
        print("📸 SIMPLE SCREEN OCR - MANUAL MODE")
        print("="*60)
        print("\nPress ENTER to capture browser window")
        print("Type 'quit' to exit\n")
        
        while True:
            user_input = input("👉 Press ENTER to capture (or 'quit'): ").strip().lower()
            
            if user_input == 'quit':
                print("✓ Exiting...")
                break
            
            # Capture
            print("\n⏳ Capturing in 2 seconds... (switch to your browser now!)")
            time.sleep(2)
            
            image, title = self.capture_browser()
            
            if image:
                print(f"📸 Captured: {title}")
                print("🔤 Extracting text...")
                text = self.extract_text(image)
                self.save_files(image, text)
            else:
                print("❌ Failed to capture")
            
            print("\n" + "="*60)

if __name__ == "__main__":
    try:
        ocr = SimpleOCR()
        ocr.run()
    except KeyboardInterrupt:
        print("\n\n✓ Stopped by user")
