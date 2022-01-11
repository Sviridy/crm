from django.db import models
from django.urls import reverse

from crm_app.models import Deal


class Payment(models.Model):
    deal = models.ForeignKey(Deal, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Сделка')
    date = models.DateField(verbose_name='Дата оплаты')
    price = models.IntegerField(verbose_name='Цена')

    def get_absolute_url(self):
        """Get id"""
        return reverse('edit_payment', kwargs={'payment_id': self.pk})

    def get_id(self):
        """Get id"""
        return reverse('delete_payment', kwargs={'payment_id': self.pk})

    class Meta:
        ordering = ['pk']
