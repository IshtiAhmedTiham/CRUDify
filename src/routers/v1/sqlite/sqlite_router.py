from fastapi import APIRouter
from src.contollers.api.v1.sqlite import customer

router = APIRouter()

router.include_router(customer.router)