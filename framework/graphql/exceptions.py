from graphql import GraphQLError


class APIError(GraphQLError):

    def __init__(self, message, code=None, *args, **kwargs):
        super().__init__(message, *args, **kwargs)
        self.locations = []
        self.path = []
        self.code = code
        self.message = message

    @property
    def formatted(self):
        return {
            "message": self.message or "An unknown error occurred.",
            "code": self.code or "UNKNOWN_ERROR",
        }


__all__ = [
    'APIError'
]
