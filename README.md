### 🚀 Machine Learning Audio Transcriptor

### 💡 Description

Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multitasking model that can perform multilingual speech recognition, speech translation, and language identification.
Approach

Approach

![Approach](https://pypi-camo.freetls.fastly.net/2f74e24341799e4f45c94c71c291603f5337f040/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f6f70656e61692f776869737065722f6d61696e2f617070726f6163682e706e67)

A Transformer sequence-to-sequence model is trained on various speech processing tasks, including multilingual speech recognition, speech translation, spoken language identification, and voice activity detection. These tasks are jointly represented as a sequence of tokens to be predicted by the decoder, allowing a single model to replace many stages of a traditional speech-processing pipeline. The multitask training format uses a set of special tokens that serve as task specifiers or classification targets.

### 🏗️ Estrutura do Projeto

```
├── data/
│   ├── raw/            # Dados originais (nunca editados)
│   └── processed/      # Dados prontos para o modelo
├── models/             # Artefatos binários (.pkl, .h5, etc.)
├── notebooks/          # Exploração (EDA) e prototipagem rápida
├── src/                # O "coração" do projeto
│   ├── ingest.py       # Extração de dados (SQL, CSV, APIs)
│   ├── preprocess.py   # Feature engineering e limpeza
│   ├── train.py        # Script de treino e validação
│   └── predict.py      # Lógica de inferência
├── tests/              # Testes para garantir a integridade dos dados
└── config.yaml         # Onde a mágica (parâmetros) acontece
```

### ⚙️ Como Utilizar

    Instale as dependências:
    Bash

    pip install -r requirements.txt

    Configure o projeto: Altere o config.yaml para definir caminhos de pastas e parâmetros do modelo.

    Execute o Pipeline:

        Para processar: python src/preprocess.py

        Para treinar: python src/train.py

        Para prever: python src/predict.py --input data/sample.csv
    
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