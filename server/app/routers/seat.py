from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from itertools import groupby
from ..db import get_session
from ..basemodels import SeatCreate, SeatRead
from ..models import Seat, Zone, Event_Zone_Price as EZP

router = APIRouter(prefix="/seat",
    tags=["seat"])

# GET all seats
@router.get("")
def get_all_seats(session: Session = Depends(get_session)):
    seats = session.exec(select(Seat)).all()
    if not seats:
        raise HTTPException(status_code=404, detail="No seats found")
    return seats

# GET one seat by ID
@router.get("/seat/{seat_id}")
def get_seat(seat_id: int, session: Session = Depends(get_session)):
    seat = session.get(Seat, seat_id)
    if not seat:
        raise HTTPException(status_code=404, detail="Seat not found")
    return seat

@router.post("/", response_model=Seat)
def create_seat(data: SeatCreate,session: Session = Depends(get_session)):
    new_seat = Seat(**data.model_dump())
    session.add(new_seat)
    session.commit()
    session.refresh(new_seat)
    return new_seat

@router.get("/getSeats/{event_id}",response_model=List[SeatRead])
def get_seats_by_id(event_id: int, session: Session = Depends(get_session)):
    statement = (
        select(Zone.zone_name, Seat.id, Seat.seat_position, EZP.price)
        .join(EZP, EZP.zone_id == Zone.id)
        .join(Seat, Seat.zone_id == Zone.id)
        .where(EZP.event_id == event_id)
    )
    results = session.exec(statement)
    
    seats_and_zones = []

    for zone_name, group in groupby(results, key=lambda x: x[0]):
        seats = [
            {
                "seat_id": seat_id,
                "seat_position": seat_position,
                "price": price
            }
            for _, seat_id, seat_position, price, in group
        ]
        seats_and_zones.append({
            "zone_name": zone_name,
            "seats": seats
        })
    
    return seats_and_zones