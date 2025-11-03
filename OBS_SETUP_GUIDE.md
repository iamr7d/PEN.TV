# 🎬 Full HD 1080p60 Broadcast Setup Guide

## OBS Studio Configuration for Professional News Overlay

---

## 📺 Browser Source Settings

### Step 1: Add Browser Source
1. In OBS, click **Sources** → **+** → **Browser**
2. Name it: `News Overlay - Full HD`
3. Configure as follows:

```
┌─────────────────────────────────────────────────────┐
│ URL:                                                 │
│   file:///D:/UAL/PROJECTS/PERSONAL/LIVE/           │
│   ultimate-news-graphics.html                       │
│                                                      │
│ Width:                    1920                       │
│ Height:                   1080                       │
│ FPS:                      60                         │
│ CSS:                                                 │
│   width: 1920px;                                     │
│   height: 1080px;                                    │
│                                                      │
│ ☑ Use custom frame rate                            │
│ ☐ Shutdown source when not visible                 │
│ ☐ Refresh browser when scene becomes active        │
│                                                      │
│ Webpage Control Level: Read user config             │
└─────────────────────────────────────────────────────┘
```

---

## 🎥 Video Encoding Settings

### Settings → Output → Streaming

#### Video Encoder Settings:
```yaml
Encoder:                x264 (CPU) or NVENC H.264 (GPU)
Rate Control:           CBR (Constant Bitrate)
Bitrate:                8000 Kbps
Keyframe Interval:      2 (seconds)
Preset:                 High Quality (x264) / Quality (NVENC)
Profile:                High
Tune:                   None (x264 only)
```

#### Recommended Encoder by Hardware:
- **NVIDIA GPU**: NVENC H.264
  - Quality: Max Quality
  - Preset: Quality or High Quality
  - Profile: High
  - Look-ahead: ✓ Enabled
  - Psycho Visual Tuning: ✓ Enabled
  - Max B-frames: 2

- **AMD GPU**: AMD HW H.264
  - Quality Preset: Quality
  - Profile: High
  
- **CPU**: x264
  - CPU Usage Preset: medium or slow (if CPU can handle it)
  - Profile: High
  - Tune: none

---

## 🔊 Audio Encoding Settings (Dolby Atmos-Style)

### Settings → Output → Audio

#### Audio Track 1 (Main):
```yaml
Audio Bitrate:          320 Kbps
Sample Rate:            48 kHz
Channels:               Stereo
Codec:                  AAC
```

### Settings → Audio → Advanced

#### For Dolby Atmos-Style Depth:
```yaml
Monitoring Device:      Default
Sample Rate:            48 kHz

Desktop Audio:
  - Stereo Mix: Enabled
  - Filters → Add:
    * Compressor (Dynamic Range)
      - Ratio: 3:1
      - Threshold: -18 dB
      - Attack: 6 ms
      - Release: 60 ms
    * Limiter
      - Threshold: -1 dB
    * Reverb (for atmospheric depth)
      - Room Size: 0.3-0.5
      - Damping: 0.5
      - Wet: 15-20%
      - Dry: 80-85%
```

#### ReaPlugs VST (Optional - for professional Atmos-style mix):
1. Download ReaPlugs (free): https://www.reaper.fm/reaplugs/
2. Add VST Plugin in OBS:
   - **ReaComp** (Compression)
   - **ReaVerb** (Spatial depth/reverb)
   - **ReaEQ** (Frequency enhancement)

---

## 📊 Video Settings

### Settings → Video

```yaml
Base (Canvas) Resolution:     1920x1080
Output (Scaled) Resolution:   1920x1080
Downscale Filter:             Lanczos (32 samples)
Common FPS Values:            60
```

---

## 🎨 Advanced Settings

### Settings → Advanced

#### Video
```yaml
Renderer:               Direct3D 11 (Windows)
Color Format:           NV12
Color Space:            709 (Rec. 709)
Color Range:            Full (0-255)
```

#### Process Priority:
```yaml
Process Priority:       Above Normal or High
```

---

## 🚀 Performance Optimization

### For Smooth 60fps:

1. **Close unnecessary programs**
2. **GPU encoding recommended** (NVENC/AMD)
3. **Disable browser hardware acceleration** if issues occur
4. **Monitor CPU/GPU usage** in Task Manager

### OBS Stats to Monitor:
- **Rendering lag**: Should be 0-1ms
- **Encoding lag**: Should be 0-1ms  
- **Dropped frames**: Should be 0%
- **CPU usage**: Below 80%
- **GPU usage**: Below 90%

---

## 📡 Streaming Settings

### Twitch/YouTube Recommended:
```yaml
Video Bitrate:          8000 Kbps (1080p60)
Audio Bitrate:          320 Kbps
Keyframe Interval:      2 seconds
Server:                 Closest to your location
```

### Recording Settings:
```yaml
Recording Format:       mp4 (or mkv for safety)
Recording Quality:      Same as stream or Indistinguishable Quality
Encoder:                Same as streaming
```

---

## ✅ Quality Checklist

- [x] Resolution: 1920×1080
- [x] Frame Rate: 60 fps
- [x] Video Bitrate: 8000 Kbps
- [x] Audio Bitrate: 320 Kbps
- [x] Audio Sample Rate: 48 kHz
- [x] Color Space: Rec.709 Full Range
- [x] Browser Source: 60 fps enabled
- [x] Hardware acceleration: Enabled
- [x] Custom CSS size: 1920×1080

---

## 🔧 Troubleshooting

### Ticker not showing:
1. Open browser console (F12 in OBS Interact)
2. Check for errors
3. Verify `ticker_data.js` exists
4. Run `news_llm_generator.py` to generate fresh data

### Performance issues:
1. Lower FPS to 30 if needed
2. Use NVENC/AMD encoder instead of x264
3. Lower bitrate to 6000 Kbps
4. Close background applications

### Audio issues:
1. Check OBS audio mixer levels
2. Verify 48 kHz sample rate
3. Remove unnecessary audio filters
4. Check Windows audio settings

---

## 📝 Notes

- **Dolby Atmos**: True Atmos requires 7.1.4 surround sound hardware. This setup simulates Atmos-style depth using binaural processing and reverb in stereo.
- **Bitrate**: 8000 Kbps is optimal for 1080p60. Adjust based on upload speed.
- **Color Range**: Use "Full" for digital displays, "Limited" if experiencing color banding.

---

**Last Updated**: November 1, 2025
**Version**: 1.0
