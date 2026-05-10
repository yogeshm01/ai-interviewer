import uuid

from fastapi import APIRouter, UploadFile, File

from rag.pdf_loader import extract_text_from_pdf
from rag.vector_store import create_vector_store

router = APIRouter()

# Temporary in-memory store
resume_store = {}


@router.post("/upload-resume")
async def upload_resume(
    file: UploadFile = File(...)
):

    # Validate PDF
    if not file.filename.endswith(".pdf"):
        return {
            "error": "Only PDF files are allowed."
        }

    # Unique ID
    resume_id = str(uuid.uuid4())

    # Save path
    file_path = f"uploads/{resume_id}.pdf"

    # Save file
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    # Extract resume text
    resume_text = extract_text_from_pdf(file_path)

    # Create vector DB
    vector_store = create_vector_store(
        resume_text=resume_text
    )

    # Store session data
    resume_store[resume_id] = {
        "resume_text": resume_text,
        "vector_store": vector_store
    }

    return {
        "message": "Resume uploaded successfully",
        "resume_id": resume_id,
        "preview": resume_text[:500]
    }