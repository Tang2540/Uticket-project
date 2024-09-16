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