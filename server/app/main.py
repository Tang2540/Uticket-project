from fastapi import FastAPI,  Depends, HTTPException
from .routers import user, venue, booking, zone, seat, payment, event, ezp
from app.db import create_db_and_tables, engine

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    create_db_and_tables()

# Include routers
app.include_router(user.router)
app.include_router(venue.router)
app.include_router(booking.router)
app.include_router(zone.router)
app.include_router(seat.router)
app.include_router(payment.router)
app.include_router(event.router)
app.include_router(ezp.router)

@app.get("/")
async def root():
    return {"message": "UTicket"}

    