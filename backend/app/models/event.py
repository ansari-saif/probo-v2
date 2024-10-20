from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from decimal import Decimal

class EventBase(SQLModel):
    event_name: str = Field(max_length=255)
    category: str = Field(max_length=100)
    start_time: datetime
    end_time: datetime
    outcome: Optional[str] = Field(max_length=50)
    description: str
    venue_stats: str
    team_stats: dict
    is_active: bool = True
    price_lower_limit: Decimal = Field(max_digits=10, decimal_places=2)
    price_upper_limit: Decimal = Field(max_digits=10, decimal_places=2)
    currency: str = Field(max_length=10)
    last_traded_price_for_yes: Decimal = Field(max_digits=10, decimal_places=2)
    last_traded_price_for_no: Decimal = Field(max_digits=10, decimal_places=2)
    total_event_trade_price: Decimal = Field(max_digits=10, decimal_places=2)
    traders_count: str = Field(max_length=20)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    event_slug: str = Field(max_length=255)
    share_link: str = Field(max_length=255)

class EventCreate(EventBase):
    pass

class Event(EventBase, table=True):
    id: int = Field(default=None, primary_key=True)

class EventUpdate(SQLModel):
    event_name: Optional[str] = None
    category: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    outcome: Optional[str] = None
    description: Optional[str] = None
    venue_stats: Optional[str] = None
    team_stats: Optional[dict] = None
    is_active: Optional[bool] = None
    price_lower_limit: Optional[Decimal] = None
    price_upper_limit: Optional[Decimal] = None
    currency: Optional[str] = None
    last_traded_price_for_yes: Optional[Decimal] = None
    last_traded_price_for_no: Optional[Decimal] = None
    total_event_trade_price: Optional[Decimal] = None
    traders_count: Optional[str] = None
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    event_slug: Optional[str] = None
    share_link: Optional[str] = None

class EventRead(EventBase):
    id: int
