from typing import Optional
from django.db.models import Q
from framework.graphql.exceptions import APIError
from framework.utils.cursor_pagination import CursorPaginator
from participant.graphql.types import ParticipantQuery, ParticipantProfileType
from participant.graphql.inputs import ParticipantFilterInput
from participant.models import Participant
import strawberry
from chowkidar.decorators import login_required
from typing import List


@strawberry.type
class ParticipantQueries:

    @strawberry.field
    # @login_required
    def participant(
            self, info,
            id: strawberry.ID
    ) -> Optional[ParticipantProfileType]:
        try:
            participant = Participant.objects.get(id=id)
            events = participant.events.all()
            return ParticipantProfileType(
                id=participant.id,
                name=participant.name,
                dob=participant.dob,
                contact=participant.contact,
                email=participant.email,
                gender=participant.gender,
                ageGroup=participant.ageGroup,
                events=events
            )
        except Participant.DoesNotExist:
            raise APIError("Participant does not exist", code="PARTICIPANT_NOT_FOUND")

    @strawberry.field
    # @login_required
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
                participants = participants.filter(events__id=filters.eventID)
            if filters.age_group is not None:
                participants = participants.filter(age_group_id=filters.age_groupID)
            if filters.isOnline is not None:
                participants = participants.filter(isOnline=filters.isOnline)

        if keyword is not None:
            participants = participants.filter(Q(name__istartswith=keyword) | Q(contact__istartswith=keyword))

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

    @strawberry.field
    # @login_required
    def get_all_participants(self, info) -> Optional[List[ParticipantProfileType]]:
        participants = list(Participant.objects.all())
        return [
            ParticipantProfileType(
                id=participant.id,
                name=participant.name,
                dob=participant.dob,
                contact=participant.contact,
                email=participant.email,
                gender=participant.gender,
                ageGroup=participant.ageGroup,
                city=participant.city,
                state=participant.state,
                country=participant.country,
                events=list(participant.events.all())
            )
            for participant in participants
        ]


__all__ = ["ParticipantQueries"]

