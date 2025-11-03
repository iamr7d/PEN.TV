import os, time, glob, pathlib, json, threading
from datetime import datetime
from dotenv import load_dotenv
from obsws_python import ReqClient
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
            # obsws-python v1.8 exposes ReqClient at top-level
            self.client = ReqClient(host=HOST, port=PORT, password=PASS, timeout=5)
            # simple call to verify
            ver = self.client.get_version()
            logger.info(f"✅ Connected to OBS at {HOST}:{PORT} | OBS {ver.obs_version} | WS {ver.obs_web_socket_version}")
            return True
        except Exception as e:
            logger.error(f"❌ Failed to connect to OBS: {e}")
            return False

    # --------------------------- OBS Controls ---------------------------

    def input_exists(self, name: str) -> bool:
        try:
            lst = self.client.get_input_list()
            inputs = lst.get('inputs') if isinstance(lst, dict) else getattr(lst, 'inputs', [])
            if isinstance(inputs, list):
                for i in inputs:
                    in_name = i.get('inputName') if isinstance(i, dict) else getattr(i, 'inputName', None)
                    if in_name == name:
                        return True
        except Exception:
            pass
        return False

    def scene_exists(self, name: str) -> bool:
        try:
            lst = self.client.get_scene_list()
            scenes = lst.get('scenes') if isinstance(lst, dict) else getattr(lst, 'scenes', [])
            if isinstance(scenes, list):
                for s in scenes:
                    s_name = s.get('sceneName') if isinstance(s, dict) else getattr(s, 'sceneName', None)
                    if s_name == name:
                        return True
        except Exception:
            pass
        return False

    def set_text(self, input_name: str, text: str):
        """Update text source content"""
        try:
            if not self.input_exists(input_name):
                logger.warning(f"⚠️ Input not found: {input_name} (skipping)")
                return
            self.client.set_input_settings(input_name, {"text": text}, True)
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
            if not self.input_exists(input_name):
                logger.warning(f"⚠️ Input not found: {input_name} (skipping)")
                return
            self.client.set_input_settings(input_name, settings, True)
            logger.info(f"🎥 Changed {input_name} to: {file_path}")
        except Exception as e:
            logger.error(f"❌ Failed to update media {input_name}: {e}")

    def refresh_browser(self, input_name: str):
        """Refresh browser source"""
        try:
            # Get current settings and toggle to force refresh
            # Simple refresh by reassigning the configured HTML file path
            if not self.input_exists(input_name):
                logger.warning(f"⚠️ Input not found: {input_name} (skipping)")
                return
            self.client.set_input_settings(input_name, {"local_file": HTML_FILE}, True)
            logger.info(f"🔄 Refreshed browser source: {input_name}")
        except Exception as e:
            logger.error(f"❌ Failed to refresh browser {input_name}: {e}")

    def switch_scene(self, scene_name: str):
        """Switch to different scene"""
        try:
            if not self.scene_exists(scene_name):
                logger.warning(f"⚠️ Scene not found: {scene_name} (skipping)")
                return
            self.client.set_current_program_scene(scene_name)
            self.current_scene = scene_name
            logger.info(f"🎬 Switched to scene: {scene_name}")
        except Exception as e:
            logger.error(f"❌ Failed to switch scene: {e}")

    def start_stream_and_record(self):
        """Start streaming and recording"""
        try:
            # Query real status first
            try:
                s = self.client.get_stream_status()
                self.is_streaming = getattr(s, 'output_active', None) if hasattr(s, 'output_active') else getattr(s, 'outputActive', False)
            except Exception:
                pass
            if not self.is_streaming:
                self.client.start_stream()
                self.is_streaming = True
                logger.info("🔴 Started streaming")
            
            try:
                r = self.client.get_record_status()
                self.is_recording = getattr(r, 'output_active', None) if hasattr(r, 'output_active') else getattr(r, 'outputActive', False)
            except Exception:
                pass
            if not self.is_recording:
                self.client.start_record()
                self.is_recording = True
                logger.info("⏺️ Started recording")
        except Exception as e:
            logger.error(f"❌ Failed to start stream/record: {e}")

    def stop_stream_and_record(self):
        """Stop streaming and recording"""
        try:
            if self.is_streaming:
                self.client.stop_stream()
                self.is_streaming = False
                logger.info("⏹️ Stopped streaming")
            
            if self.is_recording:
                self.client.stop_record()
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