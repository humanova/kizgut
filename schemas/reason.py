from typing import Dict, Optional

from pydantic import BaseModel


class ReasonBase(BaseModel):
    description: str
    evidence: Optional[str] = None

class Reason(ReasonBase):
    id: int
    user_id: int
    
    class Config:
        orm_mode = True

class ReasonCreate(ReasonBase):
    user_id: Optional[int] = None
    pass

class ReasonUpdate(ReasonBase):
    user_id: Optional[int] = None
    pass