from sqlmodel import SQLModel, Field
from typing import Optional

class Payment_Method(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    method: str
    
    