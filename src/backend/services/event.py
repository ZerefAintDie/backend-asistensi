from fastapi import Depends

from src.backend.database.models.event import Event
from src.backend.dto.event import EventResponse
from src.backend.repositories.event import EventRepository


class EventService:
    def __init__(self, event_repository: EventRepository = Depends(EventRepository)):
        self.event_repository = event_repository

    def create_event(self, event: Event) -> EventResponse:
        event = self.event_repository.create(event)
        return EventResponse(
            code=200,
            message="Event berhasil ditambahkan",
            data=None,
        )
