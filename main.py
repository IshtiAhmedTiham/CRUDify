from fastapi import FastAPI
from src.routers.v1.router import router
from contextlib import asynccontextmanager
from src.config.v1.database import init_db

@asynccontextmanager
async def lifespan(app:FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router,prefix="/api/v1")
