from fastapi import FastAPI
import redis
import uuid
import os


app = FastAPI()


r = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    decode_responses=True
)


@app.post("/jobs")
def create_job():
    job_id = str(uuid.uuid4())
    r.lpush("jobs", job_id)
    r.hset(f"job:{job_id}", "status", "queued")
    return {"id": job_id, "status": "submitted"}


@app.get("/jobs/{job_id}")
def get_job(job_id: str):
    try:
        status = r.hget(f"job:{job_id}", "status")
        if not status:
            return {"error": "not found"}
        return {"job_id": job_id, "status": status}
    except Exception as e:
        return {"error": str(e)}


@app.get("/")
def read_root():
    return {"status": "API is running"}


@app.get("/redis-status")
def redis_status():
    try:
        pong = r.ping()
        if pong:
            return {"status": "Redis is reachable"}
        return {"status": "Redis not responding"}, 503
    except Exception:
        # If redis connection fails, return 503
        return {"status": "Redis connection failed"}, 503


@app.get("/api/example")
def example_endpoint():
    return {"result": "Example endpoint works!"}
