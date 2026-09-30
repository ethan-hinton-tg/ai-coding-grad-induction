# Student Project

## Goal

You will improve a tiny data-quality module while practising a disciplined AI-assisted workflow. Records look like this:

```python
{"record_id": "r-001", "region": "West", "amount": 12.50}
```

The required fields are `record_id`, `region`, and `amount`, in that order. Read the source and tests before asking an AI tool for help. The exercises intentionally leave work for you to complete.

## Requirements

The functions in `student/src/data_quality.py` should follow these rules:

- `is_valid_amount(amount)` accepts finite, non-negative `int` and `float` values. Booleans, negative values, NaN, infinity, and other types are invalid.
- `is_valid_record(record)` accepts only dictionaries with all three required fields. `record_id` and `region` must be non-blank strings, and `amount` must be a valid amount. It must not change the input dictionary.
- `missing_required_fields(record)` returns the required field names that are not present, in the order shown above. A non-dictionary has all three fields missing. This function checks whether keys are present, not whether their values are valid.
- `summarize_by_region(records)` ignores invalid records, strips whitespace from region names, and adds valid amounts together for each region. Region keys keep the order in which they first appear.

These requirements describe the behavior you are working toward. Use them, along with the tests and source code, to decide whether an AI suggestion is correct.

## Running the tests

From the repository root:

```text
python -m pytest
```

The baseline suite should pass when you begin. As you implement each exercise, add focused tests and rerun the suite. No project installation is needed.

## Responsible use

Follow the [Thorogood AI policy](<https://thorogoodassociates.sharepoint.com/Procedures%20%20Policies/Forms/AllItems.aspx?id=%2FProcedures%20%20Policies%2FCompany%20Policies%2FThorogood%20InfoSec%20Handbook%2Epdf&parent=%2FProcedures%20%20Policies%2FCompany%20Policies&p=true&ga=1&CT=1790796583500&OR=OWA%2DNT%2DMail&CID=42711a7e%2D18dc%2De139%2D281c%2D28b1b8421ef6&SI=NonSentItems&SLSync=F>). Never put secrets, credentials, personal data, client data, or proprietary material into an AI tool unless policy explicitly permits it. Treat generated code as a proposal, not as correct by default. Review generated code and diffs; run tests; check dependencies and security implications. The developer remains accountable for code they submit. If unsure whether information or a tool is approved, stop and ask the facilitator or follow your organization’s policy.

Keep a record of important AI interactions in [exercises/AI_DECISION_LOG.md](exercises/AI_DECISION_LOG.md).