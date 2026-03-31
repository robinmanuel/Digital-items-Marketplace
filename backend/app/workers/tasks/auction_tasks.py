"""Auction related background tasks."""
from app.workers.celery_app import celery_app


@celery_app.task
def process_auction_end():
    """Process ended auctions."""
    pass


@celery_app.task
def send_auction_reminder():
    """Send auction reminders to users."""
    pass
