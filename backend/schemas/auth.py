from pydantic import BaseModel, EmailStr, validator
from utils.validators import validate_password

class UserRegister(BaseModel):
    email: EmailStr
    password: str

    @validator("password")
    def validate_register_password(cls, value):
        return validate_password(value)

class UserLogin(BaseModel):
    email: EmailStr
    password: str

    @validator("password")
    def validate_login_password(cls, value):
        return validate_password(value)

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
