import json

from utils.groq_client import llm
from utils.prompts import QUESTION_GENERATOR_PROMPT


def generate_question(
    candidate_profile: dict,
    topic: str,
    previous_questions: list
):

    prompt = QUESTION_GENERATOR_PROMPT.format(
        candidate_profile=json.dumps(
            candidate_profile,
            indent=2
        ),
        topic=topic,
        previous_questions=previous_questions
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

        print("Question JSON Parsing Error:", e)

        parsed_response = {
            "question": "Tell me about one of your recent projects."
        }

    return parsed_response