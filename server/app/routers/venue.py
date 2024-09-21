from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from ..db import get_session
from ..basemodels import VenueCreate
from ..models import Venue

router = APIRouter(prefix="/venue",
    tags=["venue"])

@router.post("", response_model=Venue)
def create_venue(data: VenueCreate, session: Session = Depends(get_session)):
    new_venue = Venue(**data.model_dump())
    session.add(new_venue)
    session.commit()
    session.refresh(new_venue)
    return new_venue

# GET one venue by ID
@router.get("/{venue_id}", response_model=Venue)
def get_venue(venue_id: int, session: Session = Depends(get_session)):
    venue = session.get(Venue, venue_id)
    if not venue:
        raise HTTPException(status_code=404, detail="Venue not found")
    return venue

@router.get("/all_venues",response_model=List[Venue])
def get_all_venues(session: Session = Depends(get_session)):
    venues = session.exec(select(Venue)).all()
    if not venues:
        raise HTTPException(status_code=404, detail="No venues found")
    return venues
