from sqlmodel import Session, select
from app.core.database import engine
from app.models.event import Event, EventCreate
from typing import List

def create_event(event: EventCreate):
    with Session(engine) as session:
        db_event = Event.from_orm(event)
        session.add(db_event)
        session.commit()
        session.refresh(db_event)
    return db_event

def get_all_events(skip: int = 0, limit: int = 100) -> List[Event]:
    with Session(engine) as session:
        statement = select(Event).offset(skip).limit(limit)
        events = session.exec(statement).all()
    return events

def get_event_by_id(event_id: int) -> Event:
    with Session(engine) as session:
        statement = select(Event).where(Event.id == event_id)
        event = session.exec(statement).first()
    return event

def delete_event(event_id: int) -> bool:
    with Session(engine) as session:
        statement = select(Event).where(Event.id == event_id)
        event = session.exec(statement).first()
        if event:
            session.delete(event)
            session.commit()
            return True
        return False

def delete_events() -> bool:
    with Session(engine) as session:
        try:
            statement = select(Event)
            events = session.exec(statement).all()
            for event in events:
                session.delete(event)
            session.commit()
            return True
        except Exception:
            return False

