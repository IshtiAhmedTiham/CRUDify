from fastapi import FastAPI,status,Depends,HTTPException
from src.schemas.v1.user_schema import UserCreate,UserResponse
from sqlalchemy.orm import Session
from src.config.v1.database import get_db
from src.models.v1.user_model import UserModel
from src.validators.v1.validator import validate_unique_email

router = FastAPI()

@router.post("",response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def crete_user(data : UserCreate=Depends(validate_unique_email), db:Session = Depends(get_db)):
    try:
        user = UserModel(
            name = data.name,
            email = data.email,
            password = data.password
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except Exception as error:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = f"Error : {str(error)}"
        )