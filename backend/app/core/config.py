"""Application configuration settings."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""
    
    # API
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Digital Items Marketplace"
    
    # Database
    DATABASE_URL: str = "postgresql://user:password@localhost/marketplace"
    
    # Security
    SECRET_KEY: str = "your-secret-key-change-this"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS
    BACKEND_CORS_ORIGINS: list[str] = ["http://localhost:3000"]
    
    class Config:
        env_file = ".env"


settings = Settings()
