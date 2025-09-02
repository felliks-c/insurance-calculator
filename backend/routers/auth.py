from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from schemas.user import UserCreate, UserOut
from crud.user import create_user, get_user_by_email
from fastapi_jwt_auth import AuthJWT

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserOut)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")
    return await create_user(db, user)

@router.post("/login")
async def login(user: UserCreate, db: AsyncSession = Depends(get_db), Authorize: AuthJWT = Depends()):
    db_user = await get_user_by_email(db, email=user.email)
    if not db_user or db_user.password != user.password:  # TODO: захэшировать пароли!
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    access_token = Authorize.create_access_token(subject=db_user.id)
    return {"access_token": access_token, "token_type": "bearer"}
