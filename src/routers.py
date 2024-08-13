# FastAPI imports
from fastapi import APIRouter, status, Response, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from .dependency import verify_token
from .schema import UserSignup, UserLogin, UserToken, UserPasswordReset
from .utils import get_hashed_password, verify_password, create_access_token, create_refresh_token
from .models import User
from .database import session as db_session


router = APIRouter()

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user_data: UserSignup):
    user = User.get_user(user_data.username)
    print(user)
    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist"
        )

    data = {
        "email": user_data.email,
        "username": user_data.username,
        "hashed_password": get_hashed_password(user_data.password),
    }
    db_user = User(**data)
    db_session.add(db_user)
    db_session.commit()
    db_session.refresh(db_user)
    return JSONResponse(content={"success": True})


@router.post("/login", status_code=status.HTTP_200_OK, response_model=UserToken)
def login(form_data: UserLogin):
    user = User.get_user(form_data.username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    return JSONResponse(content={
        "access_token": create_access_token(user.username),
        "refresh_token": create_refresh_token(user.username),
    })

@router.post("/reset-password")
def reset_password(password_serializer : UserPasswordReset, user = Depends(verify_token)):
    db_user = User.get_user(user.username)    
    db_user.hashed_password = get_hashed_password(password_serializer.password)
    db_session.commit()
    return JSONResponse(content={"message": "Password updated successfully!"})