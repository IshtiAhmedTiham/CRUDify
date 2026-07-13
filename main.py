from fastapi import FastAPI
from src.routers.v1.router import router
from contextlib import asynccontextmanager
from src.config.v1.postgresql_database import postgresql_init_db
from src.config.v1.sqlite_database import sqlite_init_db

@asynccontextmanager
async def lifespan(app:FastAPI):
    postgresql_init_db()
    sqlite_init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router,prefix="/api/v1")
