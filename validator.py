def validate_phone(phone: str) -> bool:
    """Валидация российского номера телефона."""
    import re

    cleaned = phone.replace('-', '').replace(' ', '')
    return bool(re.fullmatch(r'\+?7[0-9]{10}', cleaned))


# validator.py
def validate_email(email: str) -> bool:
    """Валидация email-адреса."""
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))


__all__ = ["validate_email", "validate_phone"]
