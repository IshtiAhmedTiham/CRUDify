from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from src.models.v1.user_model import User as UserModel
from src.schemas.v1.user_schema import UserCreate
from src.config.v1.database import get_db

def validate_unique_fields(data: UserCreate, db: Session = Depends(get_db)):
    is_name_exist = db.query(UserModel).filter(UserModel.name == data.name).first()
    if is_name_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Name already exists"
        )
    
    is_email_exist = db.query(UserModel).filter(UserModel.email == data.email).first()
    if is_email_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists"
        )

    return data