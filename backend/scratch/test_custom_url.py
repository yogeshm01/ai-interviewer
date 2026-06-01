import os
import traceback
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings

embeddings = HuggingFaceInferenceAPIEmbeddings(
    api_key="dummy_key",
    api_url="https://router.huggingface.co/hf-inference/models/sentence-transformers/all-MiniLM-L6-v2",
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

try:
    embeddings.embed_query("hello")
except Exception as e:
    print("Traceback:")
    traceback.print_exc()
