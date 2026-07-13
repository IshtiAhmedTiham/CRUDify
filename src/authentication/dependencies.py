from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.authentication.jwt import oauth2_scheme,decode_token
from src.config.v1.sqlite_database import get_db
from src.models.v1.customer_model import CustomerModel


def get_current_user(token : str = Depends(oauth2_scheme), db : Session = Depends(get_db)):
    payload = decode_token(token)
    
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are unauthorized"
        )

    user_id = payload.get("sub")
    user = db.query(CustomerModel).filter(CustomerModel.id == user_id).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Data not found"
        )

    return user
