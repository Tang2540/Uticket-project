from sqlmodel import SQLModel, Field
from typing import Optional
        
class  Booking(SQLModel, table=True):
    booking_id: Optional[int] = Field(default=None,primary_key=True)
    user_id: Optional[int] = Field(default=None,foreign_key="user.id")
    event_id: Optional[int] = Field(default=None,foreign_key="event.id")
    seat_id: Optional[int] = Field(default=None,foreign_key="seat.id")
    payment_id: Optional[int] = Field(default=None,foreign_key="payment.id")
    price: float
    tax: Optional[float] = 0
    