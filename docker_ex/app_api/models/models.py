
from pydantic import BaseModel


# Common properties shared by Create and Read
class ItemBase(BaseModel):
    title: str
    description: str | None = None

# Properties needed to create an item
class ItemCreate(ItemBase):
    pass

# Properties returned to the client (includes DB-generated ID)
class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True # Allows Pydantic to read SQLAlchemy models
