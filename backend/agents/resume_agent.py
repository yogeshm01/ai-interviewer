import json

from utils.groq_client import llm
from utils.prompts import RESUME_ANALYZER_PROMPT


def analyze_resume(resume_text: str):

    prompt = RESUME_ANALYZER_PROMPT.format(
        resume_text=resume_text
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

        print("JSON Parsing Error:", e)

        parsed_response = {
            "role": "Unknown",
            "experience_level": "Unknown",
            "skills": [],
            "projects": [],
            "strengths": []
        }

    return parsed_response