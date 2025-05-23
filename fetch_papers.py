import feedparser

def get_latest_arxiv_papers(feed_url="https://export.arxiv.org/rss/cs.AI", limit=3):
    feed = feedparser.parse(feed_url)
    papers = []
    for entry in feed.entries[:limit]:
        papers.append({
            "title": entry.title,
            "summary": entry.summary,
            "link": entry.link
        })
    return papers
