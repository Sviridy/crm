from django.views.generic import ListView
from crm_app.models import Employee


class EmployeeHome(ListView):
    model = Employee
    template_name = 'employee.html'
    context_object_name = 'employee'
