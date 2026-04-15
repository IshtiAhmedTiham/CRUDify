from pydantic import BaseModel,EmailStr,Field

class User(BaseModel):
    name : str = Field(..., min_length=3, max_length=20)
    email : EmailStr
    password : str

class UserCreate(User):
    pass

class UserResponse(UserCreate):
    id : int
    name : str
    email : EmailStr
    password : str




