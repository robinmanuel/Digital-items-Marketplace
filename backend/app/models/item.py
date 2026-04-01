import uuid
from datetime import datetime
from sqlalchemy import String, Text, Numeric, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
from decimal import Decimal

class Item(Base):
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    category: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    rarity: Mapped[str] = mapped_column(String(30), nullable=False, default="common")
    base_price: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    image_url: Mapped[str] = mapped_column(String(500), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    inventory_entries: Mapped[list["InventoryItem"]] = relationship("InventoryItem", back_populates="item")