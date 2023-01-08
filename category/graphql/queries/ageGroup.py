import strawberry
from category.graphql.types.ageGroup import AgeGroupType
from framework.graphql.exceptions import APIError
from django.core.exceptions import ObjectDoesNotExist
from typing import Optional, List
from category.graphql.inputs import AgeGroupFilterInput


@strawberry.type
class AgeGroup:
    @strawberry.field
    def AgeGroups(self,
                  filters: Optional[AgeGroupFilterInput] = None,
                  ) -> Optional[List[AgeGroupType]]:
        from category.models.age_group import AgeGroup as AgeGroupModel
        try:
            ageGroups = AgeGroupModel.objects.all()
            if filters is not None:
                if filters.eventID is not None:
                    ageGroups = ageGroups.filter(event=filters.eventID)
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
