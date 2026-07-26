from fastapi import Depends, HTTPException, status

from src.authentication.dependencies import get_current_user
from src.authorization.roles import Role


def require_roles(*roles: Role):
    def checker(current_user=Depends(get_current_user)):
        if current_user.role not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied"
            )
        return current_user

    return checker









