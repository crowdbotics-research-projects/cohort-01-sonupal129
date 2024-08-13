from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import declarative_base, engine, metadata, session as db_session

Base = declarative_base(metadata=metadata)

def initialize_database():
    print("Creating tables")
    Base.metadata.create_all(bind=engine, checkfirst=True)

# CODE BLOCK

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
    @classmethod
    def get_user(cls, username:str):
        return db_session.query(cls).filter(cls.username == username).first()
    
# initialize_database()