from django.db import models
from django.urls import reverse

from crm_app.models import Company


class Contacts(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя')
    post = models.CharField(max_length=30, blank=True, verbose_name='Позиция')
    phone_number = models.IntegerField(verbose_name='Номер телефона +375')
    e_mail = models.EmailField(max_length=50, blank=True, verbose_name='E-mail')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Компания')
    status = models.CharField(max_length=50, blank=True, verbose_name='Статус')

    def __str__(self):
        return self.name

    def number_of_deals(self):
        pass

    def get_absolute_url(self):
        """Get id"""
        return reverse('edit_contacts', kwargs={'contacts_id': self.pk})

    def get_id(self):
        """Get id"""
        return reverse('delete_contacts', kwargs={'contacts_id': self.pk})

    class Meta:
        ordering = ['pk']
