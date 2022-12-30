import strawberry

from participant.models.participant import Participant
from framework.graphql.exceptions import APIError
from chowkidar.decorators import resolve_user
from typing import Optional
from participant.graphql.types.participant import BasicParticipantType


@strawberry.type
class ParticipantRegistrationMutations:
    @strawberry.mutation
    # @resolve_user
    def register_participant_for_category(
        self, info,
        participantID: strawberry.ID,
        eventID: strawberry.ID,
    ) -> bool:
        try:
            participant = Participant.objects.get(id=participantID)
        except Participant.DoesNotExist:
            raise APIError("Participant does not exist.", code="PARTICIPANT_NOT_FOUND")
        # if not info.context.user.is_superuser:
        #     raise APIError("You do not have permission to register participants.", code="FORBIDDEN")
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
        from performance.models import Performance
        try:
            participant = Participant.objects.get(id=participantID, events__id=eventID)
        except Participant.DoesNotExist:
            raise APIError("Participant does not exist.", code="PARTICIPANT_NOT_FOUND")
        # if not info.context.user.is_superuser:
        #     raise APIError("You do not have permission to remove participants.", code="FORBIDDEN")
        participant.events.remove(eventID)
        Performance.objects.filter(participant_id=participantID, event_id=eventID).delete()
        participant.save()
        return True

    @strawberry.mutation
    # @resolve_user
    def create_participant(
        self, info,
        name: str,
        email: str,
        phone: str,
        dob: str,
        gender: str,
        city: str,
        state: str,
        country: str,
        ageGroup: strawberry.ID,
    ) -> Optional[BasicParticipantType]:
        # if not info.context.user.is_superuser:
        #     raise APIError("You do not have permission to create participants.", code="FORBIDDEN")
        participant = Participant.objects.create(
            name=name,
            email=email,
            contact=phone,
            dob=dob,
            gender=gender,
            city=city,
            state=state,
            country=country,
            ageGroup_id=ageGroup,
        )
        participant.save()
        return BasicParticipantType(
            id=participant.id,
            name=participant.name,
            dob=participant.dob,
            contact=participant.contact,
            email=participant.email,
        )


__all__ = ["ParticipantRegistrationMutations", ]