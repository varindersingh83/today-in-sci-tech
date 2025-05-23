"""
Tests for the paper fetcher module.
"""

import pytest
from today_in_sci_tech.fetcher import get_latest_arxiv_papers

def test_fetch_papers():
    """Test that papers are fetched correctly."""
    papers = get_latest_arxiv_papers(limit=1)
    assert len(papers) == 1
    paper = papers[0]
    assert "title" in paper
    assert "summary" in paper
    assert "link" in paper
    assert paper["link"].startswith("https://arxiv.org/") 