async def send_email(subject, message, to_email):
    print(f"[Email] To: {to_email} | Subject: {subject} | Message: {message}")

async def send_sms(message, to_phone):
    print(f"[SMS] To: {to_phone} | Message: {message}")

async def send_inapp(user_id, message):
    print(f"[In-App] To: {user_id} | Message: {message}")
