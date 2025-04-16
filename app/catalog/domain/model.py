from __future__ import annotations

from typing import List


class Catalog:
    items: List[Item]


class Item:
    id: int
    name: str
    parent_id: int
