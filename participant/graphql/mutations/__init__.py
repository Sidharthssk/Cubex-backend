from .participant_registeration import ParticipantRegistrationMutations
import strawberry


@strawberry.type
class ParticipantMutations(
    ParticipantRegistrationMutations
):
    pass


__all__ = [
    "ParticipantMutations",
    ]
