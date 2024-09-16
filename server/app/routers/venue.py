from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..db.db import get_session
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




