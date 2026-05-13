### 🚀 Machine Learning Audio Transcriptor

### 💡 Description

Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multitasking model that can perform multilingual speech recognition, speech translation, and language identification.
Approach

Approach

![Approach](https://pypi-camo.freetls.fastly.net/2f74e24341799e4f45c94c71c291603f5337f040/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f6f70656e61692f776869737065722f6d61696e2f617070726f6163682e706e67)

A Transformer sequence-to-sequence model is trained on various speech processing tasks, including multilingual speech recognition, speech translation, spoken language identification, and voice activity detection. These tasks are jointly represented as a sequence of tokens to be predicted by the decoder, allowing a single model to replace many stages of a traditional speech-processing pipeline. The multitask training format uses a set of special tokens that serve as task specifiers or classification targets.

### 🏗️ Project Structure

```
├── data/
│   ├── raw/              # Original data (never edited)
│   └── processed/        # Model-ready data
├── models/               # Binary artifacts (.pkl, .h5, etc.)
├── notebooks/            # Exploratory Data Analysis (EDA) and rapid prototyping
├── logs/                 # Log files
├── src/                  # Core project source code
│   ├── ingest.py         # Data extraction (SQL, CSV, APIs)
│   ├── logger_config.py  # Logger configuration setup
│   ├── preprocess.py     # Feature engineering and cleaning
│   ├── train.py          # Training and validation script
│   ├── transcriber.py    # Audio-to-text transcription script
│   └── predict.py        # Inference logic
├── tests/                # Unit tests to ensure data and code integrity
└── config.yaml           # Where the magic (parameters) happens
```

### ⚙️ How to Use

    Install dependencies:
    Bash

    pip install -r requirements.txt

    Project Configuration: Change config.yaml to define paths, folders and model parameters.

    Pipeline execution:

        To transcribe audio: python src/transcriber.py
        
        To process: python src/preprocess.py

        To train: python src/train.py

        To predict: python src/predict.py --input data/sample.csv
    
    # on Ubuntu or Debian
    sudo apt update && sudo apt install ffmpeg

    # on Arch Linux
    sudo pacman -S ffmpeg

    # on MacOS using Homebrew (https://brew.sh/)
    brew install ffmpeg

    # on Windows using Chocolatey (https://chocolatey.org/)
    choco install ffmpeg

    # on Windows using Scoop (https://scoop.sh/)
    scoop install ffmpeg