# Use the official uv image which already includes python and uv
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS runtime-environment

# No need to install pip or uv here! They are already present and optimized.

# Set up the working directory early
WORKDIR /home/kedro_docker

# add kedro user
ARG KEDRO_UID=999
ARG KEDRO_GID=0
RUN groupadd -f -g ${KEDRO_GID} kedro_group && \
    useradd -m -d /home/kedro_docker -s /bin/bash -g ${KEDRO_GID} -u ${KEDRO_UID} kedro_docker

# Install dependencies first (better for layer caching)
COPY --chown=${KEDRO_UID}:${KEDRO_GID} requirements.txt ./
RUN uv pip install --system --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY --chown=${KEDRO_UID}:${KEDRO_GID} . .

USER kedro_docker

EXPOSE 8888

CMD ["kedro", "run"]