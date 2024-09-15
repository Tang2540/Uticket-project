from sqlmodel import SQLModel, Field
from typing import Optional

class Event_Zone_Price(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    event_id: Optional[int] = Field(default=None,foreign_key="zone.id")
    zone_id: Optional[int] = Field(default=None,foreign_key="zone.id")
    price: float