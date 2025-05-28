from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, proposals, uploads, feedback, generate

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router, prefix="/auth")
app.include_router(proposals.router, prefix="/proposals")
app.include_router(uploads.router, prefix="/uploads")
app.include_router(feedback.router, prefix="/feedback")
app.include_router(generate.router, prefix="/generate")

@app.get("/")
def root():
    return {"message": "Grant App Backend is Running"}
