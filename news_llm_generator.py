#!/usr/bin/env python3
"""
LLM-Powered News Generator for R7D Live Broadcast
Fetches real news from NewsAPI, processes with Groq LLM to generate polished
breaking headlines and ticker items, outputs ticker_data.js for the overlay.
"""

import os
import sys
import json
import time
from datetime import datetime
from typing import List, Dict, Any
import argparse

try:
    from newsapi import NewsApiClient
    from groq import Groq
    from dotenv import load_dotenv
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Install with: pip install newsapi-python groq python-dotenv")
    sys.exit(1)


# Load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

if not GROQ_API_KEY or not NEWS_API_KEY:
    print("ERROR: Missing API keys in .env file")
    print("Required: GROQ_API_KEY, NEWS_API_KEY")
    sys.exit(1)


class NewsLLMGenerator:
    """Fetches news and uses Groq LLM to generate broadcast-ready content."""
    
    def __init__(self):
        self.newsapi = NewsApiClient(api_key=NEWS_API_KEY)
        self.groq = Groq(api_key=GROQ_API_KEY)
        self.model = "llama-3.3-70b-versatile"
    
    def fetch_top_headlines(self, count: int = 20) -> List[Dict[str, Any]]:
        """Fetch top headlines from multiple sources."""
        try:
            # Get top headlines from major sources
            response = self.newsapi.get_top_headlines(
                language='en',
                page_size=count,
                sources='bbc-news,cnn,reuters,the-verge,techcrunch,al-jazeera-english'
            )
            
            articles = response.get('articles', [])
            if not articles:
                # Fallback to general top headlines
                response = self.newsapi.get_top_headlines(
                    language='en',
                    page_size=count
                )
                articles = response.get('articles', [])
            
            return articles
        
        except Exception as e:
            print(f"NewsAPI fetch error: {e}")
            return []
    
    def generate_breaking_headlines(self, articles: List[Dict]) -> List[str]:
        """Use Groq LLM to generate polished breaking news headlines."""
        if not articles:
            return []
        
        # Prepare article summaries for LLM
        article_texts = []
        for idx, article in enumerate(articles[:15], 1):  # Use top 15 articles
            title = article.get('title', '')
            description = article.get('description', '')
            source = article.get('source', {}).get('name', 'Unknown')
            if title:
                article_texts.append(f"{idx}. [{source}] {title}")
                if description:
                    article_texts.append(f"   {description}")
        
        prompt = f"""You are a professional broadcast news editor for a FAMILY-FRIENDLY 24/7 TV news channel (like Good Morning America, TODAY Show).

Given these latest news articles:

{chr(10).join(article_texts)}

Generate 20 SHORT, POSITIVE breaking news HEADLINES suitable for a family-friendly TV news banner.

CRITICAL Content Rules - MUST AVOID:
❌ NO politics (elections, presidents, government, political parties)
❌ NO violence (wars, attacks, conflicts, shootings, killings)
❌ NO disasters (crashes, explosions, fires, evacuations)
❌ NO controversies, scandals, or divisive topics
❌ NO crime, arrests, investigations
❌ NO negative news (layoffs, bankruptcies, deaths)

✅ FOCUS ON POSITIVE NEWS ONLY:
- Technology and innovation
- Business success and growth
- Sports achievements
- Entertainment and culture
- Science breakthroughs
- Space exploration
- Market gains
- Award ceremonies
- Inspiring human stories

Format Requirements:
- Each headline MUST be 4-8 words (35-60 characters)
- Use ACTIVE voice and PRESENT tense
- NO QUESTIONS - only positive STATEMENTS
- Keep SHORT and UPLIFTING for TV display
- Format as numbered list

GOOD Examples (POSITIVE STATEMENTS):
1. APPLE UNVEILS REVOLUTIONARY IPHONE 16
2. STOCK MARKET HITS NEW RECORD HIGH
3. SPACEX LAUNCHES HISTORIC STARSHIP TEST
4. NETFLIX ANNOUNCES 100 NEW SHOWS
5. TESLA BEGINS CYBERTRUCK DELIVERIES
6. GOOGLE AI ACHIEVES MEDICAL BREAKTHROUGH
7. MICROSOFT STOCK REACHES ALL-TIME HIGH
8. AMAZON OPENS 50 NEW DISTRIBUTION CENTERS

Generate 20 POSITIVE headlines NOW (uplifting statements only):"""

        try:
            completion = self.groq.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a professional broadcast news editor. Generate concise, factual breaking news headlines."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model=self.model,
                temperature=0.7,
                max_tokens=800
            )
            
            response_text = completion.choices[0].message.content
            
            # Parse the numbered list
            headlines = []
            negative_keywords = [
                'KILL', 'DEATH', 'DIE', 'ATTACK', 'WAR', 'CONFLICT', 'SHOOT', 'BOMB',
                'MURDER', 'CRASH', 'FIRE', 'EVACUATE', 'ARREST', 'SCANDAL', 'TRUMP',
                'BIDEN', 'ELECTION', 'CONGRESS', 'PARLIAMENT', 'POLITICAL', 'MINISTER',
                'INVESTIGATE', 'GUILTY', 'PRISON', 'JAIL'
            ]
            
            for line in response_text.split('\n'):
                line = line.strip()
                # Remove numbering (1. or 1) or - )
                if line and (line[0].isdigit() or line.startswith('-') or line.startswith('•')):
                    # Strip numbering
                    cleaned = line.lstrip('0123456789.-•) \t').strip()
                    
                    # Skip negative content
                    if any(keyword in cleaned.upper() for keyword in negative_keywords):
                        continue
                    
                    # Filter out questions
                    if cleaned and not cleaned.endswith('?'):
                        # STRICT filter: only keep SHORT positive headlines (25-65 chars)
                        if 25 <= len(cleaned) <= 65:
                            headlines.append(cleaned.upper())
            
            print(f"✓ Generated {len(headlines)} POSITIVE breaking headlines via LLM (family-friendly content)")
            return headlines[:20]  # Cap at 20
        
        except Exception as e:
            print(f"Groq LLM error: {e}")
            # Fallback: use original titles
            fallback = [
                article.get('title', '').upper()
                for article in articles[:10]
                if article.get('title')
            ]
            return fallback
    
    def generate_ticker_items(self, articles: List[Dict]) -> List[Dict[str, str]]:
        """Use Groq LLM to generate continuous ticker items with details."""
        if not articles:
            return []
        
        # Prepare article summaries
        article_texts = []
        for idx, article in enumerate(articles[:20], 1):
            title = article.get('title', '')
            description = article.get('description', '')
            source = article.get('source', {}).get('name', 'Unknown')
            if title:
                article_texts.append(f"{idx}. [{source}] {title}")
                if description:
                    article_texts.append(f"   {description[:150]}")
        
        prompt = f"""You are a professional broadcast news editor for a FAMILY-FRIENDLY 24/7 TV news ticker (like Good Morning America, TODAY Show).

Given these latest news articles:

{chr(10).join(article_texts)}

Generate 25 POSITIVE, DETAILED news ticker items that viewers can FULLY UNDERSTAND in one read.

CRITICAL Content Rules - MUST AVOID:
❌ NO politics (elections, presidents, congress, parliament, political parties)
❌ NO violence (wars, attacks, conflicts, shootings, killings, deaths)
❌ NO disasters (crashes, explosions, fires, evacuations)
❌ NO controversies, scandals, or divisive topics
❌ NO crime, arrests, investigations
❌ NO negative economic news (layoffs, bankruptcies, closures)

✅ FOCUS ON POSITIVE NEWS:
- Technology innovations and launches
- Business success stories and growth
- Sports achievements and records
- Entertainment and cultural events
- Scientific discoveries and breakthroughs
- Space exploration and achievements
- Environmental success stories
- Human interest and inspiring stories
- Market gains and positive trends
- Award ceremonies and celebrations

Format: "HEADLINE | Complete detailed explanation with context, numbers, and location (120-180 characters)"

MAKE DETAILS VERY CLEAR AND COMPLETE - include WHO, WHAT, WHERE, WHEN, WHY/HOW

GOOD Examples (DETAILED & CLEAR):
1. APPLE UNVEILS NEW IPHONE 16 PRO | Tech giant reveals revolutionary smartphone with advanced AI camera system and enhanced battery life at California headquarters event attended by thousands
2. DOW JONES HITS NEW RECORD HIGH | US stock market celebrates strongest quarterly performance in 5 years with gains exceeding 12% as investor confidence reaches peak levels
3. SPACEX STARSHIP COMPLETES TEST FLIGHT | Elon Musk's aerospace company successfully launches and lands massive rocket in Texas marking major milestone for future Mars missions
4. NETFLIX EXPANDS ORIGINAL CONTENT | Streaming giant announces production of 100 new shows and movies across 20 countries featuring diverse stories and award-winning creators
5. TESLA CYBERTRUCK BEGINS DELIVERIES | Electric vehicle manufacturer starts shipping futuristic pickup trucks to customers nationwide with advanced autopilot and 500-mile range capability
6. GOOGLE AI BREAKTHROUGH IN HEALTHCARE | Research team develops artificial intelligence system that detects 15 types of cancer 6 months earlier than traditional screening methods

Generate 25 DETAILED, POSITIVE ticker items NOW (make each detail 120-180 characters with full context):"""

        try:
            completion = self.groq.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a professional broadcast news editor. Generate concise ticker items."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model=self.model,
                temperature=0.8,
                max_tokens=1000
            )
            
            response_text = completion.choices[0].message.content
            
            # Parse the numbered list with headline | detail format
            items = []
            negative_keywords = [
                'KILL', 'DEATH', 'DIE', 'ATTACK', 'WAR', 'CONFLICT', 'SHOOT', 'BOMB', 
                'MURDER', 'CRASH', 'FIRE', 'EVACUATE', 'ARREST', 'SCANDAL', 'TRUMP',
                'BIDEN', 'ELECTION', 'CONGRESS', 'PARLIAMENT', 'POLITICAL', 'MINISTER'
            ]
            
            for line in response_text.split('\n'):
                line = line.strip()
                if line and (line[0].isdigit() or line.startswith('-') or line.startswith('•')):
                    cleaned = line.lstrip('0123456789.-•) \t').strip()
                    
                    # Skip if contains negative keywords
                    if any(keyword in cleaned.upper() for keyword in negative_keywords):
                        continue
                    
                    # Split by | to get headline and detail
                    if '|' in cleaned:
                        parts = cleaned.split('|', 1)
                        headline = parts[0].strip().upper()
                        detail = parts[1].strip() if len(parts) > 1 else ''
                        
                        # Allow longer, more detailed content (120-200 chars for detail)
                        if 20 <= len(headline) <= 80 and 80 <= len(detail) <= 200:
                            items.append({
                                'headline': headline,
                                'detail': detail
                            })
                    else:
                        # Fallback if no | separator
                        if 30 <= len(cleaned) <= 180:
                            items.append({
                                'headline': cleaned.upper(),
                                'detail': ''
                            })
            
            print(f"✓ Generated {len(items)} POSITIVE ticker items via LLM (filtered for family-friendly content)")
            return items[:25]  # Cap at 25
        
        except Exception as e:
            print(f"Groq LLM error for ticker: {e}")
            # Fallback: use original titles
            fallback = [
                article.get('title', '').upper()
                for article in articles[:15]
                if article.get('title')
            ]
            return fallback
    
    def write_ticker_data_js(self, breaking: List[str], ticker: List[Dict[str, str]]):
        """Write ticker_data.js for the HTML overlay."""
        # ticker is now a list of {headline, detail} dicts
        ticker_objects = ticker if isinstance(ticker, list) and ticker else []
        
        # Legacy format for backward compatibility
        ticker_text = ' • '.join([item.get('headline', '') for item in ticker_objects]) + ' • ' if ticker_objects else ''
        
        js_content = f"""// Auto-generated by news_llm_generator.py
// Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

// Ticker text (pre-formatted with separators - DEPRECATED, use TICKER_OBJECTS)
window.TICKER_TEXT = `{ticker_text}`;

// Ticker items as objects with headline and detail
window.TICKER_OBJECTS = {json.dumps(ticker_objects, indent=2)};

// Breaking news headlines (array)
window.TICKER_ITEMS = {json.dumps(breaking, indent=2)};

// Timestamp
window.TICKER_UPDATED_AT = '{datetime.now().isoformat()}';
"""
        
        output_path = os.path.join(os.path.dirname(__file__), 'ticker_data.js')
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(js_content)
        
        print(f"✓ Wrote {output_path}")
    
    def generate_all(self):
        """Main generation flow."""
        print("=" * 60)
        print("LLM-Powered News Generator for R7D Live Broadcast")
        print("=" * 60)
        
        # 1. Fetch news
        print("\n[1/3] Fetching latest news from NewsAPI...")
        articles = self.fetch_top_headlines(count=25)
        if not articles:
            print("⚠ No articles fetched. Using fallback content.")
            breaking = ["LIVE BREAKING NEWS UPDATES COMING SOON"]
            ticker = ["STAY TUNED FOR LATEST DEVELOPMENTS"]
        else:
            print(f"✓ Fetched {len(articles)} articles")
            
            # 2. Generate breaking headlines with LLM
            print("\n[2/3] Generating breaking headlines via Groq LLM...")
            breaking = self.generate_breaking_headlines(articles)
            
            # 3. Generate ticker items with LLM
            print("\n[3/3] Generating ticker items via Groq LLM...")
            ticker = self.generate_ticker_items(articles)
        
        # 4. Write output
        print("\n[Output] Writing ticker_data.js...")
        self.write_ticker_data_js(breaking, ticker)
        
        print("\n" + "=" * 60)
        print("✓ Generation complete!")
        print(f"  - {len(breaking)} breaking headlines")
        print(f"  - {len(ticker)} ticker items")
        print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="LLM-powered news generator for live broadcast overlay"
    )
    parser.add_argument(
        '--interval',
        type=int,
        default=0,
        help='Run continuously every N seconds (0 = run once and exit)'
    )
    args = parser.parse_args()
    
    generator = NewsLLMGenerator()
    
    if args.interval > 0:
        print(f"Running in loop mode (every {args.interval} seconds)")
        print("Press Ctrl+C to stop\n")
        try:
            while True:
                generator.generate_all()
                print(f"\nSleeping for {args.interval} seconds...\n")
                time.sleep(args.interval)
        except KeyboardInterrupt:
            print("\n\nStopped by user.")
    else:
        generator.generate_all()


if __name__ == '__main__':
    main()
