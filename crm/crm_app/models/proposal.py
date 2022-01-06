"""Заявка"""
from django.db import models
from crm_app.models import Funnel, Employee, Contacts, Tasks, Company


class Proposal(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField()
    source = models.CharField(max_length=35)
    funnel = models.ForeignKey(Funnel, on_delete=models.SET_NULL, null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    contacts = models.ForeignKey(Contacts, on_delete=models.SET_NULL, null=True, blank=True)
    tasks = models.ForeignKey(Tasks, on_delete=models.SET_NULL, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
