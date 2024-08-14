from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from . import models, schemas, utils_sec


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(
    db: Session, 
    username: str
):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(
        db: Session, 
        skip: int = 0, 
        limit: int = 10
):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = utils_sec.get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    try:
        user = db.query(models.User).filter(models.User.id == user_id).one()
        db.delete(user)
        db.commit()
        return{"detail": "User successfully deleted"}
    except NoResultFound:
        db.rollback()
        return {"detail": "User not found"}



def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def get_one_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.model_dump(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_items_by_owner_id(
        db: Session, 
        owner_id: int
):
    return db.query(models.Item).filter(models.Item.owner_id == owner_id)

def get_comments_by_item_id(
        db: Session,
        item_id: int
):
    return db.query(models.Comment).filter(models.Comment.item_id == item_id)

def post_comment_on_blog(
        db: Session,
        item_id: int,
        commenter_username: str,
        comment: schemas.CommentCreate
):
    db_comment = models.Comment(**comment.model_dump(), commenter_username=commenter_username, item_id=item_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment