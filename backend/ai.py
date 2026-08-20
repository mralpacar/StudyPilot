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