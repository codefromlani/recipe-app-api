from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class FavoriteCreate(BaseModel):
    user_id: str 
    recipe_id: int 
    title: str 
    image: Optional[str] 
    cook_time: Optional[str] 
    servings: Optional[str] 


class FavoriteResponse(FavoriteCreate):
    id: int 
    created_at: datetime 

    model_config = ConfigDict(
        from_attributes=True
    )