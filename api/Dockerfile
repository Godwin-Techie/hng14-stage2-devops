# =========================
# STAGE 1: BUILDER
# =========================
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --user --no-cache-dir fastapi uvicorn redis


# =========================
# STAGE 2: RUNTIME
# =========================
FROM python:3.11-slim

WORKDIR /app

# install curl for healthcheck
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# create non-root user
RUN useradd -m appuser

# copy installed python packages from builder
COPY --from=builder /root/.local /home/appuser/.local

# copy app code
COPY . .

# ensure pip packages are accessible
ENV PATH=/home/appuser/.local/bin:$PATH

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=10s --timeout=5s --retries=15 --start-period=40s \
CMD curl -f http://localhost:8000/ || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]