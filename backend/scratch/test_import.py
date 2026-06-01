import os
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings

embeddings = HuggingFaceInferenceAPIEmbeddings(
    api_key="dummy_key",
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
print("HuggingFaceInferenceAPIEmbeddings imported successfully!")
