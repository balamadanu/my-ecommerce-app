from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt.exceptions import InvalidTokenError
from sqlalchemy.orm import Session

from app.core.config import settings
from app.database.connection import get_db
from app.entity.models import Users

bearer_scheme = HTTPBearer()

def get_current_user(
        credentials: Annotated[HTTPAuthorizationCredentials, Depends(bearer_scheme)],
        db: Annotated[Session, Depends(get_db)]
    ) -> Users:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
       payload = jwt.decode(
           credentials.credentials,
           settings.SECRET_KEY,
           algorithms=[settings.ALGORITHM]
       )

       user_id = payload.get("sub")
       school_id = payload.get("school_id")

       if user_id is None or school_id is None:
           raise credentials_exception

       user_id = int(user_id)
       school_id = int(school_id)
  
    except(InvalidTokenError,ValueError, TypeError):
        raise credentials_exception

    user = db.query(Users).filter(
        Users.id == user_id,
        Users.school_id == school_id,
        Users.is_active.is_(True)
    ).first()

    if user is None:
        raise credentials_exception

    return user
    