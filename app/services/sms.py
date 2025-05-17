from app.utils import logger

def send_sms_notification(phone_number: str, message: str):
    try:
        # Simulate SMS sending. Integrate with actual provider (e.g., Twilio) if needed.
        logger.info(f"SMS sent to {phone_number}: {message}")
        # For real implementation, use an SMS API like Twilio, Nexmo, etc.

    except Exception as e:
        logger.error(f"Failed to send SMS: {str(e)}")
        raise
