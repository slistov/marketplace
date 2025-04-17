"""
Только для демонстрации, пользы мало.
По сути, здесь проверяется только как репозиторий
преобразует результаты запроса в модели предметной области
"""

import pytest

from app.categories.adapters.repository import Repo
from app.categories.domain.model import Category

DB_CONTENT = [
    (1, "Электроника", None),
    (2, "Телефоны", 1),
    (3, "Ноутбуки", 1),
    (4, "Смартфоны", 2),
    (5, "Аксессуары", 2),
    (6, "Чехлы", 5),
    (7, "Зарядки", 5),
    (8, "Одежда", None),
    (9, "Мужская", 8),
    (10, "Женская", 8),
]


class FakeSession:
    def __init__(self, db_content=[]) -> None:
        self.db_content = db_content

    async def execute(self, *args, **kwargs):
        ids = [4, 5, 6, 7]
        return [r for r in self.db_content if r[0] in ids]


@pytest.mark.asyncio
async def test_repo_get_subtree():
    fake_session = FakeSession(DB_CONTENT)
    repo = Repo(fake_session)

    subtree = await repo.get_subtree(2)
    expected = [
        Category(*(4, "Смартфоны", 2)),
        Category(*(5, "Аксессуары", 2)),
        Category(*(6, "Чехлы", 5)),
        Category(*(7, "Зарядки", 5)),
    ]
    assert subtree == expected
