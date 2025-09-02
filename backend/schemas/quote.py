from pydantic import BaseModel, validator

class QuoteBase(BaseModel):
    tariff: str
    age: int
    experience: int
    car_type: str
    price: float

    @validator("age")
    def validate_age(cls, value):
        if value < 18:
            raise ValueError("Age must be at least 18")
        return value

    @validator("experience")
    def validate_experience(cls, value):
        if value < 0:
            raise ValueError("Experience must be non-negative")
        return value

class QuoteCreate(QuoteBase):
    pass

class QuoteOut(QuoteBase):
    id: int

    class Config:
        orm_mode = True
