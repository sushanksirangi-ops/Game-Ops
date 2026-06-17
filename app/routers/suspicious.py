from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from app.database import get_db
from app.models.match import Match

from app.services.suspicious_service import (
    SuspiciousService
)

router = APIRouter()


@router.get("/flagged-players")
def flagged_players(
    db: Session = Depends(get_db)
):

    matches = db.query(
        Match
    ).all()

    flagged = []

    for match in matches:

        if (
            SuspiciousService
            .is_suspicious(match)
        ):

            flagged.append({
                "player_id":
                    match.player_id,

                "reason":
                    SuspiciousService
                    .get_reason(match)
            })

    return flagged