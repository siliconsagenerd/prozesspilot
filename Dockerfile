FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml .
COPY src ./src
COPY alembic ./alembic
COPY alembic.ini .
COPY data ./data
RUN pip install --no-cache-dir .
ENV PYTHONPATH=/app/src
CMD ["prozesspilot", "serve", "--host", "0.0.0.0", "--port", "8000"]