from fastapi import APIRouter
from src.controllers.api.v1.sqlite import user_contoller


router = APIRouter()

router.include_router(user_contoller.router, prefix="/api/v1")
