from passlib.context import CryptContext
import os
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt

# Code Block
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"

# Temp

print("Setting up Temporary Secret Key for now")
JWT_SECRET_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.IntcbiAgIFwiaXNzXCI6IFwibXlfaXNzdXJlclwiLFxuICAgXCJpYXRcIjogMTQwMDA2MjQwMDIyMyxcbiAgIFwidHlwZVwiOiBcIi9vbmxpbmUvc3RhdHVzL3YyXCIsXG4gICBcInJlcXVlc3RcIjoge1xuICAgICBcInRyYW5zYWN0aW9uX2lkXCI6IFwidHJhXzc0MzQ3MDgyXCIsXG4gICAgIFwibWVyY2hhbnRfaWRcIjogXCJtZXJjX2E3MTQxdXRuYTg0XCIsXG4gICAgIFwic3RhdHVzXCI6IFwiU1VDQ0VTU1wiXG4gICB9XG4gfSI.U-W6AF8IPyatr8s9VXkZIb2LOJPu0GjNXss8kRfC610"
JWT_REFRESH_SECRET_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.IntcbiAgIFwiaXNzXCI6IFwibXlfaXNzdXJlclwiLFxuICAgXCJpYXRcIjogMTQwMDA2MjQwMDIyMyxcbiAgIFwidHlwZVwiOiBcIi9vbmxpbmUvc3RhdHVzL3YyXCIsXG4gICBcInJlcXVlc3RcIjoge1xuICAgICBcInRyYW5zYWN0aW9uX2lkXCI6IFwidHJhXzc0MzQ3MDgyXCIsXG4gICAgIFwibWVyY2hhbnRfaWRcIjogXCJtZXJjX2E3MTQxdXRuYTg0XCIsXG4gICAgIFwic3RhdHVzXCI6IFwiU1VDQ0VTU1wiXG4gICB9XG4gfSI.6jRuw7bhl1H5e55nben2oPhF1u8zJXYvBxbPbtmWH1g"



password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)

def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt

def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt