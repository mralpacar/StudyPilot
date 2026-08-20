import streamlit as st 
import sys 
from pathlib import Path

# Allow imports from the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.pdf_reader import save_uploaded_file, extract_text
from backend.document_manager import create_document
from backend.ai import generate_summary


st.set_page_config(
    page_title="StudyPilot",
    page_icon="📚",
    layout="wide",
)

st.title("📚 StudyPilot")
st.subheader("Your AI-Powered Study Assistant")

st.write(
    """
Welcome to **StudyPilot**.

Upload your study notes and let AI help you learn smarter.
"""
)

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"],
)

if uploaded_file:

    # Save PDF
    pdf_path = save_uploaded_file(uploaded_file)

    # Create metadata
    document = create_document(pdf_path)

    st.success("✅ Document uploaded successfully!")

    st.subheader("Document Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Pages", document.page_count)

    with col2:
        st.metric("Words", document.word_count)

    with col3:
        st.metric(
            "Uploaded",
            document.uploaded_at.strftime("%H:%M"),
        )

    with st.expander("📄 Preview Extracted Text"):

        text = extract_text(pdf_path)

        st.text_area(
            "Text Preview",
            text[:3000],
            height=350,
        )
    st.divider()

st.subheader("🧠 AI Study Tools")

if st.button("Generate Summary"):

    with st.spinner("StudyPilot is analyzing your document..."):

        summary = generate_summary(text)

    st.subheader("📝 Summary")

    st.markdown(summary)
    