from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..db import get_session
from ..basemodels import ZoneCreate
from ..models import Zone

router = APIRouter(prefix="/zone",
    tags=["zone"])

# GET all zones
@router.get("")
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

@router.post("", response_model=Zone)
def create_zone(data: ZoneCreate, session: Session = Depends(get_session)):
    new_zone = Zone(**data.model_dump())
    session.add(new_zone)
    session.commit()
    session.refresh(new_zone)
    return new_zone