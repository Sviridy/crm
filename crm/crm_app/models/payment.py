from django.db import models
from crm_app.models import Deal


class Payment(models.Model):
    deal = models.ForeignKey(Deal, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    price = models.IntegerField()
