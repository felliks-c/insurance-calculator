from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Application
from schemas.application import ApplicationCreate, ApplicationOut

async def create_application(db: AsyncSession, application: ApplicationCreate) -> ApplicationOut:
    new_app = Application(**application.dict())
    db.add(new_app)
    await db.commit()
    await db.refresh(new_app)
    return new_app

async def get_application(db: AsyncSession, app_id: int) -> ApplicationOut | None:
    result = await db.execute(select(Application).where(Application.id == app_id))
    return result.scalars().first()

async def list_applications(db: AsyncSession) -> list[ApplicationOut]:
    result = await db.execute(select(Application))
    return result.scalars().all()
