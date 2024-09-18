from sqlmodel import SQLModel, Field
from typing import Optional

class Venue(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name:str
    capacity:int
