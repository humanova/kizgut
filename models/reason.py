from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.types import Text

from db.session import Base


class Reason(Base):
    __tablename__ = "reasons"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(Text, index=True)
    evidence = Column(Text, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_date = Column(DateTime)
    modified_date = Column(DateTime)

    user = relationship("User", back_populates="reasons")
    