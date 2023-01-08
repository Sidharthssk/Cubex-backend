from typing import Optional
import strawberry


@strawberry.input
class AgeGroupFilterInput:
    eventID: Optional[strawberry.ID] = None


__all__ = ['AgeGroupFilterInput']
