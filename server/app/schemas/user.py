from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    email: str
    full_name: Optional[str] = None
    is_active: Optional[bool] = True

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
