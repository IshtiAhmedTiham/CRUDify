from fastapi import APIRouter, status, Depends, Query, HTTPException
from src.schemas.user_schema import UserRequest, UserResponse
from src.config.database import get_db
from sqlalchemy.orm import Session
from src.models.user_model import UserModel
from src.utils.user_utils import hash_password
from src.validators.validator import validate_unique_email
from typing import List, Annotated
from src.filters.user_filters import Filters
from src.authorization.roles import Role
from src.authorization.permissions import require_role
 
router = APIRouter()

#Create User
@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(data : UserRequest = Depends(validate_unique_email), current_user = Depends(require_role(Role.ADMIN, Role.MANAGER)), db : Session = Depends(get_db)):
    try:
        user = UserModel(
            name = data.name,
            email = data.email,
            password = hash_password(data.password)
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


#Read User
@router.get("/", response_model=List[UserResponse], status_code=status.HTTP_200_OK)
def read_user(filters : Annotated[Filters,Query()], current_user = Depends(require_role(Role.ADMIN, Role.MANAGER, Role.USER)), db : Session = Depends(get_db)):
    try:
        user = db.query(UserModel)

        if filters.name:
            user = user.filter(UserModel.name.like(f"%{filters.name}%"))

        if filters.email:
            user = user.filter(UserModel.email.like(f"%{filters.email}%"))

        return user.all()
    except Exception as error:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = f"Error : {str(error)}"
        )


#Updated User
@router.put("/{id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def update_user(id : int, data : UserRequest, current_user = Depends(require_role(Role.ADMIN, Role.MANAGER)), db : Session = Depends(get_db)):
    try:
        user = db.query(UserModel).filter(UserModel.id == id).first()

        if not user:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Data Not Found"
            )

        data.password = hash_password(data.password)
        updated_data = data.model_dump()

        for key,value in updated_data.items():
            setattr(user,key,value)

        db.commit()
        db.refresh(user)

        return user
    except Exception as error:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = f"Error : {str(error)}"
        )


#Delete User
@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_user(id : int, current_user = Depends(require_role(Role.ADMIN, Role.MANAGER)), db : Session = Depends(get_db)):
    try:
        user = db.query(UserModel).filter(UserModel.id == id).first()

        if not user:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Data Not Found"
            )

        db.delete(user)
        db.commit()

        return ("status : Data successfuly deleted")
    except Exception as error:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = f"Error : {str(error)}"
        )


