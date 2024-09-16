<<<<<<< HEAD
from sqlmodel import Relationship, SQLModel, Field
from typing import Optional, List

from server.app.models.ticket import Ticket

class Seat(SQLModel, table=True):
    seatid: int = Field(default=None, primary_key=True)
    seatposition: str
    zone: str
    ticket_id: int = Field(default=None, foreign_key="ticket.id")
    price: float  
    ticket: "Ticket" = Relationship(back_populates="seats")
=======
from sqlmodel import SQLModel, Field
from typing import Optional

class Seat(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    seatid: int
    seatPosition: Optional[str]
    zone_id: Optional[int] = Field(default=None, foreign_key="zone.id")
        
>>>>>>> beb9e35df92e2fae1c45f7bb13d1bf83c3ef66ee
