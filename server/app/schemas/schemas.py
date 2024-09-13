from pydantic import BaseModel
from typing import List, Optional, Union

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    
class UserSignIn(BaseModel):
    username: str
    password: str

class UserRead(BaseModel):
    id: int
    username: str
    email: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class Events(BaseModel):
    eventid: int
    eventname: str
    venue: str
    eventdate: str
    available_tickets: int

class Payment(BaseModel):
    paymentid: int
    status: str
    PaymentMethod: str

class Seats(BaseModel):
    seatsid: int
    seatsposition: str
    zone: str
    price: float

class Ticket(BaseModel):
    name: str
    description: Optional[str] = ''
    price: float
    tax: Optional[float] = 0
    tags: List[str] = []
    pic: str

class VenueCreate(BaseModel):
    name: str
    capacity: int

class Organizer(BaseModel):
    id: int
    name: str
    email: str

class Booking(BaseModel):
    bookingid: int
    userid: int
    eventid: int
    seatid: str
    zone: str
    paymentid: int
    amount: int
    price: float
    tax: Optional[float] = 0