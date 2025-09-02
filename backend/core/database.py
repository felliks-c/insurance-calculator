# подключение к БД, сессии

import sqlalchemy
from config import DBKEY
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from config import settings



# Базовый класс для моделей
Base = declarative_base()


# Синхронный движок (для Alembic миграций или create_all)
sync_engine = create_engine(
    f"postgresql+psycopg2://postgres:{settings.DBKEY}@localhost:5432/postgres"
)


# Асинхронный движок (для работы FastAPI)
async_engine = create_async_engine(settings.database_url, future=True, echo=True)


# Сессия для асинхронного использования
AsyncSessionLocal = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)


# Dependency для получения сессии
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session






metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    f"postgresql+psycopg2://postgres:{DBKEY}@localhost:5432/postgres"
)