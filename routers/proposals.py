from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

router = APIRouter()

# Simulated DB
proposals = []

class Proposal(BaseModel):
    participant_code: str
    org_name: str
    business_name: str
    contact_info: str
    alt_contact: Optional[str] = None
    title: str
    description: str
    intervention: str
    partners: Optional[str] = None
    activities: list[str]
    kpis: list[str]
    impact: str
    timeline: list[str]
    funds_requested: float
    team: list[str]
    challenges: Optional[str] = None

@router.post("/")
def submit_proposal(proposal: Proposal):
    now = datetime.now().isoformat()
    proposals.append({"data": proposal.dict(), "submitted_on": now, "status": "pending", "version": "v.01"})
    return {"message": "Proposal submitted", "submitted_on": now}

@router.get("/")
def list_proposals():
    return proposals