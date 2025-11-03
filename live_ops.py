import os
import argparse
from dotenv import load_dotenv
from obsws_python import ReqClient

load_dotenv()
HOST = os.getenv("OBS_HOST", "localhost")
PORT = int(os.getenv("OBS_PORT", 4455))
PASS = os.getenv("OBS_PASSWORD", "R7D_News_2025")
PROGRAM_SOURCE = os.getenv("PROGRAM_SOURCE", "Program Video")
HEADLINE_SOURCE = os.getenv("HEADLINE_SOURCE", "Breaking Headline")
TICKER_SOURCE = os.getenv("TICKER_SOURCE", "Live Ticker")
BROWSER_SOURCE = os.getenv("BROWSER_SOURCE", "R7D HTML Graphics")

class OBSClient:
    def __init__(self):
    self.client = ReqClient(host=HOST, port=PORT, password=PASS)

    def disconnect(self):
        try:
            # ReqClient has no explicit disconnect; noop
            pass
        except Exception:
            pass

    def set_text(self, input_name: str, text: str):
    self.client.set_input_settings(input_name, {"text": text}, True)

    def set_media(self, input_name: str, path: str):
    self.client.set_input_settings(input_name, {"local_file": path, "is_local_file": True, "restart_on_activate": True}, True)

    def refresh_browser(self, input_name: str):
        # Re-apply the configured HTML path to force a refresh
        html_path = os.getenv("HTML_FILE")
        if html_path:
            self.client.set_input_settings(input_name, {"local_file": html_path}, True)

    def switch_scene(self, name: str):
    self.client.set_current_program_scene(name)

    def start(self):
    self.client.start_stream()
    self.client.start_record()

    def stop(self):
    self.client.stop_stream()
    self.client.stop_record()

    def status(self):
        s = self.client.get_stream_status()
        r = self.client.get_record_status()
        # handle case/attr names
        s_active = getattr(s, 'output_active', None)
        if s_active is None:
            s_active = getattr(s, 'outputActive', False)
        r_active = getattr(r, 'output_active', None)
        if r_active is None:
            r_active = getattr(r, 'outputActive', False)
        return s_active, r_active


def main():
    parser = argparse.ArgumentParser(description="Quick OBS Live Ops")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_head = sub.add_parser("headline", help="Update breaking headline (and cut to Breaking News)")
    p_head.add_argument("text")
    p_head.add_argument("--no-cut", action="store_true")

    p_tick = sub.add_parser("ticker", help="Update ticker text")
    p_tick.add_argument("text")

    p_vid = sub.add_parser("video", help="Switch Program Video file")
    p_vid.add_argument("path")
    p_vid.add_argument("--cut-main", action="store_true")

    p_ref = sub.add_parser("refresh", help="Refresh HTML graphics")

    p_scene = sub.add_parser("scene", help="Switch to scene by name")
    p_scene.add_argument("name", choices=["Main Program", "Full Graphics", "Breaking News Only"])  # adjust if renamed

    sub.add_parser("cut-full", help="Cut to Full Graphics")
    sub.add_parser("cut-main", help="Cut to Main Program")
    sub.add_parser("cut-breaking", help="Cut to Breaking News Only")

    sub.add_parser("start", help="Start streaming and recording")
    sub.add_parser("stop", help="Stop streaming and recording")
    sub.add_parser("status", help="Show stream/record status")

    args = parser.parse_args()
    obs = OBSClient()

    try:
        if args.cmd == "headline":
            obs.set_text(HEADLINE_SOURCE, args.text)
            if not args.no_cut:
                obs.switch_scene("Breaking News Only")
        elif args.cmd == "ticker":
            obs.set_text(TICKER_SOURCE, args.text)
        elif args.cmd == "video":
            obs.set_media(PROGRAM_SOURCE, args.path)
            if args.cut_main:
                obs.switch_scene("Main Program")
        elif args.cmd == "refresh":
            obs.refresh_browser(BROWSER_SOURCE)
        elif args.cmd == "scene":
            obs.switch_scene(args.name)
        elif args.cmd == "cut-full":
            obs.switch_scene("Full Graphics")
        elif args.cmd == "cut-main":
            obs.switch_scene("Main Program")
        elif args.cmd == "cut-breaking":
            obs.switch_scene("Breaking News Only")
        elif args.cmd == "start":
            obs.start()
        elif args.cmd == "stop":
            obs.stop()
        elif args.cmd == "status":
            s, r = obs.status()
            print(f"Streaming: {'ON' if s else 'OFF'} | Recording: {'ON' if r else 'OFF'}")
    finally:
        obs.disconnect()

if __name__ == "__main__":
    main()
