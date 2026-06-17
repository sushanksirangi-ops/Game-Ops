from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from app.database import get_db
from app.models.match import Match

from app.services.leaderboard_service import (
    LeaderboardService
)

router = APIRouter()


@router.get("/leaderboard")
def get_leaderboard(
    db: Session = Depends(get_db)
):

    matches = db.query(
        Match
    ).all()

    return LeaderboardService.generate(
        matches
    )