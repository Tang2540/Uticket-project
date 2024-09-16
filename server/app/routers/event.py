from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List
from app.auth.security import get_password_hash, authenticate_user, create_access_token, get_current_user
from app.models.event import Event
from pydantic import BaseModel


from server.app.db.db import get_session

router = APIRouter(prefix="/events", tags=["events"])

