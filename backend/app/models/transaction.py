from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from decimal import Decimal

class TransactionBase(SQLModel):
    user_id: int = Field(foreign_key="user.id")
    transaction_type: str
    amount: Decimal
    transaction_time: datetime = Field(default_factory=datetime.utcnow)

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase, table=True):
    id: int = Field(default=None, primary_key=True)

class TransactionUpdate(SQLModel):
    transaction_type: Optional[str] = None
    amount: Optional[Decimal] = None
    transaction_time: Optional[datetime] = None

class TransactionRead(TransactionBase):
    id: int
