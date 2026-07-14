from fastapi import Depends, HTTPException, status
from src.authentication.dependencies import get_current_user


def admin_manager_required(current_user=Depends(get_current_user)):
    if current_user.role not in ["admin", "manager"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission denied"
        )

    return current_user


def admin_manager_cashier_required(current_user=Depends(get_current_user)):
    if current_user.role not in ["admin", "manager", "cashier"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission denied"
        )

    return current_user