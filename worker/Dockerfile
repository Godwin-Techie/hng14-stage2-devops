# =========================
# STAGE 1: BUILDER
# =========================
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --user --no-cache-dir redis


# =========================
# STAGE 2: RUNTIME
# =========================
FROM python:3.11-slim

WORKDIR /app

# create non-root user
RUN useradd -m appuser

# copy installed dependencies from builder
COPY --from=builder /root/.local /home/appuser/.local

# copy application code
COPY . .

# ensure PATH includes installed packages
ENV PATH=/home/appuser/.local/bin:$PATH

USER appuser

# lightweight safe healthcheck
HEALTHCHECK --interval=10s --timeout=5s --retries=5 --start-period=20s \
CMD python -c "import redis; print('ok')" || exit 1

CMD ["python3", "worker.py"]