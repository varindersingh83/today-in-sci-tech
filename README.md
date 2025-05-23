# Today in Science & Tech

An automated tool that generates engaging Twitter threads about the latest AI research papers from arXiv. The tool fetches recent papers, summarizes them in an accessible way, and creates a formatted thread ready for sharing.

## Features

- Fetches latest AI research papers from arXiv RSS feed
- Uses GPT-4 to generate accessible summaries of complex research
- Creates formatted Twitter threads with paper titles, summaries, and links
- Includes error handling and SMS alerts for monitoring
- Saves generated threads as markdown files with timestamps

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

Run the main script to generate a new thread:
```bash
python generate_thread.py
```

The script will:
1. Fetch the latest AI papers from arXiv
2. Generate summaries using GPT-4
3. Create a formatted Twitter thread
4. Save the thread to a markdown file with timestamp
5. Send SMS alerts if any errors occur

## Project Structure

- `fetch_papers.py`: Handles fetching papers from arXiv RSS feed
- `summarize.py`: Uses GPT-4 to generate accessible summaries
- `generate_thread.py`: Main script that orchestrates the thread generation
- `alerts.py`: Handles error notifications via SMS
- `requirements.txt`: Project dependencies

## Testing

Run the test suite:
```bash
pytest
```

## Contributing

Feel free to submit issues and enhancement requests! 