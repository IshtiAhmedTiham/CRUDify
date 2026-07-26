from .roles import Role
from fastapi import Depends, status, HTTPException
from src.authentication.dependencies import get_current_user

def require_role(*roles : Role):
    def current_user(user =  Depends(get_current_user)):
        if user.role not in roles:
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = "Permission Denied"
            )
        return user
    return current_user
        