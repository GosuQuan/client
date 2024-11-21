from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from datetime import datetime

class FocusSession(Base):
    id = Column(Integer, primary_key=True, index=True)
    start_time = Column(DateTime, nullable=False, default=datetime.utcnow)
    end_time = Column(DateTime, nullable=True)
    duration = Column(Float, nullable=True)  # 持续时间（分钟）
    notes = Column(String(1000), nullable=True)
    
    # 外键关系
    user_id = Column(Integer, ForeignKey("user.id"))
    task_id = Column(Integer, ForeignKey("task.id"), nullable=True)
    
    # 关系
    user = relationship("User", back_populates="focus_sessions")
    task = relationship("Task", back_populates="focus_sessions")
