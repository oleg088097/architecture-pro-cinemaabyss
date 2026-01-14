from fastapi import Response, Request, FastAPI
import json
import os
import requests
import random
from fastapi.responses import JSONResponse

EXCLUDED_HEADERS = {
    "content-length",
    "transfer-encoding",
    "connection",
}

port = os.getenv("PORT", "80")
MONOLITH_URL = os.getenv("MONOLITH_URL")
MOVIES_SERVICE_URL = os.getenv("MOVIES_SERVICE_URL")
EVENTS_SERVICE_URL = os.getenv("EVENTS_SERVICE_URL")
GRADUAL_MIGRATION = os.getenv("GRADUAL_MIGRATION", "false")
MOVIES_MIGRATION_PERCENT = int(os.getenv("MOVIES_MIGRATION_PERCENT", "0"))
app = FastAPI()

@app.get("/api/movies/health")
async def movies_proxy(request: Request):
    r = requests.get(f'{MOVIES_SERVICE_URL}/api/movies/health')

    return Response(
        content=r.content,
        status_code=r.status_code,
        headers={
            k: v for k, v in r.headers.items() if k.lower() not in EXCLUDED_HEADERS
        }
    )

@app.get("/api/movies")
@app.post("/api/movies")
async def movies_proxy(request: Request):
    body = await request.body()
    if GRADUAL_MIGRATION == 'true' and random.randrange(1, 100) < MOVIES_MIGRATION_PERCENT:
        r = requests.request(request.method,
                             f'{MOVIES_SERVICE_URL}{request.url.path}',
                             data=body,
                             params=request.query_params,)
    else:
        r = requests.request(request.method,
                             f'{MONOLITH_URL}{request.url.path}',
                             data=body,
                             params=request.query_params,)

    return Response(
        content=r.content,
        status_code=r.status_code,
        headers={
            k: v for k, v in r.headers.items() if k.lower() not in EXCLUDED_HEADERS
        }
    )


@app.get("/api/users")
@app.post("/api/users")
async def users_proxy(request: Request):
    body = await request.body()
    r = requests.request(request.method,
                         f'{MONOLITH_URL}{request.url.path}',
                         data=body,
                         params=request.query_params,)

    return Response(
        content=r.content,
        status_code=r.status_code,
        headers={
            k: v for k, v in r.headers.items() if k.lower() not in EXCLUDED_HEADERS
        }
    )

@app.get("/health")
async def send_config():
    return {
        "status": "ok"
    }
