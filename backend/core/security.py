# JWT, хеширование паролей


# app/core/security.py
from fastapi_jwt_auth import AuthJWT
from passlib.context import CryptContext
from config import settings

# настройка хеширования паролей
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """Хэшируем пароль"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Проверяем пароль"""
    return pwd_context.verify(plain_password, hashed_password)

# настройка JWT
class AuthJWTSettings:
    authjwt_secret_key: str = settings.authjwt_secret_key
    authjwt_algorithm: str = settings.authjwt_algorithm
    authjwt_access_token_expires: int = settings.authjwt_access_token_expires

@AuthJWT.load_config
def get_config():
    return AuthJWTSettings()
