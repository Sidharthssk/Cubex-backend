import strawberry
from category.models.event import Event
from category.graphql.types.event import EventType
from typing import Optional
from chowkidar.decorators import resolve_user
from framework.graphql.exceptions import APIError


@strawberry.type
class EventMutation:
    @strawberry.mutation
    @resolve_user
    def create_event(self, info, name: str, description: Optional[str], start_date: Optional[str], end_date: Optional[str]) -> EventType:
        if not info.context.user.is_superuser:
            raise APIError("You are not authorized to create an event")
        try:
            event = Event.objects.create(
                name=name,
                description=description if description else None,
                start_date=start_date if start_date else None,
                end_date=end_date if end_date else None,
            )
            event.save()

            return EventType(
                id=event.id,
                name=event.name,
                description=event.description,
                start_date=event.start_date,
                end_date=event.end_date
            )
        except Exception as e:
            raise APIError(e)


__all__ = [
    'EventMutation'
]
