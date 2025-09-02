# конфигурация (БД, JWT, CORS и пр.)


from pydantic import BaseSettings
import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import subprocess


load_dotenv()
DBKEY = os.getenv("DBKEY")
SECRET_KEY = os.getenv("SECRET_KEY")


DATABASE_URL = f"postgresql+asyncpg://postgres:{DBKEY}@localhost:5432/postgres"

database = databases.Database(DATABASE_URL)







class Settings(BaseSettings):
    # JWT
    authjwt_secret_key: str = SECRET_KEY  # лучше хранить в .env
    authjwt_algorithm: str = "HS256"
    authjwt_access_token_expires: int = 60 * 60  # 1 час
    
    # DB
    database_url: str = DATABASE_URL

    class Config:
        env_file = ".env"

settings = Settings()

