import pytest

from validator import validate_email, validate_phone


def test_validate_email():
    assert validate_email("test@example.com") is True
    assert validate_email("invalid") is False


@pytest.mark.parametrize("phone", ["+79991234567", "79991234567", "+7 999 123-45-67"])
def test_validate_phone_accepts_russian_numbers(phone):
    assert validate_phone(phone) is True


@pytest.mark.parametrize("phone", [
    "89991234567", "+7999123", "", "+799912345678", "+79991234567\n",
    "+7(999)1234567", "+7999123456x", "+7９９９１２３４５６７", "++79991234567",
])
def test_validate_phone_rejects_invalid_numbers(phone):
    assert validate_phone(phone) is False
