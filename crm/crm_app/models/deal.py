"""Сделка"""
from django.db import models
from django.urls import reverse

from crm_app.models import Proposal, Status


class Deal(models.Model):
    proposal = models.OneToOneField(Proposal, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Заявка')
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Статус')
    profit = models.IntegerField(verbose_name='Прибыль')
    description = models.TextField(max_length=150, blank=True, verbose_name='Описание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    documents = models.FileField(upload_to='documents/', blank=True, verbose_name='Документы')

    def __str__(self):
        return str(self.proposal)

    @property
    def stage(self):
        """Этап"""
        a = Proposal.objects.filter(id=self.proposal.id).values('funnel__name')
        return a[0].get('funnel__name')

    @property
    def price(self):
        a = Proposal.objects.filter(id=self.proposal.id).values('price')
        return a[0].get('price')

    @property
    def contacts(self):
        a = Proposal.objects.filter(id=self.proposal.id).values('contacts__name')
        return a[0].get('contacts__name')

    @property
    def company(self):
        a = Proposal.objects.filter(id=self.proposal.id).values('company__name')
        return a[0].get('company__name')

    @property
    def employee(self):
        a = Proposal.objects.filter(id=self.proposal.id).values('employee__name')
        return a[0].get('employee__name')

    @property
    def tasks(self):
        a = Proposal.objects.filter(id=self.proposal.id).values('tasks__name')
        return a[0].get('tasks__name')

    def get_absolute_url(self):
        """Get id"""
        return reverse('edit_deal', kwargs={'deal_id': self.pk})

    def get_id(self):
        """Get id"""
        return reverse('delete_deal', kwargs={'deal_id': self.pk})

    def print(self):
        """Get id"""
        return reverse('print_deal', kwargs={'deal_id': self.pk})

    class Meta:
        ordering = ['pk']
