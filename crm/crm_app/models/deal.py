"""Сделка"""
from django.db import models
from crm_app.models import Proposal, Status


class Deal(models.Model):
    proposal = models.OneToOneField(Proposal, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)
    profit = models.IntegerField()
    description = models.TextField(max_length=150, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    documents = models.FileField(upload_to='documents/', blank=True)

    @property
    def stage(self):
        """Этап"""
        return self.proposal_set.all()

    def price(self):
        pass

    def contacts(self):
        pass

    def company(self):
        pass

    def employee(self):
        pass

    def tasks(self):
        pass

    def funnel(self):
        pass
