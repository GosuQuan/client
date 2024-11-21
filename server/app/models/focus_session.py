from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from datetime import datetime

class FocusSession(Base):
    __tablename__ = "focus_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=True)
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime, nullable=True)
    duration = Column(Integer, default=0)  # 持续时间（分钟）
    completed = Column(Boolean, default=False)
    notes = Column(String, nullable=True)

    # 关系
    user = relationship("User", back_populates="focus_sessions")
    task = relationship("Task", back_populates="focus_sessions")
