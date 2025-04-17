from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50)


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    hire_date = models.DateField()
    role = models.CharField(max_length=100)


class PerformanceRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    rating = models.FloatField()
    review_date = models.DateField()
    feedback = models.TextField()


class Attendance(models.Model):
    class Status(models.TextChoices):
        PRESENT = "Present", "Present"
        ABSENT = "Absent", "Absent"
        REMOTE = "Remote", "Remote"

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.ABSENT,
    )


class Project(models.Model):
    name = models.CharField(max_length=100)
    employee = models.ManyToManyField(Employee)


class ProjectAssignment(models.Model):
    class Status(models.TextChoices):
        ONGOING = "Ongoing", "Ongoing"
        ON_HOLD = "On Hold", "On Hold"
        COMPLETED = "Completed", "Completed"
        CANCELLED = "Cancelled", "Cancelled"

    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    assigned_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ONGOING
    )

    def __str__(self):
        return f"{self.employee.name} -> {self.project.name} ({self.status})"