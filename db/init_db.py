from sqlalchemy.orm import Session
from models.user import User
from models.reason import Reason

#from db import Base  # noqa: F401
from db.session import engine, Base


# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db() -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    Base.metadata.create_all(bind=engine)
    #User.Base.metadata.create_all(bind=engine)
    #Reason.Base.metadata.create_all(bind=engine)