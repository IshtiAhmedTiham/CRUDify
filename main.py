from fastapi import FastAPI 
from src.routers.v1.router import router
from src.config.v1.sqlite_database import init_db as sqlite_init_db
from src.config.v1.postgresql_database import init_db as postgresql_init_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app:FastAPI):
    sqlite_init_db()
    postgresql_init_db()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router)