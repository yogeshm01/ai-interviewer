import os
from dotenv import load_dotenv

load_dotenv()

_embedding_instance = None

def get_embedding_model():
    global _embedding_instance
    if _embedding_instance is None:
        from langchain_huggingface import HuggingFaceEmbeddings
        _embedding_instance = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
    return _embedding_instance

class LazyEmbeddingModel:
    def embed_documents(self, texts):
        return get_embedding_model().embed_documents(texts)

    def embed_query(self, text):
        return get_embedding_model().embed_query(text)

embedding_model = LazyEmbeddingModel()


