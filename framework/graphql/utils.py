from django.http import HttpRequest
from strawberry.django.views import GraphQLView
from strawberry.http import GraphQLHTTPResponse
from strawberry.types import ExecutionResult


class CustomGraphQLView(GraphQLView):
    def process_result(
        self, request: HttpRequest, result: ExecutionResult
    ) -> GraphQLHTTPResponse:
        data: GraphQLHTTPResponse = {"data": result.data}

        if result.errors and len(result.errors) > 0 and result.errors[0].formatted:
            data["error"] = result.errors[0].formatted

        return data


__all__ = [
    "CustomGraphQLView",
]
