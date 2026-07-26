from fastapi import APIRouter, status, Depends, HTTPException
from src.schemas.login_schema import UserLogin, LoginResponse
from src.config.database import get_db
from sqlalchemy.orm import Session
from src.models.user_model import UserModel
from src.utils.user_utils import varify_password
from src.authentication.jwt import encode_jwt

router = APIRouter()

#Login
@router.post("/", response_model=LoginResponse, status_code=status.HTTP_201_CREATED)
def create_user(data : UserLogin, db : Session = Depends(get_db)):
    try:
        user = db.query(UserModel).filter(UserModel.email == data.email).first()

        if not user:
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = "Data not found"
            )

        if not varify_password(data.password, user.password):
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = "Data not found"
            )

        payload = {
            "sub" : str(user.id),
            "name" : user.name,
            "email" : user.email,
            "role" : user.role
        }

        token = encode_jwt(payload)
        
        return token
    except Exception as error:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = f"Error : {str(error)}"
        )










