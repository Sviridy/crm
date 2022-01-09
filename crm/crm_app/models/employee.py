from django.db import models
from django.urls import reverse


class Employee(models.Model):
    """Employeee"""
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    phone_number = models.IntegerField(verbose_name='Номер телефона +375')
    post = models.CharField(max_length=30, verbose_name='Позиция')
    e_mail = models.EmailField(max_length=100, verbose_name='E_mail')
    photo = models.ImageField(upload_to="photos/", blank=True, verbose_name='Фотография')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Get id"""
        return reverse('edit_employee', kwargs={'employee_id': self.pk})

    def get_id(self):
        """Get id"""
        return reverse('delete_employee', kwargs={'employee_id': self.pk})
