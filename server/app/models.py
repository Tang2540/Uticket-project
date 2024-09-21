from sqlmodel import SQLModel, Field
from typing import Optional, List
        
class  Booking(SQLModel, table=True):
    booking_id: Optional[int] = Field(default=None,primary_key=True)
    user_id: Optional[int] = Field(default=None,foreign_key="user.id")
    event_id: Optional[int] = Field(default=None,foreign_key="event.id")
    seat_id: Optional[int] = Field(default=None,foreign_key="seat.id")
    payment_id: Optional[int] = Field(default=None,foreign_key="payment.id")
    price: float
    tax: Optional[float] = Field(default=0)
    
class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    eventname:str
    eventdate: str
    available_tickets: int
    venue_id: Optional[int] = Field(default=None, foreign_key="venue.id")
    description: Optional[str] = Field(default='No Description')
    pic: str
    organizer_id: int = Field(default=None, foreign_key="organizer.id")
    
class Tag(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tag_name: str
    
class Event_Tag(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tag_id: int = Field(default=None, foreign_key="tag.id")
    event_id: int = Field(default=None, foreign_key="event.id")
    
class Event_Zone_Price(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    event_id: Optional[int] = Field(default=None,foreign_key="event.id")
    zone_id: Optional[int] = Field(default=None,foreign_key="zone.id")
    price: float
    
class Organizer(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    email: str
    
class Payment_Method(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    method: str
    
class Payment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    status: str = Field(default="pending")
    payment_method_id: Optional[int] = Field(default=None, foreign_key="payment_method.id")
    amount: float

class Seat(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    seat_position: Optional[str]
    is_vacant: Optional[str] = Field(default="vacant")
    zone_id: Optional[int] = Field(default=None, foreign_key="zone.id")
    
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str
    
class Venue(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name:str
    capacity:int
    
class Zone(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    zone_name:str
    venue_id: Optional[int] = Field(default=None, foreign_key="venue.id")