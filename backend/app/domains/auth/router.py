from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.dependencies.db import get_db
from app.domains.auth.service import AuthService
from app.domains.auth.schemas import RegisterRequest, LoginRequest, RefreshRequest
from app.schemas.response import APIResponse

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=APIResponse)
async def register(data: RegisterRequest, db: AsyncSession = Depends(get_db)):
    service = AuthService(db)
    result = await service.register(data)
    return APIResponse.ok(result.model_dump())


@router.post("/login", response_model=APIResponse)
async def login(data: LoginRequest, db: AsyncSession = Depends(get_db)):
    service = AuthService(db)
    result = await service.login(data)
    return APIResponse.ok(result.model_dump())


@router.post("/refresh", response_model=APIResponse)
async def refresh(data: RefreshRequest, db: AsyncSession = Depends(get_db)):
    service = AuthService(db)
    result = await service.refresh(data.refresh_token)
    return APIResponse.ok(result.model_dump())
