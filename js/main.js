// Main Application Controller
class NewsGraphicsApp {
    constructor() {
        this.init();
    }

    init() {
        this.setupKeyboardShortcuts();
        this.setupGlobalEvents();
        console.log('R7D News Graphics System Initialized');
    }

    setupKeyboardShortcuts() {
        document.addEventListener('keydown', (event) => {
            // Prevent shortcuts when typing in input fields
            if (event.target.tagName === 'TEXTAREA' || event.target.tagName === 'INPUT') {
                return;
            }

            switch(event.key.toLowerCase()) {
                case 'n':
                    newsController.toggleBreaking();
                    break;
                case 'b':
                    newsController.toggleBBCBreaking();
                    break;
                case 't':
                    tickerController.toggleTicker();
                    break;
                case 'v':
                    videoController.toggleVideoBox();
                    break;
                case 'escape':
                    this.hideAllElements();
                    break;
                case ' ':
                    event.preventDefault();
                    this.toggleAllElements();
                    break;
                case 'g':
                    if (event.ctrlKey) {
                        event.preventDefault();
                        this.toggleSafeArea();
                    }
                    break;
                case 'q':
                    if (event.ctrlKey) {
                        event.preventDefault();
                        this.toggleBroadcastMode();
                    }
                    break;
            }
        });
    }

    setupGlobalEvents() {
        // Handle window resize
        window.addEventListener('resize', () => {
            this.handleResize();
        });

        // Handle visibility change (tab switching)
        document.addEventListener('visibilitychange', () => {
            if (document.hidden) {
                this.pauseAnimations();
            } else {
                this.resumeAnimations();
            }
        });
    }

    handleResize() {
        // Adjust elements for different screen sizes
        const videoBox = document.getElementById('video-box');
        if (window.innerWidth < 768) {
            videoBox.style.width = '95%';
        } else if (window.innerWidth < 1200) {
            videoBox.style.width = '90%';
        } else {
            videoBox.style.width = '1200px';
        }
    }

    hideAllElements() {
        newsController.isBreakingVisible = false;
        newsController.isBBCVisible = false;
        tickerController.isVisible = false;
        videoController.isVisible = false;

        document.getElementById('breaking-banner').style.display = 'none';
        document.getElementById('bbc-breaking').style.display = 'none';
        document.getElementById('ticker').style.display = 'none';
        document.getElementById('video-box').style.display = 'none';
    }

    toggleAllElements() {
        const allVisible = newsController.isBreakingVisible && 
                          tickerController.isVisible && 
                          videoController.isVisible;

        if (allVisible) {
            this.hideAllElements();
        } else {
            newsController.isBreakingVisible = true;
            tickerController.isVisible = true;
            videoController.isVisible = true;

            document.getElementById('breaking-banner').style.display = 'block';
            document.getElementById('ticker').style.display = 'block';
            document.getElementById('video-box').style.display = 'block';
        }
    }

    pauseAnimations() {
        document.body.style.animationPlayState = 'paused';
    }

    resumeAnimations() {
        document.body.style.animationPlayState = 'running';
    }

    // Utility methods
    updateTheme(theme) {
        document.body.setAttribute('data-theme', theme);
    }

    exportConfiguration() {
        return {
            breakingText: document.getElementById('breakingText').value,
            bbcText: document.getElementById('bbcBreakingText').value,
            tickerText: document.getElementById('tickerText').value,
            visibility: {
                breaking: newsController.isBreakingVisible,
                bbc: newsController.isBBCVisible,
                ticker: tickerController.isVisible,
                video: videoController.isVisible
            }
        };
    }

    importConfiguration(config) {
        if (config.breakingText) {
            document.getElementById('breakingText').value = config.breakingText;
            newsController.updateBreakingText(config.breakingText);
        }
        
        if (config.bbcText) {
            document.getElementById('bbcBreakingText').value = config.bbcText;
            newsController.updateBBCText(config.bbcText);
        }
        
        if (config.tickerText) {
            document.getElementById('tickerText').value = config.tickerText;
            tickerController.updateTickerText(config.tickerText);
        }
    }

    // Broadcast Quality Methods
    toggleSafeArea() {
        const safeArea = document.getElementById('safeArea');
        safeArea.classList.toggle('show');
        console.log('Broadcast safe area toggled');
    }

    toggleBroadcastMode() {
        document.body.classList.toggle('broadcast-mode');
        const isBroadcastMode = document.body.classList.contains('broadcast-mode');
        
        if (isBroadcastMode) {
            // Apply broadcast optimizations
            this.enableBroadcastOptimizations();
            console.log('Broadcast quality mode enabled');
        } else {
            this.disableBroadcastOptimizations();
            console.log('Broadcast quality mode disabled');
        }
    }

    enableBroadcastOptimizations() {
        // Force high quality rendering
        document.body.style.imageRendering = 'crisp-edges';
        document.body.style.textRendering = 'optimizeLegibility';
        
        // Enable GPU acceleration for all animated elements
        const animatedElements = document.querySelectorAll('.breaking-banner, .video-box, .ticker');
        animatedElements.forEach(el => {
            el.style.transform = 'translateZ(0)';
            el.style.willChange = 'transform, opacity';
        });
    }

    disableBroadcastOptimizations() {
        // Reset optimizations
        document.body.style.imageRendering = '';
        document.body.style.textRendering = '';
        
        const animatedElements = document.querySelectorAll('.breaking-banner, .video-box, .ticker');
        animatedElements.forEach(el => {
            el.style.transform = '';
            el.style.willChange = '';
        });
    }

    // Performance monitoring
    monitorPerformance() {
        if ('performance' in window) {
            const perfData = performance.getEntriesByType('navigation')[0];
            console.log('Page Load Time:', Math.round(perfData.loadEventEnd - perfData.loadEventStart), 'ms');
            
            // Monitor FPS
            let lastTime = performance.now();
            let frameCount = 0;
            
            const checkFPS = (currentTime) => {
                frameCount++;
                if (currentTime >= lastTime + 1000) {
                    const fps = Math.round((frameCount * 1000) / (currentTime - lastTime));
                    console.log('Current FPS:', fps);
                    frameCount = 0;
                    lastTime = currentTime;
                }
                requestAnimationFrame(checkFPS);
            };
            
            requestAnimationFrame(checkFPS);
        }
    }
}

// Initialize the main application
document.addEventListener('DOMContentLoaded', () => {
    window.newsApp = new NewsGraphicsApp();
    
    // Enable performance monitoring in development
    if (window.location.protocol === 'file:' || window.location.hostname === 'localhost') {
        window.newsApp.monitorPerformance();
    }
    
    // Auto-enable broadcast mode for professional use
    setTimeout(() => {
        window.newsApp.toggleBroadcastMode();
    }, 1000);
});

// Make controllers globally available for button onclick events
window.newsController = newsController;
window.tickerController = tickerController;
window.videoController = videoController;