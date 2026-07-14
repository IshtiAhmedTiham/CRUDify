from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict


class CreateCustomer(BaseModel):
    name: str
    email: EmailStr
    password: str


class UpdateCustomer(BaseModel):
    name: str
    email: EmailStr
    password: str


class ResponseCustomer(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)