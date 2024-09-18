from sqlmodel import SQLModel, Field, Relationship
from typing import Optional 

class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    eventname:str
    eventdate: str
    available_tickets: int
    venue_id: Optional[int] = Field(default=None, foreign_key="venue.id")
    
    
    
