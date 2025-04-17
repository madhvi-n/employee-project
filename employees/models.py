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
