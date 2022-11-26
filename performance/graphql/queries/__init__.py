from .scoreboard import ScoreboardQueries as scoreboardQueries
import strawberry


@strawberry.type
class ScoreboardQueries(
    scoreboardQueries
):
    pass


__all__ = [
    "ScoreboardQueries",
    ]
