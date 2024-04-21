from typing import Union
from pydantic import BaseModel


class BooksBase(BaseModel):
    book_name: str
    price: float


class Books(BooksBase):
    id: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    username: str
    password: str
    email: str


class LoginUser(BaseModel):
    username: str
    password: str


class User(UserBase):
    id: int
    is_active: bool
    is_superuser: bool
    is_staff: bool
    is_admin: bool
    is_manager: bool
    is_user: bool
    is_guest: bool
    is_anonymous: bool
    is_authenticated: bool

    class Config:
        from_attributes = True


class Post(BaseModel):
    title: str
    content: str
    submit_date: Union[str, None] = None