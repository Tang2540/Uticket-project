from sqlmodel import Relationship, SQLModel, Field
from typing import Optional, List

from server.app.models.booking import Booking

class Ticket(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = Field(default='')
    price: float
    tax: Optional[float] = Field(default=0.0)
    tags: List[str] = Field(default=[])
    pic: str
    bookings: List["Booking"] = Relationship(back_populates="ticket")