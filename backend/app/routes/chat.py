from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Message
from app.ai import translate_text

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/translate")
def translate(payload: dict, db: Session = Depends(get_db)):
    translated = translate_text(
        payload["text"],
        payload["to_lang"]
    )

    msg = Message(
        conversation_id=payload["conversation_id"],
        sender_role=payload["sender_role"],
        original_text=payload["text"],
        translated_text=translated
    )
    db.add(msg)
    db.commit()

    return {"translated_text": translated}
