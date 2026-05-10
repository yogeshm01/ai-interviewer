import json

from utils.groq_client import llm
from utils.prompts import FOLLOWUP_PROMPT


def generate_followup_question(
    question: str,
    answer: str,
    weak_areas: list
):

    prompt = FOLLOWUP_PROMPT.format(
        question=question,
        answer=answer,
        weak_areas=weak_areas
    )

    response = llm.invoke(prompt)

    content = response.content.strip()

    # Remove markdown wrappers
    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    try:
        parsed_response = json.loads(content)

    except Exception as e:

        print("Followup JSON Parsing Error:", e)

        parsed_response = {
            "followup_question":
            "Can you explain that in more detail?"
        }

    return parsed_response