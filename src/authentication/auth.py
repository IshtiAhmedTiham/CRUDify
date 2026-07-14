from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.authentication.jwt import encode_token
from src.config.v1.database import get_db
from src.models.v1.customer_model import CustomerModel
from src.schemas.v1.login_schema import Login, Token
from src.utils.utils import varify_password

router = APIRouter()


@router.post("/", response_model=Token, status_code=status.HTTP_200_OK)
def authentication(user_data: Login, db: Session = Depends(get_db)):
    user = (db.query(CustomerModel).filter(CustomerModel.email == user_data.email).first())

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Email or Password is incorrect"
        )

    if not varify_password(user_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Email or Password is incorrect"
        )


    token_data = {
        "sub": str(user.id),
        "email": user.email,
        "role": user.role
    }

    token = encode_token(token_data)

    return {
        "access_token": token,
        "token_type": "bearer"
    }