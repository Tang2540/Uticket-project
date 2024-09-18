from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..db.db import get_session
from ..schemas.schemas import VenueCreate
from ..models.venue import Venue

router = APIRouter(prefix="/venue",
    tags=["venue"])

# GET one venue by ID
@router.get("/venue/{venue_id}", response_model=Venue)
def get_venue(venue_id: int, session: Session = Depends(get_session)):
    venue = session.get(Venue, venue_id)
    if not venue:
        raise HTTPException(status_code=404, detail="Venue not found")
    return venue

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
