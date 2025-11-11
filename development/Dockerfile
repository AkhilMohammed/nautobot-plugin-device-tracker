# Build args for Nautobot version, Python version, and Docker Hub credentials
ARG NAUTOBOT_VER="2.4.7"
ARG PYTHON_VER="3.11"
ARG DOCKERHUB_USER
ARG DOCKERHUB_TOKEN

FROM networktocode/nautobot-dev:${NAUTOBOT_VER}-py${PYTHON_VER}

ARG NAUTOBOT_ROOT=/opt/nautobot

ENV NAUTOBOT_ROOT=${NAUTOBOT_ROOT}
ENV INVOKE_NAUTOBOT_APP_TEMPLATE_LOCAL=true

# Install Poetry with no virtualenv creation
RUN which poetry || curl -sSL https://install.python-poetry.org | python3 - && \
    poetry config virtualenvs.create false

WORKDIR /source
COPY . /source

# Configure Poetry to use Docker Hub registry for private packages
RUN poetry config http-basic.dockerhub "$DOCKERHUB_USER" "$DOCKERHUB_TOKEN"

ARG CI

RUN if [ -z "${CI+x}" ]; then \
      PY_VER="${PYTHON_VER:-3.11}"; \
      INSTALLED_NAUTOBOT_VER=$(pip show nautobot | grep "^Version" | sed "s/Version: //"); \
      poetry add --lock nautobot@${INSTALLED_NAUTOBOT_VER} --python ${PY_VER} || \
      poetry add --lock git+https://github.com/nautobot/nautobot.git#${NAUTOBOT_VER} --python ${PY_VER}; \
    fi


RUN poetry install --extras all --with dev

COPY development/nautobot_config.py ${NAUTOBOT_ROOT}/nautobot_config.py

