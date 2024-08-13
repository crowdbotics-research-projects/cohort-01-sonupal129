from pydantic import BaseModel, EmailStr


# Code Blcok

class UserSignup(BaseModel):
    username: str
    password: str
    email: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserToken(BaseModel):
    token: str

class UserDetail(BaseModel):
    username: str
    email: str

class UserPasswordReset(BaseModel):
    password: str