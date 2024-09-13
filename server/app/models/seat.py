from sqlmodel import SQLModel, Field

class Seat(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    seatid: int
    seatPosition: str
    price: float