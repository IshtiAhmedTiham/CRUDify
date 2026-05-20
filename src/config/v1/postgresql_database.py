from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from src.config.v1.base import Base


POSTGRESQL_DATABASE_URL = "postgresql://postgres:hello@localhost/fitness"
def get_engine():
    engine = create_engine(POSTGRESQL_DATABASE_URL)
    return engine


session_local = sessionmaker(autocommit=False, autoflush=False, bind=get_engine())
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

def init_db():
    from src.models.v1.user_model import UserModel 
    Base.metadata.create_all(bind=get_engine())