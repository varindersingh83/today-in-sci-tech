"""
Tests for the paper summarizer module.
"""

import pytest
from unittest.mock import patch, MagicMock
from today_in_sci_tech.summarizer import summarize_paper

@pytest.fixture
def mock_paper():
    return {
        "title": "Test Paper Title",
        "summary": "This is a test paper summary.",
        "link": "https://arxiv.org/abs/test"
    }

@pytest.fixture
def mock_openai_response():
    mock_choice = MagicMock()
    mock_choice.message.content = """
1. This is a test summary in plain English.
2. This is why it's interesting.
3. 🚀 Test tweet with emojis!
"""
    return MagicMock(choices=[mock_choice])

def test_summarize_paper(mock_paper, mock_openai_response):
    """Test that paper summarization works correctly."""
    with patch('today_in_sci_tech.summarizer.client.chat.completions.create', return_value=mock_openai_response):
        summary = summarize_paper(mock_paper)
        
        assert "test summary in plain English" in summary
        assert "interesting" in summary
        assert "🚀" in summary

def test_summarize_paper_api_error(mock_paper):
    """Test handling of API errors."""
    with patch('today_in_sci_tech.summarizer.client.chat.completions.create', side_effect=Exception("API Error")):
        with pytest.raises(Exception) as exc_info:
            summarize_paper(mock_paper)
        assert "API Error" in str(exc_info.value) 