from typing import Optional

import strawberry
from performance.models import Performance
from performance.graphql.types import ScoreboardQuery, ScoreType


@strawberry.type
class ScoreboardQueries:

    @strawberry.field
    def scoreboard(
        self, info,
        eventID: strawberry.ID,
        ageGroupID: strawberry.ID,
        keyword: Optional[str] = None,
        count: Optional[int] = 10,
        offset: Optional[int] = 0,
    ) -> ScoreboardQuery:
        scores = Performance.objects.filter(event_id=eventID, participant__ageGroup_id=ageGroupID)

        if keyword is not None:
            scores = scores.filter(participant__name__icontains=keyword)

        scores = scores.order_by(
            'duration'
        )

        totalCount = scores.count()
        scores = scores[offset:offset+count]
        scs = []
        i = offset + 1
        for s in scores:
            scs.append(
                ScoreType(
                    participant=s.participant,
                    duration=s.duration,
                    rank=i
                )
            )
            i += 1

        return ScoreboardQuery(
            scores=scs,
            hasNext=(offset + count < totalCount),
            totalCount=totalCount
        )


