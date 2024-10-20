from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.models.event import EventCreate, Event, EventRead
from app.services.event_service import create_event, get_event_by_id, get_all_events
from app.services.user_service import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/events", response_model=EventRead, status_code=status.HTTP_201_CREATED)
async def create_new_event(event: EventCreate):
    # Here you might want to add some authorization logic
    # to check if the current user has permission to create events
    new_event = create_event(event)
    if not new_event:
        raise HTTPException(status_code=400, detail="Failed to create event")
    return new_event

@router.get("/events", response_model=List[EventRead])
async def read_events(skip: int = 0, limit: int = 100):
    events = get_all_events(skip=skip, limit=limit)
    return events

@router.get("/events/{event_id}", response_model=EventRead)
async def read_event(event_id: int):
    event = get_event_by_id(event_id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event
