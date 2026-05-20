from fastapi import APIRouter
from .sqlite import sqlite_router

router = APIRouter()

router.include_router(sqlite_router.router, prefix="/sqlite")