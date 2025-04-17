from fastapi import APIRouter, Depends

from app.categories.adapters.orm import get_session
from app.categories.domain.model import Category
from app.categories.services import category

router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("")
async def get_item_subtree(id: int, session=Depends(get_session)) -> list[Category]:
    data = await category.get_subtree(id, session)
    return data
