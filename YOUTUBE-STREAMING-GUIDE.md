# YouTube Live Streaming Setup Guide

## 🎥 **YouTube Live Stream Configuration**

### **Step 1: YouTube Channel Requirements**
- ✅ YouTube channel with no live streaming restrictions in past 90 days
- ✅ Channel verification (phone number)
- ✅ No mobile live streaming restrictions
- ✅ Good standing with YouTube Community Guidelines

### **Step 2: Enable Live Streaming**
1. Go to [YouTube Studio](https://studio.youtube.com)
2. Click **"Create"** → **"Go Live"**
3. Follow prompts to enable live streaming
4. Choose **"Stream"** option (not webcam)

---

## 🔧 **OBS Studio Setup for YouTube**

### **Download & Install**
1. Download [OBS Studio](https://obsproject.com/) (FREE)
2. Install with default settings
3. Run OBS as Administrator

### **YouTube Stream Configuration**

#### **Stream Settings**
1. **File** → **Settings** → **Stream**
2. **Service**: YouTube - RTMPS
3. **Server**: Primary YouTube ingest server
4. **Stream Key**: Get from YouTube Live dashboard

#### **Output Settings**
```
Recording Quality: Indistinguishable Quality
Recording Format: mp4
Encoder: Hardware (NVENC) if available, otherwise x264
Rate Control: CBR
Bitrate: 6000 Kbps (1080p60) or 9000 Kbps (1080p60 high quality)
Keyframe Interval: 2
Preset: Quality (for x264) / Quality (for NVENC)
Profile: high
```

#### **Video Settings**
```
Base (Canvas) Resolution: 1920x1080
Output (Scaled) Resolution: 1920x1080
Downscale Filter: Lanczos (Sharpened scaling, 36 samples)
Common FPS Values: 60 or 30
```

#### **Audio Settings**
```
Sample Rate: 44.1 kHz or 48 kHz
Channels: Stereo
Desktop Audio Device: Default
Mic/Auxiliary Audio: None (unless you want commentary)
```

---

## 🌐 **Browser Source Setup**

### **Adding Your News Graphics**
1. **Add Source** → **Browser Source**
2. **Create New** → Name: "R7D News Graphics"
3. **Properties**:
   ```
   URL: file:///D:/UAL/PROJECTS/PERSONAL/LIVE/index.html
   Width: 1920
   Height: 1080
   FPS: 60
   Custom CSS: (leave blank)
   Shutdown source when not visible: ✓
   Refresh browser when scene becomes active: ✓
   ```

### **Advanced Browser Settings**
- **Hardware Acceleration**: ✓ Enabled
- **Reroute Audio**: ✓ (if you want audio from videos)

---

## 🚀 **YouTube Stream Setup Process**

### **1. Create Stream on YouTube**
1. Go to [YouTube Studio](https://studio.youtube.com)
2. **Create** → **Go Live** → **Stream**
3. **Stream Title**: "R7D News Live"
4. **Description**: Your news channel description
5. **Visibility**: Public/Unlisted as needed
6. **Category**: News & Politics
7. **Thumbnail**: Upload your channel logo/banner
8. Copy **Stream Key**

### **2. Configure OBS**
1. **Settings** → **Stream**
2. Paste **Stream Key** from YouTube
3. **Apply** → **OK**

### **3. Test Your Setup**
1. Click **"Start Streaming"** in OBS
2. Check YouTube Studio for stream status
3. Verify video and audio quality
4. Test all graphics elements

---

## 📊 **Recommended Streaming Settings**

### **High Quality (Recommended)**
```
Resolution: 1920x1080
Frame Rate: 60 FPS
Bitrate: 8000-9000 Kbps
Encoder: NVENC H.264 (NVIDIA) or Hardware (AMD)
Audio Bitrate: 128-320 kbps
```

### **Standard Quality (Lower bandwidth)**
```
Resolution: 1920x1080
Frame Rate: 30 FPS
Bitrate: 4500-6000 Kbps
Encoder: x264 (Medium/Fast preset)
Audio Bitrate: 128 kbps
```

### **Ultra Quality (High-end systems)**
```
Resolution: 1920x1080
Frame Rate: 60 FPS
Bitrate: 12000-15000 Kbps
Encoder: NVENC H.264 (High Quality)
Audio Bitrate: 320 kbps
```

---

## 🎛️ **Live Control Setup**

### **Scene Configuration**
Create multiple scenes for different layouts:

#### **Scene 1: Full Graphics**
- Browser Source: R7D News Graphics
- Audio: Desktop audio if needed

#### **Scene 2: Picture-in-Picture**
- Browser Source: News Graphics (75% size)
- Video Capture Device: Webcam (25% corner)

#### **Scene 3: Breaking News Only**
- Browser Source with custom CSS to hide elements

### **Hotkeys Setup**
1. **Settings** → **Hotkeys**
2. Configure keys for:
   - Start/Stop Streaming
   - Switch Scenes
   - Mute/Unmute Audio
   - Enable/Disable Sources

---

## 🔴 **Going Live Checklist**

### **Pre-Stream Setup**
- [ ] Internet speed test (minimum 10 Mbps upload)
- [ ] OBS settings configured
- [ ] YouTube stream key entered
- [ ] News graphics tested and working
- [ ] Audio levels checked
- [ ] Stream title and description set
- [ ] Backup internet connection ready

### **During Stream**
- [ ] Monitor chat for viewer feedback
- [ ] Watch stream health in YouTube Studio
- [ ] Monitor OBS stats (CPU usage, dropped frames)
- [ ] Use keyboard shortcuts to control graphics
- [ ] Keep content engaging and professional

### **Technical Monitoring**
- [ ] CPU Usage: <80%
- [ ] Dropped Frames: 0%
- [ ] Network Status: Stable
- [ ] Audio Levels: -6dB to -23dB
- [ ] Video Quality: No artifacts

---

## 🛠️ **Troubleshooting**

### **Common Issues & Solutions**

#### **High CPU Usage**
- Lower OBS preset to "Fast" or "Very Fast"
- Reduce frame rate to 30 FPS
- Use hardware encoding (NVENC/VCE)
- Close unnecessary programs

#### **Dropped Frames**
- Reduce bitrate by 1000-2000 Kbps
- Check internet connection stability
- Use wired connection instead of WiFi
- Change YouTube server in OBS settings

#### **Audio Issues**
- Check Windows audio settings
- Verify OBS audio sources
- Test with headphones/speakers
- Adjust audio levels in OBS mixer

#### **Video Quality Issues**
- Increase bitrate if bandwidth allows
- Check source resolution matches output
- Verify graphics card drivers updated
- Test different encoder settings

---

## 📱 **Mobile Monitoring**

### **YouTube Studio Mobile App**
- Monitor live chat
- Check stream analytics
- View stream health
- Respond to comments
- End stream remotely

### **OBS Remote Apps**
- Control OBS from phone/tablet
- Switch scenes during broadcast
- Adjust audio levels
- Start/stop recording

---

## 🎯 **Professional Tips**

### **Content Strategy**
- Plan your news segments
- Prepare backup content
- Have technical support ready
- Test everything before going live
- Create engaging thumbnails

### **Audience Engagement**
- Respond to live chat
- Ask for viewer feedback
- Create interactive segments
- Use polls and community posts
- Schedule regular broadcast times

### **Technical Best Practices**
- Stream at consistent times
- Maintain stable internet
- Have backup systems ready
- Monitor stream quality constantly
- Record streams for later upload

---

## 🔐 **Privacy & Security**

### **Stream Key Security**
- Never share your stream key publicly
- Reset stream key if compromised
- Use strong YouTube account passwords
- Enable 2-factor authentication

### **Content Guidelines**
- Follow YouTube Community Guidelines
- Avoid copyrighted music/content
- Maintain professional standards
- Have moderation policies ready

---

## 📈 **Analytics & Improvement**

### **YouTube Analytics**
- Monitor viewer retention
- Check peak concurrent viewers
- Analyze traffic sources
- Review audience demographics
- Track subscriber growth

### **Technical Metrics**
- Average bitrate delivered
- Stream stability percentage
- Audio/video quality scores
- Dropped frames percentage
- CPU/GPU usage patterns

---

**Your R7D News Graphics system is now ready for professional YouTube live streaming! 🎬📺**