from sqlmodel import SQLModel, Field
from typing import Optional

class Seat(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    seatid: int
    seatPosition: Optional[str]
    is_vacant: bool = Field(default=True)
    zone_id: Optional[int] = Field(default=None, foreign_key="zone.id")
        
