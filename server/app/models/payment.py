from sqlmodel import SQLModel, Field
from typing import Optional

class Payment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    status: str = Field(default="pending")
    payment_method_id: Optional[int] = Field(default=None, foreign_key="payment_method.id")