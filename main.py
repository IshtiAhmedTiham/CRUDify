from fastapi import FastAPI
from src.routes.v1.router import router as v1_router
from src.controllers.api.v1.user.database import init_db
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app : FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(v1_router, prefix="/api/v1")



