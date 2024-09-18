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

# GET all venues
@router.get("/venue")
def get_all_venues(session: Session = Depends(get_session)):
    venues = session.exec(select(Venue)).all()
    if not venues:
        raise HTTPException(status_code=404, detail="No venues found")
    return venues

# GET one venue by ID
@router.get("/venue/{venue_id}")
def get_venue(venue_id: int, session: Session = Depends(get_session)):
    venue = session.get(Venue, venue_id)
    if not venue:
        raise HTTPException(status_code=404, detail="Venue not found")
    return venue


# GET all events
@router.get("/event")
def get_all_events(session: Session = Depends(get_session)):
    events = session.exec(select(Event)).all()
    if not events:
        raise HTTPException(status_code=404, detail="No events found")
    return events

# GET one event by ID
@router.get("/event/{event_id}")
def get_event(event_id: int, session: Session = Depends(get_session)):
    event = session.get(Event, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


# GET all zones
@router.get("/zone")
def get_all_zones(session: Session = Depends(get_session)):
    zones = session.exec(select(Zone)).all()
    if not zones:
        raise HTTPException(status_code=404, detail="No zones found")
    return zones

# GET one zone by ID
@router.get("/zone/{zone_id}")
def get_zone(zone_id: int, session: Session = Depends(get_session)):
    zone = session.get(Zone, zone_id)
    if not zone:
        raise HTTPException(status_code=404, detail="Zone not found")
    return zone


# GET all EZP records
@router.get("/ezp")
def get_all_ezps(session: Session = Depends(get_session)):
    ezps = session.exec(select(EZP)).all()
    if not ezps:
        raise HTTPException(status_code=404, detail="No EZP records found")
    return ezps

# GET one EZP by ID
@router.get("/ezp/{ezp_id}")
def get_ezp(ezp_id: int, session: Session = Depends(get_session)):
    ezp = session.get(EZP, ezp_id)
    if not ezp:
        raise HTTPException(status_code=404, detail="EZP not found")
    return ezp


# GET all seats
@router.get("/seat")
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


# GET all payment methods
@router.get("/paymentMethod")
def get_all_payment_methods(session: Session = Depends(get_session)):
    payment_methods = session.exec(select(Payment_Method)).all()
    if not payment_methods:
        raise HTTPException(status_code=404, detail="No payment methods found")
    return payment_methods

# GET one payment method by ID
@router.get("/paymentMethod/{method_id}")
def get_payment_method(method_id: int, session: Session = Depends(get_session)):
    method = session.get(Payment_Method, method_id)
    if not method:
        raise HTTPException(status_code=404, detail="Payment method not found")
    return method


