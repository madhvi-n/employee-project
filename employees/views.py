from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination

from .models import Department, Employee, PerformanceRecord, Attendance, Project
from .serializers import DepartmentSerializer, EmployeeSerializer, PerformanceRecordSerializer, AttendanceSerializer, ProjectSerializer


class CustomPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'  # Allow client to specify the number of items per page
    max_page_size = 100


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["department__name", "role"]
    search_fields = ["name", "email"]
    pagination_class = CustomPagination


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class PerformanceRecordViewSet(ModelViewSet):
    queryset = PerformanceRecord.objects.all()
    serializer_class = PerformanceRecordSerializer
    pagination_class = CustomPagination


class AttendanceViewSet(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    pagination_class = CustomPagination


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = CustomPagination