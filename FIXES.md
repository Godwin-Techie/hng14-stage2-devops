API SERVICES

1. api/.env/
   file: .env/
   Issue: .env/ file is not suppose to be pushed to a Repo
   fix: Deleted the file, since it was not even needed for the project at hand.

2. File: api/main.py  
   Line: 9  
   Issue: Redis host was hardcoded as `"localhost"`, which will fail inside Docker because containers communicate by service name on the internal network  
   Fix: Changed to use environment variables with sensible defaults and enabled `decode_responses` so Redis returns strings directly.

3. File: api/main.py
   Line: 13 (create_job function)  
   Issue: Jobs were pushed to the wrong list ("job" instead of "jobs"), causing mismatch with worker expectations.
   Fix: Corrected the queue name to "jobs".

4. File: api/main.py
   Line: 16 (create_job response)  
   Issue: API response only returned {"job_id": job_id}.
   Fix: Updated the response to include both the ID and a "submitted" status

5. File: api/main.py
   Line: 21 (get_job function)  
   Issue: Used .decode() on Redis values, which caused errors because decode_responses=True already returns strings.
   Fix: Removed .decode() and returned the status directly.

6. File: api/main.py
   Line: 20–27 (get_job function)  
   Issue: No error handling for Redis connection issues.
   Fix: Wrapped the call in a try/except block to return a JSON error message if something goes wrong.

7. File: api/main.py
   Line: 30 (root endpoint)  
   Issue: No health endpoint existed to confirm API was running.
   Fix: Added a root route

FRONTEND SERVICES

8. File: frontend/app.js  
   Line: 6 (API_URL definition)  
   Issue: API URL was hardcoded as `"http://localhost:8000"`, which breaks when running inside Docker because the frontend container cannot reach `localhost` of the host machine.  
   Fix: Changed to use an environment variable with a default fallback

9. File: frontend/app.js
   Line: 11–18 (submit route)  
    Issue 1: No timeout was set for Axios requests, which could cause the frontend to hang indefinitely if the API is unresponsive.
   Fix: Added a timeout option to Axios POST requests
   Issue 2: Error handling was generic ("something went wrong") and did not log useful details.
   Fix: Improved error handling by logging the error message and returning it in the response

10. File: frontend/app.js
    Line: 29 (app.listen)  
    Issue: Server was bound only to localhost, making it inaccessible from outside the container.
    Fix: Changed to bind to "0.0.0.0" so the service is reachable externally

11. File: frontend/app.js
    Line: 10 (health route)  
    Issue: No health check endpoint existed to confirm the frontend was running.
    Fix: Added a /health route

12. File: frontend/views/index.html  
    Line: 22 (submitJob function)  
    Issue: No feedback was shown while submitting a job, and the code referenced `data.job_id` which no longer matched the API response format.  
    Fix: Added a "Submitting..." message before the request, and updated to use `data.id` instead of `data.job_id`

13. File: frontend/views/index.html
    Line: 22–28 (submitJob function)  
    Issue: No error handling existed for failed submissions.
    Fix: Wrapped the request in a try/catch block, logged the error, and displayed a user‑friendly message

14. File: frontend/views/index.html
    Line: 30–37 (pollJob function)  
    Issue 1: Polling loop could run indefinitely if a job never completed.
    Fix: Added an attempts counter with a maximum of 10 retries.
    Issue 2: If Redis returned no status, the UI would break.
    Fix: Defaulted to "unknown" when status was missing:

WORKER SERVICES

15. File: worker/worker.py  
    Line: 7
    Issue: Redis host was hardcoded as `"localhost"`, which fails inside Docker because containers communicate by service name on the internal network.  
    Fix: Changed to use environment variables with sensible defaults and enabled `decode_responses` so Redis returns strings directly.

16. File: worker/worker.py
    Line: 18
    Issue: Worker was listening on the wrong Redis list ("job" instead of "jobs"), causing mismatch with the API.
    Fix: Corrected the queue name to "jobs"

17. File: worker.py
    Line: 21
    Issue: Used .decode() on job IDs, which caused errors because decode_responses=True already returns strings.
    Fix: Removed .decode() and passed the job ID directly

18. File: worker.py
    Line: 10 (process_job function)  
    Issue: Function worked but lacked type hints and clarity.
    Fix: Added a type hint for job_id and improved readability

MISSING FILES/CONFIGURATIONS

19. File: .gitignore  
    Issue: No `.gitignore` file was present, meaning heavy files (e.g. `node_modules/`, `__pycache__/`, logs, build artifacts) could accidentally be committed.  
    Fix: Added a `.gitignore` file to exclude unnecessary and sensitive files.

20. File: .env.example  
    Issue: No environment variable template was provided, making it unclear which variables are required.  
    Fix: Added `.env.example` with placeholder values for `REDIS_HOST`, `REDIS_PORT`, `API_URL`, etc.

21. File: README.md  
    Issue: No documentation existed to explain how to set up and run the stack.  
    Fix: Added a `README.md` with prerequisites, setup instructions, and expected outputs.

22. File: FIXES.md  
    Issue: No record of bugs and fixes was included.  
    Fix: Created `FIXES.md` documenting every bug found, file, line, issue, and fix.

23. File: GitHub Actions workflow (e.g. `.github/workflows/ci.yml`)  
    Issue: No CI/CD pipeline configuration was present.  
    Fix: Added a workflow file implementing lint → test → build → security scan → integration test → deploy stages.

24. File: Unit tests (e.g. `tests/test_api.py`)  
    Issue: No unit tests existed for the API.  
    Fix: Added at least 3 pytest unit tests with Redis mocked, plus coverage reporting.

25. File: Healthcheck endpoints  
    Issue: Frontend and API lacked health endpoints.  
    Fix: Added `/health` route in frontend and root `/` route in API to confirm services are running.

26. File: Dockerfiles (for api, frontend, worker)  
    Issue: No Dockerfiles were present initially, meaning services couldn’t be containerized.  
    Fix: Created production‑quality Dockerfiles for each service with non‑root users, health checks, and multi‑stage builds where appropriate.

27. File: docker-compose.yml  
    Issue: No Compose file was present to orchestrate the stack.  
    Fix: Added `docker-compose.yml` with named internal network, dependency health checks, resource limits, and environment variable configuration.

28. file: README.md
    issue: not properly documented
    fixed: added a well structed write-up that explains how to bring the entire stack up on a clean machine from scratch — list prerequisites, all commands, and what a successful startup looks like.
