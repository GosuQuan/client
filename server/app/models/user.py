from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from datetime import datetime

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    full_name = Column(String(255))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 关系
    tasks = relationship("Task", back_populates="user")
    focus_sessions = relationship("FocusSession", back_populates="user")
