from django.contrib import admin
from .models import (
    Department,
    Employee,
    PerformanceRecord,
    Attendance,
    Project,
    ProjectAssignment,
)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "department", "hire_date", "role")
    list_filter = ("department", "role")
    search_fields = ("name", "email")


@admin.register(PerformanceRecord)
class PerformanceRecordAdmin(admin.ModelAdmin):
    list_display = ("id", "employee", "rating", "review_date", "feedback")
    list_filter = ("employee", "rating")
    search_fields = ("employee__name",)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("id", "employee", "date", "status")
    list_filter = ("status", "employee")
    search_fields = ("employee__name",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    filter_horizontal = ("employee",)
    search_fields = ("name",)


@admin.register(ProjectAssignment)
class ProjectAssignmentAdmin(admin.ModelAdmin):
    list_display = ("employee", "project", "status", "assigned_date", "end_date")
    list_filter = ("status", "assigned_date", "end_date")
    search_fields = ("employee__name", "project__name")
