# Today in Sci-Tech

An automated tool that generates engaging Twitter threads about the latest AI research papers.

## Features

- Fetches latest AI research papers from arXiv
- Summarizes papers using OpenAI's GPT models
- Generates engaging Twitter threads
- Sends SMS alerts for errors or important updates
- Modular and extensible architecture

## Project Structure

```
today-in-sci-tech/
├── src/
│   └── today_in_sci_tech/
│       ├── __init__.py
│       ├── alerts.py        # SMS alert functionality
│       ├── fetcher.py       # arXiv paper fetching
│       ├── summarizer.py    # Paper summarization
│       └── thread_generator.py  # Twitter thread generation
├── tests/
│   ├── __init__.py
│   ├── test_alerts.py
│   ├── test_fetcher.py
│   ├── test_integration.py
│   ├── test_summarizer.py
│   └── test_thread_generator.py
├── data/
│   └── threads/            # Generated thread files
├── .env.example           # Example environment variables
├── .gitignore
├── pyproject.toml        # Project metadata and dependencies
├── pytest.ini           # Pytest configuration
└── README.md
```

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/today-in-sci-tech.git
cd today-in-sci-tech
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install the package in development mode:
```bash
pip install -e ".[dev]"
```

4. Copy `.env.example` to `.env` and fill in your credentials:
```bash
cp .env.example .env
```

Required environment variables:
- `OPENAI_API_KEY`: Your OpenAI API key
- `ALERT_EMAIL`: Email address for sending alerts
- `ALERT_EMAIL_PASS`: Email password
- `ALERT_SMS_GATEWAY`: SMS gateway email address

## Usage

Run the thread generator:
```bash
python -m today_in_sci_tech.thread_generator
```

This will:
1. Fetch the latest AI research papers
2. Generate summaries
3. Create a Twitter thread
4. Save the thread to `data/threads/`

## Development

### Code Style

The project uses:
- Black for code formatting
- isort for import sorting
- flake8 for linting

Run the formatters:
```bash
black src tests
isort src tests
flake8 src tests
```

### Testing

The project uses pytest for testing. Run tests with:
```bash
PYTHONPATH=src pytest
```

Test structure:
- Unit tests for each module
- Integration tests for the full pipeline
- Mocked external dependencies (OpenAI API, SMTP)

### Data Directory

The `data/threads/` directory stores generated Twitter threads:
- Files are named with timestamp: `thread_YYYY-MM-DD_HH-MM.md`
- Directory structure is preserved in git with `.gitkeep`
- Generated files are ignored by git

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and formatters
5. Submit a pull request

## License

MIT License - see LICENSE file for details 