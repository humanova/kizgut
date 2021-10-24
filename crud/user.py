from typing import List

from sqlalchemy.orm import Session, load_only

from crud.base import CRUDBase
from models.user import User
from schemas.user import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    async def get_by_username(self, db: Session, username: str) -> User:
        return db.query(self.model).filter(self.model.username == username).first()
    
    async def get_all_users(self, db: Session, fields: List[str] = []) -> User:
        fields = fields if fields else ['id', 'username', 'category']
        return db.query(self.model).options(load_only(*fields)).all()

user = CRUDUser(User)