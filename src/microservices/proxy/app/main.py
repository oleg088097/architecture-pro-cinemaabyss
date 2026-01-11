from fastapi import Response, FastAPI
import json
import os
import requests
import random
from fastapi.responses import JSONResponse

port = os.getenv("PORT", "80")
MONOLITH_URL = os.getenv("MONOLITH_URL")
MOVIES_SERVICE_URL = os.getenv("MOVIES_SERVICE_URL")
EVENTS_SERVICE_URL = os.getenv("EVENTS_SERVICE_URL")
GRADUAL_MIGRATION = os.getenv("GRADUAL_MIGRATION", "false")
MOVIES_MIGRATION_PERCENT = int(os.getenv("MOVIES_MIGRATION_PERCENT", "0"))
app = FastAPI()

@app.get("/api/movies")
async def send_config():
    if GRADUAL_MIGRATION == 'true' and random.randrange(1, 100) < MOVIES_MIGRATION_PERCENT:
        r = requests.get(f'{MOVIES_SERVICE_URL}/api/movies')
    else:
        r = requests.get(f'{MONOLITH_URL}/api/movies')

    return r.json()

@app.get("/api/users")
async def send_config():
    r = requests.get(f'{MONOLITH_URL}/api/users')
    return Response(
        content=r.content,
        status_code=r.status_code,
        headers=dict(r.headers) # Convert requests headers (CaseInsensitiveDict) to a standard dict
    )

@app.get("/health")
async def send_config():
    return {
        "status": "ok"
    }
