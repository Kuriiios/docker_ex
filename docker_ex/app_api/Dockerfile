FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app
ENV UV_COMPILE_BYTECODE=1

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies (ignoring workspace members to keep it isolated)
RUN uv sync --frozen --no-cache --no-install-workspace

COPY . .

# Ensure the venv bin is in the path (extra safety)
ENV PATH="/app/.venv/bin:$PATH"

# Use uv run to execute uvicorn
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]