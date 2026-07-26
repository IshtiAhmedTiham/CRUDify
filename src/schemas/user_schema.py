from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserRequest(BaseModel):
    name : str
    email : EmailStr
    password : str

class UserResponse(BaseModel):
    id : int
    name : str
    email : EmailStr
    password : str
    role : str
    created_at : datetime
    updated_at : datetime