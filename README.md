# Smart Home Simulator

Learning project to explore:
- Django & FastAPI
- Celery, RabbitMQ, Redis
- MQTT (Mosquitto)
- React
- Docker & Kubernetes

## Tech Stack
- Backend: Django, FastAPI
- Frontend: React
- Messaging: RabbitMQ, Redis, MQTT
- Infra: Docker, Docker Compose, Kubernetes

## Goals
- Understand distributed systems
- Practice real-world backend architecture
- Build a safe smart-home simulator


# How to run the Smart Home app

## Install Docker and Docker Compose

### For Windows/Mac
Install [Docker Desctop](https://www.docker.com/products/docker-desktop/)

### For Linux terminal
```bash
sudo apt update
sudo apt install docker.io docker-compose -y
sudo usermod -aG docker $USER
```

## Create containers
```bash
docker compose up -d
```

# How to test containers

## Postgres
```bash
set -a
source .env
set +a
docker compose exec postgres psql -U $DATABASE_USERNAME -d $DATABASE_NAME
```
You should see `smarthomedb=#`.

## Redis
```bash
docker compose exec redis redis-cli
PING
```
You should see `PONG`.

## Rabbitmq
Go to [Link](http://localhost:15672/)
You should see login page.

## Mosquitto
Subscribe to a topic.
```bash
docker compose exec mosquitto sh
mosquitto_sub -t test/topic
```
Open another terminal and send a message
```bash
docker compose exec mosquitto sh -c 'mosquitto_pub -t test/topic -m "hello mqtt"'
```
Go to the first terminal.
You should see ```hello mqtt`.

## Django
Go to [Link](http://localhost:8000/).
You should see login page.