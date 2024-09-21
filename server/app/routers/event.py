from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from itertools import groupby
from ..db import get_session
from ..models import Event, Venue, Zone, Seat, Event_Zone_Price as EZP
from ..basemodels import EventCreate

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
@router.get("")
def get_all_events(session: Session = Depends(get_session)):
    events = session.exec(select(Event)).all()
    if not events:
        raise HTTPException(status_code=404, detail="No events found")
    return events

#Get one event by ID
@router.get("/event/{event_id}")
def get_event(event_id: int, session: Session = Depends(get_session)):
    event = session.get(Event, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event