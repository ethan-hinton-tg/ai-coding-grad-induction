"""Validation helpers for the workshop's small record format."""

from math import isfinite
from typing import Any


REQUIRED_FIELDS = ("record_id", "region", "amount")


def is_valid_amount(amount: Any) -> bool:
    """Return whether amount is a finite, non-negative number."""
    return (
        isinstance(amount, (int, float))
        and not isinstance(amount, bool)
        and isfinite(amount)
        and amount >= 0
        and bool(amount)
    )


def is_valid_record(record: Any) -> bool:
    """Return whether record has valid values for every required field."""
    if not isinstance(record, dict):
        return False
    if any(field not in record for field in REQUIRED_FIELDS):
        return False
    return (
        isinstance(record["record_id"], str)
        and bool(record["record_id"].strip())
        and isinstance(record["region"], str)
        and bool(record["region"].strip())
        and is_valid_amount(record["amount"])
    )


def missing_required_fields(record: Any) -> list[str]:
    """Return required field names that are absent, in required order."""
    raise NotImplementedError


def summarize_by_region(records: Any) -> dict[str, int | float]:
    """Return summed valid amounts grouped by trimmed region name."""
    raise NotImplementedError