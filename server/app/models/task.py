from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from datetime import datetime
import enum

class TaskStatus(str, enum.Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class TaskPriority(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Task(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(1000))
    status = Column(SQLEnum(TaskStatus), default=TaskStatus.TODO)
    priority = Column(SQLEnum(TaskPriority), default=TaskPriority.MEDIUM)
    due_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 外键关系
    user_id = Column(Integer, ForeignKey("user.id"))
    
    # 关系
    user = relationship("User", back_populates="tasks")
    focus_sessions = relationship("FocusSession", back_populates="task")
