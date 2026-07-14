from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.authentication.jwt import decode_token, oauth2_scheme
from src.config.v1.database import get_db
from src.models.v1.customer_model import CustomerModel


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = decode_token(token)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    user_id = int(payload["sub"])

    user = (db.query(CustomerModel).filter(CustomerModel.id == int(user_id)).first())

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user