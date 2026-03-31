"""Response schemas."""
from pydantic import BaseModel
from datetime import datetime


class BaseResponse(BaseModel):
    """Base response schema."""
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
