from pydantic import BaseModel, EmailStr, validator
from utils.validators import validate_email

class ApplicationBase(BaseModel):
    fullname: str
    phone: str
    email: EmailStr
    tariff: str
    quote_id: int

    @validator("email")
    def validate_app_email(cls, value):
        return validate_email(value)

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationOut(ApplicationBase):
    id: int

    class Config:
        orm_mode = True
