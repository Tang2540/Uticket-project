from sqlmodel import Relationship, SQLModel, Field
from typing import Optional, List

from server.app.models.booking import Booking

class Payment(SQLModel, table=True):
    paymentid: int = Field(default=None, primary_key=True)
    status: str
    PaymentMethod: str
    bookings: List[Booking] = Relationship(back_populates="payment")
