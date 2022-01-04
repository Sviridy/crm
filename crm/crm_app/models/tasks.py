from django.db import models
from crm_app.models import Employee, Status


class Tasks(models.Model):
    name = models.CharField(max_length=60)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField(max_length=250, blank=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)
    deadline = models.DateTimeField(blank=True)
    note = models.TextField(max_length=250, blank=True)
