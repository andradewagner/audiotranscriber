from setuptools import setup, find_packages

setup(
    name="audiotranscriber",
    version="0.1.0",
    description="Modular Speech-to-Text pipeline using Whisper, spaCy, NLTK and FAISS.",
    author="Wagner Andrade",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=[
        "openai-whisper",
        "nltk",
        "spacy",
        "sentence-transformers",
        "faiss-cpu",
        "pyyaml",
        "numpy",
        "soundfile",
        "tqdm"
    ],
    include_package_data=True,
)