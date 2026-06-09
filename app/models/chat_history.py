from db.database import Base
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid


class ChatHistory(Base):
    __tablename__ = "chat-history"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_uuid = Column(UUID(as_uuid=True), ForeignKey("users.uuid"), nullable=False)
    role = Column(String, default="user")
    content = Column(String)
    created_at = Column(DateTime)