import uuid
from datetime import datetime
from sqlalchemy import ForeignKey, DateTime, func, Boolean, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
import enum

class LockReason(str, enum.Enum):
    AUCTION = "auction"
    TRADE = "trade"

class InventoryItem(Base):
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    owner_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    item_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("items.id"), nullable=False)
    is_locked: Mapped[bool] = mapped_column(Boolean, default=False)
    lock_reason: Mapped[LockReason | None] = mapped_column(SAEnum(LockReason), nullable=True)
    lock_reference_id: Mapped[str | None] = mapped_column(nullable=True)  # auction_id / trade_id
    acquired_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    owner: Mapped["User"] = relationship("User", back_populates="inventory_items")
    item: Mapped["Item"] = relationship("Item", back_populates="inventory_entries")