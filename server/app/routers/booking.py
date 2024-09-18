from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from ..db.db import get_session
from ..schemas.schemas import BookingCreate
from ..models import Payment, Booking, Event

router = APIRouter(prefix="/booking",
    tags=["booking"])

new_bookings = []

# GET a booking by ID
@router.get("/{booking_id}", response_model=Booking)
def get_booking_by_id(booking_id: int, session: Session = Depends(get_session)):
    booking = session.get(Booking, booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

# GET all bookings
@router.get("/", response_model=List[Booking])
def get_all_bookings(session: Session = Depends(get_session)):
    bookings = session.exec(select(Booking)).all()
    if not bookings:
        raise HTTPException(status_code=404, detail="No bookings found")
    return bookings

@router.post("/",response_model=List[Booking])
def create_booking(data:BookingCreate, session: Session = Depends(get_session)):
    event = session.get(Event, data.event_id)
    if data.payment_method_id == 2 or data.payment_method_id == 3:
        new_payment = Payment(status="Paid",payment_method_id=data.payment_method_id)
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
        
