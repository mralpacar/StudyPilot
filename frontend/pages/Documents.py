import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Documents")

st.title("📄 Documents")

UPLOAD_FOLDER = Path("uploads")

pdfs = list(UPLOAD_FOLDER.glob("*.pdf"))

if not pdfs:
    st.info("No documents uploaded yet.")

else:
    st.write("### Uploaded Documents")

    for pdf in pdfs:
        st.write(f"📄 {pdf.name}")