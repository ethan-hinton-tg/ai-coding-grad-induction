# AI Coding Workshop: Data Quality

A small, local Python workshop for practising careful use of GitHub Copilot or a similar AI coding assistant. The project validates simple records and gives you progressively more challenging exercises in understanding, testing, reviewing, and improving code.

## Quick start

Requirements: Python 3.10 or newer and `pytest`.

```text
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pytest
```

The root command runs only the student baseline suite. You do not need to install this project as a package; pytest is configured to import from `student/src`.

Start with [student/README.md](student/README.md), then work through [student/exercises/WORKSHEETS.md](student/exercises/WORKSHEETS.md). Instructor-only answers and the completed project are under `instructor/`; do not distribute that folder to participants.

## Responsible use

Follow the [Thorogood AI policy](<https://thorogoodassociates.sharepoint.com/Procedures%20%20Policies/Forms/AllItems.aspx?id=%2FProcedures%20%20Policies%2FCompany%20Policies%2FThorogood%20InfoSec%20Handbook%2Epdf&parent=%2FProcedures%20%20Policies%2FCompany%20Policies&p=true&ga=1&CT=1790796583500&OR=OWA%2DNT%2DMail&CID=42711a7e%2D18dc%2De139%2D281c%2D28b1b8421ef6&SI=NonSentItems&SLSync=F>) and your organization’s approved-tool and data-handling policies. Never put secrets, credentials, personal data, client data, or proprietary material into an AI tool unless policy explicitly permits it. Treat generated code as a proposal, review the code and diff, run tests, and check dependencies and security implications. The developer remains accountable for code they submit. If you are unsure whether information or a tool is approved, stop and ask the facilitator or follow your organization’s policy.
