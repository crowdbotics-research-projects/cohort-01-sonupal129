from fastapi import Request, HTTPException, status
from .utils import (ALGORITHM, JWT_SECRET_KEY)
from jose import jwt
from .schema import UserDetail
from datetime import datetime
from .models import User
# Code Block


def verify_token(request:Request):
    try:
        authorization_token = request.headers['Authorization']
        payload = jwt.decode(authorization_token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        if datetime.fromtimestamp(payload["exp"]) < datetime.now():
            raise HTTPException(
                status=status.HTTP_401_UNAUTHORIZED,
                detail='Token Expired!'
            )
    except KeyError:
        raise HTTPException(status_code=401, detail="Token not provided!")
    except:
        raise HTTPException(status_code=401, detail="Invalid Token!")
    user = User.get_user(payload["sub"])
    return UserDetail(username=user.username, email=user.email)