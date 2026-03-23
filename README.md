# FastAPI Template

A clean FastAPI project template designed to accelerate backend development with best practices in structure, configuration, and tooling.

---

## Features

- Structured and modular code organization under `/src`
- Custom JSON response models and error handling
- Built-in logging middleware
- Centralized configuration management via `pydantic-settings`
- Auto-generated OpenAPI docs with enriched metadata and code samples
- CORS middleware with flexible configuration
- Custom exception handlers for validation and backend errors
- FastAPI router and middleware examples included
- Poetry-managed dependencies and scripts

---

## Requirements

- Python 3.12+
- Poetry (for dependency and environment management)

---

## Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/fastapi-template.git
cd fastapi-template
```

2. Install dependencies with Poetry
```bash
poetry install
```

3. Activate the virtual environment
```bash
poetry shell
```
---

## Running the Application

1. Development server with hot reloading
```bash
poetry run local
```

2. Production-like server
```bash
poetry run server
```

## Project Structure
```
.vscode/           # VSCode settings
src/
    ├── core/           # Configuration and settings
    ├── docs.py         # Custom OpenAPI doc generation
    ├── main.py         # FastAPI app initialization, middleware, and routes
    ├── middleware/     # Logging and other middleware
    ├── routes/         # API route handlers
    ├── schemas/        # Pydantic request and response models
    ├── run.py          # Uvicorn server runners for local and prod
    └── utility.py      # Example utility route(s)
.gitignore          # Git ignore file
pyproject.toml      # Poetry configuration
README.md           # This file
```

## Configuration
- `src/core/config.py`: Centralized configuration management via `pydantic-settings`. You can override settings via environment variables or a `.env` file.

## API Documentation
Once running, visit:
- OpenAPI docs: http://localhost:8000/docs
- Redoc docs: http://localhost:8000/redoc

## Authors
- Muzaffar Shaikh - [muzaffar@sirpi.io](mailto:"Muzaffar%20Shaikh"<muzaffar@sirpi.io>)