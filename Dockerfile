FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /educational_platform
COPY pyproject.toml /temp/pyproject.toml
COPY educational_platform /educational_platform
EXPOSE 8000

RUN mkdir /educational_platform/static && chown -R educational_platform:educational_platform /educational_platform && chmod 755 /educational_platform
COPY --chown=educational_platform:educational_platform . .

RUN pip install -r /temp/pyproject.toml

RUN adduser --disabled-password platform-user

USER platform-user