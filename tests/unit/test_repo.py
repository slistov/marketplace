from collections import namedtuple

import pytest
from sqlalchemy import text

from app.categories import exceptions
from app.categories.adapters.repository import Repo
from app.categories.domain.model import Category


async def load_to_db(session, rows: list[tuple]):
    Row = namedtuple("Row", ["id", "name", "path", "parent_id"])
    for row in rows:
        await session.execute(
            text(
                "INSERT INTO categories (id, name, parent_id, path) VALUES (:id, :name, :parent_id, :path)"
            ),
            Row(*row)._asdict(),
        )


@pytest.mark.asyncio
async def test_get(session, db_content):
    await load_to_db(session, db_content)
    repo = Repo(session)
    valid_item = await repo.get(200)
    assert valid_item == Category(
        id=200, name="Телефоны", parent_id=100, path="100,200"
    )


@pytest.mark.asyncio
async def test_get_unlucky(session, db_content):
    await load_to_db(session, db_content)
    repo = Repo(session)

    with pytest.raises((exceptions.CategoryNotFound)):
        non_exist_item = await repo.get(id=404)


@pytest.mark.asyncio
async def test_get_subtree(session, db_content):
    await load_to_db(session, db_content)
    repo = Repo(session)
    subtree = await repo.get_subtree(200)
    expected = [
        (400, "Смартфоны", "100,200,400", 200),
        (500, "Аксессуары", "100,200,500", 200),
        (600, "Чехлы", "100,200,500,600", 500),
        (700, "Зарядки", "100,200,500,700", 500),
    ]
    assert subtree == [Category(*e) for e in expected]
