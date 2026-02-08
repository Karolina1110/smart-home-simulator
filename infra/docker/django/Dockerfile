FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade pip 

COPY backend/django/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/django .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
