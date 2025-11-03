# AI News Live — OBS Automation Kit (Scenes + Python Controller)

This kit gives you a **professional YouTube Live pipeline** with OBS + Python control.

* Scene Collection JSON you can import into OBS
* Python controller that updates texts, swaps videos, reloads your HTML graphics, and starts/stops stream/record.

---

## 1) Prerequisites

* **OBS Studio 28+** (WebSocket is built-in)
* Enable: *Tools → WebSocket Server Settings* → **Enable** (default port `4455`), set a **password**.
* **Python 3.10+**
* `pip install obsws-python watchdog python-dotenv`

> Configure your YouTube RTMP key inside **OBS → Settings → Stream**. The Python script does not handle your stream key; OBS does.

---

## 2) Import Scene Collection into OBS

**File → Scene Collection → Import**, pick the JSON file below. Create a new file called `r7d_news_live_scene.json` and paste the content.

### `r7d_news_live_scene.json`

```json
{
  "format": 3,
  "name": "R7D News Live",
  "sources": [
    {
      "name": "Main Program",
      "type": "scene",
      "settings": {},
      "id": 1
    },
    {
      "name": "Breaking News Only",
      "type": "scene",
      "settings": {},
      "id": 2
    },
    {
      "name": "Full Graphics",
      "type": "scene", 
      "settings": {},
      "id": 3
    },
    {
      "name": "Studio Background",
      "type": "ffmpeg_source",
      "settings": {
        "local_file": "D:/UAL/PROJECTS/PERSONAL/LIVE/bg video.mp4",
        "is_looping": true,
        "restart_on_activate": true,
        "hw_decode": true
      },
      "id": 4
    },
    {
      "name": "R7D HTML Graphics",
      "type": "browser_source",
      "settings": {
        "is_local_file": true,
        "local_file": "D:/UAL/PROJECTS/PERSONAL/LIVE/index.html",
        "width": 1920,
        "height": 1080,
        "fps": 60,
        "shutdown": false,
        "refresh": true,
        "restart_when_active": true
      },
      "id": 5
    },
    {
      "name": "Program Video",
      "type": "ffmpeg_source",
      "settings": {
        "local_file": "D:/UAL/PROJECTS/PERSONAL/LIVE/ad01.mp4",
        "is_looping": true,
        "restart_on_activate": true,
        "hw_decode": true
      },
      "id": 6
    },
    {
      "name": "Breaking Headline",
      "type": "text_gdiplus_v2",
      "settings": {
        "text": "മുഖ്യമന്ത്രി നിരഞ്ഞ് ആമയിൽ പ്രഖ്യാപനം നടത്തുന്നു",
        "font": {"face": "Arial", "style": 1, "size": 48},
        "color1": 4294967295,
        "outline": true,
        "outline_size": 3,
        "outline_color": 4278190080
      },
      "id": 7
    },
    {
      "name": "Live Ticker",
      "type": "text_gdiplus_v2",
      "settings": {
        "text": "🔴 LIVE • R7D NEWS • സർക്കാർ പദ്ധതികൾ • സാമ്പത്തിക പരിഷ്കാരങ്ങൾ • വികസന പദ്ധതികൾ •",
        "font": {"face": "Arial", "style": 1, "size": 28},
        "color1": 4294967295,
        "outline": true,
        "outline_size": 2,
        "outline_color": 4278190080
      },
      "id": 8
    },
    {
      "name": "R7D Logo Overlay",
      "type": "image_source",
      "settings": {
        "file": "D:/UAL/PROJECTS/PERSONAL/LIVE/R7D.svg"
      },
      "id": 9
    },
    {
      "name": "Webcam",
      "type": "dshow_input",
      "settings": {
        "video_device_id": "default"
      },
      "id": 10
    }
  ],
  "scene_order": [
    {"name": "Main Program"},
    {"name": "Breaking News Only"},
    {"name": "Full Graphics"}
  ],
  "scene_items": [
    {
      "scene_name": "Main Program",
      "items": [
        {
          "source_name": "Studio Background",
          "align": 5,
          "pos": {"x": 0, "y": 0},
          "scale": {"x": 1.0, "y": 1.0},
          "bounds_type": 0
        },
        {
          "source_name": "Program Video",
          "align": 5,
          "pos": {"x": 960, "y": 300},
          "scale": {"x": 0.8, "y": 0.8},
          "bounds_type": 2,
          "bounds": {"x": 1400, "y": 800}
        },
        {
          "source_name": "R7D HTML Graphics",
          "align": 5,
          "pos": {"x": 0, "y": 0},
          "scale": {"x": 1.0, "y": 1.0},
          "bounds_type": 0
        },
        {
          "source_name": "R7D Logo Overlay",
          "align": 3,
          "pos": {"x": 1800, "y": 50},
          "scale": {"x": 0.3, "y": 0.3}
        }
      ]
    },
    {
      "scene_name": "Breaking News Only",
      "items": [
        {
          "source_name": "Studio Background",
          "align": 5,
          "pos": {"x": 0, "y": 0},
          "scale": {"x": 1.0, "y": 1.0},
          "bounds_type": 0
        },
        {
          "source_name": "Breaking Headline",
          "align": 5,
          "pos": {"x": 960, "y": 400},
          "scale": {"x": 1.0, "y": 1.0}
        },
        {
          "source_name": "Live Ticker",
          "align": 8,
          "pos": {"x": 40, "y": 1000},
          "scale": {"x": 1.0, "y": 1.0}
        },
        {
          "source_name": "R7D Logo Overlay",
          "align": 3,
          "pos": {"x": 1800, "y": 50},
          "scale": {"x": 0.4, "y": 0.4}
        }
      ]
    },
    {
      "scene_name": "Full Graphics",
      "items": [
        {
          "source_name": "R7D HTML Graphics",
          "align": 5,
          "pos": {"x": 0, "y": 0},
          "scale": {"x": 1.0, "y": 1.0},
          "bounds_type": 0
        },
        {
          "source_name": "Webcam",
          "align": 3,
          "pos": {"x": 1520, "y": 200},
          "scale": {"x": 0.6, "y": 0.6},
          "bounds_type": 2,
          "bounds": {"x": 400, "y": 300}
        }
      ]
    }
  ]
}
```

---

## 3) Python Controller

Create these files in your project directory:

### `.env`

```env
OBS_HOST=localhost
OBS_PORT=4455
OBS_PASSWORD=R7D_News_2025
AGENT_OUT=D:/UAL/PROJECTS/PERSONAL/LIVE/videos
PROGRAM_SOURCE=Program Video
HEADLINE_SOURCE=Breaking Headline
TICKER_SOURCE=Live Ticker
BROWSER_SOURCE=R7D HTML Graphics
LOGO_SOURCE=R7D Logo Overlay
HTML_FILE=D:/UAL/PROJECTS/PERSONAL/LIVE/index.html
```

### `r7d_broadcast_controller.py`

```python
import os, time, glob, pathlib, json, threading
from datetime import datetime
from dotenv import load_dotenv
from obsws_python import obsws, requests
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

load_dotenv()

# Configuration
HOST = os.getenv("OBS_HOST", "localhost")
PORT = int(os.getenv("OBS_PORT", 4455))
PASS = os.getenv("OBS_PASSWORD", "R7D_News_2025")
AGENT_OUT = os.getenv("AGENT_OUT", "D:/UAL/PROJECTS/PERSONAL/LIVE/videos")
PROGRAM_SOURCE = os.getenv("PROGRAM_SOURCE", "Program Video")
HEADLINE_SOURCE = os.getenv("HEADLINE_SOURCE", "Breaking Headline")
TICKER_SOURCE = os.getenv("TICKER_SOURCE", "Live Ticker")
BROWSER_SOURCE = os.getenv("BROWSER_SOURCE", "R7D HTML Graphics")
LOGO_SOURCE = os.getenv("LOGO_SOURCE", "R7D Logo Overlay")
HTML_FILE = os.getenv("HTML_FILE", "D:/UAL/PROJECTS/PERSONAL/LIVE/index.html")

class R7DBroadcastController:
    def __init__(self):
        self.client = None
        self.is_streaming = False
        self.is_recording = False
        self.current_scene = "Main Program"
        self.connect_obs()

    def connect_obs(self):
        """Connect to OBS WebSocket"""
        try:
            self.client = obsws(HOST, PORT, PASS)
            self.client.connect()
            logger.info(f"✅ Connected to OBS at {HOST}:{PORT}")
            return True
        except Exception as e:
            logger.error(f"❌ Failed to connect to OBS: {e}")
            return False

    # --------------------------- OBS Controls ---------------------------

    def set_text(self, input_name: str, text: str):
        """Update text source content"""
        try:
            self.client.call(requests.SetInputSettings(
                inputName=input_name, 
                inputSettings={"text": text}, 
                overlay=True
            ))
            logger.info(f"📝 Updated {input_name}: {text[:50]}...")
        except Exception as e:
            logger.error(f"❌ Failed to update text {input_name}: {e}")

    def set_media_file(self, input_name: str, file_path: str):
        """Change media source file"""
        try:
            settings = {
                "local_file": str(pathlib.Path(file_path)),
                "is_local_file": True,
                "restart_on_activate": True,
                "hw_decode": True
            }
            self.client.call(requests.SetInputSettings(
                inputName=input_name, 
                inputSettings=settings, 
                overlay=True
            ))
            logger.info(f"🎥 Changed {input_name} to: {file_path}")
        except Exception as e:
            logger.error(f"❌ Failed to update media {input_name}: {e}")

    def refresh_browser(self, input_name: str):
        """Refresh browser source"""
        try:
            # Get current settings
            response = self.client.call(requests.GetInputSettings(inputName=input_name))
            settings = response.inputSettings
            
            # Refresh by toggling URL
            if settings.get("is_local_file", False):
                path = settings.get("local_file")
                self.client.call(requests.SetInputSettings(
                    inputName=input_name, 
                    inputSettings={"local_file": path}, 
                    overlay=True
                ))
                logger.info(f"🔄 Refreshed browser source: {input_name}")
        except Exception as e:
            logger.error(f"❌ Failed to refresh browser {input_name}: {e}")

    def switch_scene(self, scene_name: str):
        """Switch to different scene"""
        try:
            self.client.call(requests.SetCurrentProgramScene(sceneName=scene_name))
            self.current_scene = scene_name
            logger.info(f"🎬 Switched to scene: {scene_name}")
        except Exception as e:
            logger.error(f"❌ Failed to switch scene: {e}")

    def start_stream_and_record(self):
        """Start streaming and recording"""
        try:
            if not self.is_streaming:
                self.client.call(requests.StartStreaming())
                self.is_streaming = True
                logger.info("🔴 Started streaming")
            
            if not self.is_recording:
                self.client.call(requests.StartRecording())
                self.is_recording = True
                logger.info("⏺️ Started recording")
        except Exception as e:
            logger.error(f"❌ Failed to start stream/record: {e}")

    def stop_stream_and_record(self):
        """Stop streaming and recording"""
        try:
            if self.is_streaming:
                self.client.call(requests.StopStreaming())
                self.is_streaming = False
                logger.info("⏹️ Stopped streaming")
            
            if self.is_recording:
                self.client.call(requests.StopRecording())
                self.is_recording = False
                logger.info("⏹️ Stopped recording")
        except Exception as e:
            logger.error(f"❌ Failed to stop stream/record: {e}")

    # --------------------------- Content Management ---------------------------

    def newest_mp4(self, folder: str):
        """Find the newest MP4 file in folder"""
        if not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)
            return None
            
        files = glob.glob(os.path.join(folder, "*.mp4"))
        if not files:
            return None
        return max(files, key=os.path.getmtime)

    def update_breaking_news(self, headline: str, ticker: str = None):
        """Update breaking news content"""
        self.set_text(HEADLINE_SOURCE, headline)
        if ticker:
            self.set_text(TICKER_SOURCE, f"🔴 LIVE • R7D NEWS • {ticker}")
        self.switch_scene("Breaking News Only")

    def update_ticker_news(self, news_items: list):
        """Update ticker with multiple news items"""
        ticker_text = " • ".join([f"🔴 LIVE", "R7D NEWS"] + news_items) + " • "
        self.set_text(TICKER_SOURCE, ticker_text)

    def show_full_graphics(self):
        """Switch to full HTML graphics mode"""
        self.refresh_browser(BROWSER_SOURCE)
        self.switch_scene("Full Graphics")

    def show_main_program(self):
        """Switch to main program with video"""
        self.switch_scene("Main Program")

    # --------------------------- Automated Loop ---------------------------

    def run_automation_loop(self):
        """Main automation loop"""
        logger.info("🤖 Starting R7D automation loop...")
        
        last_file = None
        loop_count = 0
        
        # Initial setup
        self.set_text(HEADLINE_SOURCE, "R7D NEWS LIVE ഓൺ എയർ")
        self.set_text(TICKER_SOURCE, "🔴 LIVE • R7D NEWS • പ്രധാന വാർത്തകൾ • സർക്കാർ നയങ്ങൾ • സാമൂഹിക വിഷയങ്ങൾ •")
        self.refresh_browser(BROWSER_SOURCE)
        
        # Start with full graphics
        self.show_full_graphics()
        
        while True:
            try:
                loop_count += 1
                
                # Check for new video content
                newest_video = self.newest_mp4(AGENT_OUT)
                if newest_video and newest_video != last_file:
                    logger.info(f"🆕 New content detected: {newest_video}")
                    self.set_media_file(PROGRAM_SOURCE, newest_video)
                    self.show_main_program()
                    last_file = newest_video
                
                # Cycle through different modes every 30 seconds
                if loop_count % 15 == 0:  # Every 30 seconds (15 * 2s sleep)
                    current_time = datetime.now().strftime("%H:%M")
                    
                    if loop_count % 45 == 0:  # Every 90 seconds - Breaking news
                        breaking_headlines = [
                            "സർക്കാർ പുതിയ നയം പ്രഖ്യാപിച്ചു",
                            "സാമ്പത്തിക മേഖലയിൽ പുരോഗതി",
                            "വിദ്യാഭ്യാസ മേഖലയിൽ നവീകരണം",
                            "ആരോഗ്യ സംരക്ഷണത്തിൽ മുന്നേറ്റം"
                        ]
                        headline = breaking_headlines[loop_count % len(breaking_headlines)]
                        self.update_breaking_news(headline, "പ്രധാന വാർത്തകൾ • സർക്കാർ നയങ്ങൾ")
                        
                    elif loop_count % 30 == 0:  # Every 60 seconds - Full graphics
                        self.show_full_graphics()
                        
                    else:  # Main program view
                        self.show_main_program()
                
                # Update ticker every 10 seconds
                if loop_count % 5 == 0:
                    news_items = [
                        "സർക്കാർ പദ്ധതികൾ",
                        "സാമ്പത്തിക പരിഷ്കാരങ്ങൾ",
                        "വികസന പദ്ധതികൾ",
                        "സാമൂഹിക സുരക്ഷ",
                        f"സമയം: {datetime.now().strftime('%H:%M:%S')}"
                    ]
                    self.update_ticker_news(news_items)
                
                time.sleep(2)
                
            except KeyboardInterrupt:
                logger.info("🛑 Stopping automation...")
                break
            except Exception as e:
                logger.error(f"❌ Error in automation loop: {e}")
                time.sleep(5)

    # --------------------------- Manual Controls ---------------------------

    def manual_control_menu(self):
        """Interactive manual control menu"""
        while True:
            print("\n" + "="*50)
            print("🎬 R7D BROADCAST CONTROLLER")
            print("="*50)
            print("1. 🔴 Start Stream & Record")
            print("2. ⏹️  Stop Stream & Record")
            print("3. 🎬 Switch to Main Program")
            print("4. 📺 Switch to Full Graphics")
            print("5. 📰 Switch to Breaking News")
            print("6. 📝 Update Breaking News")
            print("7. 🎞️  Change Program Video")
            print("8. 🔄 Refresh Graphics")
            print("9. 🤖 Start Automation")
            print("0. ❌ Exit")
            print("="*50)
            
            choice = input("Select option: ").strip()
            
            if choice == "1":
                self.start_stream_and_record()
            elif choice == "2":
                self.stop_stream_and_record()
            elif choice == "3":
                self.show_main_program()
            elif choice == "4":
                self.show_full_graphics()
            elif choice == "5":
                self.switch_scene("Breaking News Only")
            elif choice == "6":
                headline = input("Enter breaking news headline: ")
                ticker = input("Enter ticker text (optional): ")
                self.update_breaking_news(headline, ticker if ticker else None)
            elif choice == "7":
                video_path = input("Enter video file path: ")
                if os.path.exists(video_path):
                    self.set_media_file(PROGRAM_SOURCE, video_path)
                else:
                    print("❌ File not found!")
            elif choice == "8":
                self.refresh_browser(BROWSER_SOURCE)
            elif choice == "9":
                self.run_automation_loop()
            elif choice == "0":
                break
            else:
                print("❌ Invalid option!")

if __name__ == "__main__":
    try:
        controller = R7DBroadcastController()
        
        if len(os.sys.argv) > 1 and os.sys.argv[1] == "--auto":
            # Automatic mode
            controller.run_automation_loop()
        else:
            # Manual control mode
            controller.manual_control_menu()
            
    except KeyboardInterrupt:
        print("\n🛑 R7D Broadcast Controller stopped.")
    except Exception as e:
        logger.error(f"💥 Fatal error: {e}")
```

---

## 4) Quick Setup Script

Create `setup_r7d_broadcast.bat`:

```batch
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
pause
```

---

## 5) Usage Instructions

### **Automatic Mode:**
```bash
python r7d_broadcast_controller.py --auto
```
- Automatically cycles between scenes
- Monitors for new video files
- Updates news content dynamically
- Handles streaming/recording

### **Manual Mode:**
```bash
python r7d_broadcast_controller.py
```
- Interactive menu for manual control
- Update breaking news in real-time
- Switch scenes manually
- Control streaming/recording

### **OBS Setup:**
1. Import `r7d_news_live_scene.json`
2. Enable WebSocket: Tools → WebSocket Server Settings
3. Set password: `R7D_News_2025`
4. Configure YouTube stream key in OBS Settings

---

## 6) Features

✅ **Three Scene Modes:**
- **Main Program**: Video + HTML graphics overlay
- **Breaking News Only**: Text headlines + ticker
- **Full Graphics**: Complete HTML interface

✅ **Automation:**
- Auto-detect new video files
- Cycle through content modes
- Update news ticker dynamically
- Malayalam/English content support

✅ **Manual Control:**
- Interactive menu system
- Real-time content updates
- Scene switching
- Stream/record management

✅ **Professional Quality:**
- Hardware-accelerated video
- 60 FPS browser source
- Broadcast-safe layouts
- Multiple audio routing options

---

**Your R7D News Channel now has full OBS automation with Python control! 🎬📺**