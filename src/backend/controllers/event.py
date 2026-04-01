from fastapi import Depends

from src.backend.database.models.event import Event
from src.backend.dto.event import EventRequest
from src.backend.services.event import EventService


class EventController:
    def __init__(self, event_service: EventService = Depends(EventService)):
        self.event_service = event_service

    def create_event(self, req_body: EventRequest):
        event_data = Event(
            name=req_body.name,
            description=req_body.description,
            quota=req_body.quota,
            started_at=req_body.start_date,
            end_at=req_body.end_date,
        )
        response = self.event_service.create_event(event_data)
        return response
