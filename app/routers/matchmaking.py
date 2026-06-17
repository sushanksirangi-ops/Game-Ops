from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from app.database import get_db
from app.models.match import Match

from app.services.leaderboard_service import (
    LeaderboardService
)

from app.services.matchmaking_service import (
    MatchmakingService
)

router = APIRouter()


@router.get("/matchmaking")
def matchmaking(
    db: Session = Depends(get_db)
):

    matches = db.query(
        Match
    ).all()

    leaderboard = (
        LeaderboardService
        .generate(matches)
    )

    return (
        MatchmakingService()
        .generate_groups(
            leaderboard
        )
    )