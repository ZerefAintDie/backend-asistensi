from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select, SQLModel
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel
from src.models import Event
from src.database import get_session

class EventCreate(SQLModel):
    name: Optional[str] = None
    description: Optional[str] = None
    quota: Optional[int] = None
    started_at: datetime
    ended_at: datetime

class EventUpdate(SQLModel):
    name: Optional[str] = None
    description: Optional[str] = None
    quota: Optional[int] = None
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None

router = APIRouter(prefix="/events", tags=["events"])

@router.get("/", response_model=List[Event])
def get_events(session: Session = Depends(get_session)):
    events = session.exec(select(Event)).all()
    return events

@router.get("/{event_id}", response_model=Event)
def get_event(event_id: int, session: Session = Depends(get_session)):
    event = session.get(Event, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.post("/", response_model=Event)
def create_event(event_data: EventCreate, session: Session = Depends(get_session)):
    try:
        event = Event()
        for key, value in event_data.__dict__.items():
            if value is not None:
                setattr(event, key, value)
        session.add(event)
        session.commit()
        session.refresh(event)
        return event
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{event_id}", response_model=Event)
def update_event(event_id: int, event_data: EventUpdate, session: Session = Depends(get_session)):
    event = session.get(Event, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    for key, value in event_data.dict(exclude_unset=True).items():
        setattr(event, key, value)
    event.updated_at = datetime.utcnow()
    session.commit()
    session.refresh(event)
    return event

@router.delete("/{event_id}")
def delete_event(event_id: int, session: Session = Depends(get_session)):
    event = session.get(Event, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    session.delete(event)
    session.commit()
    return {"message": "Event deleted"}