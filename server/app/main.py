from fastapi import FastAPI,  Depends, HTTPException
from .routers import users, venue, utility, booking
from app.db.db import create_db_and_tables, engine

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    create_db_and_tables()

app.include_router(users.router)
app.include_router(venue.router)
app.include_router(utility.router)
app.include_router(booking.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}