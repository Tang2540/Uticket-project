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
    
class EventCreate(BaseModel):
    eventname: str
    eventdate: str
    available_tickets: int
    venue_id: int

class Payment(BaseModel):
    paymentid: int
    status: str
    PaymentMethod: str
    
class PaymentCreate(BaseModel):
    payment_method_id: int
    
class PaymentMethodCreate(BaseModel):
    method: str

class Seats(BaseModel):
    seatsid: int
    seatsposition: str
    zone: str
    price: float
    
class SeatCreate(BaseModel):
    seatid:int
    seatPosition:str
    zone_id:int

class Ticket(BaseModel):
    name: str
    description: Optional[str] = ''
    price: float
    tax: Optional[float] = 0
    tags: List[str] = []
    pic: str
    
class EZPCreate(BaseModel):
    event_id:int
    zone_id:int
    price:float

class VenueCreate(BaseModel):
    name: str
    capacity: int
    
class ZoneCreate(BaseModel):
    zone_name:str
    venue_id:int

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
    
class BookingCreate(BaseModel):
    user_id: int
    event_id: int
    seat_id: List[int]
    payment_method_id: int
    price: float
    tax: Optional[float] = 0
    