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

    # @property
    # def stage(self):
    #     """Этап"""
    #     return self.proposal_set.all().count()

    def price(self):
        pass

    def contacts(self):
        pass

    def company(self):
        pass

    def employee(self):
        pass

    def tasks(self):
        pass

    def funnel(self):
        pass

    def get_absolute_url(self):
        """Get id"""
        return reverse('edit_deal', kwargs={'deal_id': self.pk})

    def get_id(self):
        """Get id"""
        return reverse('delete_deal', kwargs={'deal_id': self.pk})
