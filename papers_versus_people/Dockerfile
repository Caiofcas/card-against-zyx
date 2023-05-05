FROM python:3.10.6

WORKDIR /app
COPY ./.env .
COPY ./pyproject.toml .
COPY ./poetry.lock .


# install poetry and dependencies

WORKDIR /app/papers_versus_people
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH="/root/.local/bin:${PATH}"
RUN poetry config virtualenvs.create false
RUN poetry install

WORKDIR /app
