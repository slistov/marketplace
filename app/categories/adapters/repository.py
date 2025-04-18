from sqlalchemy import text

from app.categories.domain.model import Category

from . import sqls


class Repo:
    def __init__(self, session) -> None:
        self.session = session

    async def get_subtree(self, id):
        return await self._get_subtree(id)

    async def _get_subtree(self, id) -> list[Category]:
        condition1 = f"= {id}" if id else "ISNULL"
        sql = sqls.SUBTREE.replace(":condition1", condition1)
        return await self.__get_as_models(
            self.__exec_sql,
            stmt=sql,
        )

    async def __get_as_models(self, sql_func, **kwargs) -> list[Category]:
        """Convert sql result to models list"""
        sql_result = await sql_func(**kwargs)
        return [Category(*row) for row in sql_result]

    async def __exec_sql(self, stmt, **kwargs):
        return await self.session.execute(text(stmt), kwargs)
