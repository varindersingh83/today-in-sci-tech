import openai
import os
from dotenv import load_dotenv
load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_paper(paper):
    prompt = f"""
You are a science communicator who explains complex topics to smart, curious nerds.
Summarize this research paper in 3 parts:
1. What it says (in plain English)
2. Why it's interesting or important
3. A catchy tweet-style hook with emojis

Title: {paper['title']}
Abstract: {paper['summary']}
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content
