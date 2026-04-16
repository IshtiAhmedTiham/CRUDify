from pydantic import BaseModel,Field,EmailStr
from typing import Optional

class UserFilters(BaseModel):
    name : Optional[str] = Field(None,min_length=1)
    email : Optional[EmailStr] = None
