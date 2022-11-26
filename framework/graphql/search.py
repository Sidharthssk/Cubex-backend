from participant.models import Participant
import strawberry, typing, datetime
from enum import Enum
from typing import Optional, List
from django.db.models import Q


@strawberry.enum
class SearchTypeEnum(Enum):
    NAME = "Name"
    PHONE_NUMBER = "Phone Number"


@strawberry.type
class Events:
    id: strawberry.ID
    name: str
    description: str
    start_date: datetime.date
    end_date: datetime.date


@strawberry.type
class ParticipantSearchResult:
    id: strawberry.ID
    name: str
    phone_number: str
    dob: datetime.date
    gender: str
    country: str
    age_group: str
    events: typing.List[Events]


@strawberry.type
class SearchQueries:
    @strawberry.field
    def search(
            self, info,
            keyword: str,
            type: Optional[SearchTypeEnum] = None
    ) -> List[ParticipantSearchResult]:
        result = []
        if type == SearchTypeEnum.NAME:
            participants = Participant.objects.filter(
                Q(name__icontains=keyword)
            )
            result = [
                ParticipantSearchResult(
                    id=participant.id,
                    name=participant.name,
                    phone_number=participant.contact,
                    dob=participant.dob,
                    gender=participant.gender,
                    country=participant.country,
                    age_group=participant.ageGroup.name,
                    events=participant.events.all(),
                )
                for participant in participants
            ]
        elif type == SearchTypeEnum.PHONE_NUMBER:
            participants = Participant.objects.filter(
                Q(contact__icontains=keyword)
            )
            result = [
                ParticipantSearchResult(
                    id=participant.id,
                    name=participant.name,
                    phone_number=participant.contact,
                    dob=participant.dob,
                    gender=participant.gender,
                    country=participant.country,
                    age_group=participant.ageGroup.name,
                    events=participant.events.all(),
                )
                for participant in participants
            ]
        else:
            participants = Participant.objects.filter(
                Q(name__icontains=keyword) | Q(contact__icontains=keyword)
            )
            result = [
                ParticipantSearchResult(
                    id=participant.id,
                    name=participant.name,
                    phone_number=participant.contact,
                    dob=participant.dob,
                    gender=participant.gender,
                    country=participant.country,
                    age_group=participant.ageGroup.name,
                    events=participant.events.all(),
                )
                for participant in participants
            ]
        return result


__all__ = ["SearchQueries"]
