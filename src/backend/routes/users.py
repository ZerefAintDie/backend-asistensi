from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel
from src.models import User
from src.database import get_session

class UserCreate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    whatsapp: Optional[str] = None

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    whatsapp: Optional[str] = None

router = APIRouter(prefix="/users", tags=["users"])

# CRUD operations for User model

# 1. Get all users
@router.get("/", response_model=List[User])
def get_users(session: Session = Depends(get_session)):
    users = session.exec(select(User)).all()
    return users

# 2. Get a user by ID
@router.get("/{user_id}", response_model=User)
def get_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# 3. Create a new user
@router.post("/", response_model=User)
def create_user(user_data: UserCreate, session: Session = Depends(get_session)):
    user = User(**user_data.dict())
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

# 4. Update an existing user
@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, user_data: UserUpdate, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user_data.dict(exclude_unset=True).items():
        setattr(user, key, value)
    user.updated_at = datetime.utcnow()
    session.commit()
    session.refresh(user)
    return user

# 5. Delete a user
@router.delete("/{user_id}")
def delete_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"message": "User deleted"}