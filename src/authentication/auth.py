from fastapi import APIRouter, status, Depends, HTTPException
from src.schemas.v1.login_schema import Login
from sqlalchemy.orm import Session
from src.config.v1.sqlite_database import get_db
from src.models.v1.customer_model import CustomerModel
from src.utils.utils import varify_password
from src.authentication.jwt import encode_token

router = APIRouter()

@router.post("/", status_code=status.HTTP_200_OK)
def authentication(user_data: Login, db: Session = Depends(get_db)):
    saved_data = db.query(CustomerModel).filter(CustomerModel.email == user_data.email).first()
    
    if not saved_data:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Data Not Found"
        )

    if not varify_password(user_data.password, saved_data.password):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Data Not Found"
        )
    
    token_data = {
        "sub": str(saved_data.id),
        "email": saved_data.email
    }

    token = encode_token(token_data)

    return {
        "access_token": token,
        "token_type": "bearer"
    }

