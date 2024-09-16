from sqlmodel import SQLModel, Field

class Venue(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    capacity: int




