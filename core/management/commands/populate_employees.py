import random
from concurrent.futures import ThreadPoolExecutor
from django.core.management.base import BaseCommand
from faker import Faker
from employees.models import (
    Employee,
    Department,
    PerformanceRecord,
    Attendance,
    Project,
    ProjectAssignment,
)
from datetime import timedelta, date

NUM_EMPLOYEES = 200
THREADS = 10


class Command(BaseCommand):
    help = "Seeds the database with 200 employees and associated data"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Step 1: Create departments
        departments = ["Engineering", "Marketing", "HR", "Sales", "Finance"]
        department_objects = [
            Department.objects.create(name=dept) for dept in departments
        ]

        # Step 2: Create projects
        project_names = ["Project X", "Project Y", "Project Z"]
        project_objects = [Project.objects.create(name=name) for name in project_names]

        #Predefined roles 
        roles = ['Senior', 'Lead', 'Manager', 'VP', 'Intern']

        # Step 3: Define seeding function
        def seed_employee(_):
            department = random.choice(department_objects)
            role = random.choice(roles)

            employee = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                age=random.randint(22, 60),
                department=department,
                hire_date=fake.date_between(start_date="-5y", end_date="today"),
                role=role,
            )

            # Attendance
            for _ in range(random.randint(5, 15)):
                Attendance.objects.create(
                    employee=employee,
                    date=fake.date_between(start_date="-30d", end_date="today"),
                    status=random.choice(
                        [choice[0] for choice in Attendance.Status.choices]
                    ),
                )

            # PerformanceRecord
            for _ in range(random.randint(1, 3)):
                PerformanceRecord.objects.create(
                    employee=employee,
                    rating=round(random.uniform(1.0, 5.0), 1),
                    review_date=fake.date_between(start_date="-2y", end_date="today"),
                    feedback=fake.sentence(nb_words=10),
                )

            # Only assign projects to certain departments
            if department.name in ["Engineering", "Sales"]:
                for project in random.sample(
                    project_objects, k=random.randint(1, len(project_objects))
                ):
                    ProjectAssignment.objects.create(employee=employee, project=project)

        # Run in threads
        with ThreadPoolExecutor(max_workers=THREADS) as executor:
            executor.map(seed_employee, range(NUM_EMPLOYEES))

        print("Successfully seeded 200 employees with data!")
