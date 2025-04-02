FROM ghcr.io/tenstorrent/tt-metal/tt-metalium-ubuntu-22.04-amd64-release:latest-rc AS release

# Install system-level dependencies (using apt-get)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libgl1-mesa-glx \
        git-lfs \
        libsndfile1 \
        docker.io && \
    rm -rf /var/lib/apt/lists/*  # Clean up apt cache

# Initialize git lfs (must be done before any git operations)
RUN git lfs install

# Upgrade pip (best practice before installing Python packages)
RUN python3 -m pip install --upgrade pip

# Set the extra index URL for pip (for PyTorch)
RUN python3 -m pip config set global.extra-index-url https://download.pytorch.org/whl/cpu

# Install Python dependencies from requirements-dev.txt and pytest-github-report
COPY requirements-dev.txt /tmp/requirements-dev.txt
COPY requirements.txt /tmp/requirements.txt

RUN python3 -m pip install --no-cache-dir -r /tmp/requirements-dev.txt && \
    python3 -m pip install --no-cache-dir pytest-github-report

# Clean up the temporary requirements files
RUN rm /tmp/requirements-dev.txt /tmp/requirements.txt
