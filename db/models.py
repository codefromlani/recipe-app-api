from sqlalchemy import Column, Integer, String, DateTime, func
from .database import Base


class Favorite(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True, nullable=False)
    recipe_id = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    image = Column(String)
    cook_time = Column(String)
    servings = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
