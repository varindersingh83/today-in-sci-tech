"""
Main module for generating Twitter threads from research papers.
"""

import logging
import os
from datetime import datetime
from typing import List, Dict
from pathlib import Path

from .fetcher import get_latest_arxiv_papers
from .summarizer import summarize_paper
from .alerts import send_sms_alert

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def save_thread_to_file(text: str) -> str:
    """
    Save the generated thread to a markdown file in the data/threads directory.
    
    Args:
        text: The thread text to save
        
    Returns:
        Path to the saved file
    """
    # Create data/threads directory if it doesn't exist
    output_dir = Path("data/threads")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    now = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = output_dir / f"thread_{now}.md"
    
    with open(filename, "w") as f:
        f.write(text)
    logger.info(f"✅ Saved to {filename}")
    return str(filename)

def create_twitter_thread() -> str:
    """
    Create a Twitter thread from the latest research papers.
    
    Returns:
        Formatted thread text
    """
    try:
        papers = get_latest_arxiv_papers()
        logger.info(f"Fetched {len(papers)} papers.")
        
        thread = ["Here are 3 wild new things in AI research this week 🧵👇"]
        
        for i, paper in enumerate(papers):
            logger.info(f"Summarizing paper {i+1}: {paper['title']}")
            summary = summarize_paper(paper)
            thread.append(f"{i+1}. {paper['title']}\n{summary}\n🔗 {paper['link']}")
            
        return "\n\n".join(thread)
    except Exception as e:
        logger.error("Thread generation failed", exc_info=True)
        raise

def main() -> None:
    """Main entry point for the thread generator."""
    try:
        thread_text = create_twitter_thread()
        print("\n--- THREAD OUTPUT ---\n")
        print(thread_text)
        save_thread_to_file(thread_text)
    except Exception as e:
        send_sms_alert("Sci-Tech Thread Failed", str(e))
        raise 