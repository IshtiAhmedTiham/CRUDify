from fastapi import APIRouter
from src.controllers.api.v1 import user_controller
from src.authentication import auth


router = APIRouter()

router.include_router(user_controller.router, prefix="/user", tags=["User"])
router.include_router(auth.router, prefix="/login", tags=["User"])
