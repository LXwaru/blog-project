from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from pydantic import BaseModel

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")
    comments = relationship("Comment", back_populates="commenter")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
    comments = relationship("Comment", back_populates="item")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    content = Column(String, index=True)
    commenter_id = Column(Integer, ForeignKey("users.id"))
    item_id = Column(Integer, ForeignKey("items.id"))

    commenter = relationship("User", back_populates="comments")
    item = relationship("Item", back_populates="comments")


class HttpError(BaseModel):
    detail: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None