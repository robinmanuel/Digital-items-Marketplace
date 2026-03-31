"""Authentication data access layer."""
from sqlalchemy.orm import Session

from app.models.user import User


class AuthRepository:
    """Authentication repository."""
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_user_by_email(self, email: str):
        """Get user by email."""
        return self.db.query(User).filter(User.email == email).first()
    
    def create_user(self, email: str, hashed_password: str):
        """Create new user."""
        user = User(email=email, hashed_password=hashed_password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
