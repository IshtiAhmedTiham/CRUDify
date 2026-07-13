from fastapi import status, Depends, HTTPException
from src.schemas.v1.customer_schema import CreateCustomer, ResponseCustomer
from sqlalchemy.orm import Session
from src.config.v1.postgresql_database import get_db
from src.models.v1.customer_model import CustomerModel


def validate_unique_email(data : CreateCustomer, db : Session = Depends(get_db)):
    is_emial_exists = db.query(CustomerModel).filter(CustomerModel.email == data.email).first()

    if is_emial_exists:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "Email Already Exist"
        )
    
    return data