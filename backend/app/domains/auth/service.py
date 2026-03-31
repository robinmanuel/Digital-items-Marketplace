"""Authentication business logic."""
from sqlalchemy.orm import Session

from app.core.security import create_access_token, get_password_hash, verify_password
from app.domains.auth.repository import AuthRepository


class AuthService:
    """Authentication service."""
    
    def __init__(self, db: Session):
        self.repository = AuthRepository(db)
    
    async def authenticate_user(self, email: str, password: str):
        """Authenticate user and return token."""
        user = self.repository.get_user_by_email(email)
        if not user or not verify_password(password, user.hashed_password):
            raise ValueError("Invalid credentials")
        
        access_token = create_access_token(data={"sub": str(user.id)})
        return {"access_token": access_token, "token_type": "bearer"}
    
    async def create_user(self, email: str, password: str):
        """Create new user."""
        existing_user = self.repository.get_user_by_email(email)
        if existing_user:
            raise ValueError("Email already registered")
        
        hashed_password = get_password_hash(password)
        user = self.repository.create_user(email, hashed_password)
        return user
