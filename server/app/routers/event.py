from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from itertools import groupby
from ..db import get_session
from ..models import Event, Venue, Zone, Seat, Event_Zone_Price as EZP, Zone_Tier
from ..basemodels import EventCreate, EventRead

router = APIRouter(prefix="/event",
    tags=["event"])

#Create event
@router.post("", response_model=Event)
def create_event(data: EventCreate, session: Session = Depends(get_session)):
    new_event = Event(**data.model_dump())
    session.add(new_event)
    session.commit()
    session.refresh(new_event)
    return new_event

# GET all events
@router.get("", response_model=List[EventRead])
def get_all_events(session: Session = Depends(get_session)):
    statement = select(Event.slug,Event.eventname,Event.card_img,Event.eventdate,Venue.name).join(Venue, Venue.id == Event.venue_id)
    events = session.exec(statement).all()
    
    if not events:
        raise HTTPException(status_code=404, detail="No events found")
    
    return events

#Get one event by ID
@router.get("/event/{slug}")
def get_event(slug: str, session: Session = Depends(get_session)):
    # Query to fetch event and related data
    statement = (
        select(
            Event.seat_map,
            Zone.zone_name,
            Zone_Tier.price,
            Zone_Tier.color,
            EZP.coor
        )
        .join(EZP, EZP.event_id == Event.id)
        .join(Zone_Tier, Zone_Tier.event_id == Event.id)
        .join(Zone, Zone.id == EZP.zone_id)  # Assuming Zone is related through EZP
        .where(Event.slug == slug)  # Filter by slug
    )

    # Execute the query
    result = session.execute(statement).fetchall()

    return result