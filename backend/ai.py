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