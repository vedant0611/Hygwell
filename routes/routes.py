from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from pydantic import BaseModel
import uuid
from database import get_db
from models import Content
from utils.utils import scrape_url, extract_pdf_text, simple_search

router = APIRouter()

class URLInput(BaseModel):
    url: str

class ChatInput(BaseModel):
    question: str
    chat_id: str

@router.post("/process_url")
async def process_url(url_input: URLInput, db: Session = Depends(get_db)):
    try:
        content = scrape_url(url_input.url)
        chat_id = str(uuid.uuid4())
        db_content = Content(chat_id=chat_id, content=content, content_type='url')
        db.add(db_content)
        db.commit()
        return {"chat_id": chat_id, "message": "URL content processed and stored successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/process_pdf")
async def process_pdf(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        content = await extract_pdf_text(file)
        chat_id = str(uuid.uuid4())
        db_content = Content(chat_id=chat_id, content=content, content_type='pdf')
        db.add(db_content)
        db.commit()
        return {"chat_id": chat_id, "message": "PDF content processed and stored successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/chat")
async def chat(chat_input: ChatInput, db: Session = Depends(get_db)):
    content = db.query(Content).filter(Content.chat_id == chat_input.chat_id).first()
    if not content:
        raise HTTPException(status_code=404, detail="Chat ID not found")
    
    response = simple_search(chat_input.question, content.content)
    return {"response": response}