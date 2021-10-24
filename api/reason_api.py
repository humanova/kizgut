from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

import crud, schemas
from api import deps

router = APIRouter()


# add new reason
@router.post("/api/reason", response_model=schemas.Reason)
async def create_reason(username: str, reason: schemas.ReasonCreate, db: Session = Depends(deps.get_db)):
    user_db = await crud.user.get_by_username(db=db, username=username)
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    reason.user_id = user_db.id
    try:
        reason_db = await crud.reason.create(db=db, obj_in=reason)
    except Exception as e:
        print(e.__traceback__)
        print(e)
        raise HTTPException(status_code=503, detail="Couldn't add new reason.")

    return reason_db

# return reason
@router.get("/api/reason", response_model=schemas.Reason)
async def read_reason(id : int, db: Session = Depends(deps.get_db)):
    reason_db = await crud.reason.get(db=db, id=id)
    if not reason_db:
        raise HTTPException(status_code=404, detail="Reason not found")
    
    return reason_db

# update reason
@router.put("/api/reason", response_model=schemas.Reason)
async def update_reason(id: int, reason: schemas.ReasonUpdate, db: Session = Depends(deps.get_db)):
    reason_db = await crud.reason.get(db=db, id=id)
    if not reason_db:
        raise HTTPException(status_code=404, detail="Reason not found")
    
    reason.user_id = reason_db.user_id
    reason_db = await crud.reason.update(db=db, db_obj=reason_db, obj_in=reason)
    return reason_db

# delete reason
@router.delete("/api/reason", response_model=schemas.Reason)
async def delete_reason(id: int, db: Session = Depends(deps.get_db)):
    reason_db = await crud.reason.get(db=db, id=id)
    if not reason_db:
        raise HTTPException(status_code=404, detail="Reason not found")
    reason_db = await crud.reason.remove(db=db, id=id)
    return reason_db