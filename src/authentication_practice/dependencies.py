from fastapi import APIRouter, status, Depends, HTTPException
from src.config.database import get_db
from sqlalchemy.orm import Session
from src.models.user_model import UserModel
from src.authentication.jwt import oauth2_schema, decode_jwt

router = APIRouter()

def get_current_user(token = Depends(oauth2_schema), db : Session = Depends(get_db)):
    try:
        payload = decode_jwt(token)

        user_id = int(payload["sub"])
        user = db.query(UserModel).filter(UserModel.id == user_id).first()

        if not user:
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = "Data Not Found"
            )
        
        return user
    
    except Exception as error:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = f"Error : {str(error)}"
        )
