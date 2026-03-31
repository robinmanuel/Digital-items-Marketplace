"""Authentication routes."""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password, create_access_token
from app.db.session import get_db
from app.domains.auth.schemas import LoginRequest, TokenResponse
from app.domains.auth.service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    """User login endpoint."""
    service = AuthService(db)
    token = await service.authenticate_user(request.email, request.password)
    return token


@router.post("/register")
async def register(request: LoginRequest, db: Session = Depends(get_db)):
    """User registration endpoint."""
    service = AuthService(db)
    user = await service.create_user(request.email, request.password)
    return user
