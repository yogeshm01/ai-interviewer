from langchain_text_splitters import RecursiveCharacterTextSplitter

from rag.embeddings import embedding_model


def create_vector_store(
    resume_text: str
):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = text_splitter.split_text(resume_text)

    embeddings = embedding_model.embed_documents(chunks)

    return {
        "chunks": chunks,
        "embeddings": embeddings
    }