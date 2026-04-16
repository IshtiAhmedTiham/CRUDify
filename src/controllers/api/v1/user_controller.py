from fastapi import APIRouter,status,Depends,HTTPException,Query
from src.schemas.v1.user_schema import UserCreate,UserResponse
from sqlalchemy.orm import Session
from src.config.v1.database import get_db
from src.models.v1.user_model import User as UserModel
from src.helpers.v1.helper import validate_unique_fields
from typing import Optional,Annotated
from src.filters.v1.filter import UserFilters

router = APIRouter()

# create user
@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(data: UserCreate = Depends(validate_unique_fields), db: Session = Depends(get_db)):
    try:
        new_user = UserModel(
            name=data.name,
            email=data.email,
            password=data.password
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as error:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User creation failed: {str(error)}"
        )


# read users
@router.get("/", response_model=list[UserResponse], status_code=status.HTTP_200_OK)
def read_user(filters : Annotated[UserFilters,Query()], db : Session = Depends(get_db)):
    user = db.query(UserModel)

    if filters.name:
        user = user.filter(UserModel.name.like(f"%{filters.name}%"))
    if filters.email:
        user = user.filter(UserModel.email.like(f"%{filters.email}%"))
        
    return user.all()

# read specific user
@router.get("/{id}",response_model=UserResponse,status_code=status.HTTP_200_OK)
def read_specific_user(id:int, db:Session = Depends(get_db)):
    try:
        user = db.query(UserModel).filter(UserModel.id == id).order_by(UserModel.id.asc()).first()
        return{"user" : user}
    except Exception as error:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"error : {str(error)}"
        )


# delete user
@router.delete("/{id}")
def delete_user(id:int, db:Session = Depends(get_db)):
    try:
        user = db.query(UserModel).filter(UserModel.id == id).one()
        db.delete(user)
        db.commit()
        return{"status" : "user successfully delete"}
    except Exception as error:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"error : {str(error)}" 
        )
    