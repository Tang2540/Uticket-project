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
    pic:str
    organizer_id:int
    
class PaymentCreate(BaseModel):
    payment_method_id: int
    
class PaymentMethodCreate(BaseModel):
    method: str
    
class SeatCreate(BaseModel):
    seat_position:str
    zone_id:int
    
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

class OrganizerCreate(BaseModel):
    name: str
    email: str
    
class BookingCreate(BaseModel):
    event_id: int
    seat_id: List[int]
    payment_method_id: int
    tax: Optional[float] = 0
    
class Seats(BaseModel):
    seat_id:int
    seat_position: str
    price:float
    
class SeatRead(BaseModel):
    zone_name:str
    seats: List[Seats]
    
class Payments(BaseModel):
    seat_position: str
    price: float
    status: str
    
class BookingRead(BaseModel):
    eventname:str
    payments: List[Payments]
    
class PaymentIn(BaseModel):
    payment_id: int
    