from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from app.domains.users.repository import UserRepository
from app.domains.wallet.service import WalletService
from app.core.security import hash_password, verify_password, create_access_token, create_refresh_token, decode_token
from app.domains.auth.schemas import RegisterRequest, LoginRequest, TokenResponse
from jose import JWTError

class AuthService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.user_repo = UserRepository(db)
        self.wallet_service = WalletService(db)

    async def register(self, data: RegisterRequest) -> TokenResponse:
        if await self.user_repo.get_by_email(data.email):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")
        if await self.user_repo.get_by_username(data.username):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username already taken")

        hashed = hash_password(data.password)
        user = await self.user_repo.create(data.username, data.email, hashed)

        # Every new user gets a wallet with starting balance
        await self.wallet_service.create_wallet(user.id)

        return TokenResponse(
            access_token=create_access_token(str(user.id)),
            refresh_token=create_refresh_token(str(user.id)),
        )

    async def login(self, data: LoginRequest) -> TokenResponse:
        user = await self.user_repo.get_by_email(data.email)
        if not user or not verify_password(data.password, user.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        if not user.is_active:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Account disabled")

        return TokenResponse(
            access_token=create_access_token(str(user.id)),
            refresh_token=create_refresh_token(str(user.id)),
        )

    async def refresh(self, refresh_token: str) -> TokenResponse:
        try:
            payload = decode_token(refresh_token)
            if payload.get("type") != "refresh":
                raise JWTError("Wrong token type")
            user_id = payload.get("sub")
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")

        user = await self.user_repo.get_by_id(user_id)
        if not user or not user.is_active:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

        return TokenResponse(
            access_token=create_access_token(str(user.id)),
            refresh_token=create_refresh_token(str(user.id)),
        )