from django.db import models
from crm_app.models import Company


class Contacts(models.Model):
    name = models.CharField(max_length=50, unique=True)
    post = models.CharField(max_length=30, blank=True)
    phone_number = models.IntegerField()
    e_mail = models.EmailField(max_length=50, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=50, blank=True)

    def number_of_deals(self):
        pass
