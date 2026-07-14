from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from src.authentication.permissions import admin_manager_required, admin_manager_cashier_required
from src.config.v1.database import get_db
from src.filters.v1.customer_filter import CustomerFilters
from src.models.v1.customer_model import CustomerModel
from src.schemas.v1.customer_schema import CreateCustomer, UpdateCustomer, ResponseCustomer
from src.utils.utils import hash_password
from src.validators.v1.validator import validate_unique_email

router = APIRouter()


# Create Customer
@router.post("/", response_model=ResponseCustomer, status_code=status.HTTP_201_CREATED)
def create_customer(data: CreateCustomer = Depends(validate_unique_email),current_user=Depends(admin_manager_required),db: Session = Depends(get_db)):    
    customer = CustomerModel(
        name=data.name,
        email=data.email,
        password=hash_password(data.password)
    )

    db.add(customer)
    db.commit()
    db.refresh(customer)

    return customer


# Read All Customers
@router.get("/", response_model=list[ResponseCustomer])
def read_customers(filters: Annotated[CustomerFilters, Query()], current_user=Depends(admin_manager_cashier_required),db: Session = Depends(get_db)):
    customer = db.query(CustomerModel)

    if filters.name:
        customer = customer.filter(CustomerModel.name.like(f"%{filters.name}%"))

    if filters.email:
        customer = customer.filter(CustomerModel.email.like(f"%{filters.email}%"))

    return customer.all()


# Read Single Customer
@router.get("/{id}", response_model=ResponseCustomer)
def read_customer(id: int,current_user=Depends(admin_manager_cashier_required),db: Session = Depends(get_db)):
    customer = db.query(CustomerModel).filter(CustomerModel.id == id).first()

    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )

    return customer


# Update Customer
@router.put("/{id}", response_model=ResponseCustomer)
def update_customer(id: int,data: UpdateCustomer,current_user=Depends(admin_manager_required),db: Session = Depends(get_db)):
    customer = db.query(CustomerModel).filter(CustomerModel.id == id).first()

    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )

    updated_data = data.model_dump()
    updated_data["password"] = hash_password(data.password)

    for key,value in updated_data.items():
        setattr(customer, key, value)

    db.commit()
    db.refresh(customer)

    return customer


# Delete Customer
@router.delete("/{id}")
def delete_customer(id: int, current_user=Depends(admin_manager_required),db: Session = Depends(get_db)):
    customer = db.query(CustomerModel).filter(CustomerModel.id == id).first()

    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )

    db.delete(customer)
    db.commit()

    return {"message": "Customer deleted successfully"}