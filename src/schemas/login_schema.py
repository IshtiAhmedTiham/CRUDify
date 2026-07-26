from pydantic import BaseModel, EmailStr

class UserLogin(BaseModel):
    email : EmailStr
    password : str

class LoginResponse(BaseModel):
    token : str
    token_type : str