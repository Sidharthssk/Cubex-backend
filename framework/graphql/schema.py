import strawberry
from chowkidar.extension import JWTAuthExtension
from django.conf import settings
from graphql import NoSchemaIntrospectionCustomRule
from strawberry.extensions import (
    QueryDepthLimiter,
    ValidationCache,
    ParserCache,
    AddValidationRules,
)
from strawberry.tools import merge_types
from participant.graphql import ParticipantMutations, ParticipantQueries
from performance.graphql import ScoreboardMutations, ScoreboardQueries
from user.graphql import UserMutations
from .search import SearchQueries
from category.graphql import EventQuery, EventMutations


Mutations = merge_types(
    "Mutations",
    (
        ParticipantMutations,
        ScoreboardMutations,
        UserMutations,
        EventMutations,
    ),
)

Queries = merge_types(
    "Queries",
    (
        ParticipantQueries,
        ScoreboardQueries,
        SearchQueries,
        EventQuery,
    ),
)

extensions = [
    JWTAuthExtension,
    QueryDepthLimiter(max_depth=10),
    ParserCache(maxsize=100),
    ValidationCache(maxsize=100),
]

if not settings.DEBUG:
    extensions.append(AddValidationRules([NoSchemaIntrospectionCustomRule]))

schema = strawberry.Schema(query=Queries, mutation=Mutations, extensions=extensions)


__all__ = [
    "schema",
    "Queries",
    "Mutations",
]
