FROM python:3.9.5-slim

LABEL org.opencontainers.image.source https://github.com/samedamci/basedbin-frontend

EXPOSE 5000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV SERVER_HOSTNAME=localhost
ENV SERVER_PORT=5000

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "frontend:app"]
