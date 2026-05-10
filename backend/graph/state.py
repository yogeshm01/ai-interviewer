from typing import TypedDict, List, Dict
class InterviewState(TypedDict):
    resume_text: str
    role: str
    experience_level: str
    skills: List[str]
    projects: List[str]
    strengths: List[str]
    current_question: str
    question_history: List[str]
    answers: List[str]
    scores: List[float]
    weak_areas: List[str]
    final_report: Dict