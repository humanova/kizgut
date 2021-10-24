from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.reason import Reason
from schemas.reason import ReasonCreate, ReasonUpdate


class CRUDReason(CRUDBase[Reason, ReasonCreate, ReasonUpdate]):
    pass


reason = CRUDReason(Reason)