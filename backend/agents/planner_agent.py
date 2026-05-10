import json

from utils.groq_client import llm
from utils.prompts import INTERVIEW_PLANNER_PROMPT


def create_interview_plan(candidate_profile: dict):

    prompt = INTERVIEW_PLANNER_PROMPT.format(
        candidate_profile=json.dumps(candidate_profile, indent=2)
    )

    response = llm.invoke(prompt)

    content = response.content.strip()

    # Clean markdown wrappers
    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    try:
        parsed_response = json.loads(content)

    except Exception as e:

        print("Planner JSON Parsing Error:", e)

        parsed_response = {
            "interview_plan": [
                "Technical Discussion",
                "Projects",
                "Problem Solving"
            ]
        }

    return parsed_response