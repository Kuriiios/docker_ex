# Use the official UV image with Python 3.12
FROM python3.12-bookworm-slim

# Set the working directory
WORKDIR /app

# Enable bytecode compilation for faster startup
ENV UV_COMPILE_BYTECODE=1

# Copy the lockfile and pyproject.toml files first to leverage caching
# We include the sub-project pyprojects because they are part of the workspace
COPY uv.lock pyproject.toml ./
COPY docker_ex/app_front/pyproject.toml ./docker_ex/app_front/
COPY docker_ex/app_api/pyproject.toml ./docker_ex/app_api/

# Install the dependencies without installing the actual project code yet
# This layer is cached unless your dependencies change
RUN uv sync --frozen --no-install-project --no-dev

# Copy the rest of the source code
COPY . .

# Now install the project (this links your workspace members)
RUN uv sync --frozen --no-dev

# --- Final Runtime Stage ---
FROM python:3.12-slim-bookworm

WORKDIR /app

# Add kedro user for security
RUN groupadd -r kedro && useradd -r -g kedro kedro_user

# Copy the virtual environment from the builder
COPY --from=builder /app/.venv /app/.venv

# Copy the source code
COPY --from=builder --chown=kedro_user:kedro /app /app

# Set the PATH to use the virtual environment
ENV PATH="/app/.venv/bin:$PATH"

USER kedro_user

EXPOSE 8888

# The project.scripts section in your toml defines "docker-ex"
CMD ["kedro", "run"]