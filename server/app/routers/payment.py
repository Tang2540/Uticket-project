from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from ..db import get_session
from ..security import get_current_user
from ..basemodels import PaymentMethodCreate, PaymentIn
from ..models import Payment_Method, User

router = APIRouter(prefix="/payment",
    tags=["payment"])

# GET all payment methods
@router.get("/paymentMethod",response_model=List[Payment_Method])
def get_all_payment_methods(session: Session = Depends(get_session)):
    payment_methods = session.exec(select(Payment_Method)).all()
    if not payment_methods:
        raise HTTPException(status_code=404, detail="No payment methods found")
    return payment_methods

# GET one payment method by ID
@router.get("/paymentMethod/{method_id}",response_model=Payment_Method)
def get_payment_method(method_id: int, session: Session = Depends(get_session)):
    method = session.get(Payment_Method, method_id)
    if not method:
        raise HTTPException(status_code=404, detail="Payment method not found")
    return method

@router.post("/paymentMethod", response_model=Payment_Method)
def create_payment_method(data: PaymentMethodCreate , session: Session = Depends(get_session)):
    new_method = Payment_Method(method=data.method)
    session.add(new_method)
    session.commit()
    session.refresh(new_method)
    return new_method

@router.delete("/cancelPayment")
async def cancel_booking(data:PaymentIn, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    payment = session.get(Payment,data.payment_id)
    if payment.payment_method_id == 2 or payment.payment_method_id == 3 or payment.status == "Paid":
        raise HTTPException(
                status_code=404, detail="Already Paid"
            )
    else:
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not logged in",
                headers={"WWW-Authenticate": "Bearer"},
            )
        session.delete(payment)
        session.commit()
    return data

@router.put("/payWithBankTransfer")
async def pay_with_bank_transfer(data:PaymentIn, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not logged in",
                headers={"WWW-Authenticate": "Bearer"},
            )
    payment = session.get(Payment, data.payment_id)
    payment.status = "Paid"
    session.commit()