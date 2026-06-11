from utils import load_documents

if __name__ == "__main__":
    documents = load_documents("data/")
    print(documents[0].metadata)
