from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from decimal import Decimal

class UserBase(SQLModel):
    mobile: str = Field(unique=True, index=True)
    balance: Decimal = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    last_login: Optional[datetime] = None

class UserCreate(UserBase):
    pass

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class UserUpdate(SQLModel):
    balance: Optional[Decimal] = None
    last_login: Optional[datetime] = None

class UserRead(UserBase):
    id: int
