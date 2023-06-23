FROM python:3.10-slim
RUN pip install poetry
WORKDIR /
COPY pyproject.toml poetry.lock /
RUN poetry install --no-root --no-interaction --no-ansi
COPY . /
WORKDIR /
EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]