import datetime
import hashlib
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from SQLApp.database import SessionLocal, engine
from SQLApp import models, schemas, crud

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

# 允许所有源的请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return {"data": "de word"}


@app.post("/create/", response_model=schemas.Books)
def create_book(book: schemas.BooksBase, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)


@app.get("/books/")
def show_books(db: Session = Depends(get_db)):
    ans = crud.show_books(db=db)
    return {"data": ans}


@app.post("/register/")
def register(user: schemas.UserBase, db: Session = Depends(get_db)):
    if crud.is_user_name_in_table_user(db=db, username=user.username):
        return {"data": "user_name already exists"}
    crud.register(db=db, user=user)
    return {"data": "register"}


@app.get("/login/")
async def login():
    return {"data": "login"}


@app.post("/login/")
async def login(user: schemas.LoginUser, db: Session = Depends(get_db)):
    user.password = hashlib.md5(user.password.encode("utf-8")).hexdigest()
    if not crud.is_user_exist(db=db, user=user):
        return {"data": "login failed"}
    return {"data": "success"}


@app.get("/posts/")
async def get_post(db: Session = Depends(get_db)):
    post_title = crud.get_posts_titles(db=db)
    return {"data": post_title}


@app.get('/post/{post_id}')
async def get_post(post_id: int, db: Session = Depends(get_db)):
    post = crud.get_post(db=db, post_id=post_id)
    return {"data": post}

@app.post("/manage/")
async def create_post(post: schemas.Post, db: Session = Depends(get_db)):
    if not post.submit_date:
        post.submit_date = datetime.datetime.utcnow()
    crud.create_post(db=db, post=post)
    return {'code': 200, "data": "create post success"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)