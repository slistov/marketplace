from sqlalchemy import Column, Integer, MetaData, String, Table
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.config import DATABASE_URL

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

meta = MetaData()

categories = Table(
    "categories",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("parent_id", Integer),
)


async def get_session():
    async with async_session() as session:
        yield session
