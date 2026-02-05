from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Message
from app.ai import generate_summary

router = APIRouter()

@router.post("/summary/{conversation_id}")
def summary(conversation_id: str, db: Session = Depends(SessionLocal)):
    messages = db.query(Message).filter(
        Message.conversation_id == conversation_id
    ).all()

    full_text = "\n".join([m.original_text for m in messages])
    summary = generate_summary(full_text)

    return {"summary": summary}
