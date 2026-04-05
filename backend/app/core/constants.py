from decimal import Decimal

# Wallet
STARTING_BALANCE = Decimal("1000.00")
MIN_BID_INCREMENT = Decimal("1.00")

# Pagination
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100

# Cache TTLs (seconds)
CACHE_TTL_ITEMS = 300        # 5 minutes
CACHE_TTL_USER_PROFILE = 60  # 1 minute
CACHE_TTL_AUCTION = 30       # 30 seconds

# Item rarities
RARITIES = ["common", "uncommon", "rare", "epic", "legendary"]

# WebSocket
WS_CHAT_CHANNEL = "chat:{user_id}"
WS_AUCTION_CHANNEL = "auction:{auction_id}"