import streamlit as st
import sys
from pathlib import Path

# Allow frontend to import from app/
sys.path.append(str(Path(__file__).resolve().parent.parent))

from backend.pdf_reader import save_uploaded_file, extract_text

st.set_page_config(
    page_title="StudyPilot",
    page_icon="📚",
    layout="wide"
)

st.title("📚 StudyPilot")
st.subheader("Your AI-Powered Study Assistant")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file:

    pdf_path = save_uploaded_file(uploaded_file)

    st.success("PDF uploaded successfully!")

    text = extract_text(pdf_path)

    st.subheader("Extracted Text")

    st.text_area(
        "",
        text[:5000],
        height=400
    )