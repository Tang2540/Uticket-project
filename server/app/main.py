from fastapi import FastAPI
from app.routers import users, venue  # Use the correct import path for the routers
from app.db.db import create_db_and_tables  # Ensure correct import for create_db_and_tables

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    create_db_and_tables()

# Include routers
app.include_router(users.router)
app.include_router(venue.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

    