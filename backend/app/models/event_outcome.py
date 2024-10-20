from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class EventOutcomeBase(SQLModel):
    event_id: int = Field(foreign_key="event.id")
    outcome_type: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class EventOutcomeCreate(EventOutcomeBase):
    pass

class EventOutcome(EventOutcomeBase, table=True):
    id: int = Field(default=None, primary_key=True)

class EventOutcomeUpdate(SQLModel):
    outcome_type: Optional[str] = None

class EventOutcomeRead(EventOutcomeBase):
    id: int
