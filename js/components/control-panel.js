// Control Panel Component
class ControlPanel {
    constructor() {
        this.init();
    }

    init() {
        this.render();
        this.attachEventListeners();
    }

    render() {
        const controlPanel = document.getElementById('control-panel');
        controlPanel.className = 'master-control';
        controlPanel.innerHTML = `
            <h3 class="master-title">R7D News Graphics</h3>
            
            <!-- Breaking News Theme -->
            <div class="theme-section">
                <div class="theme-title">Breaking News Theme</div>
                
                <div class="control-group">
                    <label class="control-label">Breaking News Text</label>
                    <textarea id="breakingText" class="control-textarea" rows="2" placeholder="Enter breaking news...">മുഖ്യമന്ത്രി നിരഞ്ഞ് ആമയിൽ പ്രഖ്യാപനം നടത്തുന്നു • സർക്കാർ പദ്ധതികൾ • സാമ്പത്തിക പരിഷ്കാരങ്ങൾ</textarea>
                </div>
                
                <button class="control-button" onclick="newsController.toggleBreaking()">Toggle Breaking Banner</button>
            </div>

            <!-- BBC Theme -->
            <div class="theme-section">
                <div class="theme-title">BBC Style</div>
                
                <div class="control-group">
                    <label class="control-label">BBC Breaking News</label>
                    <textarea id="bbcBreakingText" class="control-textarea" rows="2" placeholder="BBC breaking news...">PRIME MINISTER ANNOUNCES MAJOR ECONOMIC REFORMS • SCIENTISTS ACHIEVE FUSION ENERGY BREAKTHROUGH • GLOBAL CLIMATE SUMMIT REACHES HISTORIC AGREEMENT</textarea>
                </div>
                
                <button class="control-button" onclick="newsController.toggleBBCBreaking()">Toggle BBC Breaking</button>
            </div>

            <!-- Ticker Control -->
            <div class="theme-section">
                <div class="theme-title">News Ticker</div>
                
                <div class="control-group">
                    <label class="control-label">Ticker Text</label>
                    <textarea id="tickerText" class="control-textarea" rows="2" placeholder="Ticker content...">BREAKING: MAJOR INFRASTRUCTURE BILL PASSES • TECH STOCK RALLY CONTINUES • WEATHER: SEVERE STORMS EXPECTED TONIGHT • SPORTS: WORLD CUP QUALIFIERS BEGIN</textarea>
                </div>
                
                <button class="control-button" onclick="tickerController.toggleTicker()">Toggle Ticker</button>
            </div>

            <!-- Video Controls -->
            <div class="theme-section">
                <div class="theme-title">Video Box</div>
                <button class="control-button" onclick="videoController.toggleVideoBox()" style="background: linear-gradient(135deg, #333333 0%, #555555 100%);">Toggle Video Box</button>
            </div>

            <!-- Broadcast Quality Controls -->
            <div class="theme-section">
                <div class="theme-title">Broadcast Quality</div>
                <button class="control-button" onclick="newsApp.toggleBroadcastMode()" style="background: linear-gradient(135deg, #28a745 0%, #20c997 100%);">Toggle Broadcast Mode</button>
                <button class="control-button" onclick="newsApp.toggleSafeArea()" style="background: linear-gradient(135deg, #17a2b8 0%, #6f42c1 100%);">Toggle Safe Area</button>
            </div>

            <!-- Keyboard Shortcuts -->
            <div class="shortcuts-info">
                <div class="shortcuts-title">Keyboard Shortcuts</div>
                <div class="shortcut-item">
                    <span>Toggle Breaking News</span>
                    <span class="shortcut-key">N</span>
                </div>
                <div class="shortcut-item">
                    <span>Toggle BBC Breaking</span>
                    <span class="shortcut-key">B</span>
                </div>
                <div class="shortcut-item">
                    <span>Toggle Ticker</span>
                    <span class="shortcut-key">T</span>
                </div>
                <div class="shortcut-item">
                    <span>Toggle Video Box</span>
                    <span class="shortcut-key">V</span>
                </div>
                <div class="shortcut-item">
                    <span>Broadcast Mode</span>
                    <span class="shortcut-key">Ctrl+Q</span>
                </div>
                <div class="shortcut-item">
                    <span>Safe Area Guide</span>
                    <span class="shortcut-key">Ctrl+G</span>
                </div>
            </div>
        `;
    }

    attachEventListeners() {
        // Update text content when textarea values change
        document.getElementById('breakingText').addEventListener('input', (e) => {
            newsController.updateBreakingText(e.target.value);
        });

        document.getElementById('bbcBreakingText').addEventListener('input', (e) => {
            newsController.updateBBCText(e.target.value);
        });

        document.getElementById('tickerText').addEventListener('input', (e) => {
            tickerController.updateTickerText(e.target.value);
        });
    }
}

// Initialize control panel
const controlPanel = new ControlPanel();