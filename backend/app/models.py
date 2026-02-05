from sqlalchemy import Column, String, Text, Enum, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from .database import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    conversation_id = Column(UUID(as_uuid=True))
    sender_role = Column(Enum("doctor", "patient", name="role"))
    original_text = Column(Text)
    translated_text = Column(Text)
    audio_url = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
