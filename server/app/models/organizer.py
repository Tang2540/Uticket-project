from sqlmodel import SQLModel, Field
from typing import Optional, List

class Organizer(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    email: str