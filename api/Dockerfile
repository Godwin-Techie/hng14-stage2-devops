
# STAGE 1: BUILDER
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt



# STAGE 2: RUNTIME
FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/* # install curl for healthcheck
RUN adduser --disabled-password --gecos "" appuser
COPY --from=builder /root/.local /home/appuser/.local
COPY . .
ENV PATH=/home/appuser/.local/bin:$PATH
USER appuser
EXPOSE 8000
HEALTHCHECK --interval=10s --timeout=5s --retries=15 --start-period=40s \
CMD curl -f http://localhost:8000/ || exit 1
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]