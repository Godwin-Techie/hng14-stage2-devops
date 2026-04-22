import redis
import time
import os
import signal

# Use environment variables so it works locally and in Docker
r = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port = int(os.getenv("REDIS_PORT") or "6379"),
    decode_responses=True  # ensures values are returned as strings, not bytes
)

def process_job(job_id: str):
    print(f"Processing job {job_id}")
    time.sleep(2)  # simulate work
    r.hset(f"job:{job_id}", "status", "completed")
    print(f"Done: {job_id}")

while True:
    job = r.brpop("jobs", timeout=5)
    if job:
        _, job_id = job
        process_job(job_id)  # no need to decode if decode_responses=True
