from datetime import datetime

from pydantic import BaseModel, Field

from src.backend.dto.base import Response


class EventRequest(BaseModel):
    name: str = Field(default="Event Name", examples=["Event Name"])
    description: str = Field(
        default="Event Description", examples=["Event Description"]
    )
    quota: int = Field(default=100, examples=[100])
    start_date: datetime = Field(
        default_factory=datetime.now, examples=["2026-04-02T00:00:00"]
    )
    end_date: datetime = Field(
        default_factory=datetime.now, examples=["2026-04-02T00:00:00"]
    )


class EventResponse(Response):
    pass
