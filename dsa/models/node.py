from typing import Self

from pydantic import BaseModel


class Node(BaseModel):
    value: int = 0
    next: Self | None = None
