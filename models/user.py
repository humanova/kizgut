from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.types import Text

from db.session import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    category = Column(String)
    notes = Column(Text)
    is_active = Column(Boolean, default=True)
    created_date = Column(DateTime)
    modified_date = Column(DateTime)

    reasons = relationship("Reason", back_populates="user")



    