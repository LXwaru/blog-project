from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from . import schemas, crud, utils_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/api/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, 
    item: schemas.ItemCreate, 
    db: Session = Depends(utils_db.get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@router.get("/api/users/{user_id}/items/", response_model=list[schemas.Item])
def read_items_by_owner_id(
    owner_id: int,
    db: Session = Depends(utils_db.get_db)
):
    items = crud.get_items_by_owner_id(db=db, owner_id=owner_id)
    return items

@router.get("/api/items/", response_model=list[schemas.Item])
def read_items(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(utils_db.get_db)
):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
