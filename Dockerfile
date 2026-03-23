# Stage 1: export dependencies via Poetry (not shipped in final image)
FROM python:3.12-slim AS builder
WORKDIR /build

RUN pip install --no-cache-dir poetry==1.8.5

COPY pyproject.toml poetry.lock ./
RUN poetry export --without-hashes --format=requirements.txt -o requirements.txt

# Stage 2: lean production image
FROM python:3.12-slim AS final
WORKDIR /app

COPY --from=builder /build/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY pyproject.toml ./

RUN useradd --uid 1000 --no-create-home appuser && chown -R appuser /app
USER appuser

EXPOSE 5001
CMD ["python", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5001"]
