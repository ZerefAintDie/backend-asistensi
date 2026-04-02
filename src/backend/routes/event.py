from typing import Annotated

from fastapi import APIRouter, Depends, Path

from src.backend.controllers.event import EventController
from src.backend.dto.event import (
    EventRequest,
    EventResponse,
    GetEventRequest,
    GetEventResponse,
)

router = APIRouter(prefix="/event")


@router.post("/")
def create_event(
    req_body: EventRequest, controller: EventController = Depends(EventController)
) -> EventResponse:
    return controller.create_event(req_body)


@router.get(f"/{id}")
def get_event(
    req_params: Annotated[GetEventRequest, Path(title="The ID of the item to get")],
    controller: EventController = Depends(EventController),
) -> GetEventResponse:
    return controller.get_event(req_params)
