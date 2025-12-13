@echo off
echo ================================================
echo  Screen OCR Assistant - Admin Launcher
echo ================================================
echo.
echo This script will run the OCR assistant with
echo administrator privileges (required for hotkeys)
echo.
pause

PowerShell -Command "Start-Process python -ArgumentList 'screen_ocr_assistant.py' -Verb RunAs"
