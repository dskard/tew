FROM gliderlabs/alpine:3.4

# Install base packages and build dependencies
RUN set -ex; \
    apk add --no-cache \
      bash \
      python \
      python3 \
      py-setuptools; \
    apk add --no-cache --virtual build-dependencies \
      git \
      py-pip \
      wget;

# Install BATS in /usr/local
RUN set -ex; \
    git clone https://github.com/sstephenson/bats.git; \
    cd bats; \
    ./install.sh /usr/local; \
    cd ../; \
    rm -rf bats;

# Install Python modules through pipenv
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN set -ex; \
    pip install pipenv; \
    pipenv install --system;\
    pip uninstall --yes pipenv; \
    pip3 install pipenv; \
    pipenv install --system;\
    pip3 uninstall --yes pipenv; \
    rm -f Pipfile Pipfile.lock;

# Clean up unnecessary packages
RUN apk del build-dependencies;

# Prevent python from creating .pyc files and __pycache__ dirs
ENV PYTHONDONTWRITEBYTECODE=1

# Add a python startup file
COPY pystartup /usr/local/share/python/pystartup
ENV PYTHONSTARTUP=/usr/local/share/python/pystartup
