FROM python3.12-bookworm-slim

WORKDIR /app

# 1. Force UV to ignore any parent workspaces
ENV UV_PROJECT_ENVIRONMENT=/app/.venv
ENV UV_NO_WORKSPACE=1

# 2. Copy dependency files first
COPY pyproject.toml uv.lock ./

# 3. Install - explicitly naming the package helps if the toml is tricky
RUN uv sync --frozen --no-cache

# 4. Copy source code
COPY . .

# 5. Set Path
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8501

# 6. Verify the file exists (This will show in your build logs!)
RUN ls -la /app/.venv/bin/streamlit

# Replace your previous CMD with this:
CMD ["uv", "run", "streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]