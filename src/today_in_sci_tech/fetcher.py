"""
Module for fetching research papers from arXiv.
"""

import feedparser
from typing import List, Dict

def get_latest_arxiv_papers(feed_url: str = "https://export.arxiv.org/rss/cs.AI", limit: int = 3) -> List[Dict[str, str]]:
    """
    Fetch the latest papers from arXiv RSS feed.
    
    Args:
        feed_url: The arXiv RSS feed URL
        limit: Maximum number of papers to fetch
        
    Returns:
        List of dictionaries containing paper information
    """
    feed = feedparser.parse(feed_url)
    papers = []
    for entry in feed.entries[:limit]:
        papers.append({
            "title": entry.title,
            "summary": entry.summary,
            "link": entry.link
        })
    return papers 