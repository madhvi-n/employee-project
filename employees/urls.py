from django.urls import path, include
from rest_framework_nested import routers
from .views import EmployeeViewSet

router = routers.SimpleRouter()
router.register(r"employees", EmployeeViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
