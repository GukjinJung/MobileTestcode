# Web E2E Test Framework (Playwright + Pytest)

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
python -m playwright install --with-deps chromium
```

2. Run tests:
```bash
pytest -m e2e -q
```

## Config
- See `config/settings.py` for base URL, timeouts, and directories.
- Default `HEADLESS=True` for CI-friendly runs.

## Structure
See directories `tests/`, `pages/`, `utils/`, `resources/`, `reports/`, `config/`.
