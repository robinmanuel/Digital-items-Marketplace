"""Authentication dependencies."""
from typing import Annotated

from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt

from app.core.config import settings
from app.core.security import verify_password


async def get_current_user(token: str):
    """Get current authenticated user from JWT token."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    return {"user_id": user_id}
