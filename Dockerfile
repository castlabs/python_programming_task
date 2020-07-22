FROM ubuntu:20.04
MAINTAINER Pedro José Piquero Plaza <pedropiqueroplaza@gmail.com>

ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.0.9 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry'

RUN apt-get update -y \
    && apt-get install --no-install-recommends -y \
    gunicorn python3-pip python3-venv curl \
    && apt-get autoremove -y \
    && apt-get clean -y

RUN pip3 install "poetry==$POETRY_VERSION"

COPY . /flask-api
WORKDIR /flask-api

RUN poetry install --no-dev

CMD ["gunicorn", "-b 0.0.0.0:5000", "castlabs_proxy:create_app()"]

EXPOSE 5000