FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade pip 

COPY backend/django/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/django .

RUN apt-get update
RUN apt-get install netcat-openbsd
COPY backend/django/entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
