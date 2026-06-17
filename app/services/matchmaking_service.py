class MatchmakingService:

    @staticmethod
    def calculate_skill(player):

        return (
            player["score"] * 0.5 +
            player["kills"] * 20 -
            player["deaths"] * 10
        )

    @staticmethod
    def get_tier(skill):

        if skill < 2000:
            return "Bronze"
        elif skill < 5000:
            return "Silver"
        elif skill < 10000:
            return "Gold"

        return "Platinum"

    def generate_groups(self, leaderboard):

        groups = {}

        for player in leaderboard:

            skill = self.calculate_skill(player)

            tier = self.get_tier(skill)

            key = f"{player['region']}-{tier}"

            if key not in groups:
                groups[key] = []

            groups[key].append(
                player["player_id"]
            )

        return groups