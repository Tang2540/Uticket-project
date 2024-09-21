from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from ..db import get_session
from ..basemodels import EZPCreate
from ..models import Event_Zone_Price as EZP

router = APIRouter(prefix="/ezp",
    tags=["ezp"])

# GET all EZP records
@router.get("", response_model=List[EZP])
def get_all_ezps(session: Session = Depends(get_session)):
    ezps = session.exec(select(EZP)).all()
    if not ezps:
        raise HTTPException(status_code=404, detail="No EZP records found")
    return ezps

# GET one EZP by ID
@router.get("/{ezp_id}",response_model=EZP)
def get_ezp(ezp_id: int, session: Session = Depends(get_session)):
    ezp = session.get(EZP, ezp_id)
    if not ezp:
        raise HTTPException(status_code=404, detail="EZP not found")
    return ezp

@router.post("", response_model=EZP)
def create_ezp(data: EZPCreate, session: Session = Depends(get_session)):
    new_ezp = EZP(**data.model_dump())
    session.add(new_ezp)
    session.commit()
    session.refresh(new_ezp)
    return new_ezp