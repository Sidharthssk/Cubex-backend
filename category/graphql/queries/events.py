import strawberry
from category.graphql.types.event import EventType
from framework.graphql.exceptions import APIError
from typing import Optional, List
from django.core.exceptions import ObjectDoesNotExist


@strawberry.type
class Event:
    @strawberry.field
    def event(self, id: strawberry.ID) -> EventType:
        from category.models.event import Event as EventModel
        try:
            event = EventModel.objects.get(id=id)
            return EventType(
                id=event.id,
                name=event.name,
                description=event.description,
                start_date=event.start_date,
                end_date=event.end_date,
            )
        except ObjectDoesNotExist:
            raise APIError("Event does not exist", code="EVENT_NOT_FOUND")

    @strawberry.field
    def events(self, info) -> Optional[List[EventType]]:
        from category.models.event import Event as EventModel
        try:
            events = EventModel.objects.all()
        except ObjectDoesNotExist:
            raise APIError("Event does not exist", code="EVENT_NOT_FOUND")
        return [EventType(
            name=event.name,
            description=event.description,
            start_date=event.start_date,
            end_date=event.end_date,
        ) for event in events]


__all__ = ["Event", ]
