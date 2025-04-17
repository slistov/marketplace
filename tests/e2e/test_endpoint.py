from collections import namedtuple

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import text

from app.categories.adapters.orm import get_session
from app.categories.routers.main import app

client = TestClient(app=app)


Row = namedtuple("Row", ["id", "name", "parent_id"])


async def load_to_db(session, rows: list[tuple]):
    for row in rows:
        await session.execute(
            text(
                "INSERT INTO categories (id, name, parent_id) VALUES (:id, :name, :parent_id)"
            ),
            Row(*row)._asdict(),
        )


@pytest.mark.asyncio
async def test_tree_by_category_id(session, db_content):
    async def override_session_dependency():
        await load_to_db(session, db_content)
        return session

    app.dependency_overrides[get_session] = override_session_dependency

    params = {"id": 200}
    response = client.get("/categories", params=params)
    assert response.status_code == 200

    expected = [
        (400, "Смартфоны", 200),
        (500, "Аксессуары", 200),
        (600, "Чехлы", 500),
        (700, "Зарядки", 500),
    ]
    assert response.json() == [Row(*e)._asdict() for e in expected]
