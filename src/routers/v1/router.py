from fastapi import APIRouter
from .postgresql import postgresql_router
from .sqlite import sqlite_router
from src.authentication.auth import router as auth_router

router = APIRouter()

router.include_router(postgresql_router.router, prefix="/postgresql/customer")
router.include_router(sqlite_router.router, prefix="/sqlite/customer")
router.include_router(auth_router, prefix="/sqlite/customer/auth")

