from data_quality import is_valid_amount, is_valid_record


def test_valid_amounts_are_accepted():
    assert is_valid_amount(12)
    assert is_valid_amount(12.5)


def test_negative_amount_is_rejected():
    assert not is_valid_amount(-1)


def test_non_numeric_amount_is_rejected():
    assert not is_valid_amount("12.5")


def test_booleans_are_not_amounts():
    assert not is_valid_amount(True)
    assert not is_valid_amount(False)


def test_valid_record_is_accepted():
    assert is_valid_record({"record_id": "r-001", "region": "West", "amount": 12.5})


def test_non_dictionary_record_is_rejected():
    assert not is_valid_record(["r-001", "West", 12.5])


def test_record_with_missing_field_is_rejected():
    assert not is_valid_record({"record_id": "r-001", "region": "West"})


def test_blank_record_id_or_region_is_rejected():
    base = {"record_id": "r-001", "region": "West", "amount": 12.5}
    blank_id = {**base, "record_id": "  "}
    blank_region = {**base, "region": "\t"}
    assert not is_valid_record(blank_id)
    assert not is_valid_record(blank_region)


def test_record_validation_does_not_mutate_input():
    record = {"record_id": "r-001", "region": "West", "amount": 12.5}
    original = record.copy()
    is_valid_record(record)
    assert record == original