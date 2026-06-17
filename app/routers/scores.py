from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from app.database import get_db
from app.models.match import Match
from app.schemas.match_schema import MatchCreate

router = APIRouter()


@router.post("/submit-score")
def submit_score(
    payload: MatchCreate,
    db: Session = Depends(get_db)
):

    match = Match(
        **payload.model_dump()
    )

    db.add(match)

    db.commit()

    db.refresh(match)

    return {
        "message": "Score submitted",
        "id": match.id
    }