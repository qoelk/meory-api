import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models.model import Base


class Post(Base):
    __tablename__ = "posts"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(128))
    description = Column(String(512))
    asset = relationship("Asset")
