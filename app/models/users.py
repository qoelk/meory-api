import uuid

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID

from app.models.model import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(unique=True)
