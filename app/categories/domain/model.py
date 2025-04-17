from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Category:
    id: int
    name: str
    parent_id: int | None = None
