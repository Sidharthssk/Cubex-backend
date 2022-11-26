import strawberry

from participant.models.participant import Participant
from framework.graphql.exceptions import APIError


@strawberry.type
class ParticipantRegistrationMutations:
    @strawberry.mutation
    def register_participant_for_category(
        self, info,
        participantID: strawberry.ID,
        eventID: strawberry.ID,
    ) -> bool:
        try:
            participant = Participant.objects.get(id=participantID)
        except Participant.DoesNotExist:
            raise APIError("Participant does not exist.", code="PARTICIPANT_NOT_FOUND")
        participant.events.add(eventID)
        participant.save()
        return True

    @strawberry.mutation
    def remove_participant_from_category(
        self, info,
        participantID: strawberry.ID,
        eventID: strawberry.ID
    ) -> bool:
        try:
            participant = Participant.objects.get(participant_id=participantID, events__id=eventID)
        except Participant.DoesNotExist:
            raise APIError("Participant does not exist.", code="PARTICIPANT_NOT_FOUND")
        participant.events.remove(eventID)
        participant.save()
        return True


__all__ = ["ParticipantRegistrationMutations", ]