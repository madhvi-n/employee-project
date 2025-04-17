# 🧠 Design Decisions

This document outlines key design choices made during the development of this project.


## 📦 Basic Models First

I began the project by defining the core data models required to represent an organization structure:

- `Department`
- `Employee`
- `Project`

Each model was kept minimal and directly reflected real-world relationships:
- An `Employee` belongs to a `Department`.
- A `Project` is a standalone entity with a name and description.


## 🖁️ Projects & Employee Assignment

### Initial Approach:
Originally, I added a direct many-to-many relationship between `Employees` and `Projects`. However, I quickly realized this lacked flexibility — we couldn’t track:
- Who assigned the employee
- When they were assigned
- The status of the assignment (active, completed, etc.)

### Final Decision:
I **removed the direct M2M field** and introduced a dedicated **`ProjectAssignment`** model. This allowed us to:
- Track assignment metadata (status, assigned_at)
- Make the design more extensible
- Keep business logic isolated

```python
class ProjectAssignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(...)  # E.g. Active, Completed
    assigned_at = models.DateTimeField(...)
```


## 🧘 Minimal and Modular

We intentionally kept the codebase **minimal**:
- Avoided overengineering early
- Lean and understandable models
- Simple admin registration

The goal was: **get working APIs and basic views fast**, then iterate.


## 🛠️ Django REST Framework (DRF)

We relied heavily on Django REST Framework for rapid API development:
- Used **ModelSerializers** for easy serialization
- Built all endpoints using **ModelViewSet**
- Enabled full CRUD out of the box

> This helped us focus more on features than boilerplate.


## 🥪 Swagger Integration

All APIs are documented using **drf-spectacular** and are available at:

```
/api/swagger
```



## 📊 Data Visualization

Added simple chart views using:
- `Chart.js` in the frontend
- TemplateViews + JSON context in Django

We exposed:
- **Department-wise employee distribution**
- **Employee roles per department**

Additional endpoints which couldn't be added due to time limit
- **Performance review per department**
- **Attendance per department**
- **Employee performance review by quarter**
- **Employee attendance by month**
- **Department projects per status**

The data was injected via Django templates and rendered dynamically on the frontend.


## 🐳 Dockerization

We have a simple `Dockerfile` to containerize the app.

- `Dockerfile` sets up the Python environment
- Optional: `docker-compose.yml` can be used to run the project + DB easily (Postgres, etc.)

> This ensures smoother deployment and easier onboarding for collaborators.

