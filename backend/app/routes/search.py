from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Message

router = APIRouter()

@router.get("/search")
def search(q: str, db: Session = Depends(SessionLocal)):
    results = db.query(Message).filter(
        Message.original_text.ilike(f"%{q}%")
    ).all()
    return results
