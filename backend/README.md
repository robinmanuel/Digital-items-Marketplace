"""Digital Items Marketplace Backend

A FastAPI-based backend for a digital items marketplace platform with support for:
- User authentication and authorization
- Item management
- Auction system
- Trading marketplace
- Wallet/payment integration
- Chat messaging
- Background task processing with Celery

## Setup

1. Install dependencies: `poetry install`
2. Copy `.env.example` to `.env` and configure
3. Run migrations: `alembic upgrade head`
4. Start the server: `uvicorn app.main:app --reload`

## Docker

Run with Docker Compose:
```bash
docker-compose up -d
```

## API Documentation

Once running, visit `http://localhost:8000/docs` for interactive API docs.
"""
