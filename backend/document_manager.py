from dataclasses import dataclass
from pathlib import Path
from datetime import datetime
import fitz


@dataclass
class Document:
    filename: str
    path: Path
    uploaded_at: datetime
    page_count: int
    word_count: int


def create_document(pdf_path: Path) -> Document:
    """Read a PDF and create its metadata."""

    document = fitz.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()

    metadata = Document(
        filename=pdf_path.name,
        path=pdf_path,
        uploaded_at=datetime.now(),
        page_count=document.page_count,
        word_count=len(text.split())
    )

    document.close()

    return metadata