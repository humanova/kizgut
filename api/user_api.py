from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

import crud, schemas
from api import deps

router = APIRouter()


# create user data
@router.post("/api/user", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(deps.get_db)):
    try:
        user_db = await crud.user.create(db=db, obj_in=user)
    except IntegrityError:
        raise HTTPException(status_code=422, detail="User is already added.")
    except Exception as e:
        print(e.__traceback__)
        print(e)
        raise HTTPException(status_code=503, detail="Couldn't add new user.")

    return user_db

# read user data
@router.get("/api/user", response_model=schemas.User)
async def read_user(username: str, db: Session= Depends(deps.get_db)):
    user_db = await crud.user.get_by_username(db=db, username=username)
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    return user_db

# get all users
@router.get("/api/users")
async def read_users(db: Session= Depends(deps.get_db)):
    users_db = await crud.user.get_all_users(db=db, fields=['username', 'category'])
    if not users_db:
        raise HTTPException(status_code=404, detail="Couldn't retrieve users")
    return users_db

# update user data
@router.put("/api/user", response_model=schemas.User)
async def update_user(user: schemas.UserUpdate, db: Session=Depends(deps.get_db)):
    user_db = await crud.user.get_by_username(db=db, username=user.username)
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    user_db = await crud.user.update(db=db, db_obj=user_db, obj_in=user)
    return user_db

# delete (deactivate) user data
@router.delete("/api/user", response_model=schemas.User)
async def delete_user(username: str, db: Session = Depends(deps.get_db)):
    user_db = await crud.user.get_by_username(db=db, username=username)
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    user = schemas.UserUpdate(username=username, is_active=False)
    user_db = await crud.user.update(db=db, db_obj=user_db, obj_in=user)
    return user_db
    