from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from .database import Base
# 创建基本的数据库模型

class Books(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    book_name = Column(String, index=True)
    price = Column(Integer)


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    password = Column(String)
    email = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    is_staff = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    is_manager = Column(Boolean, default=False)
    is_user = Column(Boolean, default=True)
    is_guest = Column(Boolean, default=False)
    is_anonymous = Column(Boolean, default=False)
    is_authenticated = Column(Boolean, default=False)

class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    modified_date = Column(DateTime)
