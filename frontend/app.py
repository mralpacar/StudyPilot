import streamlit as st

st.set_page_config(
    page_title="StudyPilot",
    page_icon="📚",
    layout="wide"
)

st.title("📚 StudyPilot")

st.subheader("Your AI-Powered Study Assistant")

st.write("""
Upload your study notes and let AI generate:

- 📝 Summaries
- 🎴 Flashcards
- ❓ Quizzes
- 📈 Progress Tracking
""")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")