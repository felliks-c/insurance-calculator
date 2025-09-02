# логирование, middleware для ошибок

import logging
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR
import traceback
import sys
from fastapi import HTTPException


# настройка логгера
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)        
# middleware для логирования ошибок
class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            logger.info(f"{request.method} {request.url} - {response.status_code}")
            return response
        except HTTPException as e:
            raise e
        except Exception as e:
            tb = traceback.format_exc()
            logger.error(f"Unhandled error: {e}\n{tb}")
            return JSONResponse(
                status_code=HTTP_500_INTERNAL_SERVER_ERROR,
                content={"detail": "Internal Server Error"}
            )
