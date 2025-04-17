from rest_framework import serializers
from employees.models import Department, Employee, PerformanceRecord, Attendance, Project


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'age', 'department', 'role']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']

class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'age', 'department', 'hire_date', 'role']

class PerformanceRecordSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = PerformanceRecord
        fields = ['id', 'employee', 'rating', 'review_date', 'feedback']

class AttendanceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = Attendance
        fields = ['id', 'employee', 'date', 'status']

class ProjectSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'employee']
