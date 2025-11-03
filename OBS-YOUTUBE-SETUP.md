# OBS Studio → YouTube Live Setup Guide

Based on your YouTube Live configuration, here's how to connect everything:

## 📺 Your YouTube Stream Details:
- **Stream Key**: `6w0p-kdz0-4xrj-tt6m-d4qz` 
- **Primary Server**: `rtmp://a.rtmp.youtube.com/live2`
- **Backup Server**: `rtmp://b.rtmp.youtube.com/live2?backup`

---

## 🚀 Step 1: Configure OBS Stream Settings

1. **Open OBS Studio**
2. **Go to Settings** → **Stream**
3. **Configure as follows**:
   ```
   Service: YouTube - RTMPS
   Server: Primary YouTube ingest server
   Stream Key: 6w0p-kdz0-4xrj-tt6m-d4qz
   ```

   **OR use Custom Server:**
   ```
   Service: Custom...
   Server: rtmp://a.rtmp.youtube.com/live2
   Stream Key: 6w0p-kdz0-4xrj-tt6m-d4qz
   ```

---

## ⚙️ Step 2: Enable OBS WebSocket (For Python Control)

1. **Tools** → **WebSocket Server Settings**
2. **Enable WebSocket server** ✅
3. **Server Port**: `4455` (default)
4. **Server Password**: `R7D_News_2025`
5. **Click Apply & OK**

---

## 🎬 Step 3: Import R7D Scene Collection

1. **File** → **Scene Collection** → **Import**
2. **Select**: `r7d_news_live_scene.json` (from your project folder)
3. **Activate the collection** after import

You'll now have these scenes:
- **Main Program**: Video content + HTML graphics
- **Breaking News Only**: Malayalam headlines + ticker
- **Full Graphics**: Complete R7D interface

---

## 🎥 Step 4: Configure Video Settings

**Settings** → **Video**:
```
Base (Canvas) Resolution: 1920x1080
Output (Scaled) Resolution: 1920x1080
Downscale Filter: Lanczos
Common FPS Values: 30 FPS
```

**Settings** → **Output** → **Streaming**:
```
Video Bitrate: 6000 Kbps (for 1080p60)
Audio Bitrate: 160 Kbps
Encoder: Hardware (NVENC) if available, else x264
Rate Control: CBR
Keyframe Interval: 2 seconds
```

---

## 🔧 Step 5: Test Connection

1. **Click "Start Streaming"** in OBS
2. **Check YouTube Studio** → **Live** tab
3. **Verify stream appears** in YouTube Live dashboard
4. **Stream health should show "Good" or "Excellent"**

---

## 🤖 Step 6: Launch Python Controller

**Option A: Automatic Mode**
```bash
cd "D:\UAL\PROJECTS\PERSONAL\LIVE"
python r7d_broadcast_controller.py --auto
```

**Option B: Manual Control**
```bash
cd "D:\UAL\PROJECTS\PERSONAL\LIVE"
python r7d_broadcast_controller.py
```

**Option C: One-Click Setup**
```bash
setup_r7d_broadcast.bat
```

---

## 📊 Live Control Features

Once connected, your Python controller can:

✅ **Auto-Switch Scenes**: Cycles between Main Program, Breaking News, Full Graphics
✅ **Update Headlines**: Real-time Malayalam breaking news
✅ **Video Management**: Auto-detects new videos in `videos/` folder
✅ **Stream Control**: Start/stop streaming and recording
✅ **Graphics Refresh**: Reload HTML graphics without interruption

---

## 🎛️ Controller Menu Options:

```
🎬 R7D BROADCAST CONTROLLER
==================================================
1. 🔴 Start Stream & Record
2. ⏹️  Stop Stream & Record
3. 🎬 Switch to Main Program
4. 📺 Switch to Full Graphics
5. 📰 Switch to Breaking News
6. 📝 Update Breaking News
7. 🎞️  Change Program Video
8. 🔄 Refresh Graphics
9. 🤖 Start Automation
0. ❌ Exit
```

---

## 📱 YouTube Live Dashboard

Monitor your stream at:
- **YouTube Studio** → **Content** → **Live**
- **Stream health**: Connection quality
- **Analytics**: Viewer count, engagement
- **Chat moderation**: Interact with viewers

---

## ⚠️ Troubleshooting

**Connection Issues:**
- Check stream key is correct
- Verify internet upload speed (minimum 8 Mbps for 1080p)
- Try backup server: `rtmp://b.rtmp.youtube.com/live2?backup`

**Python Controller Issues:**
- Ensure OBS WebSocket is enabled with correct password
- Check `.env` file has correct paths
- Install dependencies: `pip install obsws-python python-dotenv`

**Scene Issues:**
- Update file paths in scene collection JSON
- Ensure `index.html`, `bg video.mp4`, `R7D.svg` exist
- Check browser source loads correctly

---

## 🚀 Ready to Go Live!

Your R7D News channel is now configured for professional YouTube Live streaming with:
- ✅ OBS Studio configured with your stream key
- ✅ Professional scene collection imported
- ✅ Python automation controller ready
- ✅ Malayalam content support
- ✅ Real-time control capabilities

**Start streaming and broadcast your R7D News content live to YouTube!** 📺🎬