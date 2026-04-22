# Building a Full-Stack DevOps System with CI/CD, Docker, Redis, and GitHub Actions (HNG Stage 2 Project)

# Introduction

This project demonstrates a complete DevOps workflow for a containerized full-stack system. It includes a frontend, backend API, worker service, Redis queue, and a fully automated CI/CD pipeline using GitHub Actions.

The goal is to simulate a real-world production system with proper software engineering and DevOps practices: testing, linting, security scanning, integration testing, and automated deployment.

# System Architecture

The system is composed of four core services:

- Frontend → User interface for interacting with the system
- API (FastAPI) → Handles job creation and status tracking
- Worker Service → Processes jobs asynchronously from Redis
- Redis → Message broker for queue management

# Data Flow

1. User submits a job via frontend or API
2. API pushes job ID into Redis queue
3. Worker consumes job from Redis
4. Worker processes job and updates status
5. API retrieves updated status

This architecture ensures asynchronous processing, scalability, and decoupled services.

# Technologies Used

- FastAPI (Python backend)
- Redis (queue system)
- Node.js (frontend)
- Docker & Docker Compose
- GitHub Actions (CI/CD)
- Pytest (testing)
- Flake8 (Python linting)
- ESLint (JavaScript linting)
- Hadolint (Docker linting)
- Trivy (security scanning)

# Project Structure

hng14-stage2-devops/
│
├── api/ (FastAPI backend)
├── worker/ (Background job processor)
├── frontend/ (UI application)
├── docker-compose.yml
├── .github/workflows/
│ └── pipeline.yml
└── README.md

# Running the Project Locally

# 1. Clone the repository

```bash
git https://github.com/Godwin-Techie/hng14-stage2-devops.git
cd hng14-stage2-devops
```

# 2. Start all services

```bash
docker compose up --build
```

# Access Services

| Service  | URL                     |
| -------- | ----------------------- |
| Frontend | [http://localhost:3000] |
| API      | [http://localhost:8000] |
| Redis    | Internal only           |

# API Endpoints

# Create a Job

POST/jobs

# Response

{
"id": "uuid",
"status": "submitted"
}

# Get Job Status

GET /jobs/{job_id}

# Response

{
"job_id": "uuid",
"status": "queued | processing | completed"
}

# System Behavior

When the system is running correctly:
API receives requests
Jobs are queued in Redis
Worker processes jobs in background
Status is updated dynamically
Frontend reflects real-time updates

# Testing Strategy

The project includes automated tests using Pytest.
Run tests locally:

```bash
pip install -r api/requirements.txt
PYTHONPATH=. pytest api/tests --cov=api
```

# What is tested:

-API endpoint functionality
-Job creation logic
-Redis queue interactions (mocked)

# Environment Variables

-REDIS_HOST=redis
-REDIS_PORT=6379
-API_URL=http://localhost:8000
-APP_ENV=production

# CI/CD Pipeline Overview

The project uses GitHub Actions to automate the entire software lifecycle.

# Pipeline Flow:

lint → test → build → security scan → integration test → deploy

# CI/CD Breakdown

# 1. Lint Stage

-Ensures code quality:
-Python: Flake8
-JavaScript: ESLint
-Docker: Hadolint

# 2. Test Stage

-Runs Pytest unit tests
-Uses mocked Redis
-Generates coverage reports

# 3. Build Stage

-Builds Docker images for all services
-Tags images with commit SHA

# 4. Security Stage

-Runs Trivy vulnerability scan
-Fails pipeline on CRITICAL issues

# 5. Integration Stage

-Spins up full system in CI environment
-Sends real HTTP requests
-Validates response correctness

# 6. Deployment Stage

-Stops old container
-Builds new image
-Starts updated container
-Ensures safe rollout

# Deployment Strategy

-A simple rolling deployment approach:
-Stop existing container
-Build new Docker image
-Start new container
-Verify service health
-Replace old version safely

# Expected Output

When system is running correctly:
-API → Running on http://0.0.0.0:8000
-Worker → Listening for jobs
-Redis → Active queue system
-Frontend → Running on http://localhost:3000

# Key DevOps Concepts Demonstrated

This project demonstrates:
-Microservices architecture
-Container orchestration
-CI/CD automation
-Security scanning
-Test-driven development
-Infrastructure as code principles
-Stateless service design

# Stopping the System

```bash
docker compose down
```

# Why This Project Matters

This system simulates a real production environment, where:
-Services are decoupled
-Jobs are processed asynchronously
-Deployments are automated
-Code quality is enforced before deployment

-It reflects how modern backend systems are built in industry environments.
