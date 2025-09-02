from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from crud.application import create_application, get_application, list_applications
from schemas.application import ApplicationCreate, ApplicationOut
from fastapi_jwt_auth import AuthJWT
from utils import *

router = APIRouter(prefix="/applications", tags=["applications"])

@router.post("/", response_model=ApplicationOut)
async def create_new_application(application: ApplicationCreate, db: AsyncSession = Depends(get_db), Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    return await create_application(db, application)

@router.get("/{app_id}", response_model=ApplicationOut)
async def read_application(app_id: int, db: AsyncSession = Depends(get_db), Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    app = await get_application(db, app_id)
    if not app:
        raise HTTPException(status_code=404, detail="Application not found")
    return app

@router.get("/", response_model=list[ApplicationOut])
async def read_applications(db: AsyncSession = Depends(get_db), Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    return await list_applications(db)
