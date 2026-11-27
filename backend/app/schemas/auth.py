from pydantic import BaseModel, EmailStr, Field

class LoginRequest(BaseModel):
    school_id: int = Field(gt=0)
    email: EmailStr
    password: str = Field(min_length=1)

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class CurrentUserResponse(BaseModel):
    id: int
    school_id: int
    full_name: str
    email: EmailStr
    role: str
    is_active: bool