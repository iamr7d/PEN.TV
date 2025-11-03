# Broadcasting Quality Standards

## Video Quality Settings for OBS Studio

### 🎥 **Recommended OBS Settings**

#### **Output Settings**
- **Resolution**: 1920x1080 (Full HD) or 3840x2160 (4K)
- **Frame Rate**: 60 FPS for smooth motion
- **Bitrate**: 
  - 1080p: 6,000-8,000 Kbps
  - 4K: 25,000-40,000 Kbps
- **Encoder**: Hardware (NVENC/AMD VCE) for performance
- **Format**: MP4 or FLV

#### **Video Settings**
```
Base Resolution: 1920x1080
Output Resolution: 1920x1080
Downscale Filter: Lanczos (Sharpened scaling, 36 samples)
FPS Type: Common FPS Values
Common FPS Values: 60
```

#### **Audio Settings**
```
Sample Rate: 48 kHz
Channels: Stereo
Bitrate: 320 Kbps
```

### 🎨 **Color Standards**

#### **Broadcast Safe Colors**
- **Red**: #E31E24 (instead of pure red)
- **White**: #F0F0F0 (instead of pure white)
- **Black**: #0A0A0A (instead of pure black)
- **Text**: #EBEBEB for optimal readability

#### **Color Calibration**
- Use Rec. 709 color space for HD broadcasting
- Ensure colors are within broadcast safe ranges
- Avoid pure white (#FFFFFF) and pure black (#000000)

### 📺 **Broadcasting Standards**

#### **Safe Areas**
- **Title Safe**: Keep text within 90% of screen area
- **Action Safe**: Keep important graphics within 95% of screen area
- Use `Ctrl + G` to toggle safe area guides

#### **Typography Standards**
- **Minimum Font Size**: 24px for 1080p, 48px for 4K
- **Font Weight**: Minimum 600 for broadcast visibility
- **Text Shadow**: Always add for readability over video
- **Line Height**: 1.4 minimum for broadcast text

### 🔧 **Technical Specifications**

#### **Frame Rates**
- **60 FPS**: Smooth motion for news graphics
- **30 FPS**: Acceptable for static graphics
- **24 FPS**: Not recommended for news

#### **Aspect Ratios**
- **16:9**: Standard HD/4K broadcasting
- **Safe Margins**: 5% on all sides for broadcast safety

#### **Audio Levels**
- **Peak**: -6dB maximum
- **RMS**: -23dB for broadcast standards
- **Background Music**: -30dB to -40dB under voice

### 🎯 **OBS Studio Setup**

#### **Scene Configuration**
1. **Browser Source**: Point to `index.html`
2. **Resolution**: Match your broadcast resolution
3. **FPS**: 60 for smooth animations
4. **Hardware Acceleration**: Enable if available

#### **Browser Source Settings**
```
URL: file:///D:/UAL/PROJECTS/PERSONAL/LIVE/index.html
Width: 1920
Height: 1080
FPS: 60
Custom CSS: (optional optimizations)
```

#### **Chroma Key Setup** (if needed)
- Add chroma key filter to browser source
- Use pure green (#00FF00) background
- Adjust similarity and smoothness as needed

### 🚀 **Performance Optimization**

#### **System Requirements**
- **CPU**: Intel i7/AMD Ryzen 7 or better
- **GPU**: GTX 1660/RX 580 or better for hardware encoding
- **RAM**: 16GB minimum, 32GB recommended
- **Storage**: SSD for better performance

#### **Browser Optimization**
- Use Chrome/Edge for best WebGL performance
- Enable hardware acceleration in browser settings
- Close unnecessary tabs and applications

### 📊 **Quality Monitoring**

#### **Metrics to Watch**
- **CPU Usage**: Keep under 80%
- **GPU Usage**: Monitor encoding load
- **Dropped Frames**: Should be 0%
- **Network**: Stable upload speed
- **Audio Levels**: Consistent without clipping

#### **Testing Checklist**
- [ ] All text readable at target resolution
- [ ] Colors within broadcast safe ranges
- [ ] Smooth animations without stuttering
- [ ] Audio levels within broadcast standards
- [ ] No visual artifacts or compression issues

### 🎬 **Professional Broadcasting Tips**

#### **Content Guidelines**
- Keep important information in safe areas
- Use high contrast for text readability
- Ensure animations are smooth and purposeful
- Test on different display sizes

#### **Technical Best Practices**
- Regular system maintenance
- Monitor encoding performance
- Use wired internet connection
- Have backup systems ready
- Test before going live

### 🔍 **Quality Control**

#### **Pre-Broadcast Checklist**
- [ ] Video quality set to broadcast standards
- [ ] Audio levels properly balanced
- [ ] All graphics displaying correctly
- [ ] Network connection stable
- [ ] Backup systems operational
- [ ] Content reviewed and approved

---

**Note**: These settings ensure broadcast-quality output suitable for professional television and streaming platforms.