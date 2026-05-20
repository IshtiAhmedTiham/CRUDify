from fastapi import status, Depends, HTTPException
from src.schemas.v1.user_schema import UserCreate
from sqlalchemy.orm import Session
from src.config.v1.database import get_db
from src.models.v1.user_model import UserModel


def validate_unique_email(data : UserCreate, db : Session = Depends(get_db)):
    is_email_exist = db.query(UserModel).filter(UserModel.email == data.email).first()
    
    if is_email_exist:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "Email already exist"
        )
    return data
