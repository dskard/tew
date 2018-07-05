FROM ubuntu:xenial

# Install base packages and build dependencies
RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y \
        bash \
        curl \
        jq \
        python3 \
        python3-pip \
        virtualenv \
        wget; \
    apt-get install -y \
        g++ \
        gcc \
        git \
        libffi-dev \
        libc6-dev \
        libssl-dev \
        python3-dev; \
    rm -rf /var/lib/apt/lists/*;


# Install BATS in /usr/local
RUN set -ex; \
    git clone https://github.com/sstephenson/bats.git; \
    cd bats; \
    ./install.sh /usr/local; \
    cd ../; \
    rm -rf bats;


# Install Python modules through pipenv
# set workdir to anything other than / so pipenv
# can properly install packages
WORKDIR /opt/pipenv
COPY python3/Pipfile Pipfile
COPY python3/Pipfile.lock Pipfile.lock
RUN set -ex; \
    export LC_ALL=C.UTF-8; \
    export LANG=C.UTF-8; \
    python3 -m pip install --no-cache-dir pipenv; \
    pipenv --python 3 install --system --verbose;\
    python3 -m pip uninstall --yes pipenv; \
    rm -f Pipfile Pipfile.lock;


# Clean up unnecessary packages
RUN set -ex; \
    apt-get purge -y \
        g++ \
        gcc \
        git \
        libffi-dev \
        libc6-dev \
        libssl-dev \
        python3-dev; \
    apt-get autoremove -y;


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
