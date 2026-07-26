from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
from src.authentication.jwt import oauth2_schema, decode_jwt
from src.config.database import get_db
from src.models.user_model import UserModel


def get_current_user(token = Depends(oauth2_schema), db : Session = Depends(get_db)):
    payload = decode_jwt(token)

    user_id = int(payload["sub"])
    user = db.query(UserModel).filter(UserModel.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Data not Found"
        )

    return user