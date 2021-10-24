import datetime
from typing import Optional, List

from pydantic import BaseModel

import schemas.reason
from db.session import Base


class UserBase(BaseModel):
    username:str
    category:Optional[str] = None
    notes:Optional[str] = None
    
class User(UserBase):
    id: int
    reasons:Optional[List[schemas.reason.Reason]] = []
    is_active: bool
    created_date: datetime.datetime = None
    modified_date: datetime.datetime = None

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    is_active:Optional[bool] = None
    pass