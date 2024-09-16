from typing import List
from sqlmodel import Relationship, SQLModel, Field

from server.app.models.booking import Booking
from server.app.models.venue import Venue

class Event(SQLModel, table=True):
    eventid: int = Field(default=None, primary_key=True)
    eventname: str
    venue_id: int = Field(default=None, foreign_key="venue.id")
    eventdate: str
    available_tickets: int
    bookings: List["Booking"] = Relationship(back_populates="event")
    venue: "Venue" = Relationship(back_populates="events")