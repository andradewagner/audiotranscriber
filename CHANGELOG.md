# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] - 2026-05-19
### Added
- Initial release of **AudioTranscriptor**.
- Modular Whisper transcription pipeline.
- Text preprocessing pipeline (normalization, stopwords, stemming, lemmatization).
- Tokenization support with NLTK and spaCy.
- Configurable processing via `config.yaml`.
- Logging system with rotating logs.
- CLI interface using Typer (`audiotranscriber`).
- Project structure with `src/` layout.
- MIT License.
- README.md in English.
- pyproject.toml for packaging.

### Changed
- N/A (first release)

### Fixed
- N/A (first release)

---

## [Unreleased]
### Planned
- Full pipeline command (`audiotranscriber run`).
- FAISS vector indexing.
- Semantic search module.
- FastAPI REST API.
- Streamlit dashboard.
- GitHub Actions CI/CD.