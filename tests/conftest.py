import pytest
import pytest_asyncio

from app.categories.adapters.orm import async_session

DB_CONTENT = [
    (100, "Электроника", None),
    (200, "Телефоны", 100),
    (300, "Ноутбуки", 100),
    (400, "Смартфоны", 200),
    (500, "Аксессуары", 200),
    (600, "Чехлы", 500),
    (700, "Зарядки", 500),
    (800, "Одежда", None),
    (900, "Мужская", 800),
    (1000, "Женская", 800),
]


@pytest.fixture(scope="function")
def db_content():
    return DB_CONTENT


@pytest_asyncio.fixture(scope="function")
async def session():
    async with async_session() as s:
        yield s
