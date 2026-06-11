from langchain_community.document_loaders import DirectoryLoader
from pathlib import Path


def load_documents(path: Path | str, glob="*.pdf"):
    loader = DirectoryLoader(str(path), glob=glob)
    documents = loader.load()
    return documents
