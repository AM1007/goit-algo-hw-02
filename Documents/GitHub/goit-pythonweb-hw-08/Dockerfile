FROM python:3.13-slim

RUN apt-get update && apt-get install -y gcc curl

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /src

COPY . /src

RUN poetry install --no-interaction --no-dev

EXPOSE 8000

CMD ["python3", "main.py"]
