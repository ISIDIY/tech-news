import feedparser

with open("feeds.txt") as f:
    urls = [
        line.strip()
        for line in f
        if line.strip() and not line.startswith("#")
    ]

for url in urls:
    print("=" * 50)

    feed = feedparser.parse(url)

    print(feed.feed.get("title", "Unknown"))

    for entry in feed.entries[:5]:
        print("-", entry.title)
        print(" ", entry.link)
