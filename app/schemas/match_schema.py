from pydantic import BaseModel


class MatchCreate(BaseModel):

    player_id: str
    match_id: str

    region: str
    device: str

    ping: int

    score: int

    kills: int

    deaths: int

    match_duration_seconds: int


class MatchResponse(MatchCreate):

    id: int

    class Config:
        from_attributes = True