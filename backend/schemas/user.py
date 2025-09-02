from pydantic import BaseModel, EmailStr, validator
from utils.validators import validate_password

# Базовая схема
class UserBase(BaseModel):
    email: EmailStr

# Создание пользователя
class UserCreate(UserBase):
    password: str

    @validator("password")
    def validate_user_password(cls, value):
        return validate_password(value)

# Ответ при возврате из БД
class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
