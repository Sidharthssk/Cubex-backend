from typing import Optional
from django.db.models import Q
from framework.graphql.exceptions import APIError
from framework.utils.cursor_pagination import CursorPaginator
from participant.graphql.types import ParticipantQuery, ParticipantProfileType
from participant.graphql.inputs import ParticipantFilterInput
from participant.models import Participant
import strawberry
from chowkidar.decorators import login_required


@strawberry.type
class ParticipantQueries:

    @strawberry.field
    @login_required
    def participant(
            self, info,
            id: strawberry.ID
    ) -> Optional[ParticipantProfileType]:
        try:
            return Participant.objects.get(id=id)
        except Participant.DoesNotExist:
            raise APIError("Participant does not exist", code="PARTICIPANT_NOT_FOUND")

    @strawberry.field
    @login_required
    def participants(
            self, info,
            after: Optional[str] = None,
            count: Optional[int] = 10,
            filters: Optional[ParticipantFilterInput] = None,
            keyword: Optional[str] = None,
    ) -> Optional[ParticipantQuery]:
        participants = Participant.objects.all()
        if filters is not None:
            if filters.eventID is not None:
                participants = participants.filter(event_id=filters.eventID)
            if filters.age_groupID is not None:
                participants = participants.filter(age_group_id=filters.age_groupID)
            if filters.isOnline is not None:
                participants = participants.filter(isOnline=filters.isOnline)

        if keyword is not None:
            participants = participants.filter(name__istartswith=keyword)

        totalCount = participants.count()
        ordering = ("-id",)
        paginator = CursorPaginator(participants, ordering=ordering)
        page = paginator.page(first=count, after=after)
        return ParticipantQuery(
            participants=page,
            hasNext=page.has_next,
            totalCount=totalCount,
            lastCursor=paginator.cursor(page[-1]) if page else None
        )


__all__ = ["ParticipantQueries"]

