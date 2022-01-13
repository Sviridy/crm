from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from crm_app.models import Employee
from django.db.models import Q


class EmployeeHome(ListView):
    model = Employee
    template_name = 'employee.html'
    context_object_name = 'employee'


class EmployeeSearch(ListView):
    """Search employee"""
    model = Employee
    template_name = 'employee_search.html'
    context_object_name = 'employee'

    def get_queryset(self):
        query1 = self.request.GET.get('name')
        employee = Employee.objects.filter(
            Q(name__icontains=query1) | Q(date_of_birth__icontains=query1) | Q(phone_number__icontains=query1) | Q(
                post__icontains=query1) | Q(e_mail__icontains=query1))
        return employee


class AddEmployee(CreateView):
    """Add specialization"""
    model = Employee
    fields = ['name', 'date_of_birth', 'phone_number', 'post', 'e_mail', 'photo']
    template_name = 'add_employee.html'
    context_object_name = 'employee'
    success_url = reverse_lazy('employee')


class EditEmployee(UpdateView):
    """Edit specialization"""
    model = Employee
    fields = ['name', 'date_of_birth', 'phone_number', 'post', 'e_mail', 'photo']
    template_name = 'edit_employee.html'
    pk_url_kwarg = 'employee_id'
    context_object_name = 'employee'
    success_url = reverse_lazy('employee')


def delete_employee(request, employee_id):
    """Delete employee"""
    Employee.objects.get(id=employee_id).delete()
    return HttpResponseRedirect("/employee/")
