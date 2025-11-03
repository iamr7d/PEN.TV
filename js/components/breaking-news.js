// Breaking News Component
class BreakingNewsController {
    constructor() {
        this.isBreakingVisible = true;
        this.isBBCVisible = false;
        this.init();
    }

    init() {
        this.renderBreakingNews();
        this.renderBBCBreaking();
    }

    renderBreakingNews() {
        const breakingBanner = document.getElementById('breaking-banner');
        breakingBanner.className = 'breaking-banner';
        breakingBanner.innerHTML = `
            <div class="logo-section">
                <img src="D:\\UAL\\PROJECTS\\PERSONAL\\LIVE\\R7D.svg" alt="R7D Logo">
            </div>
            <div class="latest-section">
                <div class="latest-text">LATEST</div>
            </div>
            <div class="news-section">
                <div class="news-title" id="newsTitle">മുഖ്യമന്ത്രി നിരഞ്ഞ് ആമയിൽ പ്രഖ്യാപനം നടത്തുന്നു</div>
                <div class="news-content" id="breakingContent">സർക്കാർ പദ്ധതികൾ • സാമ്പത്തിക പരിഷ്കാരങ്ങൾ • വികസന പദ്ധതികൾ</div>
            </div>
        `;
    }

    renderBBCBreaking() {
        const bbcBreaking = document.getElementById('bbc-breaking');
        bbcBreaking.innerHTML = `
            <div class="bbc-breaking-label">BREAKING NEWS</div>
            <div class="bbc-breaking-text" id="bbcBreakingContent">PRIME MINISTER ANNOUNCES MAJOR ECONOMIC REFORMS • SCIENTISTS ACHIEVE FUSION ENERGY BREAKTHROUGH</div>
        `;
        bbcBreaking.className = 'bbc-breaking';
        bbcBreaking.style.display = 'none';
    }

    toggleBreaking() {
        const breakingBanner = document.getElementById('breaking-banner');
        this.isBreakingVisible = !this.isBreakingVisible;
        breakingBanner.style.display = this.isBreakingVisible ? 'block' : 'none';
    }

    toggleBBCBreaking() {
        const bbcBreaking = document.getElementById('bbc-breaking');
        this.isBBCVisible = !this.isBBCVisible;
        
        if (this.isBBCVisible) {
            bbcBreaking.style.display = 'block';
            bbcBreaking.classList.add('active');
        } else {
            bbcBreaking.classList.remove('active');
            setTimeout(() => {
                bbcBreaking.style.display = 'none';
            }, 500);
        }
    }

    updateBreakingText(text) {
        const parts = text.split('•');
        if (parts.length >= 2) {
            document.getElementById('newsTitle').textContent = parts[0].trim();
            document.getElementById('breakingContent').textContent = parts.slice(1).join('•').trim();
        } else {
            document.getElementById('breakingContent').textContent = text;
        }
    }

    updateBBCText(text) {
        document.getElementById('bbcBreakingContent').textContent = text;
    }
}

// Initialize breaking news controller
const newsController = new BreakingNewsController();