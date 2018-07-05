FROM python:3.6.6-slim

# Install basic development tools
RUN set -ex; \
        \
        apt-get update; \
        apt-get install -y --no-install-recommends \
            bash \
            curl \
            jq \
            wget; \
        \
        rm -rf /var/lib/apt/lists/*;


# Copy in Python package requirements files
WORKDIR /opt/pipenv
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock


# Install build dependencies and Python packages
RUN set -ex; \
        \
        buildDeps=" \
            gcc \
            git \
            libc6-dev \
            libffi-dev \
            libssl-dev \
        "; \
        \
        apt-get update; \
        apt-get install -y $buildDeps --no-install-recommends; \
        rm -rf /var/lib/apt/lists/*; \
        \
        python -m pip install --no-cache-dir virtualenv; \
        python -m pip install --no-cache-dir pipenv; \
        pipenv --python 3 install --system --verbose;\
        python -m pip uninstall --yes pipenv; \
        rm -f Pipfile Pipfile.lock; \
        \
        apt-get purge -y --auto-remove $buildDeps;


# Install BATS in /usr/local
WORKDIR /tmp
RUN set -ex; \
        \
        buildDeps=" \
            git \
        "; \
        \
        apt-get update; \
        apt-get install -y $buildDeps --no-install-recommends; \
        rm -rf /var/lib/apt/lists/*; \
        \
        git clone https://github.com/sstephenson/bats.git; \
        cd bats; \
        ./install.sh /usr/local; \
        cd ../; \
        rm -rf bats; \
        \
        apt-get purge -y --auto-remove $buildDeps;


# Prevent python from creating .pyc files and __pycache__ dirs
ENV PYTHONDONTWRITEBYTECODE=1


# Show stdout when running in docker compose (dont buffer)
ENV PYTHONUNBUFFERED=1


# Add a python startup file
COPY pystartup /usr/local/share/python/pystartup
ENV PYTHONSTARTUP=/usr/local/share/python/pystartup


# Add an entry point script.
COPY entry.sh /usr/local/bin/entry.sh
RUN set -ex; \
    chmod 755 /usr/local/bin/entry.sh;
