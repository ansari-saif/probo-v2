from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from decimal import Decimal

class TradeBase(SQLModel):
    event_id: int = Field(foreign_key="event.id")
    prediction: str
    amount_staked: Decimal = Field(max_digits=10, decimal_places=2)

class TradeCreate(TradeBase):
    pass

class Trade(TradeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)

class TradeRead(TradeBase):
    id: int
    user_id: int
    created_at: datetime
