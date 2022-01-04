from django.db import models
from crm_app.models import Employee


class Contacts(models.Model):
    full_name = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=50, unique=True)
    responsible = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    type_of_activity = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=25, blank=True)
    phone_number_or_fax = models.IntegerField()
    address = models.TextField(max_length=100, blank=True)
    e_mail = models.EmailField(max_length=100)
    ynp = models.IntegerField(max_length=9)


    def contact(self):
        pass
