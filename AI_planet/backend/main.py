from fastapi import FastAPI, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .database import SessionLocal, engine, Document
from .models import DocumentCreate
from .pdf_processor import extract_text_from_pdf
import os
from datetime import datetime

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF files are allowed.")
    
    file_location = f"pdfs/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    
    text_content = extract_text_from_pdf(file_location)
    
    db = SessionLocal()
    db_document = Document(filename=file.filename, upload_date=datetime.now())
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    db.close()
    
    return {"filename": file.filename, "text_content": text_content}

@app.post("/ask/")
async def ask_question(question: str, document_id: int):
    # Here you would integrate LangChain or LlamaIndex to process the question
    # For simplicity, we will return a placeholder response
    return {"answer": "This is a placeholder answer based on the document."}