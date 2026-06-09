from sqlalchemy import Column, String, Boolean, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base
import uuid


class API_Key(Base):
    __tablename__ = "api-key"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_uuid = Column(UUID(as_uuid=True), ForeignKey("users.uuid"), nullable=False)
    api_key = Column(String(), unique=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime)