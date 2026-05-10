from sklearn.metrics.pairwise import cosine_similarity

from rag.embeddings import embedding_model


def retrieve_resume_context(
    vector_store,
    query: str,
    k: int = 3
):

    query_embedding = embedding_model.embed_query(query)

    similarities = cosine_similarity(
        [query_embedding],
        vector_store["embeddings"]
    )[0]

    top_indices = similarities.argsort()[-k:][::-1]

    relevant_chunks = [
        vector_store["chunks"][i]
        for i in top_indices
    ]

    return "\n".join(relevant_chunks)