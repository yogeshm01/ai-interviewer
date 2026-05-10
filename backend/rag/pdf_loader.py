from pypdf import PdfReader


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from uploaded PDF resume.
    """

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    return text.strip()