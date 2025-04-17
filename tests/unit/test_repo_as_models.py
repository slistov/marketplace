"""
Только для демонстрации, пользы мало.
Проверяется как репозиторий
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

    subtree = await repo.get_subtree(200)
    expected = [
        Category(*(400, "Смартфоны", 200)),
        Category(*(500, "Аксессуары", 200)),
        Category(*(600, "Чехлы", 500)),
        Category(*(700, "Зарядки", 500)),
    ]
    assert subtree == expected
