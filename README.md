# python-security-training-local

Local-only secure coding training repo.

This repo contains:

- A small secure baseline module under `src/`
- A `docs/` catalog with 100+ insecure-pattern entries written as non-runnable placeholders

## Setup

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -e .[dev]
```

## Run tests

```bash
pytest
```

## Run linters / security tooling

```bash
ruff check .
bandit -r src
pip-audit
```

## Generate 100+ deterministic findings (Semgrep)

This repo includes `fixtures/vuln_markers.py` plus `.semgrep.yml` to generate predictable findings for tool testing.

```bash
semgrep --config .semgrep.yml fixtures
```

### Export SARIF

```bash
semgrep --config .semgrep.yml fixtures --sarif --output semgrep.sarif
```

### Export JSON

```bash
semgrep --config .semgrep.yml fixtures --json --output semgrep.json
```
