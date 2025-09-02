from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from crud.quote import create_quote, get_quote, list_quotes
from schemas.quote import QuoteCreate, QuoteOut

router = APIRouter(prefix="/quotes", tags=["quotes"])

@router.post("/", response_model=QuoteOut)
async def create_new_quote(quote: QuoteCreate, db: AsyncSession = Depends(get_db)):
    return await create_quote(db, quote)

@router.get("/{quote_id}", response_model=QuoteOut)
async def read_quote(quote_id: int, db: AsyncSession = Depends(get_db)):
    return await get_quote(db, quote_id)

@router.get("/", response_model=list[QuoteOut])
async def read_quotes(db: AsyncSession = Depends(get_db)):
    return await list_quotes(db)
