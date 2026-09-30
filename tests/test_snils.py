from validator import validate_snils


def test_snils_checksum_and_format():
    assert validate_snils("112-233-445 95") is True
    assert validate_snils("11223344595") is True
    assert validate_snils("11223344596") is False
    assert validate_snils("123") is False
    assert validate_snils("not-a-number") is False
