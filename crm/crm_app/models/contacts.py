from django.db import models


class Contacts(models.Model):
    name = models.CharField(max_length=50, unique=True)
    post = models.CharField(max_length=30, blank=True)
    phone_number = models.IntegerField()
    e_mail = models.EmailField(max_length=50, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    # company =
    status = models.CharField(max_length=50, blank=True)

    def number_of_deals(self):
        pass
