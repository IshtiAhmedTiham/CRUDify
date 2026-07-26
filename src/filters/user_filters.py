from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Filters(BaseModel):
    name : Optional[str] = Field(None, min_length=1)
    email : Optional[EmailStr] = None