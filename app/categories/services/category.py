from sqlalchemy import text

from app.categories.domain.model import Category


async def get_subtree(id, session):
    stmt = """
        WITH RECURSIVE category_tree AS (
        SELECT id, name, parent_id
        FROM categories
        WHERE parent_id = :id
        
        UNION ALL

        SELECT c.id, c.name, c.parent_id
        FROM categories c
        INNER JOIN category_tree ct ON c.parent_id = ct.id
        )
        SELECT * FROM category_tree;"""
    resultproxy = await session.execute(text(stmt), dict(id=id))
    items = [Category(*row) for row in resultproxy]
    return items
