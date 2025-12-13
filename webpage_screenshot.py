"""
Full Web Page Screenshot Capture
Captures entire scrolling web pages automatically
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from PIL import Image
import time
import io
from datetime import datetime

def capture_full_webpage(url, output_file=None):
    """
    Capture full scrolling webpage screenshot
    
    Args:
        url: Website URL to capture
        output_file: Optional output filename (auto-generated if not provided)
    """
    
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in background
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")
    
    print(f"🌐 Opening: {url}")
    
    try:
        # Initialize driver
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        
        # Wait for page to load
        time.sleep(3)
        
        # Get full page dimensions
        total_width = driver.execute_script("return document.body.scrollWidth")
        total_height = driver.execute_script("return document.body.scrollHeight")
        
        # Set window size to capture full page
        driver.set_window_size(total_width, total_height)
        time.sleep(1)
        
        # Take screenshot
        print(f"📸 Capturing full page ({total_width}x{total_height} pixels)...")
        screenshot = driver.get_screenshot_as_png()
        
        # Save screenshot
        if not output_file:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = f"webpage_screenshot_{timestamp}.png"
        
        with open(output_file, 'wb') as f:
            f.write(screenshot)
        
        driver.quit()
        
        print(f"✅ Saved: {output_file}")
        print(f"📏 Size: {total_width}x{total_height} pixels")
        
        return output_file
        
    except Exception as e:
        print(f"❌ Error: {e}")
        if 'driver' in locals():
            driver.quit()
        return None

def capture_current_tab():
    """Capture the currently active browser tab"""
    import pygetwindow as gw
    from PIL import ImageGrab
    
    # Find browser window
    browser_keywords = ['Chrome', 'Firefox', 'Edge', 'Brave']
    browser_window = None
    
    for window in gw.getAllWindows():
        for keyword in browser_keywords:
            if keyword.lower() in window.title.lower() and window.visible:
                browser_window = window
                break
        if browser_window:
            break
    
    if not browser_window:
        print("❌ No browser window found!")
        return None
    
    print(f"📸 Capturing: {browser_window.title}")
    
    # Activate and capture
    browser_window.activate()
    time.sleep(0.5)
    
    screenshot = ImageGrab.grab(bbox=(
        browser_window.left,
        browser_window.top,
        browser_window.right,
        browser_window.bottom
    ))
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"browser_screenshot_{timestamp}.png"
    screenshot.save(filename)
    
    print(f"✅ Saved: {filename}")
    return filename

if __name__ == "__main__":
    print("=" * 60)
    print("📸 WEB PAGE SCREENSHOT TOOL")
    print("=" * 60)
    print()
    
    choice = input("Choose option:\n1. Capture full scrolling page (enter URL)\n2. Capture current browser tab\n\nChoice (1 or 2): ").strip()
    
    if choice == "1":
        url = input("\nEnter URL (e.g., https://example.com): ").strip()
        if not url.startswith('http'):
            url = 'https://' + url
        
        print("\nInstalling required packages...")
        import subprocess
        subprocess.run(['pip', 'install', 'selenium', 'pillow'], capture_output=True)
        
        capture_full_webpage(url)
        
    elif choice == "2":
        capture_current_tab()
    
    else:
        print("Invalid choice!")
    
    print("\n✨ Done! Check the saved PNG file.")
