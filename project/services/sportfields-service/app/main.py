# from fastapi import FastAPI
# from app.core.config import settings
# from app.routers import simple_user, owner

# app = FastAPI(
#     title="Sportfields Service",
#     version="0.1.0"
# )

# # include routers
# app.include_router(simple_user.router, prefix="/fields", tags=["fields"])
# app.include_router(owner.router, prefix="/owners", tags=["owners"])

# @app.get("/healthz", tags=["infra"])
# def healthz():
#     return {"status": "ok"}

from fastapi import FastAPI
from app.routers import simple_user, owner

app = FastAPI(
    title="Sportfields Service",
    version="0.1.0"
)

# Routers define their own full paths now, so include without any prefix:
app.include_router(simple_user.router)
app.include_router(owner.router)

@app.get("/healthz", tags=["infra"])
def healthz():
    return {"status": "ok"}
