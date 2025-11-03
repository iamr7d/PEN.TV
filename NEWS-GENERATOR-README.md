# R7D Live News - LLM-Powered News Generator

## Overview
This system uses **NewsAPI** to fetch real-time news and **Groq LLM** (Llama 3.3 70B) to generate professional, broadcast-quality breaking headlines and ticker items for your live news channel.

## Features
- ✅ Fetches real news from BBC, CNN, Reuters, Al Jazeera, TechCrunch, The Verge
- ✅ Uses Groq's ultra-fast LLM to polish headlines for broadcast
- ✅ Generates breaking news headlines (8-12 items)
- ✅ Generates continuous ticker items (15-20 items)
- ✅ Outputs `ticker_data.js` for your HTML overlay
- ✅ Can run continuously to keep content fresh

## Quick Start

### 1. Install Dependencies
```powershell
pip install newsapi-python groq python-dotenv
```

### 2. Run Once
```powershell
python news_llm_generator.py
```

### 3. Run Continuously (recommended for live broadcast)
```powershell
python news_llm_generator.py --interval 180
```
This refreshes headlines every 3 minutes (180 seconds).

### 4. Use the Batch File (Windows)
Double-click `START-NEWS-GENERATOR.bat` to run continuously.

## How It Works

1. **Fetch News**: Connects to NewsAPI and pulls the latest 25 top headlines from major sources
2. **LLM Processing**: Sends articles to Groq LLM with specific prompts for:
   - Breaking news headlines (concise, active voice, present tense)
   - Ticker items (6-12 words, factual, diverse topics)
3. **Output**: Generates `ticker_data.js` with:
   - `window.TICKER_TEXT`: Pre-formatted ticker string
   - `window.TICKER_ITEMS`: Breaking headlines array
   - `window.TICKER_UPDATED_AT`: Timestamp

## Your HTML Overlay Integration

Your `ultimate-news-graphics.html` already includes:
```html
<script src="ticker_data.js"></script>
```

The overlay automatically:
- Displays breaking headlines in the red bar (rotates every 7s)
- Scrolls ticker items at the bottom (continuous marquee)
- Falls back to cached data if offline

## API Keys (in `.env`)

```env
# Groq API for LLM processing
GROQ_API_KEY=your_groq_api_key_here

# NewsAPI for real-time news
NEWS_API_KEY=your_newsapi_key_here
```

## Example Output

### Breaking Headlines (uppercase, 8-15 words)
```
TRUMP CALLS FOR SENATE TO END FILIBUSTER TACTIC
US SETS RECORD LOW REFUGEE ADMISSIONS CAP AT 7,500
IRAN CONDEMNS TRUMP'S NUCLEAR TESTING PLANS
```

### Ticker Items (6-12 words, concise)
```
TRUMP CALLS FOR FILIBUSTER REFORM IN SENATE
IRAN CONDEMNS US NUCLEAR TESTING PROPOSAL
CHINA'S XI DOMINATES PACIFIC SUMMIT TALKS
```

## Recommended Workflow

### For Live Broadcasting:
1. Start the generator in loop mode:
   ```powershell
   python news_llm_generator.py --interval 180
   ```
   Leave this running in a terminal.

2. Open your OBS Browser Source with `ultimate-news-graphics.html`
3. Headlines update automatically every 3 minutes
4. The overlay handles rotation and display

### For Testing:
```powershell
python news_llm_generator.py
```
Generates once and exits.

## Customization

Edit `news_llm_generator.py` to:
- Change news sources (line ~47)
- Adjust LLM prompts for different styles
- Modify update interval
- Change model (`llama-3.3-70b-versatile` is default)

## Troubleshooting

**No headlines generated?**
- Check your API keys in `.env`
- Verify internet connection
- NewsAPI has rate limits (500 requests/day on free tier)

**LLM errors?**
- Check Groq API key validity
- Script falls back to raw titles if LLM fails

**Ticker not updating in overlay?**
- Refresh OBS Browser Source (right-click → Refresh)
- Check `ticker_data.js` was generated successfully
- Clear browser cache if using a regular browser

## Performance

- NewsAPI fetch: ~1-2 seconds
- Groq LLM processing: ~2-4 seconds per generation
- Total cycle: ~5-10 seconds
- Update frequency: Every 180 seconds (3 minutes) recommended

## License & Credits

- NewsAPI: [newsapi.org](https://newsapi.org)
- Groq: [groq.com](https://groq.com)
- Model: Llama 3.3 70B Versatile
