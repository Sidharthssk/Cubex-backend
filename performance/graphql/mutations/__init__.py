from .scoreboard import ScoreboardMutations as scoreboardMutations
import strawberry


@strawberry.type
class ScoreboardMutations(
    scoreboardMutations
):
    pass


__all__ = [
    "ScoreboardMutations",
    ]
