from pathlib import Path
import fitz  # PyMuPDF


UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)


def save_uploaded_file(uploaded_file):
    """
    Save uploaded PDF to the uploads folder.
    Returns the saved file path.
    """
    file_path = UPLOAD_FOLDER / uploaded_file.name

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path


def extract_text(pdf_path):
    """
    Extract all text from a PDF.
    """
    document = fitz.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text