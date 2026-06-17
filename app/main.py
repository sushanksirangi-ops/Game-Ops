from fastapi import FastAPI

from app.database import Base
from app.database import engine

from app.routers import scores
from app.routers import leaderboard
from app.routers import suspicious
from app.routers import matchmaking

Base.metadata.create_all(
    bind=engine
)

app = FastAPI(
    title="Game Ops System"
)

app.include_router(
    scores.router,
    tags=["Scores"]
)

app.include_router(
    leaderboard.router,
    tags=["Leaderboard"]
)

app.include_router(
    suspicious.router,
    tags=["Suspicious Players"]
)

app.include_router(
    matchmaking.router,
    tags=["Matchmaking"]
)