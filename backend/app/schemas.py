from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID


# ---------- Translation ----------

class TranslateRequest(BaseModel):
    conversation_id: UUID
    sender_role: str   # "doctor" or "patient"
    text: str
    to_lang: str


class TranslateResponse(BaseModel):
    translated_text: str


# ---------- Messages ----------

class MessageResponse(BaseModel):
    id: UUID
    conversation_id: UUID
    sender_role: str
    original_text: str
    translated_text: str
    audio_url: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True


# ---------- Audio ----------

class AudioTranscriptionResponse(BaseModel):
    text: str
    audio_url: str


# ---------- Summary ----------

class SummaryResponse(BaseModel):
    summary: str


# ---------- Search ----------

class SearchResult(BaseModel):
    id: UUID
    original_text: str
    translated_text: str
    created_at: datetime

    class Config:
        orm_mode = True
