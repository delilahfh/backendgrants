from fastapi import APIRouter, File, UploadFile, Form
from datetime import datetime
import os

router = APIRouter()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/")
def upload_file(file: UploadFile = File(...), category: str = Form(...), user: str = Form(...)):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{user}_{category}_{timestamp}_{file.filename}"
    path = os.path.join(UPLOAD_DIR, filename)
    with open(path, "wb") as buffer:
        buffer.write(file.file.read())
    return {"message": "File uploaded", "file_path": path}
