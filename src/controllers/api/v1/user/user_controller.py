# from fastapi import APIRouter,Depends
# from src.schemas.v1.user_schema import User,UserResponse
# from sqlalchemy.orm import Session
# from .database import get_db
# from .model import User as user_model
# from typing import List

# router = APIRouter()

# #create
# @router.post("/",response_model=UserResponse)
# def create_user(data:User, db : Session = Depends(get_db)):
#     user = user_model(
#         name = data.name,
#         email = data.email,
#         password = data.password
#     )
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return user



# #read
# @router.get("/", response_model=List[UserResponse])
# def get_all_users(db: Session = Depends(get_db)):
#     users = db.query(user_model).all()
#     return users

# #read by id
# @router.get("/{id}",response_model=UserResponse)
# def get_user(id : int, db : Session = Depends(get_db)):
#     user = db.query(user_model).filter(user_model.id == id).order_by(user_model.id.asc()).first()
#     return user


# #delete
# @router.delete("/{id}")
# def delete_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(user_model).filter(user_model.id == id).first()
 
#     db.delete(user)
#     db.commit()
#     return {"massage" : "data successfully deleted"}





