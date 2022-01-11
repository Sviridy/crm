"""Заявка"""
from django.db import models
from django.urls import reverse

from crm_app.models import Funnel, Employee, Contacts, Tasks, Company


class Proposal(models.Model):
    name = models.CharField(max_length=60, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    source = models.CharField(max_length=35, verbose_name='Источник')
    funnel = models.ForeignKey(Funnel, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Воронка')
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='Ответственный')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    contacts = models.ForeignKey(Contacts, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Контакт')
    tasks = models.ForeignKey(Tasks, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Задача')
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Компания')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Get id"""
        return reverse('edit_proposal', kwargs={'proposal_id': self.pk})

    def get_id(self):
        """Get id"""
        return reverse('delete_proposal', kwargs={'proposal_id': self.pk})

    class Meta:
        ordering = ['pk']
