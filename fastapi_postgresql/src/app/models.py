import uuid
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
import sqlalchemy.dialects.postgresql as postgresql

from .database import Base 

class User(Base):
    __tablename__ = "users"

    id = Column(postgresql.UUID(as_uuid=True), 
                primary_key=True, 
                default=uuid.uuid4,
                index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base): 
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(postgresql.UUID(as_uuid=True), ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")