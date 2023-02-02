import strawberry
from category.models.age_group import AgeGroup
from typing import Optional
from category.graphql.types import AgeGroupType
from framework.graphql.exceptions import APIError


@strawberry.type
class AgeGroupMutation:
    @strawberry.mutation
    def create_age_group(self, info, name: str, description: Optional[str], start_date: Optional[str], end_date: Optional[str]) -> Optional[AgeGroupType]:
        try:
            age_group = AgeGroup.objects.create(
                name=name,
            )
            age_group.save()

            return AgeGroupType(
                id=age_group.id,
                name=age_group.name,
            )
        except Exception as e:
            raise APIError(e)

    @strawberry.mutation
    def register_age_group(self, eventID: strawberry.ID, name: str) -> Optional[AgeGroupType]:
        from category.models.event import Event
        try:
            age_group = AgeGroup.objects.filter(name__icontains=name)
            if age_group:
                age_group.event.add(Event.objects.get(id=eventID))
                return AgeGroupType(
                    id=age_group.id,
                    name=age_group.name,
                )
            else:
                new_age_group = AgeGroup.objects.create(
                    name=name,
                )
                new_age_group.save()
                new_age_group.event.add(Event.objects.get(id=eventID))
                return AgeGroupType(
                    id=new_age_group.id,
                    name=new_age_group.name,
                )
        except Exception as e:
            raise APIError(e)


__all__ = [
    'AgeGroupMutation'
]
