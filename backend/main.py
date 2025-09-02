# точка входа в приложение FastAPI


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.responses import JSONResponse
from .config import database, DATABASE_URL, settings, DBKEY
import sqlalchemy
from .routers import auth, quote, application
from contextlib import asynccontextmanager
from .models import *
from core.database import Base, sync_engine
from core.logging import LoggingMiddleware
from .routers import auth, user, quote, application


# Создание таблиц (синхронно при старте)
Base.metadata.create_all(bind=sync_engine)



@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await database.connect()
    yield
    # Shutdown
    await database.disconnect()


app = FastAPI(title="Insurance Calculator API", lifespan=lifespan)

# CORS (чтобы фронт мог обращаться)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #  все домены могут обращаться
    allow_credentials=True,
    allow_methods=["GET", "POST"],  # только разрешённые методы
    allow_headers=["Authorization", "Content-Type"],  # только нужные заголовки
)

app.add_middleware(LoggingMiddleware)

# глобальный хэндлер ошибок JWT
@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.message}
    )





# роуты
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(quote.router)
app.include_router(application.router)


@app.get("/")
def root():
    return {"message": "Insurance Calculator API is running correctly."}
