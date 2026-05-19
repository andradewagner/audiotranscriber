# Contributing to AudioTranscriptor

Thank you for your interest in contributing to **AudioTranscriptor**!  
We welcome contributions of all kinds — bug fixes, new features, documentation improvements, and ideas.

This document explains how to set up your environment, follow the project standards, and submit contributions properly.

---

## 🧱 Project Structure

The project follows a clean `src/` layout:

~~~
src/
└── audiotranscriber/
├── transcriber.py
├── text_processor.py
├── logger_config.py
├── nlp/
└── cli.py
~~~

---

## 🚀 Getting Started

### 1. Fork the repository

Click **Fork** on GitHub and clone your fork:

```bash
git clone https://github.com/andradewagner/audiotranscriber.git
cd audiotranscriber
```

### 2. Create a virtual environment

~~~bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
~~~

### 3. Install dependencies

~~~bash
pip install -r requirements.txt
pip install -e .
~~~

### 🧪 Running Tests

Tests are located in the tests/ directory.

Run all tests with:

~~~bash
pytest
~~~

### 🧼 Code Style

This project follows:

    Black for formatting

    Ruff or Flake8 for linting

    isort for import ordering

Before committing, run:

~~~bash
black .
ruff check .
isort .
~~~

### 🌿 Branching Model

Use the following branch naming conventions:

    feature/<name> — new features

    fix/<name> — bug fixes

    docs/<name> — documentation updates

    refactor/<name> — code improvements

Example:

~~~bash
git checkout -b feature/semantic-search
~~~

### 🔀 Pull Requests

Before opening a PR:

    1. Ensure your branch is up to date:

    ~~~bash
    git pull origin main
    ~~~

    2. Run tests and linters

    3. Update documentation if needed

    4. Add entries to CHANGELOG.md under [Unreleased]

    PR Checklist

        [ ] Code follows project style

        [ ] Tests added or updated

        [ ] Documentation updated

        [ ] CHANGELOG updated

        [ ] PR title is clear and descriptive

    🐛 Reporting Issues

    Open an issue with:

        Clear description

        Steps to reproduce

        Expected behavior

        Logs or screenshots if relevant

### 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for helping improve AudioTranscriptor!