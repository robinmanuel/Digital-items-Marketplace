import uuid
from datetime import datetime
from decimal import Decimal
from sqlalchemy import ForeignKey, Numeric, DateTime, func, Enum as SAEnum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
import enum

class AuctionStatus(str, enum.Enum):
    ACTIVE = "active"
    CLOSED = "closed"
    CANCELLED = "cancelled"

class Auction(Base):
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    seller_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    inventory_item_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("inventory_items.id"), nullable=False)
    starting_price: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    current_price: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    min_bid_increment: Mapped[Decimal] = mapped_column(Numeric(18, 2), default=Decimal("1.00"))
    status: Mapped[AuctionStatus] = mapped_column(SAEnum(AuctionStatus), default=AuctionStatus.ACTIVE)
    winner_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    ends_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    seller: Mapped["User"] = relationship("User", back_populates="auctions_created", foreign_keys=[seller_id])
    winner: Mapped["User | None"] = relationship("User", foreign_keys=[winner_id])
    inventory_item: Mapped["InventoryItem"] = relationship("InventoryItem")
    bids: Mapped[list["Bid"]] = relationship("Bid", back_populates="auction", order_by="Bid.amount.desc()")

class Bid(Base):
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    auction_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("auctions.id"), nullable=False)
    bidder_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    auction: Mapped["Auction"] = relationship("Auction", back_populates="bids")
    bidder: Mapped["User"] = relationship("User", back_populates="bids_placed")