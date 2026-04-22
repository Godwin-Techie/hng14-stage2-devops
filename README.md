# Job Processing System (API + Worker + Redis + Frontend)

## Overview

This project is a simple distributed job processing system built with:

- FastAPI (Backend API)
- Redis (Queue)
- Python Worker (Background processing)
- Node.js (Frontend)
- Docker & Docker Compose

## Features

- Submit background jobs
- Track job status in real-time
- Asynchronous processing using Redis queue
- Fully containerized system

## Project Structure

- `/api` – FastAPI backend
- `/worker` – Background worker
- `/frontend` – Node.js frontend
- `docker-compose.yml` – Service orchestration

## Run Locally (Without Docker)

### 1. Start Redis

docker run -d -p 6379:6379 redis

### 2. Start API

cd api
uvicorn main:app --reload

### 3. Start Worker

cd worker
python worker.py

### 4. Start Frontend

cd frontend
node app.js

---

## Run with Docker

docker-compose up --build

---

## Access App

Frontend: http://localhost:3000
API: http://localhost:8000

---

## Notes

- Uses environment-based API URL switching for local vs Docker
- Redis queue name standardized as "jobs"
- Worker processes jobs asynchronously

---

## Author

Godwin Erharuyi
