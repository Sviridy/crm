from django.db import models
from django.urls import reverse

from crm_app.models import Employee, Status


class Tasks(models.Model):
    name = models.CharField(max_length=60, verbose_name='Имя')
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='Ответственный')
    text = models.TextField(max_length=500, blank=True, verbose_name='Текст')
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Статус')
    deadline = models.DateTimeField(blank=True, verbose_name='Дедлайн')
    note = models.TextField(max_length=500, blank=True, verbose_name='Описание')

    def get_absolute_url(self):
        """Get id"""
        return reverse('edit_tasks', kwargs={'tasks_id': self.pk})

    def get_id(self):
        """Get id"""
        return reverse('delete_tasks', kwargs={'tasks_id': self.pk})

    class Meta:
        ordering = ['pk']
