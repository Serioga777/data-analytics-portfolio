# Screen OCR Assistant - Setup Guide

## 📋 Prerequisites

### 1. Install Tesseract OCR
Tesseract is required for text extraction from images.

**Download & Install:**
- Visit: https://github.com/UB-Mannheim/tesseract/wiki
- Download the Windows installer (tesseract-ocr-w64-setup-v5.x.x.exe)
- Install to default location: `C:\Program Files\Tesseract-OCR`
- During installation, make sure to check "Add to PATH"

### 2. Verify Tesseract Installation
Open PowerShell and run:
```powershell
tesseract --version
```

If it shows version info, you're good to go!

## 🚀 Installation Steps

### Step 1: Install Python Packages
```powershell
pip install -r requirements_ocr.txt
```

### Step 2: Configure Tesseract Path (if needed)
If Tesseract is installed in a different location, edit line 16 in `screen_ocr_assistant.py`:
```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Your\Custom\Path\tesseract.exe'
```

### Step 3: Run the Assistant
```powershell
python screen_ocr_assistant.py
```

## 🎮 How to Use

### Hotkeys:
- **F9** - Capture browser window (Chrome, Firefox, Edge, etc.) + OCR
- **F10** - Capture active window + OCR
- **F11** - Capture full screen + OCR
- **ESC** - Stop the assistant

### Workflow:
1. Run the script
2. Navigate to the content you want to capture
3. Press the appropriate hotkey (F9 for browser)
4. Check the `ocr_captures/` folder for:
   - Screenshot (PNG file)
   - Extracted text (TXT file)

## 📁 Output Location

All captures are saved to: `ocr_captures/`

Files are named with timestamps:
- `browser_20241208_143052.png` - Screenshot
- `browser_20241208_143052.txt` - Extracted text

## 🔧 Advanced Features

### Capture Specific Window
The tool automatically detects browser windows by title keywords:
- Chrome
- Firefox
- Edge
- Safari
- Opera
- Brave

### OCR Accuracy
For best results:
- Use high contrast text
- Avoid small fonts (< 12pt)
- Ensure good screen brightness
- Avoid distorted or rotated text

### Improve OCR Quality
Edit the `extract_text_from_image` function to add preprocessing:
```python
def extract_text_from_image(self, image):
    # Convert to grayscale
    gray = image.convert('L')
    
    # Apply threshold (black and white)
    threshold = 150
    gray = gray.point(lambda x: 0 if x < threshold else 255, '1')
    
    # Extract text
    text = pytesseract.image_to_string(gray)
    return text.strip()
```

## 🛠️ Troubleshooting

### Issue: "Tesseract not found"
**Solution:** 
- Verify Tesseract is installed
- Update path in script line 16
- Restart your terminal/IDE

### Issue: "Permission denied"
**Solution:**
- Run PowerShell/terminal as Administrator
- Check antivirus isn't blocking keyboard hooks

### Issue: "No text extracted"
**Possible causes:**
- Text too small or blurry
- Low contrast colors
- Unusual fonts
- Non-English text (add language pack to Tesseract)

### Issue: "Browser window not detected"
**Solution:**
- Make sure browser title contains: Chrome, Firefox, Edge, etc.
- Try F10 (active window) instead
- Manually activate browser window first

## 🌍 Multi-Language Support

To extract text in other languages, install Tesseract language packs:

During Tesseract installation, select additional languages, or:
1. Download language data from: https://github.com/tesseract-ocr/tessdata
2. Place `.traineddata` files in: `C:\Program Files\Tesseract-OCR\tessdata`

Then modify the OCR call:
```python
text = pytesseract.image_to_string(image, lang='eng+spa+fra')  # English + Spanish + French
```

## ⚠️ Ethical Usage Reminder

This tool is designed for:
✅ Personal document processing
✅ Accessibility assistance
✅ Research and learning
✅ Extracting text from your own content

Do NOT use for:
❌ Academic dishonesty
❌ Cheating on tests/exams
❌ Bypassing security measures
❌ Unauthorized data collection

## 📝 License & Disclaimer

This tool is provided for educational and legitimate personal use only. Users are responsible for ensuring their usage complies with all applicable laws, regulations, and terms of service.

## 🆘 Support

If you encounter issues:
1. Check this README
2. Verify all dependencies are installed
3. Check Tesseract installation
4. Review error messages in console
5. Try running as Administrator

## 🔄 Updates & Improvements

Potential enhancements:
- Add AI-powered text analysis (GPT integration)
- Support for table detection
- PDF export functionality
- Cloud OCR API integration (Google Vision, Azure)
- Real-time monitoring mode
- Custom region selection with mouse
