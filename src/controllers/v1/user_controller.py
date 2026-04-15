from fastapi import APIRouter,status,Depends,HTTPException
from src.schemas.v1.user_schema import UserCreate,UserResponse
from sqlalchemy.orm import Session
from src.config.v1.database import get_db
from src.models.v1.user_model import User as UserModel

router = APIRouter()

# create user
@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
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
@router.get("/", response_model=UserResponse, status_code=status.HTTP_200_OK)
def read_users(db : Session = Depends(get_db)):
    users = db.query(UserModel).all()
    return{"user" : users}

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
    


