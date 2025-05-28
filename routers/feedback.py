from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

# Simulated feedback and document status DBs
feedback_log = []
status_log = {}

class Feedback(BaseModel):
    doc_type: str
    doc_id: int
    reviewer: str
    decision: str  # approved / rejected / needs attention
    comments: str

@router.post("/")
def post_feedback(feedback: Feedback):
    timestamp = datetime.now().isoformat()
    entry = feedback.dict()
    entry["timestamp"] = timestamp
    feedback_log.append(entry)
    status_log[(feedback.doc_type, feedback.doc_id)] = {"status": feedback.decision, "date": timestamp}
    return {"message": "Feedback recorded", "status": feedback.decision, "timestamp": timestamp}

@router.get("/status")
def get_status(doc_type: str, doc_id: int):
    return status_log.get((doc_type, doc_id), {"status": "pending", "date": None})

@router.get("/log")
def get_feedback():
    return feedback_log