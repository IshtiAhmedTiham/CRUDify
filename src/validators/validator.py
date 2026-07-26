from fastapi import status, Depends, HTTPException
from src.schemas.user_schema import UserRequest
from src.config.database import get_db
from sqlalchemy.orm import Session
from src.models.user_model import UserModel


def validate_unique_email(data : UserRequest, db : Session = Depends(get_db)):
    is_emial_exists = db.query(UserModel).filter(UserModel.email == data.email).first()

    if is_emial_exists:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "Email Already Exist"
        )
    
    return data
