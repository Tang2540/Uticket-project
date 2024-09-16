from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from fastapi.security import OAuth2PasswordRequestForm
from ..db.db import get_session
from ..schemas.schemas import PaymentMethodCreate, EventCreate, VenueCreate, ZoneCreate, EZPCreate, SeatCreate
from datetime import timedelta
from ..models import User, Payment_Method, Event, Venue, Zone, EZP, Seat
from ..auth.security import get_password_hash, authenticate_user, create_access_token, get_current_user

router = APIRouter(prefix="/utility",
    tags=["utility"])

@router.post("/venue", response_model=Venue)
def create_venue(something: VenueCreate, session: Session = Depends(get_session)):
    new_venue = Venue(**something.model_dump())
    session.add(new_venue)
    session.commit()
    session.refresh(new_venue)
    return new_venue

@router.post("/event", response_model=Event)
def create_event(something: EventCreate, session: Session = Depends(get_session)):
    new_event = Event(**something.model_dump())
    session.add(new_event)
    session.commit()
    session.refresh(new_event)
    return new_event

@router.post("/zone", response_model=Zone)
def create_zone(something: ZoneCreate, session: Session = Depends(get_session)):
    new_zone = Zone(**something.model_dump())
    session.add(new_zone)
    session.commit()
    session.refresh(new_zone)
    return new_zone

@router.post("/ezp", response_model=EZP)
def create_ezp(something: EZPCreate, session: Session = Depends(get_session)):
    new_ezp = EZP(**something.model_dump())
    session.add(new_ezp)
    session.commit()
    session.refresh(new_ezp)
    return new_ezp

@router.post("/seat", response_model=Seat)
def create_seat(something: SeatCreate,session: Session = Depends(get_session)):
    new_seat = Seat(**something.model_dump())
    session.add(new_seat)
    session.commit()
    session.refresh(new_seat)
    return new_seat

@router.post("/paymentMethod", response_model=Payment_Method)
def create_payment_method(something: PaymentMethodCreate , session: Session = Depends(get_session)):
    new_method = Payment_Method(method=something.method)
    session.add(new_method)
    session.commit()
    session.refresh(new_method)
    return new_method