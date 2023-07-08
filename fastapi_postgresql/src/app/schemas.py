import uuid
from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str 
    description: str | None = None 


class ItemCreate(ItemBase):
    pass 


class Item(ItemBase):
    id: int
    owner_id: uuid.UUID 

    class Config:
        orm_mode = True 


class UserBase(BaseModel):
    email: str 


class UserCreate(UserBase):
    password: str 


class User(UserBase):
    id: uuid.UUID
    is_active: bool 
    items: list[Item] = []

    class Config:
        orm_mode: True 