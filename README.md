# Today in Science & Tech

An automated tool that generates engaging Twitter threads about the latest AI research papers from arXiv. The tool fetches recent papers, summarizes them in an accessible way, and creates a formatted thread ready for sharing.

## Features

- Fetches latest AI research papers from arXiv RSS feed
- Uses GPT-4 to generate accessible summaries of complex research
- Creates formatted Twitter threads with paper titles, summaries, and links
- Includes error handling and SMS alerts for monitoring
- Saves generated threads as markdown files with timestamps

## Project Structure

```
today-in-sci-tech/
├── data/                  # Data directory
│   └── threads/          # Generated thread files
├── src/                  # Source code
│   └── today_in_sci_tech/
│       ├── __init__.py
│       ├── __main__.py   # CLI entry point
│       ├── alerts.py     # SMS notification system
│       ├── fetcher.py    # arXiv paper fetching
│       ├── summarizer.py # GPT-4 summarization
│       └── thread_generator.py # Main thread generation
├── tests/                # Test suite
├── .gitignore
├── README.md
├── requirements.txt
└── setup.py
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

4. Create a `.env` file with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ALERT_EMAIL=your_email@gmail.com
   ALERT_EMAIL_PASS=your_app_specific_password
   ALERT_SMS_GATEWAY=your_phone@carrier_gateway.com
   ```

   Note: For Gmail, you'll need to use an App Password. For SMS gateway, use your carrier's email-to-SMS gateway address.

## Usage

Run the main script to generate a new thread:
```bash
python -m today_in_sci_tech
```

The script will:
1. Fetch the latest AI papers from arXiv
2. Generate summaries using GPT-4
3. Create a formatted Twitter thread
4. Save the thread to `data/threads/thread_YYYY-MM-DD_HH-MM.md`
5. Send SMS alerts if any errors occur

## Development

### Running Tests
```bash
pytest
```

### Code Style
The project uses:
- `black` for code formatting
- `isort` for import sorting
- `flake8` for linting

Run all checks:
```bash
black src tests
isort src tests
flake8 src tests
```

### Adding New Features
1. Create a new branch
2. Add tests for your feature
3. Implement the feature
4. Run tests and style checks
5. Submit a pull request

## Data Directory

The `data/threads` directory stores all generated thread files. Each file is named with a timestamp:
- Format: `thread_YYYY-MM-DD_HH-MM.md`
- Example: `thread_2024-05-23_10-28.md`

The directory structure is maintained in git, but the generated files are ignored.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and style checks
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 