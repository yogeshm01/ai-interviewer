import os
# Fix for macOS grpc/fork issues when using AI libraries (e.g. sentence-transformers)
# This prevents the [mutex.cc : 452] RAW: Lock blocking error
os.environ["GRPC_ENABLE_FORK_SUPPORT"] = "0"
os.environ["OBJC_DISABLE_INITIALIZE_FORK_SAFETY"] = "YES"

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.interview_routes import router as interview_router

from utils.groq_client import llm
from api.upload_routes import router as upload_router

app = FastAPI(
    title="AI Interview Copilot",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(upload_router)
app.include_router(interview_router)

@app.get("/")
def home():
    return {
        "message": "AI Interview Copilot Backend Running"
    }

@app.get("/test-llm")
def test_llm():

    response = llm.invoke(
        "Say hello in one line."
    )

    return {
        "response": response.content
    }