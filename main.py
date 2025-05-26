import feedparser

# Indian news channel RSS feeds
rss_feeds = [
    'https://feeds.feedburner.com/ndtvnews-top-stories',         # NDTV
    'https://www.thehindu.com/news/feeder/default.rss',          # The Hindu
    'https://www.indiatoday.in/rss/1206584',                     # India Today
    'https://timesofindia.indiatimes.com/rssfeedstopstories.cms', # TOI
    'https://www.hindustantimes.com/feeds/rss/top-news/rssfeed.xml' # HT
]

for rss_url in rss_feeds:
    print(f"\nFetching RSS feed from: {rss_url}")
    feed = feedparser.parse(rss_url)
    if feed.bozo:
        print("Failed to parse RSS feed. Please check the URL or feed format.")
    else:
        # Print first 2 items (to keep output manageable)
        for entry in feed.entries[:2]:
            print("Title:", entry.title)
            print("Description:", entry.get('description', 'No description'))
            print("Link:", entry.link)
            print("---")
