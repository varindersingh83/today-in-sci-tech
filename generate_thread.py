from fetch_papers import get_latest_arxiv_papers
from summarize import summarize_paper
from datetime import datetime
import logging
from alerts import send_sms_alert


logging.basicConfig(level=logging.INFO)

def save_thread_to_file(text):
    now = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"thread_{now}.md"
    with open(filename, "w") as f:
        f.write(text)
    print(f"\n✅ Saved to {filename}")


def create_twitter_thread():
    try:
        papers = get_latest_arxiv_papers()
        logging.info(f"Fetched {len(papers)} papers.")
        thread = ["Here are 3 wild new things in AI research this week 🧵👇"]
        for i, paper in enumerate(papers):
            logging.info(f"Summarizing paper {i+1}: {paper['title']}")
            summary = summarize_paper(paper)
            thread.append(f"{i+1}. {paper['title']}\n{summary}\n🔗 {paper['link']}")
        return "\n\n".join(thread)
    except Exception as e:
        logging.error("Thread generation failed", exc_info=True)
        raise



if __name__ == "__main__":
    try:
        thread_text = create_twitter_thread()
        print("\n--- THREAD OUTPUT ---\n")
        print(thread_text)
        save_thread_to_file(thread_text)
    except Exception as e:
        send_sms_alert("Sci-Tech Thread Failed", str(e))
        raise

