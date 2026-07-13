from typing import Optional
from pydantic import BaseModel, Field, EmailStr

class CustomerFilters(BaseModel):
    name : Optional[str] = Field(None,min_length=1)
    email : Optional[EmailStr] = None
