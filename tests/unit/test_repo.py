from collections import namedtuple

import pytest
from sqlalchemy import text

from app.categories.adapters.repository import Repo
from app.categories.domain.model import Category


async def load_to_db(session, rows: list[tuple]):
    Row = namedtuple("Row", ["id", "name", "parent_id"])
    for row in rows:
        await session.execute(
            text(
                "INSERT INTO categories (id, name, parent_id) VALUES (:id, :name, :parent_id)"
            ),
            Row(*row)._asdict(),
        )


@pytest.mark.asyncio
async def test_get_subtree(session, db_content):
    await load_to_db(session, db_content)
    repo = Repo(session)
    subtree = await repo.get_subtree(200)
    expected = [
        Category(*(400, "Смартфоны", 200)),
        Category(*(500, "Аксессуары", 200)),
        Category(*(600, "Чехлы", 500)),
        Category(*(700, "Зарядки", 500)),
    ]
    assert subtree == expected
