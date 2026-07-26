from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from src.schemas.login_schema import UserLogin, LoginResponse
from src.config.database import get_db
from src.models.user_model import UserModel
from src.utils.user_utils import varify_password
from src.authentication.jwt import encode_jwt

router = APIRouter()

@router.post("/", response_model=LoginResponse, status_code=status.HTTP_200_OK)
def login(data : UserLogin, db : Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.email == data.email).first()

    if not user:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Data not Found"
        )

    if not varify_password(data.password, user.password):
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Data not Found"
        )

    payload = {
        "sub" : str(user.id),
        "name" : user.name,
        "email" : user.email,
        "role" : user.role
    }

    token = encode_jwt(payload)

    return {
        "token" : token,
        "token_type" : "bearer"
    }