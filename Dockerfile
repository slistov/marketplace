FROM alpine:3.18.4

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

COPY ./alembic.ini /app/alembic.ini
COPY ./alembic /app/alembic

RUN apk add --no-cache --update py-pip bash

RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "app.categories.routers.main:app"]
