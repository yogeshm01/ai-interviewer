from fastapi import APIRouter

from api.upload_routes import resume_store

from agents.resume_agent import analyze_resume
from agents.planner_agent import create_interview_plan
from agents.question_agent import generate_question
from agents.evaluation_agent import evaluate_answer
from agents.followup_agent import generate_followup_question
from agents.report_agent import generate_final_report

router = APIRouter()

# Temporary in-memory interview sessions
interview_sessions = {}


@router.get("/analyze-resume/{resume_id}")
def analyze_resume_route(resume_id: str):

    if resume_id not in resume_store:
        return {
            "error": "Resume not found"
        }

    resume_text = resume_store[resume_id]["resume_text"]

    analysis = analyze_resume(resume_text)

    return analysis


@router.get("/create-interview-plan/{resume_id}")
def create_interview_plan_route(resume_id: str):

    if resume_id not in resume_store:
        return {
            "error": "Resume not found"
        }

    resume_text = resume_store[resume_id]["resume_text"]

    candidate_profile = analyze_resume(resume_text)

    interview_plan = create_interview_plan(
        candidate_profile
    )

    return interview_plan


@router.get("/start-interview/{resume_id}")
def start_interview(resume_id: str):

    if resume_id not in resume_store:
        return {
            "error": "Resume not found"
        }

    resume_text = resume_store[resume_id]["resume_text"]

    # Analyze candidate
    candidate_profile = analyze_resume(
        resume_text
    )

    # Create plan
    plan_response = create_interview_plan(
        candidate_profile
    )

    interview_plan = plan_response.get(
        "interview_plan",
        []
    )

    # Initialize session
    interview_sessions[resume_id] = {
        "candidate_profile": candidate_profile,
        "interview_plan": interview_plan,
        "current_topic_index": 0,
        "question_history": [],
        "evaluations": [],
        "followup_count": 0
    }

    # Generate first question
    first_topic = interview_plan[0]

    question_response = generate_question(
        candidate_profile=candidate_profile,
        topic=first_topic,
        previous_questions=[]
    )

    first_question = question_response.get(
        "question"
    )

    # Store question
    interview_sessions[resume_id][
        "question_history"
    ].append(first_question)

    return {
        "topic": first_topic,
        "question": first_question
    }


@router.post("/submit-answer/{resume_id}")
def submit_answer(
    resume_id: str,
    payload: dict
):

    if resume_id not in interview_sessions:
        return {
            "error": "Interview session not found"
        }

    user_answer = payload.get("answer")

    session = interview_sessions[resume_id]

    previous_question = session[
        "question_history"
    ][-1]

    # Evaluate answer
    evaluation = evaluate_answer(
        question=previous_question,
        answer=user_answer
    )

    # Save evaluation
    session["evaluations"].append(
        evaluation
    )

    score = evaluation.get("score", 0)

    weak_areas = evaluation.get(
        "weak_areas",
        []
    )

    followup_needed = evaluation.get(
        "followup_needed",
        False
    )

    # Generate follow-up if needed
    # Maximum 2 follow-ups per topic
    if followup_needed and session["followup_count"] < 2:

        followup_response = generate_followup_question(
            question=previous_question,
            answer=user_answer,
            weak_areas=weak_areas
        )

        next_question = followup_response.get(
            "followup_question"
        )

        session["followup_count"] += 1

    else:

        # Reset followup counter
        session["followup_count"] = 0

        # Move to next topic
        session["current_topic_index"] += 1

        topic_index = session[
            "current_topic_index"
        ]

        interview_plan = session[
            "interview_plan"
        ]

        # Interview completed
        if topic_index >= len(interview_plan):

            final_report = generate_final_report(
                session["evaluations"]
            )

            return {
                "message": "Interview completed",
                "final_report": final_report
            }

        next_topic = interview_plan[
            topic_index
        ]

        question_response = generate_question(
            candidate_profile=session[
                "candidate_profile"
            ],
            topic=next_topic,
            previous_questions=session[
                "question_history"
            ]
        )

        next_question = question_response.get(
            "question"
        )

    # Save history
    session["question_history"].append(
        next_question
    )

    return {
        "evaluation": evaluation,
        "next_question": next_question
    }