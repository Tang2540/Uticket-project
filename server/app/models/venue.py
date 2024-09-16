from sqlmodel import SQLModel, Field
<<<<<<< HEAD

class Venue(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    capacity: int




=======
from typing import Optional

class Venue(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name:str
    capacity:int
>>>>>>> beb9e35df92e2fae1c45f7bb13d1bf83c3ef66ee
