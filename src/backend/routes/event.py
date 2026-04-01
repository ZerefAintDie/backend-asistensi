from fastapi import APIRouter, Depends

from src.backend.controllers.event import EventController
from src.backend.dto.event import EventRequest, EventResponse

router = APIRouter(prefix="/event")


@router.post("/")
def create_event(
    req_body: EventRequest, controller: EventController = Depends(EventController)
) -> EventResponse:
    return controller.create_event(req_body)
