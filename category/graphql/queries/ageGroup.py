import strawberry
from category.graphql.types.ageGroup import AgeGroupType
from framework.graphql.exceptions import APIError
from django.core.exceptions import ObjectDoesNotExist
from typing import Optional, List


@strawberry.type
class AgeGroup:
    @strawberry.field
    def AgeGroups(self, event_id: strawberry.ID) -> Optional[List[AgeGroupType]]:
        from category.models.age_group import AgeGroup as AgeGroupModel
        try:
            ageGroups = AgeGroupModel.objects.filter(
                event=event_id
            )
            return [
                AgeGroupType(
                    id=ageGroup.id,
                    name=ageGroup.name,
                    minAge=ageGroup.minAge,
                    maxAge=ageGroup.maxAge,
                )for ageGroup in ageGroups
            ]
        except ObjectDoesNotExist:
            raise APIError("Age group does not exist", code="AGE_GROUP_NOT_FOUND")


__all__ = ['AgeGroup']
