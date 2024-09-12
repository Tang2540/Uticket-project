from fastapi import FastAPI
from .routers import users
from app.db.db import create_db_and_tables, engine
from app.models.user import User

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    create_db_and_tables()

app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}