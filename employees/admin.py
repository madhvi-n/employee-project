from django.contrib import admin
from .models import Department, Employee, PerformanceRecord, Attendance, Project


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


admin.site.register(Department, DepartmentAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "department", "hire_date", "role")
    list_filter = ("department", "role")
    search_fields = ("name", "email")


admin.site.register(Employee, EmployeeAdmin)


class PerformanceRecordAdmin(admin.ModelAdmin):
    list_display = ("id", "employee", "rating", "review_date", "feedback")
    list_filter = ("employee", "rating")
    search_fields = ("employee__name",)


admin.site.register(PerformanceRecord, PerformanceRecordAdmin)


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("id", "employee", "date", "status")
    list_filter = ("status", "employee")
    search_fields = ("employee__name",)


admin.site.register(Attendance, AttendanceAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    filter_horizontal = ("employee",)
    search_fields = ("name",)


admin.site.register(Project, ProjectAdmin)
