from app.db.database import Base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid

class User(Base):
    __tablename__ = "users"
    
    uuid = Column(UUID(as_uuid=True), unique=True, primary_key=True, default=uuid.uuid4)
    username = Column(String, unique=True)
    password = Column(String)
    created_at = Column(DateTime)