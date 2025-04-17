from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Employee Project API",
        default_version="v1",
        description="API documentation for the employees app project",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)