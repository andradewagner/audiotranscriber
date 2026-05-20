### 🚀 AudioTranscriptor — Speech‑to‑Text + NLP Pipeline

<p align="center">
  <a href="https://python.org"><img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python Version" /></a>
  <a href="https://opensource.org"><img src="https://img.shields.io/badge/license-MIT-green" alt="License" /></a>
  <img src="https://img.shields.io/badge/status-active-success" alt="Status" />
  <a href="https://github.com"><img src="https://img.shields.io/github/last-commit/andradewagner/audiotranscriber" alt="Last Commit" /></a>
  <a href="https://github.com"><img src="https://github.com/andradewagner/audiotranscriber/actions/workflows/tests.yml/badge.svg" alt="Last Commit" /></a>
</p>

### 💡 Overview

AudioTranscriptor is a modular, fully configurable pipeline for:

* Speech‑to‑text transcription using Whisper
* Advanced text preprocessing (normalization, accent removal, stopwords, stemming, lemmatization)
* Tokenization using NLTK or spaCy
* Embedding preparation (Sentence Transformers)
* Vector storage using FAISS

Everything is controlled through `config.yaml`, enabling fast experimentation without modifying the source code.

### ✨ Features

* Whisper‑based multilingual speech recognition
* Text normalization and cleaning
* Tokenization with NLTK or spaCy
* Optional stemming and lemmatization
* Accent removal
* Stopword filtering
* Embedding‑ready text output
* Vector store integration (FAISS)
* Clean and extensible architecture
* CLI powered by Typer

### 🧠 Architecture Overview

```text
Audio File → Whisper Transcription → Text Preprocessing → Tokenization → Embeddings → Vector Store
```

### 🏗️ Project Structure

```text
├── data/
│   ├── raw/              # Original audio files
│   └── processed/        # Transcriptions and processed text
├── models/               # Model artifacts (spaCy, embeddings, FAISS)
├── logs/                 # Log files
├── notebooks/            # EDA and prototyping
├── src/
│   ├── audiotranscriber/
│   │   ├── transcriber.py       # Whisper transcription pipeline
│   │   ├── text_processor.py    # NLP preprocessing pipeline
│   │   ├── logger_config.py     # Centralized logging
│   │   ├── nlp/                 # Tokenizers, preprocessors, etc.
│   │   └── cli.py               # Typer CLI
├── tests/                # Unit tests
└── config.yaml           # Pipeline configuration
```

### ⚙️ Installation

#### 1. Install dependencies

```bash
pip install -r requirements.txt
```

#### 2. Install FFmpeg (required by Whisper)

**Ubuntu / Debian**
```bash
sudo apt update && sudo apt install ffmpeg
```

**Arch Linux**
```bash
sudo pacman -S ffmpeg
```

**macOS (Homebrew)**
```bash
brew install ffmpeg
```

**Windows (Chocolatey)**
```bash
choco install ffmpeg
```

### 🛠️ Configuration

Edit `config.yaml` to define:
* Audio and transcription paths
* Whisper model
* Tokenizer (NLTK or spaCy)
* Normalization options
* Stopwords, stemming, lemmatization
* spaCy model
* Embedding model
* Vector store backend

Example:
```yaml
text_processing:
  lowercase: true
  remove_accents: true
  remove_stopwords: true
  stemming: true
  lemmatization: true
  tokenizer_language: portuguese
  spacy:
    model_name: pt_core_news_md
```

### 🚀 Usage (CLI)

#### 🔊 Transcribe audio
```bash
audiotranscriber transcribe data/raw/audio.m4a
```

#### ✏️ Process text
```bash
audiotranscriber process data/processed/transcription.txt
```

#### 🧪 Running scripts manually
```bash
python src/audiotranscriber/transcriber.py
python src/audiotranscriber/text_processor.py
```