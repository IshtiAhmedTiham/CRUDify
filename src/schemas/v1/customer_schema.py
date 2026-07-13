from pydantic import BaseModel,EmailStr

class CreateCustomer(BaseModel):
    name : str
    email : EmailStr
    password : str

class ResponseCustomer(BaseModel):
    id : int
    name : str
    email : EmailStr
    password : str