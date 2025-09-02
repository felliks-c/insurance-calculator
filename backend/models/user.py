from sqlalchemy import Column, Integer, String
from core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)





#from pydantic import BaseModel
# import sqlalchemy
# from config import metadata






# users = sqlalchemy.Table(
#     "users",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("email", sqlalchemy.String),
#     sqlalchemy.Column("password", sqlalchemy.String),
# )