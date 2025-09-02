from sqlalchemy import Column, Integer, String, Float, ForeignKey
from core.database import Base

class Quote(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True, index=True)
    tariff = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    experience = Column(Integer, nullable=False)
    car_type = Column(String, nullable=False)
    price = Column(Float, nullable=False)









# from pydantic import BaseModel
# import sqlalchemy
# from config import metadata






# applications = sqlalchemy.Table(
#     "applications",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id")),
#     sqlalchemy.Column("price", sqlalchemy.String),
#     sqlalchemy.Column("age", sqlalchemy.Integer),
#     sqlalchemy.Column("expirience", sqlalchemy.Integer),
#     sqlalchemy.Column("auto_type", sqlalchemy.String),
#     sqlalchemy.Column("coast", sqlalchemy.Integer),
# )