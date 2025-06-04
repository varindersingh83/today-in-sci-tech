"""
Integration tests for the entire pipeline.
"""

import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from today_in_sci_tech.thread_generator import main
from today_in_sci_tech.fetcher import get_latest_arxiv_papers
from today_in_sci_tech.summarizer import summarize_paper
from today_in_sci_tech.alerts import send_sms_alert
import os

@pytest.fixture
def mock_papers():
    return [
        {
            "title": "Integration Test Paper 1",
            "summary": "Test summary 1",
            "link": "https://arxiv.org/abs/test1"
        },
        {
            "title": "Integration Test Paper 2",
            "summary": "Test summary 2",
            "link": "https://arxiv.org/abs/test2"
        }
    ]

@pytest.fixture
def mock_summaries():
    return [
        "1. Integration test summary 1\n2. Interesting 1\n3. 🚀 Tweet 1",
        "1. Integration test summary 2\n2. Interesting 2\n3. 🚀 Tweet 2"
    ]

@pytest.fixture
def mock_env_vars(monkeypatch):
    """Set up mock environment variables."""
    monkeypatch.setenv("OPENAI_API_KEY", "test_key")
    monkeypatch.setenv("ALERT_EMAIL", "test@example.com")
    monkeypatch.setenv("ALERT_EMAIL_PASS", "test_password")
    monkeypatch.setenv("ALERT_SMS_GATEWAY", "test@carrier.com")

def test_full_pipeline_success(tmp_path, mock_papers, mock_summaries, mock_env_vars):
    """Test the entire pipeline from fetching papers to saving the thread."""
    # Change to temporary directory
    original_dir = Path.cwd()
    try:
        os.chdir(tmp_path)
        
        # Create data/threads directory
        (tmp_path / "data" / "threads").mkdir(parents=True)
        
        # Mock all external dependencies
        with patch('today_in_sci_tech.thread_generator.get_latest_arxiv_papers', return_value=mock_papers), \
             patch('today_in_sci_tech.thread_generator.summarize_paper', side_effect=mock_summaries), \
             patch('today_in_sci_tech.thread_generator.send_sms_alert') as mock_alert:
            
            # Run the main function
            main()
            
            # Verify thread file was created
            thread_files = list(Path("data/threads").glob("thread_*.md"))
            assert len(thread_files) == 1
            
            # Verify thread content
            thread_content = thread_files[0].read_text()
            assert "Integration Test Paper 1" in thread_content
            assert "Integration Test Paper 2" in thread_content
            assert "https://arxiv.org/abs/test1" in thread_content
            assert "https://arxiv.org/abs/test2" in thread_content
            
            # Verify no alerts were sent (success case)
            mock_alert.assert_not_called()
            
    finally:
        os.chdir(original_dir)

def test_full_pipeline_error_handling(tmp_path, mock_env_vars):
    """Test error handling in the full pipeline."""
    # Change to temporary directory
    original_dir = Path.cwd()
    try:
        os.chdir(tmp_path)
        
        # Create data/threads directory
        (tmp_path / "data" / "threads").mkdir(parents=True)
        
        # Mock dependencies to simulate an error
        with patch('today_in_sci_tech.thread_generator.get_latest_arxiv_papers', 
                  side_effect=Exception("Test error")), \
             patch('today_in_sci_tech.thread_generator.send_sms_alert') as mock_alert:
            
            # Run the main function and expect it to raise the error
            with pytest.raises(Exception) as exc_info:
                main()
            
            assert "Test error" in str(exc_info.value)
            
            # Verify alert was sent
            mock_alert.assert_called_once()
            assert "Sci-Tech Thread Failed" in mock_alert.call_args[0][0]
            assert "Test error" in mock_alert.call_args[0][1]
            
    finally:
        os.chdir(original_dir) 