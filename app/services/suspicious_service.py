from app.models.match import Match


class SuspiciousService:

    @staticmethod
    def is_suspicious(match: Match):

        score_per_minute = (
            match.score /
            (match.match_duration_seconds / 60)
        )

        if (
            match.score > 50000
            and match.match_duration_seconds < 120
        ):
            return True

        if (
            match.kills > 100
            and match.deaths == 0
        ):
            return True

        if score_per_minute > 5000:
            return True

        return False

    @staticmethod
    def get_reason(match: Match):

        reasons = []

        if (
            match.score > 50000
            and match.match_duration_seconds < 120
        ):
            reasons.append(
                "High score in short duration"
            )

        if (
            match.kills > 100
            and match.deaths == 0
        ):
            reasons.append(
                "Abnormal kills with zero deaths"
            )

        return reasons