from sqlalchemy import Column, ForeignKey, Integer, MetaData, String, Table
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import registry, relationship

from app.categories.domain import model
from app.config import DATABASE_URL

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
)
async_session = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

meta = MetaData()

categories = Table(
    "categories",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("parent_id", Integer, ForeignKey("categories.id")),
)

mapper_registry = registry()
mapper_registry.map_imperatively(
    model.Category,
    categories,
    properties={"children": relationship(model.Category, order_by=categories.c.id)},
)


async def get_session():
    async with async_session() as session:
        yield session
