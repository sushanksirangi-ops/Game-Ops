import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from app.services.suspicious_service import SuspiciousService

class MockMatch:

    def __init__(self,score,kills,deaths,match_duration_seconds):
        self.score = score
        self.kills = kills
        self.deaths = deaths
        self.match_duration_seconds = (match_duration_seconds)


def test_high_score_short_duration():
    match = MockMatch(score=99000,kills=50,deaths=2,match_duration_seconds=60)
    assert (SuspiciousService.is_suspicious(match)is True)


def test_abnormal_kills_zero_deaths():
    match = MockMatch(score=5000,kills=250,deaths=0,match_duration_seconds=300)
    assert (SuspiciousService.is_suspicious(match)is True)


def test_high_score_per_minute():
    match = MockMatch(score=100000,kills=20,deaths=1,match_duration_seconds=30)
    assert (SuspiciousService.is_suspicious(match)is True)


def test_normal_player():
    match = MockMatch(score=3200,kills=18,deaths=4,match_duration_seconds=420)
    assert (SuspiciousService.is_suspicious(match)is False)