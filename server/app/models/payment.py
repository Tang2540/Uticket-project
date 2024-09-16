<<<<<<< HEAD
from sqlmodel import Relationship, SQLModel, Field
from typing import Optional, List

from server.app.models.booking import Booking

class Payment(SQLModel, table=True):
    paymentid: int = Field(default=None, primary_key=True)
    status: str
    PaymentMethod: str
    bookings: List[Booking] = Relationship(back_populates="payment")
=======
from sqlmodel import SQLModel, Field
from typing import Optional

class Payment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    status: str = Field(default="pending")
    payment_method_id: Optional[int] = Field(default=None, foreign_key="payment_method.id")
>>>>>>> beb9e35df92e2fae1c45f7bb13d1bf83c3ef66ee
