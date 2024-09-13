import os
from fastapi import UploadFile
from app.config import UPLOAD_DIR

def save_upload_file(upload_file: UploadFile, title: str) -> str:
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_extension = os.path.splitext(upload_file.filename)[1]
    file_name = f"{title.replace(' ', '_')}{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, file_name)

    with open(file_path, "wb") as buffer:
        buffer.write(upload_file.file.read())

    return file_path