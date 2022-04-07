# sea-events-data-engineering
An app including all the flows used to process data for the prevaction project.

# Requirements
- Docker
- Docker-Compose
- Python 3.10
- Poetry

# Installation

```bash
git clone git@github.com:PhilippeGalvan/sea-events-data-engineering.git
cd sea-events-data-engineering
poetry install
```

# Test
```bash
poetry run coverage run -m pytest -vv tests/
```

# Prefect configuration

See:
ui-config: https://docs.prefect.io/orchestration/server/deploy-local.html#ui-configuration
agents: https://docs.prefect.io/orchestration/agents/overview.html#agent-types

Install docker-compose: `poetry run pip install docker-compose`

# Configure your local prefect server

1) Start the backend: `poetry run prefect server start`
2) Launch at least one agent: `poetry run prefect agent local start`
3) If no repository is configured to keep track of registered tasks and logs, register your tasks:
`poetry run python3 main.py`
4) PROFIT => http://localhost:8080
