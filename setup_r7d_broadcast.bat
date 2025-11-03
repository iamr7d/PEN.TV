@echo off
echo ===============================================
echo    R7D NEWS LIVE - OBS AUTOMATION SETUP
echo ===============================================

echo Installing Python dependencies...
pip install obsws-python watchdog python-dotenv

echo.
echo Creating videos directory...
mkdir "D:\UAL\PROJECTS\PERSONAL\LIVE\videos" 2>nul

echo.
echo ===============================================
echo SETUP COMPLETE!
echo ===============================================
echo.
echo Next steps:
echo 1. Import r7d_news_live_scene.json into OBS
echo 2. Enable OBS WebSocket (Tools → WebSocket Server Settings)
echo 3. Set password to: R7D_News_2025
echo 4. Run: python r7d_broadcast_controller.py
echo.
echo Starting R7D Broadcast Controller...
echo.
python r7d_broadcast_controller.py
pause