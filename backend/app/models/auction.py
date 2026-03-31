"""Auction database model."""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.db.base import Base


class Auction(Base):
    """Auction model."""
    __tablename__ = "auctions"
    
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    creator_id = Column(Integer, ForeignKey("users.id"))
    starting_price = Column(Float)
    current_price = Column(Float)
    status = Column(String, default="active")
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    creator = relationship("User", back_populates="auctions")
