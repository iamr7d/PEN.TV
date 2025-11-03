# Quick YouTube Live Setup

## 🚀 **Fast Setup (5 Minutes)**

### **1. Download OBS Studio**
- Go to: https://obsproject.com/
- Download and install (FREE)
- Run as Administrator

### **2. YouTube Setup**
1. Go to: https://studio.youtube.com
2. Click **"Create"** → **"Go Live"**
3. Select **"Stream"** (not webcam)
4. Copy your **Stream Key**

### **3. OBS Configuration**
1. **Settings** → **Stream**
   - Service: **YouTube - RTMPS**
   - Stream Key: **[Paste your key]**

2. **Settings** → **Output**
   - Output Mode: **Simple**
   - Video Bitrate: **6000 Kbps**
   - Audio Bitrate: **160**

3. **Settings** → **Video**
   - Base Resolution: **1920x1080**
   - Output Resolution: **1920x1080**
   - FPS: **60**

### **4. Add Your News Graphics**
1. **Sources** → **+** → **Browser Source**
2. **URL**: `file:///D:/UAL/PROJECTS/PERSONAL/LIVE/index.html`
3. **Width**: 1920
4. **Height**: 1080
5. **FPS**: 60
6. Click **OK**

### **5. Go Live!**
1. Click **"Start Streaming"** in OBS
2. Go to YouTube Studio to monitor
3. Your R7D News Graphics are now LIVE! 🔴

---

## ⚡ **One-Click OBS Scene Import**

Save this as `R7D-News-Scene.json` and import into OBS:

```json
{
    "current_scene": "R7D News Live",
    "preview_locked": false,
    "scenes": [
        {
            "name": "R7D News Live",
            "sources": [
                {
                    "name": "R7D News Graphics",
                    "type": "browser_source",
                    "settings": {
                        "url": "file:///D:/UAL/PROJECTS/PERSONAL/LIVE/index.html",
                        "width": 1920,
                        "height": 1080,
                        "fps": 60,
                        "shutdown": true,
                        "restart_when_active": true
                    }
                }
            ]
        }
    ]
}
```

## 🎛️ **Live Control Hotkeys**
Add these hotkeys in OBS → Settings → Hotkeys:
- **F1**: Start/Stop Streaming
- **F2**: Toggle News Graphics
- **F3**: Mute/Unmute Audio
- **Spacebar**: Switch Scenes

---

## 🔴 **INSTANT STREAMING CHECKLIST**

### Before Going Live:
- [ ] Internet: 10+ Mbps upload speed
- [ ] OBS: Stream key configured
- [ ] Graphics: R7D system working
- [ ] Audio: Levels checked (-6dB max)
- [ ] Title: Set on YouTube

### Click "Start Streaming" When Ready! 
**Your professional R7D News Channel is LIVE on YouTube! 📺🎬**