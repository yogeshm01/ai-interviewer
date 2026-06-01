import math
from rag.embeddings import embedding_model


def dot_product(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))


def magnitude(v):
    return math.sqrt(sum(x * x for x in v))


def pure_cosine_similarity(v1, v2):
    m1 = magnitude(v1)
    m2 = magnitude(v2)
    if m1 == 0 or m2 == 0:
        return 0.0
    return dot_product(v1, v2) / (m1 * m2)


def retrieve_resume_context(
    vector_store,
    query: str,
    k: int = 3
):

    query_embedding = embedding_model.embed_query(query)

    # Compute cosine similarity using pure Python
    similarities = [
        pure_cosine_similarity(query_embedding, doc_emb)
        for doc_emb in vector_store["embeddings"]
    ]

    # Get top k indices sorted descending by similarity score
    top_indices = sorted(
        range(len(similarities)),
        key=lambda i: similarities[i],
        reverse=True
    )[:k]

    relevant_chunks = [
        vector_store["chunks"][i]
        for i in top_indices
    ]

    return "\n".join(relevant_chunks)