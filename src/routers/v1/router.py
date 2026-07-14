from fastapi import APIRouter
from src.contollers.api.v1 import customer
from src.authentication.auth import router as auth_router

router = APIRouter()

router.include_router(customer.router, prefix="/customer")
router.include_router(auth_router, prefix="/customer/auth")

