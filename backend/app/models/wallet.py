"""Wallet database model."""
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Float

from app.db.base import Base


class Wallet(Base):
    """Wallet model."""
    __tablename__ = "wallets"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    balance = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
