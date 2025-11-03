# R7D News Graphics System

A professional news channel graphics system with modular architecture for easy customization and maintenance.

## 🚀 Features

### 📺 **Broadcast Quality**
- **4K/HD Support**: Optimized for 1080p and 4K broadcasting
- **Broadcast Safe Colors**: Professional color standards compliance
- **GPU Acceleration**: Smooth 60fps animations for live broadcasting
- **OBS Studio Ready**: Perfect integration with streaming software
- **Safe Area Guides**: Broadcast-standard safe margins (Ctrl+G)
- **Performance Monitoring**: Real-time FPS and performance tracking

### 🎨 **Graphics System**
- **Modular Architecture**: Separated into reusable components
- **Breaking News Banner**: Animated red gradient background with logo and latest news
- **Video Box**: Customizable video overlay with click-to-unmute functionality
- **News Ticker**: Scrolling news ticker at the bottom
- **Control Panel**: Real-time control of all graphics elements
- **Keyboard Shortcuts**: Quick access to all functions
- **Responsive Design**: Works on different screen sizes
- **Background Video**: Support for background video with dimming overlay

## 📁 Project Structure

```
├── index.html                 # Main HTML file
├── css/
│   ├── base.css              # Base styles and utilities
│   ├── animations.css        # All keyframe animations
│   ├── breaking-news.css     # Breaking news banner styles
│   ├── video-box.css         # Video box component styles
│   ├── ticker.css            # News ticker styles
│   ├── control-panel.css     # Control panel styles
│   └── responsive.css        # Responsive design rules
├── js/
│   ├── components/
│   │   ├── control-panel.js  # Control panel component
│   │   ├── breaking-news.js  # Breaking news controller
│   │   ├── ticker.js         # Ticker controller
│   │   └── video-box.js      # Video box controller
│   └── main.js               # Main application controller
└── assets/
    ├── R7D.svg              # Channel logo
    ├── bg video.mp4         # Background video
    └── ad01.mp4             # Video box content
```

## 🎮 Controls

### Keyboard Shortcuts
- **N** - Toggle Breaking News Banner
- **B** - Toggle BBC Breaking News
- **T** - Toggle News Ticker
- **V** - Toggle Video Box
- **Ctrl+Q** - Toggle Broadcast Quality Mode
- **Ctrl+G** - Toggle Safe Area Guides
- **ESC** - Hide All Elements
- **SPACE** - Toggle All Elements

### Control Panel
Use the left control panel to:
- Edit breaking news text
- Edit BBC breaking news text
- Edit ticker content
- Toggle individual components

## 🔧 Customization

### Adding New Components
1. Create CSS file in `css/` directory
2. Create JavaScript component in `js/components/`
3. Add references in `index.html`
4. Update `main.js` for integration

### Modifying Styles
- **Colors**: Edit color variables in `base.css`
- **Animations**: Modify keyframes in `animations.css`
- **Layout**: Adjust positioning in component-specific CSS files

### Video Sources
Update video sources in:
- `index.html` for background video
- `js/components/video-box.js` for overlay video

## 🚀 Usage

1. Open `index.html` in a modern web browser
2. Use the control panel to customize content
3. Use keyboard shortcuts for quick control
4. Perfect for OBS Studio or similar streaming software

## 📱 Responsive Breakpoints

- **Desktop**: 1200px and above
- **Tablet**: 768px - 1199px  
- **Mobile**: Below 768px

## 🎨 Customization Options

### Logo
- Replace `R7D.svg` with your channel logo
- Adjust logo size in `breaking-news.css`

### Colors
- Primary red: `#dc143c`
- Background: `#000000`
- Text: `#ffffff`

### Animations
- Speed: Modify animation duration in `animations.css`
- Effects: Add new keyframes for custom animations

## 🔄 Updates & Maintenance

The modular structure makes it easy to:
- Update individual components without affecting others
- Add new graphics elements
- Modify styling without breaking functionality
- Debug issues in specific components

## 📞 Support

For customization or support, modify the components according to your needs. The modular architecture ensures easy maintenance and updates.

---

**R7D News Graphics System** - Professional news channel graphics made easy.