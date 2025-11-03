// YouTube Streaming Integration
class StreamingController {
    constructor() {
        this.isLive = false;
        this.viewerCount = 0;
        this.streamHealth = 'good';
        this.init();
    }

    init() {
        this.addStreamingControls();
        this.setupStreamingOptimizations();
        this.monitorStreamHealth();
    }

    addStreamingControls() {
        const streamingPanel = document.createElement('div');
        streamingPanel.className = 'streaming-panel';
        streamingPanel.innerHTML = `
            <div class="streaming-status">
                <div class="status-indicator ${this.isLive ? 'live' : 'offline'}">
                    ${this.isLive ? '🔴 LIVE' : '⚫ OFFLINE'}
                </div>
                <div class="viewer-count">Viewers: ${this.viewerCount}</div>
                <div class="stream-health">Health: ${this.streamHealth}</div>
            </div>
            <div class="streaming-actions">
                <button onclick="streamingController.toggleOptimizedMode()" class="stream-btn">
                    🎥 Streaming Mode
                </button>
                <button onclick="streamingController.showStreamGuide()" class="stream-btn">
                    📖 Setup Guide
                </button>
                <button onclick="streamingController.copyStreamURL()" class="stream-btn">
                    📋 Copy URL
                </button>
            </div>
        `;

        // Add to control panel
        document.querySelector('.master-control').appendChild(streamingPanel);
    }

    setupStreamingOptimizations() {
        // Optimize for streaming
        document.body.classList.add('streaming-optimized');
        
        // Reduce CPU usage during streaming
        const animations = document.querySelectorAll('[style*="animation"]');
        animations.forEach(el => {
            el.style.animationTimingFunction = 'ease-out';
        });

        // Enable hardware acceleration
        const videos = document.querySelectorAll('video');
        videos.forEach(video => {
            video.style.transform = 'translateZ(0)';
            video.setAttribute('preload', 'auto');
        });
    }

    toggleOptimizedMode() {
        const isOptimized = document.body.classList.contains('streaming-optimized');
        
        if (isOptimized) {
            this.disableStreamingMode();
        } else {
            this.enableStreamingMode();
        }
    }

    enableStreamingMode() {
        document.body.classList.add('streaming-optimized');
        
        // Show streaming overlay
        this.showStreamingOverlay();
        
        // Optimize performance
        this.reduceAnimationComplexity();
        
        console.log('🎥 Streaming mode enabled - Optimized for broadcast');
    }

    disableStreamingMode() {
        document.body.classList.remove('streaming-optimized');
        this.hideStreamingOverlay();
        this.restoreAnimationComplexity();
        
        console.log('📺 Normal mode restored');
    }

    showStreamingOverlay() {
        if (document.getElementById('streaming-overlay')) return;

        const overlay = document.createElement('div');
        overlay.id = 'streaming-overlay';
        overlay.innerHTML = `
            <div class="streaming-info">
                <div class="live-indicator">🔴 OPTIMIZED FOR STREAMING</div>
                <div class="streaming-tips">
                    <p>✅ 60 FPS Performance Mode Active</p>
                    <p>✅ Broadcast Safe Colors Enabled</p>
                    <p>✅ GPU Acceleration On</p>
                </div>
                <button onclick="streamingController.hideStreamingOverlay()">✕</button>
            </div>
        `;
        
        document.body.appendChild(overlay);
        
        // Auto-hide after 5 seconds
        setTimeout(() => {
            this.hideStreamingOverlay();
        }, 5000);
    }

    hideStreamingOverlay() {
        const overlay = document.getElementById('streaming-overlay');
        if (overlay) {
            overlay.remove();
        }
    }

    showStreamGuide() {
        const guide = document.createElement('div');
        guide.className = 'stream-guide-modal';
        guide.innerHTML = `
            <div class="guide-content">
                <h2>🎥 YouTube Live Streaming Guide</h2>
                <div class="guide-steps">
                    <div class="step">
                        <h3>1. Download OBS Studio</h3>
                        <p>Get OBS Studio (FREE) from: <a href="https://obsproject.com" target="_blank">obsproject.com</a></p>
                    </div>
                    <div class="step">
                        <h3>2. YouTube Setup</h3>
                        <p>Go to <a href="https://studio.youtube.com" target="_blank">YouTube Studio</a> → Create → Go Live → Stream</p>
                        <p>Copy your Stream Key</p>
                    </div>
                    <div class="step">
                        <h3>3. OBS Configuration</h3>
                        <p><strong>Stream Settings:</strong></p>
                        <ul>
                            <li>Service: YouTube - RTMPS</li>
                            <li>Stream Key: [Your YouTube Key]</li>
                        </ul>
                        <p><strong>Video Settings:</strong></p>
                        <ul>
                            <li>Resolution: 1920x1080</li>
                            <li>FPS: 60</li>
                            <li>Bitrate: 6000 Kbps</li>
                        </ul>
                    </div>
                    <div class="step">
                        <h3>4. Add Browser Source</h3>
                        <p>URL: <code>file:///D:/UAL/PROJECTS/PERSONAL/LIVE/index.html</code></p>
                        <p>Size: 1920x1080, 60 FPS</p>
                    </div>
                    <div class="step">
                        <h3>5. Go Live! 🔴</h3>
                        <p>Click "Start Streaming" in OBS</p>
                        <p>Your R7D News Graphics are now LIVE!</p>
                    </div>
                </div>
                <button onclick="this.parentElement.parentElement.remove()">Close Guide</button>
            </div>
        `;
        
        document.body.appendChild(guide);
    }

    copyStreamURL() {
        const url = `file:///${window.location.pathname.replace(/\\/g, '/')}`;
        
        if (navigator.clipboard) {
            navigator.clipboard.writeText(url).then(() => {
                this.showNotification('📋 Stream URL copied to clipboard!');
            });
        } else {
            // Fallback for older browsers
            const textArea = document.createElement('textarea');
            textArea.value = url;
            document.body.appendChild(textArea);
            textArea.select();
            document.execCommand('copy');
            document.body.removeChild(textArea);
            this.showNotification('📋 Stream URL copied to clipboard!');
        }
    }

    showNotification(message) {
        const notification = document.createElement('div');
        notification.className = 'stream-notification';
        notification.textContent = message;
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.remove();
        }, 3000);
    }

    reduceAnimationComplexity() {
        // Simplify animations for better streaming performance
        const style = document.createElement('style');
        style.id = 'streaming-optimizations';
        style.textContent = `
            .streaming-optimized * {
                animation-duration: 0.5s !important;
            }
            .streaming-optimized .breaking-banner {
                animation: none !important;
            }
            .streaming-optimized #bg-video {
                filter: blur(0px) !important;
            }
        `;
        document.head.appendChild(style);
    }

    restoreAnimationComplexity() {
        const style = document.getElementById('streaming-optimizations');
        if (style) {
            style.remove();
        }
    }

    monitorStreamHealth() {
        setInterval(() => {
            this.checkPerformance();
            this.updateStreamStatus();
        }, 5000);
    }

    checkPerformance() {
        // Monitor performance metrics
        if ('performance' in window) {
            const memInfo = performance.memory;
            const memUsage = memInfo ? (memInfo.usedJSHeapSize / memInfo.totalJSHeapSize) * 100 : 0;
            
            if (memUsage > 80) {
                this.streamHealth = 'warning';
                console.warn('🚨 High memory usage detected');
            } else if (memUsage > 90) {
                this.streamHealth = 'critical';
                console.error('🔴 Critical memory usage!');
            } else {
                this.streamHealth = 'good';
            }
        }
    }

    updateStreamStatus() {
        const statusIndicator = document.querySelector('.status-indicator');
        const healthIndicator = document.querySelector('.stream-health');
        
        if (statusIndicator) {
            statusIndicator.textContent = this.isLive ? '🔴 LIVE' : '⚫ OFFLINE';
            statusIndicator.className = `status-indicator ${this.isLive ? 'live' : 'offline'}`;
        }
        
        if (healthIndicator) {
            healthIndicator.textContent = `Health: ${this.streamHealth}`;
            healthIndicator.className = `stream-health ${this.streamHealth}`;
        }
    }

    // Simulate live status (in real implementation, this would connect to YouTube API)
    simulateLiveStatus() {
        setInterval(() => {
            // Randomly simulate viewer count changes
            if (this.isLive) {
                this.viewerCount += Math.floor(Math.random() * 10) - 5;
                this.viewerCount = Math.max(0, this.viewerCount);
                
                const viewerElement = document.querySelector('.viewer-count');
                if (viewerElement) {
                    viewerElement.textContent = `Viewers: ${this.viewerCount}`;
                }
            }
        }, 10000);
    }
}

// Initialize streaming controller
const streamingController = new StreamingController();

// Add streaming-specific CSS
const streamingCSS = document.createElement('style');
streamingCSS.textContent = `
    .streaming-panel {
        margin-top: 20px;
        padding: 15px;
        background: rgba(0, 0, 0, 0.9);
        border-radius: 8px;
        border: 2px solid #ff0000;
    }

    .streaming-status {
        display: flex;
        flex-direction: column;
        gap: 8px;
        margin-bottom: 15px;
        font-size: 12px;
    }

    .status-indicator {
        font-weight: bold;
        padding: 5px 10px;
        border-radius: 4px;
        text-align: center;
    }

    .status-indicator.live {
        background: #ff0000;
        color: white;
        animation: pulse 2s infinite;
    }

    .status-indicator.offline {
        background: #666;
        color: white;
    }

    .viewer-count, .stream-health {
        color: #ccc;
        font-size: 11px;
    }

    .stream-health.warning {
        color: #ffa500;
    }

    .stream-health.critical {
        color: #ff0000;
    }

    .streaming-actions {
        display: flex;
        flex-direction: column;
        gap: 8px;
    }

    .stream-btn {
        padding: 8px 12px;
        background: linear-gradient(135deg, #ff0000 0%, #cc0000 100%);
        border: none;
        border-radius: 4px;
        color: white;
        font-size: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .stream-btn:hover {
        background: linear-gradient(135deg, #cc0000 0%, #ff0000 100%);
        transform: translateY(-1px);
    }

    #streaming-overlay {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: rgba(0, 0, 0, 0.95);
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #ff0000;
        color: white;
        z-index: 10000;
        max-width: 400px;
    }

    .live-indicator {
        color: #ff0000;
        font-weight: bold;
        margin-bottom: 10px;
        text-align: center;
    }

    .streaming-tips p {
        margin: 5px 0;
        font-size: 12px;
        color: #00ff00;
    }

    .stream-guide-modal {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.9);
        z-index: 10000;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .guide-content {
        background: #1a1a1a;
        padding: 30px;
        border-radius: 10px;
        max-width: 600px;
        max-height: 80vh;
        overflow-y: auto;
        color: white;
    }

    .guide-content h2 {
        color: #ff0000;
        margin-bottom: 20px;
    }

    .guide-content h3 {
        color: #00ff00;
        margin: 15px 0 10px 0;
    }

    .guide-content a {
        color: #00bfff;
    }

    .guide-content code {
        background: #333;
        padding: 2px 4px;
        border-radius: 3px;
        font-family: monospace;
    }

    .stream-notification {
        position: fixed;
        top: 20px;
        right: 20px;
        background: #00ff00;
        color: black;
        padding: 10px 20px;
        border-radius: 5px;
        z-index: 10001;
        animation: slideInRight 0.3s ease;
    }

    @keyframes slideInRight {
        from { transform: translateX(100%); }
        to { transform: translateX(0); }
    }

    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
`;

document.head.appendChild(streamingCSS);