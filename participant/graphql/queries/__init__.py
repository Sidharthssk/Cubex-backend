import strawberry

from .participant import ParticipantQueries as participantQueries


@strawberry.type
class ParticipantQueries(
    participantQueries
):
    pass


__all__ = [
    "ParticipantQueries",
    ]