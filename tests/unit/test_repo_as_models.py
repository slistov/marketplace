"""
Только для демонстрации, пользы мало.
По сути, здесь проверяется только как репозиторий
преобразует результаты запроса в модели предметной области
"""

import pytest

from app.categories.adapters.repository import Repo
from app.categories.domain.model import Category


class FakeSession:
    def __init__(self, db_content=[]) -> None:
        self.db_content = db_content

    async def execute(self, *args, **kwargs):
        """Вернётся только набор с указанными id"""
        ids = [400, 500, 600, 700]
        return [r for r in self.db_content if r[0] in ids]


@pytest.mark.asyncio
async def test_repo_get_subtree(db_content):
    fake_session = FakeSession(db_content)
    repo = Repo(fake_session)

    subtree = await repo.get_subtree(2)
    expected = [
        Category(*(4, "Смартфоны", 2)),
        Category(*(5, "Аксессуары", 2)),
        Category(*(6, "Чехлы", 5)),
        Category(*(7, "Зарядки", 5)),
    ]
    assert subtree == expected
