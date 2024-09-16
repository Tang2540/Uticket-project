# In app/models/booking.py
from sqlmodel import Relationship, SQLModel, Field
from typing import Optional, List

from app.models.payment import Payment
from app.models.seat import Seat
from app.models.user import User
from app.models.event import Event  # Ensure Event is in the correct module


class Booking(SQLModel, table=True):
    bookingid: int = Field(default=None, primary_key=True)
    userid: int = Field(default=None, foreign_key="user.id")
    eventid: int = Field(default=None, foreign_key="event.eventid")
    seatid: int = Field(default=None, foreign_key="seat.seatid")
    paymentid: int = Field(default=None, foreign_key="payment.paymentid")
    amount: int
    price: float = Field(default=None)  # To be updated based on ticket's price
    tax: Optional[float] = Field(default=0.0)
    user: "User" = Relationship(back_populates="bookings")
    event: "Event" = Relationship(back_populates="bookings")
    seat: "Seat" = Relationship(back_populates="bookings")
    payment: "Payment" = Relationship(back_populates="bookings")
