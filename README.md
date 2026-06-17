# Game Ops System

## Overview

Game Ops System is a backend application developed using FastAPI and PostgreSQL to manage multiplayer game event data. The system processes player match information, generates leaderboards, identifies suspicious players, and creates matchmaking groups based on player performance and region.

This project was developed as part of a Gaming Assignment to demonstrate backend development, data processing, API design, and system architecture skills.

---

## Features

### Leaderboard Generation

* Global leaderboard ranking players by score.
* Tie-breaking using deaths and kills.
* Dynamic leaderboard generation from match data.

### Suspicious Player Detection

* Detects abnormal gameplay patterns.
* Flags players with unrealistic scores, kills, or score-per-minute values.
* Prevents suspicious players from influencing fair rankings.

### Matchmaking System

* Groups players based on:

  * Region
  * Skill Level
  * Performance Metrics
* Creates balanced matchmaking recommendations.

### REST APIs

* Submit match scores.
* Retrieve leaderboard data.
* Retrieve flagged players.
* Generate matchmaking groups.

---

## Technology Stack

### Backend

* Python
* FastAPI

### Database

* PostgreSQL
* SQLAlchemy ORM

### Validation

* Pydantic

### Testing

* Pytest

---

## Project Structure

```text
Game_Ops/
│
├── app/
│   ├── main.py
│   ├── database.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── match.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── match_schema.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── leaderboard_service.py
│   │   ├── suspicious_service.py
│   │   └── matchmaking_service.py
│   │
│   └── routers/
│       ├── __init__.py
│       ├── scores.py
│       ├── leaderboard.py
│       ├── suspicious.py
│       └── matchmaking.py
│
├── tests/
│   └── test_suspicious.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## Database Schema

### Match Table

| Field                  | Type    |
| ---------------------- | ------- |
| id                     | Integer |
| player_id              | String  |
| match_id               | String  |
| region                 | String  |
| device                 | String  |
| ping                   | Integer |
| score                  | Integer |
| kills                  | Integer |
| deaths                 | Integer |
| match_duration_seconds | Integer |

---

## API Endpoints

### Submit Match Score

```http
POST /submit-score
```

Stores player match data in PostgreSQL.

### Get Leaderboard

```http
GET /leaderboard
```

Returns ranked players based on score.

### Get Suspicious Players

```http
GET /flagged-players
```

Returns players flagged for abnormal gameplay.

### Get Matchmaking Groups

```http
GET /matchmaking
```

Returns grouped players based on region and skill tier.

---

## Suspicious Player Detection Logic

A player is flagged if:

* Score exceeds 50,000 within a short match duration.
* Kills exceed 100 with zero deaths.
* Score per minute exceeds acceptable thresholds.

Example:

```text
Score: 99000
Kills: 250
Deaths: 0
Duration: 60 seconds
```

Such players are marked as suspicious and can be reviewed separately.

---

## Matchmaking Logic

Players are grouped using:

1. Region
2. Skill Rating
3. Match Performance

### Skill Formula

```text
Skill =
(Score × 0.5) +
(Kills × 20) -
(Deaths × 10)
```

Skill tiers:

* Bronze
* Silver
* Gold
* Platinum

This helps create balanced and fair matches.

---

## Running the Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/game_ops
```

### Start FastAPI Server

```bash
uvicorn app.main:app --reload
```

### Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

## Running Tests

```bash
pytest -v
```

---

## Future Improvements

* Redis Caching for Leaderboards
* Machine Learning-Based Cheat Detection
* Real-Time Event Processing
* Seasonal Leaderboards
* Advanced Matchmaking Algorithms
* Prometheus & Grafana Monitoring
* Docker Deployment

---

## Conclusion

This project demonstrates the design and implementation of a scalable Game Operations System capable of processing match data, generating fair leaderboards, detecting suspicious player behavior, and providing matchmaking recommendations using a modern Python backend architecture.
