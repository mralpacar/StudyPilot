# 📚 StudyPilot

**StudyPilot is a local AI-powered study assistant that transforms PDF study materials into useful learning resources.**

Built as a personal software engineering project using Python, FastAPI, Streamlit, PyMuPDF, and Ollama.

---

## 💻 Installation & Setup

Follow the steps below to run StudyPilot locally.

### 1. Clone the repository

```bash
git clone https://github.com/mralpacar/StudyPilot.git
cd StudyPilot

### 2.  Create a Python virtual environment
Make sure Python 3.10 or newer is installed.

python3 -m venv .venv

### 3.  Activate the virtual environment
On macOS/Linux:
source .venv/bin/activate

On Windows:
.venv\Scripts\activate

### 4.  Install Python dependencies
pip install -r requirements.txt

### 5.  Install Ollama
StudyPilot uses Ollama to run the AI model locally.
Download and install Ollama from:
https://ollama.com/

### 6.  Download the AI model
StudyPilot currently uses the llama3.2 model.
ollama pull llama3.2

### 7.  Start the Ollama model
Ollama normally runs in the background after installation. You can test the model with:
ollama run llama3.2
Try asking it a simple question to make sure it responds.
To exit the model:
/bye

### 8.  Start StudyPilot
From the StudyPilot project directory, run:
streamlit run frontend/home.py
Streamlit will provide a local URL

## 🚀 Features

### 📄 PDF Document Processing
- Upload PDF study materials through the Streamlit interface.
- Extract text automatically using PyMuPDF.
- Store uploaded documents locally.
- Display document metadata including:
  - Page count
  - Word count
  - Upload time

### 🧠 AI Summaries
- Generate concise summaries from uploaded study materials.
- Uses a locally hosted LLM through Ollama.
- Documents can be processed without sending their contents to a cloud AI API.

### 🎴 AI Flashcards
- Generate study flashcards from uploaded documents.
- Adjustable number of flashcards.
- Focuses on important concepts and facts.

### 📝 AI Quiz Generation
- Generate multiple-choice question from study materials.
- Designed to test understanding of the uploaded material.

### 📂 Document Library
- View previously uploaded PDF documents.
- Keep study materials organized inside the application.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | Backend/API framework |
| Streamlit | User interface |
| PyMuPDF | PDF text extraction |
| Ollama | Local AI inference |
| Git & GitHub | Version control |

---

## 🏗️ Architecture

```text
                    StudyPilot
                        │
                        ▼
                 Streamlit Frontend
                        │
                        ▼
                  Document Upload
                        │
                        ▼
                  PDF Processing
                        │
                        ▼
                  Text Extraction
                        │
                        ▼
                  AI Processing
                        │
                        ▼
                    Ollama
                        │
             ┌──────────┼──────────┐
             ▼          ▼          ▼
          Summary   Flashcards    Quiz