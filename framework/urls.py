from framework.graphql.schema import schema
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from chowkidar.view import auth_enabled_view

from framework.graphql.utils import CustomGraphQLView

admin.site.site_header = "CubeX Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        "graphql/",
        csrf_exempt(
            auth_enabled_view(
                CustomGraphQLView.as_view(schema=schema, graphiql=settings.DEBUG)
            )
        ),
    ),
]
