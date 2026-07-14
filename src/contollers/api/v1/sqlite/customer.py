from fastapi import APIRouter, status, Depends, HTTPException, Query
from src.schemas.v1.customer_schema import CreateCustomer, ResponseCustomer 
from sqlalchemy.orm import Session
from src.config.v1.sqlite_database import get_db
from src.models.v1.customer_model import CustomerModel
from src.validators.v1.validator import validate_unique_email
from typing import Annotated
from src.filters.v1.customer_filter import CustomerFilters
from src.utils.utils import hash_password

router = APIRouter()

#Create
@router.post("/",response_model = ResponseCustomer, status_code = status.HTTP_201_CREATED)
def create_customer(data : CreateCustomer = Depends(validate_unique_email), db : Session = Depends(get_db)):
    try:
        hash = hash_password(data.password)

        customers = CustomerModel(
            name = data.name,
            email = data.email,
            password = hash
        )
        
        db.add(customers)
        db.commit()
        db.refresh(customers)
        
        return customers
    
    except Exception as error:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = f"Error : {str(error)}"
        )


#Read
@router.get("/",response_model = list[ResponseCustomer], status_code = status.HTTP_200_OK)
def read_customer(filters : Annotated[CustomerFilters,Query()], db : Session = Depends(get_db)):
    try:
        customers = db.query(CustomerModel)
        
        if filters.name:
            customers = customers.filter(CustomerModel.name.like(f"%{filters.name}%"))

        if filters.email:
            customers = customers.filter(CustomerModel.email.like(f"%{filters.email}%"))
    
        return customers.all()
        
    except Exception as error:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = f"Error : {str(error)}"
        )


#Update
@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=ResponseCustomer)
def customer_update(data: CreateCustomer, id: int, db: Session = Depends(get_db)):
    try:
        data.password = hash_password(data.password)

        customer = db.query(CustomerModel).filter(CustomerModel.id == id).first()
        
        if not customer:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Data Not Found"
            )
        
        update_customer = data.model_dump()

        for key,value in update_customer.items():
            setattr(customer, key, value)

        db.commit()
        db.refresh(customer)
        return customer
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Error : {str(error)}"
        )
  

#Delete
@router.delete("/{id}",status_code = status.HTTP_200_OK)
def delete_customer(id : int, db : Session = Depends(get_db)):
    customers = db.query(CustomerModel).filter(CustomerModel.id == id).first()

    if customers is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Data not found"
        )
    
    db.delete(customers)
    db.commit()

    return {"massage" : "Data successfully deleted"}
        
