# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base, sessionmaker


# DATABASE_URL = "postgresql://postgres:hello@localhost/fitness"
# engine = create_engine(DATABASE_URL)
# def get_engine():
#     return engine

# Base = declarative_base()

# session_local = sessionmaker(autocommit=False, autoflush=False, bind=get_engine())
# def get_db():
#     db = session_local()
#     try:
#         yield db
#     finally:
#         db.close()


# def init_db():
#     from . import model
#     model.Base.metadata.create_all(bind=get_engine())