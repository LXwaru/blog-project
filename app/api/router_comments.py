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


@router.post("/api/{item_id}/{commenter_username}/comment/", response_model=schemas.Comment)
def post_comment(
    item_id: int,
    commenter_username: str,
    comment: schemas.CommentCreate,
    db: Session = Depends(utils_db.get_db)
):
    return crud.post_comment_on_blog(
    db, 
    item_id=item_id, 
    commenter_username=commenter_username,
    comment=comment)

@router.get("/api/{item_id}/comments/", response_model=list[schemas.Comment])
def list_comments_by_item_id(
    item_id: int,
    db: Session = Depends(utils_db.get_db)
):
    return crud.get_comments_by_item_id(db=db, item_id=item_id)