from django.urls import path, include
from rest_framework_nested import routers
from .views import EmployeeViewSet, PerformanceRecordViewSet, AttendanceViewSet, DepartmentViewSet, ProjectViewSet, DepartmentDistributionChartView, EmployeeRolePerDepartmentChartView


router = routers.SimpleRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'projects', ProjectViewSet)

employee_router = routers.NestedSimpleRouter(
    router, r'employees', lookup='employee'
)
employee_router.register(r'attendance', AttendanceViewSet, basename='employee-attendance')
employee_router.register(r'performance', PerformanceRecordViewSet, basename='employee-performance')


urlpatterns = [
    path('chart/department-distribution/', DepartmentDistributionChartView.as_view(), name='department_distribution_chart'),
    path('chart/employee-roles/<int:department_id>/', EmployeeRolePerDepartmentChartView.as_view(), name='employee_role_per_department_chart'),
    path("api/v1/", include(router.urls)),
    path("api/v1/", include(employee_router.urls)),
]
