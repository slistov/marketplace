from pydantic import BaseModel


class CategoryResponse(BaseModel):
    id: int
    name: str
    parent_id: int
