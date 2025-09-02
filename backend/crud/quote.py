from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Quote
from schemas.quote import QuoteCreate, QuoteOut

async def create_quote(db: AsyncSession, quote: QuoteCreate) -> QuoteOut:
    new_quote = Quote(**quote.dict())
    db.add(new_quote)
    await db.commit()
    await db.refresh(new_quote)
    return new_quote

async def get_quote(db: AsyncSession, quote_id: int) -> QuoteOut | None:
    result = await db.execute(select(Quote).where(Quote.id == quote_id))
    return result.scalars().first()

async def list_quotes(db: AsyncSession) -> list[QuoteOut]:
    result = await db.execute(select(Quote))
    return result.scalars().all()
