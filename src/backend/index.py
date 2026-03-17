from fastapi import FastAPI
from src.backend.routes.users import router as users_router
from src.backend.routes.events import router as events_router
from src.backend.routes.registrations import router as registrations_router

app = FastAPI(title="Backend API", version="1.0.0")

app.include_router(users_router)
app.include_router(events_router)
app.include_router(registrations_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Backend API"}
