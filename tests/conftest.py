import pytest
import pytest_asyncio

from app.categories.adapters.orm import async_session

DB_CONTENT = [
    (100, "Электроника", "100", None),
    (200, "Телефоны", "100,200", 100),
    (300, "Ноутбуки", "100,300", 100),
    (400, "Смартфоны", "100,200,400", 200),
    (500, "Аксессуары", "100,200,500", 200),
    (600, "Чехлы", "100,200,500,600", 500),
    (700, "Зарядки", "100,200,500,700", 500),
    (800, "Одежда", "800", None),
    (900, "Мужская", "800,900", 800),
    (1000, "Женская", "800,1000", 800),
]


@pytest.fixture(scope="function")
def db_content():
    return DB_CONTENT


@pytest_asyncio.fixture(scope="function")
async def session():
    async with async_session() as s:
        yield s
