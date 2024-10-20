from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from decimal import Decimal

class ResultBase(SQLModel):
    event_id: int = Field(foreign_key="event.id")
    user_id: int = Field(foreign_key="user.id")
    trade_id: int = Field(foreign_key="trade.id")
    amount_won: Decimal
    resolved_at: datetime = Field(default_factory=datetime.utcnow)

class ResultCreate(ResultBase):
    pass

class Result(ResultBase, table=True):
    id: int = Field(default=None, primary_key=True)

class ResultUpdate(SQLModel):
    amount_won: Optional[Decimal] = None
    resolved_at: Optional[datetime] = None

class ResultRead(ResultBase):
    id: int
