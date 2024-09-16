from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..db.db import get_session
<<<<<<< HEAD
from ..schemas.user import VenueCreate
from ..models.venue import Venue

router = APIRouter(prefix="/venues", tags=["venues"])

@router.post("/", response_model=Venue)
def create_venue(venue: VenueCreate, session: Session = Depends(get_session)):
    new_venue = Venue(name=venue.name, capacity=venue.capacity)
    session.add(new_venue)
    session.commit()
    session.refresh(new_venue)
    return new_venue




=======
from ..schemas.schemas import VenueCreate
from ..models.venue import Venue

router = APIRouter(prefix="/venue",
    tags=["venue"])

@router.post("/", response_model=Venue)
def create_user(venue: VenueCreate, session: Session = Depends(get_session)):
    existed_venue = session.exec(select(Venue).where(Venue.name == venue.name)).first()
    if existed_venue:
        raise HTTPException(status_code=400, detail="Username already registered")
    new_venue=Venue(name=venue.name,capacity=venue.capacity)
    session.add(new_venue)
    session.commit()
    session.refresh(new_venue)
    return new_venue
>>>>>>> beb9e35df92e2fae1c45f7bb13d1bf83c3ef66ee
