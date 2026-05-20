from fastapi import APIRouter
from .sqlite import sqlite_router
from .postgresql import postgresql_router

router = APIRouter()

router.include_router(sqlite_router.router, prefix="/sqlite")
router.include_router(postgresql_router.router, prefix="/postgresql")
