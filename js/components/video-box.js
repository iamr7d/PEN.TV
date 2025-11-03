// Video Box Component
class VideoController {
    constructor() {
        this.isVisible = true;
        this.init();
    }

    init() {
        this.renderVideoBox();
        this.initVideo();
    }

    renderVideoBox() {
        const videoBox = document.getElementById('video-box');
        videoBox.className = 'video-box';
        videoBox.innerHTML = `
            <div class="video-container">
                <video id="box-video" autoplay muted loop>
                    <source src="D:\\UAL\\PROJECTS\\PERSONAL\\LIVE\\ad01.mp4" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
        `;
    }

    initVideo() {
        const boxVideo = document.getElementById('box-video');
        
        if (boxVideo) {
            boxVideo.volume = 1.0; // Full volume when unmuted
            
            // Click to unmute functionality
            boxVideo.addEventListener('click', () => {
                if (boxVideo.muted) {
                    boxVideo.muted = false;
                    console.log('Video unmuted - audio enabled');
                } else {
                    boxVideo.muted = true;
                    console.log('Video muted - audio disabled');
                }
            });
            
            // Handle autoplay when box is shown
            boxVideo.addEventListener('loadeddata', () => {
                if (this.isVisible) {
                    boxVideo.play().catch(error => {
                        console.log('Autoplay blocked, user interaction required');
                    });
                }
            });
            
            // Ensure video loops properly
            boxVideo.addEventListener('ended', () => {
                boxVideo.currentTime = 0;
                boxVideo.play();
            });
        }
    }

    toggleVideoBox() {
        const videoBox = document.getElementById('video-box');
        this.isVisible = !this.isVisible;
        videoBox.style.display = this.isVisible ? 'block' : 'none';
        
        // Play/pause video based on visibility
        const boxVideo = document.getElementById('box-video');
        if (boxVideo) {
            if (this.isVisible) {
                boxVideo.play();
            } else {
                boxVideo.pause();
            }
        }
    }
}

// Initialize video controller
const videoController = new VideoController();