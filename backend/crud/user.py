from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import User
from schemas.user import UserCreate, UserOut

async def create_user(db: AsyncSession, user: UserCreate) -> UserOut:
    new_user = User(email=user.email, password=user.password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

async def get_user_by_email(db: AsyncSession, email: str) -> UserOut | None:
    result = await db.execute(select(User).where(User.email == email))
    return result.scalars().first()

async def get_user(db: AsyncSession, user_id: int) -> UserOut | None:
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalars().first()
