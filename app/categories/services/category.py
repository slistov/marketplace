from app.categories.adapters.repository import Repo


async def get_subtree(id, session):
    repo = Repo(session)
    return await repo.get_subtree(id)
