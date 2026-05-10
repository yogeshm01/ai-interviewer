import json

from utils.groq_client import llm
from utils.prompts import EVALUATION_PROMPT


def evaluate_answer(
    question: str,
    answer: str
):

    prompt = EVALUATION_PROMPT.format(
        question=question,
        answer=answer
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

        print("Evaluation JSON Parsing Error:", e)

        parsed_response = {
            "score": 5,
            "strengths": [],
            "weak_areas": [],
            "followup_needed": False,
            "feedback": "Evaluation failed."
        }

    return parsed_response