import json

from utils.groq_client import llm
from utils.prompts import REPORT_PROMPT


def generate_final_report(
    evaluation_data: list
):

    prompt = REPORT_PROMPT.format(
        evaluation_data=json.dumps(
            evaluation_data,
            indent=2
        )
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

        print("Report JSON Parsing Error:", e)

        parsed_response = {
            "overall_score": 5,
            "strengths": [],
            "weak_areas": [],
            "recommendations": [],
            "final_feedback":
            "Could not generate report."
        }

    return parsed_response