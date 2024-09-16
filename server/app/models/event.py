<<<<<<< HEAD
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
=======
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional 

class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    eventname:str
    eventdate: str
    available_tickets: int
    venue_id: Optional[int] = Field(default=None, foreign_key="venue.id")
    
    
    
>>>>>>> beb9e35df92e2fae1c45f7bb13d1bf83c3ef66ee
