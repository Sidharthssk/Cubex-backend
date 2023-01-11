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
                description=description if description else None,
                start_date=start_date if start_date else None,
                end_date=end_date if end_date else None,
            )
            age_group.save()

            return AgeGroupType(
                id=age_group.id,
                name=age_group.name,
                description=age_group.description,
                start_date=age_group.start_date,
                end_date=age_group.end_date
            )
        except Exception as e:
            raise APIError(e)


__all__ = [
    'AgeGroupMutation'
]
