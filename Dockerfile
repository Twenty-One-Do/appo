FROM python:3.11-slim-buster as builder

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.8.3

WORKDIR /app

COPY . /app

RUN pip install "poetry==$POETRY_VERSION"

RUN poetry install --without dev

CMD ["gunicorn", "-c", "gunicorn.conf.py", "appo_api.main:create_app"]