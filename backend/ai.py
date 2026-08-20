import ollama


MODEL_NAME = "llama3.2"


def generate_summary(text: str) -> str:
    """Generate a concise study summary from document text."""

    prompt = f"""
You are StudyPilot, an AI study assistant.

Summarize the following study material for a student.

Your summary should:
- Identify the main ideas.
- Explain important concepts clearly.
- Include important definitions, formulas, or facts.
- Use bullet points where appropriate.
- Avoid unnecessary information.
- Do not invent information that is not present in the document.

Study material:

{text}
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response["message"]["content"]

def generate_flashcards(text: str, number_of_cards: int = 10) -> str:
    """Generate study flashcards from document text."""

    prompt = f"""
You are StudyPilot, an AI study assistant.

Create {number_of_cards} useful study flashcards from the
following study material.

Rules:
- Focus on important concepts and facts.
- Make questions clear and specific.
- Make answers concise but informative.
- Do not invent information.
- Number each flashcard.
- Use exactly this format:

1. Question: ...
   Answer: ...

2. Question: ...
   Answer: ...

Study material:

{text}
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response["message"]["content"]

def generate_quiz(text: str, number_of_questions: int = 5):
    """Generate structured multiple-choice questions."""

    prompt = f"""
Create exactly {number_of_questions} multiple-choice questions
using ONLY the study material below.

Return ONLY valid JSON.
Do not include markdown.
Do not include ```.

The JSON must have exactly this structure:

{{
    "questions": [
        {{
            "question": "Question text",
            "options": [
                "Option A",
                "Option B",
                "Option C",
                "Option D"
            ],
            "answer": 0
        }}
    ]
}}

Rules:
- Create exactly {number_of_questions} questions.
- Each question has exactly 4 options.
- "answer" must be 0, 1, 2, or 3.
- Only one answer is correct.
- Use only information contained in the study material.

Study material:

{text}
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response["message"]["content"]