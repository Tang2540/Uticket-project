<<<<<<< HEAD
from fastapi import FastAPI
from app.routers import users, venue  # Use the correct import path for the routers
from app.db.db import create_db_and_tables  # Ensure correct import for create_db_and_tables
=======
from fastapi import FastAPI,  Depends, HTTPException
from .routers import users, venue, utility, booking
from app.db.db import create_db_and_tables, engine
>>>>>>> beb9e35df92e2fae1c45f7bb13d1bf83c3ef66ee

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    create_db_and_tables()

# Include routers
app.include_router(users.router)
app.include_router(venue.router)
<<<<<<< HEAD
=======
app.include_router(utility.router)
app.include_router(booking.router)
>>>>>>> beb9e35df92e2fae1c45f7bb13d1bf83c3ef66ee

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

    