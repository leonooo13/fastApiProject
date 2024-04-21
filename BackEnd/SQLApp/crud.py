import hashlib

from sqlalchemy.orm import Session

from . import schemas
from . import models


def create_book(db: Session, book: schemas.BooksBase):
    db_book = models.Books(book_name=book.book_name, price=book.price)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def show_books(db: Session):
    return db.query(models.Books).all()


def register(db: Session, user: schemas.UserBase):
    user.password = hashlib.md5(user.password.encode("utf-8")).hexdigest()
    db_user = models.User(username=user.username, password=user.password, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def is_user_exist(db: Session, user: schemas.LoginUser):
    # 判断用户名和密码是否正确
    user_obj = db.query(models.User).filter(models.User.username == user.username,
                                            models.User.password == user.password).first()
    return user_obj is not None


def is_user_name_in_table_user(db: Session, username: str) -> bool:
    user_obj = db.query(models.User).filter(models.User.username == username).first()
    return user_obj is not None


def get_posts_titles(db: Session):
    date = ""
    data = db.query(models.Post.id, models.Post.title, models.Post.modified_date).all()
    res_list = []
    for item in data:
        if item[2]:
            date = item[2].strftime("%Y-%m-%d")
        res_list.append({"id": item[0], "title": item[1], "date": date})
    return res_list


def get_post(db: Session, post_id: int):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    return post

def create_post(db: Session, post: schemas.Post):
    db_post = models.Post(title=post.title, content=post.content, modified_date=post.submit_date)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

