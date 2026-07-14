from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


POSTGRESQL_DATABASE_URL = "postgresql://postgres:hello@localhost/CRUDify"
def get_engine():
    engine = create_engine(POSTGRESQL_DATABASE_URL)
    return engine

Base  = declarative_base()

session_local = sessionmaker(autocommit=False, autoflush=False, bind=get_engine())
def get_db():
    db = session_local()
    try: 
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=get_engine())