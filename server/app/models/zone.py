from sqlmodel import SQLModel, Field
from typing import Optional

class Zone(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    zone_name:str
    venue_id: Optional[int] = Field(default=None, foreign_key="venue.id")