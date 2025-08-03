from pydantic import BaseModel
from typing import Optional

# Base schema for an item
class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    is_done: bool = False

# Schema for creating an item (inherits from ItemBase)
class ItemCreate(ItemBase):
    pass

# Schema for reading an item (includes the id)
class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
