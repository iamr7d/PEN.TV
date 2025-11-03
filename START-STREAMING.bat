@echo off
echo ======================================
echo    R7D NEWS GRAPHICS - STREAMING LAUNCHER
echo ======================================
echo.

REM Check if OBS Studio is installed
if exist "C:\Program Files\obs-studio\bin\64bit\obs64.exe" (
    echo ✓ OBS Studio found
) else (
    echo ✗ OBS Studio not found
    echo Please download OBS Studio from: https://obsproject.com/
    echo.
    pause
    exit /b 1
)

REM Check if Chrome is available for better performance
if exist "C:\Program Files\Google\Chrome\Application\chrome.exe" (
    echo ✓ Chrome found - will use for optimal performance
    set BROWSER="C:\Program Files\Google\Chrome\Application\chrome.exe"
) else if exist "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" (
    echo ✓ Chrome found - will use for optimal performance  
    set BROWSER="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
) else (
    echo ⚠ Chrome not found - using default browser
    set BROWSER=start
)

echo.
echo Starting R7D News Graphics System...
echo.

REM Open the news graphics in browser for preview
echo Opening graphics preview...
%BROWSER% "file:///%~dp0index.html" --new-window --disable-web-security --disable-features=VizDisplayCompositor --enable-gpu-rasterization

REM Wait a moment for browser to load
timeout /t 3 /nobreak >nul

REM Launch OBS Studio
echo.
echo Launching OBS Studio...
start "" "C:\Program Files\obs-studio\bin\64bit\obs64.exe"

echo.
echo ======================================
echo    SETUP INSTRUCTIONS
echo ======================================
echo.
echo 1. Configure OBS Studio:
echo    - Add Browser Source
echo    - URL: file:///%~dp0index.html
echo    - Size: 1920x1080, 60 FPS
echo.
echo 2. YouTube Stream Setup:
echo    - Go to: https://studio.youtube.com
echo    - Create → Go Live → Stream
echo    - Copy Stream Key to OBS
echo.
echo 3. OBS Settings:
echo    - Stream: YouTube - RTMPS
echo    - Video: 1920x1080, 60 FPS
echo    - Bitrate: 6000 Kbps
echo.
echo 4. Click "Start Streaming" in OBS
echo.
echo Your R7D News Channel will be LIVE! 🔴
echo.
echo Press any key to open setup guides...
pause

REM Open setup guides
start "" "%~dp0QUICK-START-STREAMING.md"
start "" "%~dp0YOUTUBE-STREAMING-GUIDE.md"

echo.
echo Setup guides opened. Happy streaming! 🎥📺
echo.
pause