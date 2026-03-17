from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List, Optional
from pydantic import BaseModel
from src.models import Registration
from src.database import get_session

class RegistrationCreate(BaseModel):
    user_id: Optional[int] = None
    event_id: Optional[int] = None

class RegistrationUpdate(BaseModel):
    user_id: Optional[int] = None
    event_id: Optional[int] = None

router = APIRouter(prefix="/registrations", tags=["registrations"])

# CRUD operations for Registration model

# 1. Get all registrations
@router.get("/", response_model=List[Registration])
def get_registrations(session: Session = Depends(get_session)):
    registrations = session.exec(select(Registration)).all()
    return registrations

# 2. Get a registration by ID
@router.get("/{registration_id}", response_model=Registration)
def get_registration(registration_id: int, session: Session = Depends(get_session)):
    registration = session.get(Registration, registration_id)
    if not registration:
        raise HTTPException(status_code=404, detail="Registration not found")
    return registration

# 3. Create a new registration
@router.post("/", response_model=Registration)
def create_registration(registration_data: RegistrationCreate, session: Session = Depends(get_session)):
    registration = Registration(**registration_data.dict())
    session.add(registration)
    session.commit()
    session.refresh(registration)
    return registration

# 4. Update an existing registration
@router.put("/{registration_id}", response_model=Registration)
def update_registration(registration_id: int, registration_data: RegistrationUpdate, session: Session = Depends(get_session)):
    registration = session.get(Registration, registration_id)
    if not registration:
        raise HTTPException(status_code=404, detail="Registration not found")
    for key, value in registration_data.dict(exclude_unset=True).items():
        setattr(registration, key, value)
    session.commit()
    session.refresh(registration)
    return registration

# 5. Delete a registration
@router.delete("/{registration_id}")
def delete_registration(registration_id: int, session: Session = Depends(get_session)):
    registration = session.get(Registration, registration_id)
    if not registration:
        raise HTTPException(status_code=404, detail="Registration not found")
    session.delete(registration)
    session.commit()
    return {"message": "Registration deleted"}