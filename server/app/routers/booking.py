from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from itertools import groupby
from ..security import get_current_user
from ..db import get_session
from ..basemodels import BookingCreate, BookingRead
from ..models import Payment, Booking, Event, Event_Zone_Price as EZP, Zone, User, Seat

router = APIRouter(prefix="/booking",
    tags=["booking"])

#get all bookings of a user by ID
@router.get("", response_model=List[BookingRead])
async def get_booking(session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    #ถ้าไม่ได้ Login จะ Error
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not logged in",
            headers={"WWW-Authenticate": "Bearer"},
        )
    statement = (
        select(Event.eventname,Payment.id, Seat.seat_position, Booking.price, Payment.status)
        .join(Event, Event.id == Booking.event_id)
        .join(Seat, Seat.id == Booking.seat_id)
        .join(Payment, Payment.id == Booking.payment_id)
        .where(Booking.user_id == user.id)  # Add this line to sort results by eventname
    )
    results = session.exec(statement)
    
    bookings = []
    for eventname, group in groupby(results, key=lambda x: x[0]):
        payments = [
            {
                "payment_id": id,
                "seat_position": seat_position,
                "price": price,
                "status": status
            }
            for _, id,seat_position, price, status in group
        ]
        bookings.append({
            "eventname": eventname,
            "payments": payments
        })
    
    return bookings

#create booking
@router.post("")
async def create_booking(data:BookingCreate, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not logged in",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    new_payment_price = 0
    
    for i in data.seat_id:
        seat = session.get(Seat, i)
        zone = session.get(Zone,seat.zone_id)
        statement = select(EZP.price).where(
            (EZP.zone_id==zone.id)&
            (EZP.event_id==data.event_id)
        )
        get_price = session.exec(statement).first()
        new_payment_price += get_price
    
    #ถ้า method_id เท่ากับ 2 หรือ 3 ในตาราง Payment ตรง status จะเปลี่ยนเป็น Paid ทันทีเพราะจ่ายผ่านบัตร
    if data.payment_method_id == 2 or data.payment_method_id == 3:
        new_payment = Payment(status="Paid",payment_method_id=data.payment_method_id,amount=float(new_payment_price))
    #ตรงนี้คือจ่ายผ่านการโอน มันก็จะขึ้น Pending ตรง status
    else:
        new_payment = Payment(payment_method_id=data.payment_method_id,amount=float(new_payment_price))
    session.add(new_payment)
    session.commit()

    event = session.get(Event, data.event_id)
    
    for i in data.seat_id:
        seat = session.get(Seat,i)
        zone = session.get(Zone,seat.zone_id)
        statement = select(EZP.price).where(
            (EZP.zone_id==zone.id)&
            (EZP.event_id==data.event_id)
        )
        booking_price = session.exec(statement).first()
        #ถ้าที่นั่งไม่ว่างจะขึ้น Error
        if seat.is_vacant == "reserved":
            raise HTTPException(
                status_code=404, detail="Seat taken"
            )
        else:
            new_booking = Booking(user_id=user.id,event_id=data.event_id,seat_id=i,payment_id=new_payment.id,price=booking_price,tax=data.tax)
            seat.is_vacant = "reserved"
            event.available_tickets -= 1
            session.add(new_booking)
            session.commit()
            session.refresh(new_booking)
    return "Booking completed"
        
