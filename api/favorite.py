from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import and_
from typing import List

from schemas.favorite import FavoriteCreate, FavoriteResponse
from db.database import get_db
from db.models import Favorite


router = APIRouter(tags=["Favorites"])

@router.post("/favorites/", response_model=FavoriteResponse, status_code=status.HTTP_201_CREATED)
async def create_favorite(favorite_data: FavoriteCreate, db: Session = Depends(get_db)):
    try:
        new_favorite = Favorite(**favorite_data.model_dump())

        db.add(new_favorite)
        db.commit()
        db.refresh(new_favorite)

        return new_favorite 
    except Exception as e:
        print(f"Error adding favorite: {e}") 
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong"
        )


@router.get("/favorites/{user_id}", response_model=List[FavoriteResponse])
async def get_user_favorites(user_id: str, db: Session = Depends(get_db)):
    try:
        user_favorites = db.query(Favorite).filter(Favorite.user_id == user_id).all()
        return user_favorites 
    except Exception as e:
        print(f"Error fetching the favorites: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong"
        )


@router.delete("/favorites/{user_id}/{recipe_id}", status_code=status.HTTP_200_OK)
async def delete_favorite(
    user_id: str,
    recipe_id: int, 
    db: Session = Depends(get_db)
):
    try:
        favorite_to_delete = db.query(Favorite).filter(
            and_(
                Favorite.user_id == user_id,
                Favorite.recipe_id == recipe_id
            )
        ).first()

        if not favorite_to_delete:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Favorite not found"
            )

        db.delete(favorite_to_delete)
        db.commit()

        return {"message": "Favorite removed successfully"}
    except Exception as e:
        print(f"Error removing a favorite: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong"
        )