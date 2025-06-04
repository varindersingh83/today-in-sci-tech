"""
Tests for the thread generator module.
"""

import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from today_in_sci_tech.thread_generator import create_twitter_thread, save_thread_to_file
import os

@pytest.fixture
def mock_papers():
    return [
        {
            "title": "Test Paper 1",
            "summary": "Summary 1",
            "link": "https://arxiv.org/abs/test1"
        },
        {
            "title": "Test Paper 2",
            "summary": "Summary 2",
            "link": "https://arxiv.org/abs/test2"
        }
    ]

@pytest.fixture
def mock_summaries():
    return [
        "1. Summary 1\n2. Interesting 1\n3. 🚀 Tweet 1",
        "1. Summary 2\n2. Interesting 2\n3. 🚀 Tweet 2"
    ]

def test_create_twitter_thread(mock_papers, mock_summaries):
    """Test thread creation with mocked dependencies."""
    with patch('today_in_sci_tech.thread_generator.get_latest_arxiv_papers', return_value=mock_papers), \
         patch('today_in_sci_tech.thread_generator.summarize_paper', side_effect=mock_summaries):
        
        thread = create_twitter_thread()
        
        assert "Here are 3 wild new things in AI research this week" in thread
        assert "Test Paper 1" in thread
        assert "Test Paper 2" in thread
        assert "https://arxiv.org/abs/test1" in thread
        assert "https://arxiv.org/abs/test2" in thread

def test_save_thread_to_file(tmp_path):
    """Test saving thread to file."""
    # Change to temporary directory
    original_dir = Path.cwd()
    try:
        os.chdir(tmp_path)
        
        # Create data/threads directory
        (tmp_path / "data" / "threads").mkdir(parents=True)
        
        test_thread = "Test thread content"
        filename = save_thread_to_file(test_thread)
        
        # Verify file was created
        assert Path(filename).exists()
        assert Path(filename).read_text() == test_thread
        assert filename.startswith("data/threads/thread_")
    finally:
        os.chdir(original_dir)

def test_thread_generation_error_handling():
    """Test error handling during thread generation."""
    with patch('today_in_sci_tech.thread_generator.get_latest_arxiv_papers', 
              side_effect=Exception("Test error")):
        with pytest.raises(Exception) as exc_info:
            create_twitter_thread()
        assert "Test error" in str(exc_info.value) 