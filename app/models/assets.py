import uuid

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID

from app.models.model import Base


class Asset(Base):
    __tablename__ = "assets"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
