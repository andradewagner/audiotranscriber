### 🚀 AudioTranscriptor — Machine Learning Speech-to-Text Pipeline

### 💡 Overview

AudioTranscriptor é um pipeline modular e totalmente configurável para:

    Transcrição de áudio com Whisper

    Processamento avançado de texto (normalização, stopwords, stemming, lematização)

    Tokenização com NLTK ou spaCy

    Preparação para embeddings e armazenamento vetorial (FAISS)

Tudo é controlado via config.yaml, permitindo experimentação rápida sem alterar o código.

### 🎙️ Whisper — Speech Recognition

Whisper é um modelo Transformer multitarefa treinado em:

    Reconhecimento de fala multilíngue

    Tradução de fala

    Identificação de idioma

    Detecção de atividade de voz

Ele substitui pipelines tradicionais com um único modelo seq2seq.

![Approach](https://pypi-camo.freetls.fastly.net/2f74e24341799e4f45c94c71c291603f5337f040/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f6f70656e61692f776869737065722f6d61696e2f617070726f6163682e706e67)


### 🏗️ Project Structure

```
├── data/
│   ├── raw/              # Áudios originais
│   └── processed/        # Transcrições e textos processados
├── models/               # Artefatos de modelos
├── notebooks/            # EDA e prototipação
├── logs/                 # Arquivos de log
├── src/
│   ├── ingest.py         # Coleta de dados
│   ├── logger_config.py  # Configuração de logs
│   ├── text_processor.py # Pipeline de processamento de texto
│   ├── transcriber.py    # Transcrição com Whisper
│   ├── train.py          # Treinamento de modelos
│   └── predict.py        # Inferência
├── tests/                # Testes unitários
└── config.yaml           # Configurações do pipeline
```

### ⚙️ How to Use

    Install dependencies:
    Bash

    pip install -r requirements.txt

    ## 2. Configurar o projeto

    Edite config.yaml para definir:

        Caminhos de áudio e transcrição

        Modelo Whisper

        Tokenizer (NLTK ou spaCy)

        Normalização, stopwords, stemming, lematização

        Modelo spaCy

        Embeddings e vector store

    ## 3. Executar o pipeline
    
    # Transcrever áudio

    python src/transcriber.py

    # Processar texto

    python src/text_processor.py

    # Treinar modelo

    python src/train.py

    # Fazer predições

    python src/predict.py --input data/sample.csv


### 🎧 FFmpeg — Dependência obrigatória

## Whisper requer FFmpeg para manipular arquivos de áudio.

# Ubuntu / Debian

sudo apt update && sudo apt install ffmpeg

# Arch Linux

sudo pacman -S ffmpeg

# macOS (Homebrew)

brew install ffmpeg

# Windows (Chocolatey)

choco install ffmpeg

# Windows (Scoop)

scoop install ffmpeg
