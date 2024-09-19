from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List
from ..db.db import get_session
from ..schemas.schemas import BookingCreate
from ..models import Payment, Booking, Event

router = APIRouter(prefix="/booking",
    tags=["booking"])

new_bookings = []

@router.post("/",response_model=List[Booking])
def create_booking(data:BookingCreate, session: Session = Depends(get_session)):
    event = session.get(Event, data.event_id)
    if data.payment_method_id == 2 or data.payment_method_id == 3:
        new_payment = Payment(status="Paid",payment_method_id=data.payment_method_id,amount=float(data.price*len(data.seat_id)))
    else:
        new_payment = Payment(payment_method_id=data.payment_method_id)
    session.add(new_payment)
    session.commit()
    for i in data.seat_id:
        new_booking = Booking(user_id=data.user_id,event_id=data.event_id,seat_id=i,payment_id=new_payment.id,price=data.price,tax=data.tax,is_vacant=False)
        new_bookings.append(new_booking)
        event.available_tickets -= 1
        session.add(new_booking)
        session.commit()
        session.refresh(new_booking)
    return new_bookings
        
