// Ticker Component
class TickerController {
    constructor() {
        this.isVisible = true;
        this.init();
    }

    init() {
        this.renderTicker();
    }

    renderTicker() {
        const ticker = document.getElementById('ticker');
        ticker.className = 'ticker';
        ticker.innerHTML = `
            <div class="ticker-label">LIVE</div>
            <div class="ticker-content" id="tickerContent">
                BREAKING: MAJOR INFRASTRUCTURE BILL PASSES • TECH STOCK RALLY CONTINUES • WEATHER: SEVERE STORMS EXPECTED TONIGHT • SPORTS: WORLD CUP QUALIFIERS BEGIN • HEALTH: NEW VACCINE TRIALS SHOW PROMISING RESULTS • ECONOMY: GDP GROWTH EXCEEDS EXPECTATIONS
            </div>
        `;
    }

    toggleTicker() {
        const ticker = document.getElementById('ticker');
        this.isVisible = !this.isVisible;
        ticker.style.display = this.isVisible ? 'block' : 'none';
    }

    updateTickerText(text) {
        document.getElementById('tickerContent').textContent = text;
    }
}

// Initialize ticker controller
const tickerController = new TickerController();