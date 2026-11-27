from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.core.security import(verify_password, create_access_token,)
from app.core.dependencies import get_current_user
from app.database.connection import get_db
from app.entity.models.user import Users
from app.schemas.auth import (LoginRequest, TokenResponse, CurrentUserResponse)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

@router.post("/login", response_model = TokenResponse)
def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db)
   ):
    #Find user within the specific school
    user = db.query(Users).filter(
        Users.school_id == login_data.school_id,
        func.lower(Users.email) == login_data.email.lower()
    ).first()

    #verify account and password
    if(
        user is None or not user.is_active or not verify_password(login_data.password, user.password_hash)
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid school ID, email, or password",
        )

    #update last login
    user.last_login = datetime.now()
    db.commit()

    #Generate JWT
    access_token = create_access_token(
        user_id = user.id,
        school_id= user.school_id,
        role= user.role,
    )

    return {
        "access_token" : access_token,
        "token_type" : "bearer"
    }

@router.get("/me", response_model=CurrentUserResponse)
def get_me(
       current_user : Users = Depends(get_current_user)
    ):
    return current_user