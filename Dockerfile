FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8010

# Set the environment variables

ENV REDIS_URL=redis://127.0.0.1:6379/2

CMD python manage.py migrate_and_createsuperuser && gunicorn --config gunicorn_conf.py core.wsgi --preload
