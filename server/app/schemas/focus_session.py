from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class FocusSessionBase(BaseModel):
    task_id: Optional[int] = None
    notes: Optional[str] = None

class FocusSessionCreate(FocusSessionBase):
    pass

class FocusSessionUpdate(FocusSessionBase):
    end_time: Optional[datetime] = None

class FocusSession(FocusSessionBase):
    id: int
    user_id: int
    start_time: datetime
    end_time: Optional[datetime] = None
    duration: Optional[float] = None

    class Config:
        from_attributes = True
