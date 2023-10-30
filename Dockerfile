FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /educational_platform
COPY pyproject.toml poetry.lock /educational_platform/

RUN pip install -U pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install
COPY . ./
COPY ../.env ./.env
EXPOSE 8000
ENTRYPOINT ["bash", "-c", "/educational_platform/entrypoint.sh"]