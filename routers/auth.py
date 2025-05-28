from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import hashlib

router = APIRouter()

# Simulated DB
users = {}

class User(BaseModel):
    email: str
    password: str
    role: Optional[str] = "beneficiary"

@router.post("/register")
def register(user: User):
    if user.email in users:
        raise HTTPException(status_code=400, detail="User already exists")
    hashed_pw = hashlib.sha256(user.password.encode()).hexdigest()
    users[user.email] = {"password": hashed_pw, "role": user.role}
    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: User):
    if user.email not in users:
        raise HTTPException(status_code=404, detail="User not found")
    hashed_pw = hashlib.sha256(user.password.encode()).hexdigest()
    if users[user.email]["password"] != hashed_pw:
        raise HTTPException(status_code=401, detail="Incorrect password")
    return {"message": "Login successful", "role": users[user.email]["role"]}