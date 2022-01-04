from django.db import models


class Employee(models.Model):
    """Employeee"""
    name = models.CharField(max_length=50, unique=True)
    date_of_birth = models.DateField()
    phone_number = models.IntegerField()
    post = models.CharField(max_length=30)
    e_mail = models.EmailField(max_length=100)
    photo = models.ImageField(upload_to="photos/", blank=True)
