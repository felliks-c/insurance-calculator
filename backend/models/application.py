from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    tariff = Column(String, nullable=False)

    quote_id = Column(Integer, ForeignKey("quotes.id"), nullable=False)





# from pydantic import BaseModel
# import sqlalchemy
# from config import metadata






# applications = sqlalchemy.Table(
#     "applications",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("user_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id")),
#     sqlalchemy.Column("name", sqlalchemy.String),
#     sqlalchemy.Column("number", sqlalchemy.Integer),
#     sqlalchemy.Column("email", sqlalchemy.String, sqlalchemy.ForeignKey("users.email")),
#     sqlalchemy.Column("price", sqlalchemy.String),
#     sqlalchemy.Column("quote_id", sqlalchemy.Integer, sqlalchemy.ForeignKey("quotes.id")),
# )