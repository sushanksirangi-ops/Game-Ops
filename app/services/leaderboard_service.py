from collections import defaultdict


class LeaderboardService:

    @staticmethod
    def generate(matches):

        players = defaultdict(
            lambda: {
                "score": 0,
                "kills": 0,
                "deaths": 0,
                "region": ""
            }
        )

        for match in matches:

            player = players[
                match.player_id
            ]

            player["score"] += match.score
            player["kills"] += match.kills
            player["deaths"] += match.deaths
            player["region"] = match.region

        leaderboard = []

        for player_id, stats in players.items():

            leaderboard.append({
                "player_id": player_id,
                **stats
            })

        leaderboard.sort(
            key=lambda x: (
                -x["score"],
                x["deaths"],
                -x["kills"]
            )
        )

        for idx, player in enumerate(
            leaderboard,
            start=1
        ):
            player["rank"] = idx

        return leaderboard