from fastapi import FastAPI
from app.routers import auth#, users
from app.database import engine, Base



# Create the tables.
Base.metadata.create_all(bind = engine)



# Initialize the FastAPI application and include the routers.
app = FastAPI(title = "Authentication Service")
app.include_router(auth.router)
#app.include_router(users.router)