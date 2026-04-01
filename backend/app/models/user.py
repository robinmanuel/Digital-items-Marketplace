import uuid
from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base

class User(Base):
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    # Relationships
    wallet: Mapped["Wallet"] = relationship("Wallet", back_populates="user", uselist=False)
    inventory_items: Mapped[list["InventoryItem"]] = relationship("InventoryItem", back_populates="owner")
    auctions_created: Mapped[list["Auction"]] = relationship("Auction", back_populates="seller")
    bids_placed: Mapped[list["Bid"]] = relationship("Bid", back_populates="bidder")
    trades_offered: Mapped[list["Trade"]] = relationship("Trade", foreign_keys="Trade.offerer_id", back_populates="offerer")
    trades_received: Mapped[list["Trade"]] = relationship("Trade", foreign_keys="Trade.receiver_id", back_populates="receiver")
    messages_sent: Mapped[list["Message"]] = relationship("Message", foreign_keys="Message.sender_id", back_populates="sender")
    messages_received: Mapped[list["Message"]] = relationship("Message", foreign_keys="Message.receiver_id", back_populates="receiver")