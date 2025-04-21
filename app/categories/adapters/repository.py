from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.categories import exceptions
from app.categories.domain.model import Category


class Repo:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get(self, id):
        return await self._get(id)

    async def _get(self, id) -> Category:
        cat = await self.session.get(Category, id)
        if not cat:
            raise exceptions.CategoryNotFound(id)
        return cat

    async def get_subtree(self, id):
        return await self._get_subtree(id)

    async def _get_subtree(self, id):
        parent_cat = await self.get(id)
        path_filter = parent_cat.path + ","

        q = select(Category).filter(Category.path.startswith(path_filter))
        result = await self.session.execute(q)
        subtree = result.scalars().all()
        return subtree
