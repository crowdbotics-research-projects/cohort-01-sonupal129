from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://app_user:app_password@db/app"
# SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
metadata = MetaData()
# metadata.reflect(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()