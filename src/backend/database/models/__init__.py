import uuid
from datetime import datetime

from sqlmodel import Field, SQLModel


class Event(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    description: str
    quota: int
    started_at: datetime
    end_at: datetime
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=created_at)
