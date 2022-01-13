from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from crm_app.models import Tasks


class TasksHome(ListView):
    model = Tasks
    template_name = 'tasks.html'
    context_object_name = 'tasks'


class TasksSearch(ListView):
    """Search employee"""
    model = Tasks
    template_name = 'tasks_search.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        query1 = self.request.GET.get('name')
        tasks = Tasks.objects.filter(
            Q(name__icontains=query1) | Q(employee__name__icontains=query1) | Q(text__icontains=query1) | Q(
                status__name__icontains=query1) | Q(deadline__icontains=query1) | Q(note__icontains=query1))
        return tasks


class AddTasks(CreateView):
    """Add specialization"""
    model = Tasks
    fields = ['name', 'employee', 'text', 'status', 'deadline', 'note']
    template_name = 'add_tasks.html'
    context_object_name = 'tasks'
    success_url = reverse_lazy('tasks')

    def get_form(self, form_class=None):
        form = super(AddTasks, self).get_form(form_class)
        # form.fields['date_of_birth'].widget = forms.SplitDateTimeWidget(date_format='%Y-%m-%d')
        form.fields['employee'].empty_label = 'Ответственный не выбран'
        form.fields['status'].empty_label = 'Статус не выбран'
        return form


class EditTasks(UpdateView):
    """Edit employee"""
    model = Tasks
    fields = ['name', 'employee', 'text', 'status', 'deadline', 'note']
    template_name = 'edit_tasks.html'
    pk_url_kwarg = 'tasks_id'
    context_object_name = 'tasks'
    success_url = reverse_lazy('tasks')

    def get_form(self, form_class=None):
        form = super(EditTasks, self).get_form(form_class)
        # form.fields['date_of_birth'].widget = forms.SplitDateTimeWidget(date_format='%Y-%m-%d')
        form.fields['employee'].empty_label = 'Ответственный не выбран'
        form.fields['status'].empty_label = 'Статус не выбран'
        return form


def delete_tasks(request, tasks_id):
    """Delete employee"""
    Tasks.objects.get(id=tasks_id).delete()
    return HttpResponseRedirect("/tasks/")
