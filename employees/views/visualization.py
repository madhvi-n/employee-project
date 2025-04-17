from django.views.generic import TemplateView
from django.db.models import Count
from employees.models import Employee
import json


class DepartmentDistributionChartView(TemplateView):
    template_name = 'department_distribution_chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the count of employees per department
        department_counts = Employee.objects.values('department__name').annotate(count=Count('id'))

        department_data = {
            'labels': [item['department__name'] for item in department_counts],
            'datasets': [{
                'data': [item['count'] for item in department_counts],
                'backgroundColor': ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FF5733']
            }]
        }

        context['data'] = json.dumps(department_data)

        return context


class EmployeeRolePerDepartmentChartView(TemplateView):
    template_name = 'employee_role_chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        department_id = self.kwargs['department_id']

        print(department_id)

        # Using values() and annotate() to get role counts for the department
        role_counts = Employee.objects.filter(department_id=department_id).values('role').annotate(count=Count('id'))

        context['data'] = {
            'labels': [item['role'] for item in role_counts],
            'datasets': [{
                'data': [item['count'] for item in role_counts],
                'backgroundColor': ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FF5733']
            }]
        }
        print(context)
        return context
