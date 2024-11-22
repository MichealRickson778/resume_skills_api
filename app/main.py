from fastapi import FastAPI
from app.api.routes import router
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME)

@app.on_event("startup")
async def startup():
    print(f"Starting {settings.APP_NAME} in {settings.ENV} environment")

@app.on_event("shutdown")
async def shutdown():
    print("Shutting down the application")

app.include_router(router, prefix="/api")
