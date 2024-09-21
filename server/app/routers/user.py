from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from fastapi.security import OAuth2PasswordRequestForm
from ..db import get_session
from ..basemodels import UserCreate, Token, UserRead
from datetime import timedelta
from ..models import User
from ..security import get_password_hash, authenticate_user, create_access_token, get_current_user

router = APIRouter(prefix="/user",
    tags=["user"])

@router.post("", response_model=User)
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    existed_user = session.exec(select(User).where(User.username == user.username)).first()
    if existed_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(user.password)
    new_user=User(username=user.username, email=user.email,password=hashed_password)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

@router.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    user = authenticate_user(form_data.username, form_data.password, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token,token_type="bearer")

@router.get("/getCurrentUser", response_model=UserRead)
async def get_current_user(user: User = Depends(get_current_user)):
    current_user = UserRead(id=user.id,username=user.username,email=user.email)
    return current_user