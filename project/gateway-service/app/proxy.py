import os
from fastapi import APIRouter, Request, Response, HTTPException
import httpx

router = APIRouter()

# Backend URLs from env
AUTH_URL = os.getenv("AUTH_URL", "https://auth-service-cc-gvfyfdd4bhggbhah.francecentral-01.azurewebsites.net")
SPORT_URL = os.getenv("SPORT_URL", "https://sportfields-service-cfgggwa6akegh2hm.francecentral-01.azurewebsites.net")

@router.api_route("/auth/{path:path}", methods=["GET","POST","PUT","DELETE","PATCH","OPTIONS"])
async def auth_proxy(path: str, request: Request):
    backend = f"{AUTH_URL}/auth/{path}"
    async with httpx.AsyncClient() as client:
        # resp = await client.request(
        #     request.method, backend,
        #     headers=request.headers.raw,
        #     content=await request.body(),
        #     params=request.query_params
        # )
        forward_headers = {
            k: v
            for k, v in request.headers.items()
            if k.lower() != "host"
        }
        resp = await client.request(
            request.method,
            backend,
            headers=forward_headers,
            content=await request.body(),
            params=request.query_params,
        )
    return Response(resp.content, status_code=resp.status_code, headers=resp.headers)

@router.api_route("/{path:path}", methods=["GET","POST","PUT","DELETE","PATCH","OPTIONS"])
async def sport_proxy(path: str, request: Request):
    # everything not /auth/* goes to Sportfields Service
    backend = f"{SPORT_URL}/{path}"
    async with httpx.AsyncClient() as client:
        # resp = await client.request(
        #     request.method, backend,
        #     headers=request.headers.raw,
        #     content=await request.body(),
        #     params=request.query_params
        # )
        forward_headers = {
            k: v
            for k, v in request.headers.items()
            if k.lower() != "host"
        }
        resp = await client.request(
            request.method,
            backend,
            headers=forward_headers,
            content=await request.body(),
            params=request.query_params,
        )
    return Response(resp.content, status_code=resp.status_code, headers=resp.headers)
