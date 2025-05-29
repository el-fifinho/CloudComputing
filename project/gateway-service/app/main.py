from fastapi import FastAPI
from app.proxy import router

app = FastAPI(title="Manual API Gateway")
app.include_router(router)
