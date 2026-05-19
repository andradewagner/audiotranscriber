### 🚀 AudioTranscriptor — Speech‑to‑Text + NLP Pipeline

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10%2B-blue" />
  <img src="https://img.shields.io/badge/license-MIT-green" />
  <img src="https://img.shields.io/badge/status-active-success" />
  <img src="https://img.shields.io/github/last-commit/SEU_USUARIO/AudioTranscriptor" />
</p>


### 💡 Overview

AudioTranscriptor is a modular, fully configurable pipeline for:

    Speech‑to‑text transcription using Whisper

    Advanced text preprocessing (normalization, accent removal, stopwords, stemming, lemmatization)

    Tokenization using NLTK or spaCy

    Embedding preparation (Sentence Transformers)

    Vector storage using FAISS

Everything is controlled through config.yaml, enabling fast experimentation without modifying the source code.

### ✨ Features

    Whisper‑based multilingual speech recognition

    Text normalization and cleaning

    Tokenization with NLTK or spaCy

    Optional stemming and lemmatization

    Accent removal

    Stopword filtering

    Embedding‑ready text output

    Vector store integration (FAISS)

    Clean and extensible architecture

    CLI powered by Typer

### 🧠 Architecture Overview

Audio File → Whisper Transcription → Text Preprocessing → Tokenization → Embeddings → Vector Store


### 🏗️ Project Structure

```
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
## 1. Install dependencies

    pip install -r requirements.txt

## 2. Install FFmpeg (required by Whisper)
# Ubuntu / Debian

    sudo apt update && sudo apt install ffmpeg

# 3. Arch Linux

    sudo pacman -S ffmpeg

# 4. macOS (Homebrew)

    brew install ffmpeg

# 5. Windows (Chocolatey)

    choco install ffmpeg

### 🛠️ Configuration
Edit config.yaml to define:

    audio and transcription paths

    Whisper model

    tokenizer (NLTK or spaCy)

    normalization options

    stopwords, stemming, lemmatization

    spaCy model

    embedding model

    vector store backend

Example:
~~~
text_processing:
  lowercase: true
  remove_accents: true
  remove_stopwords: true
  stemming: true
  lemmatization: true
  tokenizer_language: portuguese
  spacy:
    model_name: pt_core_news_md
~~~

### 🚀 Usage (CLI)

## 🔊 Transcribe audio
~~~
audiotranscriber transcribe data/raw/audio.m4a
~~~

## ✏️ Process text
~~~
audiotranscriber process data/processed/transcription.txt
~~~

## 🧪 Running scripts manually

~~~
python src/audiotranscriber/transcriber.py
python src/audiotranscriber/text_processor.py
~~~