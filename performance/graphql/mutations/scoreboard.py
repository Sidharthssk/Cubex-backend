import strawberry
from typing import Optional, List
from performance.graphql.inputs import ScoreboardInput
from performance.models import Performance
from performance.graphql.types import ScoreboardType


@strawberry.type
class ScoreboardMutations:

    @strawberry.mutation
    def record_score(
            self, info,
            scoreboard: ScoreboardInput
    ) -> Optional[ScoreboardType]:
        score = Performance()
        if scoreboard.participantID is not None:
            score.participant_id = scoreboard.participantID
        if scoreboard.eventID is not None:
            score.event_id = scoreboard.eventID
        if scoreboard.duration is not None:
            score.duration = scoreboard.duration

        score.save()
        return score


__all__ = ["ScoreboardMutations", ]
