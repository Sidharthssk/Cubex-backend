import strawberry

from participant.models.participant import Participant
from framework.graphql.exceptions import APIError
from chowkidar.decorators import resolve_user


@strawberry.type
class ParticipantRegistrationMutations:
    @strawberry.mutation
    @resolve_user
    def register_participant_for_category(
        self, info,
        participantID: strawberry.ID,
        eventID: strawberry.ID,
    ) -> bool:
        try:
            participant = Participant.objects.get(id=participantID)
        except Participant.DoesNotExist:
            raise APIError("Participant does not exist.", code="PARTICIPANT_NOT_FOUND")
        if not info.context.user.is_superuser:
            raise APIError("You do not have permission to register participants.", code="FORBIDDEN")
        participant.events.add(eventID)
        participant.save()
        return True

    @strawberry.mutation
    # @resolve_user
    def remove_participant_from_category(
        self, info,
        participantID: strawberry.ID,
        eventID: strawberry.ID
    ) -> bool:
        try:
            participant = Participant.objects.get(id=participantID, events__id=eventID)
        except Participant.DoesNotExist:
            raise APIError("Participant does not exist.", code="PARTICIPANT_NOT_FOUND")
        # if not info.context.user.is_superuser:
        #     raise APIError("You do not have permission to remove participants.", code="FORBIDDEN")
        participant.events.remove(eventID)
        participant.save()
        return True


__all__ = ["ParticipantRegistrationMutations", ]