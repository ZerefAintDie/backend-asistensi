from fastapi import FastAPI

from src.backend.routes.event import router as event_router

app = FastAPI()
app.include_router(event_router)
