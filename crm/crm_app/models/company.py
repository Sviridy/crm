from django.db import models
from django.urls import reverse

from crm_app.models import Employee


class Company(models.Model):
    full_name = models.CharField(max_length=100, unique=True, verbose_name='Полное наименование компании')
    name = models.CharField(max_length=50, unique=True, verbose_name='Сокращенное наименование')
    responsible = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True,
                                    verbose_name='Ответственный')
    type_of_activity = models.CharField(max_length=50, blank=True, verbose_name='Тип занятости')
    city = models.CharField(max_length=25, blank=True, verbose_name='Город')
    phone_number_or_fax = models.IntegerField(verbose_name='Телефонный номер/факс')
    address = models.TextField(max_length=100, blank=True, verbose_name='Адрес')
    e_mail = models.EmailField(max_length=100, verbose_name='E-mail')
    ynp = models.IntegerField(blank=True, verbose_name='УНП')
    kpp = models.IntegerField(blank=True, verbose_name='КПП')
    legal_address = models.TextField(max_length=100, blank=True, verbose_name='Юридический адрес')
    b_s = models.CharField(max_length=28, blank=True, verbose_name='Банковский счёт')
    bank = models.CharField(max_length=100, blank=True, verbose_name='Банк')

    def __str__(self):
        return self.name

    def contact(self):
        pass

    def get_absolute_url(self):
        """Get id"""
        return reverse('edit_company', kwargs={'company_id': self.pk})

    def get_id(self):
        """Get id"""
        return reverse('delete_company', kwargs={'company_id': self.pk})
