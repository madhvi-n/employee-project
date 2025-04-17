# 🏢 Employee Management System
A Django-based web application to manage employees, departments, and visualize role distributions using charts. Built with RESTful APIs and interactive UI components.


## 🚀 Features
- 📋 Employee and Department CRUD operations
- 📊 Chart visualization (e.g., employee roles per department)
- 🔐 API documentation with Swagger UI
- 🧪 Faker-powered dummy data for testing
- ⚙️ Django Admin for backend management

## 🛠️ Tech Stack
- Python 3.11
- Django 5.2
- Django REST Framework
- Chart.js
- Faker (for generating test data)
- PostgreSQL

## 📦 Setup Instructions
1. Clone the repo
```sh
git clone https://github.com/madhvi-n/employee-project.git
cd employee-project
```

2.  Create virtual environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```sh
pip install -r requirements.txt
```

4. Apply migrations
```sh
python manage.py migrate
```

5. Populate the database
```sh
python manage.py populate_employees
```

6. Create superuser
```sh
python manage.py createsuperuser
```

7. Start the server
```sh
python manage.py runserver
```

## Environment variables
Create a `.env` file similar to `.env.example` with correct credentials
```sh
SECRET_KEY=django-secret-key
DATABASE_NAME=db-name
DATABASE_USER=db-user
DATABASE_PASSWORD=db-password
DATABASE_HOST=db-host
DATABASE_PORT=5432
```

## 🚀 Running with Docker
### 🐳 Build and Run with Docker
To build and run the project using Docker:
```sh
# Step 1: Build the Docker image
docker build -t employee-dashboard .

# Step 2: Run the container
docker run -p 8000:8000 employee-dashboard
```

### 🧩 Using Docker Compose
If you prefer Docker Compose, use the following
```
# Build and run services
docker-compose up --build
```

Or if the image is already built:
```sh
docker-compose up
```

To stop the services
```sh
docker-compose down
```


## 📚 API Documentation
Interactive Swagger UI is available at:
📍 `localhost:8000/api/swagger`

## 📈 Charts
- Department-wise employee role distribution using Chart.js.
- Visual data is rendered in templates with Django + JS integration.

API endpoint for charts
- `http://localhost:8000/chart/department-distribution/` for visualizing employees distribution per department
- `http://localhost:8000/chart/employee-roles/<department_id>/` displays roles per department


## TODO
- [] Add authentication and permission classes
- [] Add visualiztion endpoints for employee performance, projects per status
- [] Add unit tests and custom logging
