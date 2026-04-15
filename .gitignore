from pydantic import BaseModel,EmailStr

class User(BaseModel):
    name : str
    email : EmailStr
    password : str

class UserCreate(User):
    pass

class UserResponse(BaseModel):
    id : int
    name : str
    email : EmailStr
    password : str