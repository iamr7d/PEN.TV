import os
from dotenv import load_dotenv
from obsws_python import ReqClient

load_dotenv()
HOST = os.getenv("OBS_HOST", "localhost")
PORT = int(os.getenv("OBS_PORT", 4455))
PASS = os.getenv("OBS_PASSWORD", "R7D_News_2025")

print(f"Connecting to OBS at {HOST}:{PORT} ...")

try:
    client = ReqClient(host=HOST, port=PORT, password=PASS)
    ver = client.get_version()
    # support both attribute styles
    ws_ver = getattr(ver, 'obs_web_socket_version', None) or getattr(ver, 'obsWebSocketVersion', 'unknown')
    obs_ver = getattr(ver, 'obs_version', None) or getattr(ver, 'obsVersion', 'unknown')
    print("Connected! OBS WebSocket:", ws_ver, " OBS:", obs_ver)
except Exception as e:
    print("Connection failed:", e)
    print("- Ensure OBS is running")
    print("- Tools → WebSocket Server Settings is enabled")
    print("- Port and password match your .env settings")
