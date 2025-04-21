from typing import List

from fastapi import APIRouter, Depends

from app.categories.adapters.orm import get_session
from app.categories.domain.model import Category
from app.categories.routers import schemas
from app.categories.services import category

router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("", response_model=List[schemas.CategoryResponse])
async def get_item_subtree(
    id: int | None = None, session=Depends(get_session)
) -> list[Category]:
    data = await category.get_subtree(id, session)
    return data
