import pytest
from fetch_papers import get_latest_arxiv_papers
from summarize import summarize_paper

def test_fetch_papers():
    papers = get_latest_arxiv_papers(limit=2)
    assert isinstance(papers, list)
    assert len(papers) == 2
    assert "title" in papers[0]
    assert "summary" in papers[0]

def test_summarize_paper_structure():
    paper = {
        "title": "Test Title",
        "summary": "This is a fake abstract used for testing."
    }
    summary = summarize_paper(paper)
    assert isinstance(summary, str)
    assert len(summary) > 20
    assert "plain English" in summary or "What it says" in summary
