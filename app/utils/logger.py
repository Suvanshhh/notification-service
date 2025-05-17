import logging
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def format_notification_log(notification):
    return f"[{datetime.utcnow().isoformat()}] Notification -> User: {notification['user_id']}, Type: {notification['type']}, Subject: {notification.get('subject', 'N/A')}"

def log_notification(notification):
    log_msg = format_notification_log(notification)
    logger.info(log_msg)

def retry_handler(func, retries=3):
    async def wrapper(*args, **kwargs):
        attempt = 0
        while attempt < retries:
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                logger.warning(f"Attempt {attempt + 1} failed: {e}")
                attempt += 1
        logger.error(f"All {retries} attempts failed for function {func.__name__}")
    return wrapper
