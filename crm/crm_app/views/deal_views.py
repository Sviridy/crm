import os
import sys
from datetime import datetime

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from docxtpl import DocxTemplate

from crm_app.models import Deal


class DealHome(ListView):
    model = Deal
    template_name = 'deal.html'
    context_object_name = 'deal'


class AddDeal(CreateView):
    """Add specialization"""
    model = Deal
    fields = ['proposal', 'status', 'profit', 'description', 'documents']
    template_name = 'add_deal.html'
    context_object_name = 'deal'
    success_url = reverse_lazy('deal')

    def get_form(self, form_class=None):
        form = super(AddDeal, self).get_form(form_class)
        # form.fields['date_of_birth'].widget = forms.SplitDateTimeWidget(date_format='%Y-%m-%d')
        form.fields['proposal'].empty_label = 'Сделка не выбрана'
        form.fields['status'].empty_label = 'Статус не выбран'
        return form


class EditDeal(UpdateView):
    """Edit employee"""
    model = Deal
    fields = ['proposal', 'status', 'profit', 'description', 'documents']
    template_name = 'edit_deal.html'
    pk_url_kwarg = 'deal_id'
    context_object_name = 'deal'
    success_url = reverse_lazy('deal')

    def get_form(self, form_class=None):
        form = super(EditDeal, self).get_form(form_class)
        # form.fields['date_of_birth'].widget = forms.SplitDateTimeWidget(date_format='%Y-%m-%d')
        form.fields['proposal'].empty_label = 'Сделка не выбрана'
        form.fields['status'].empty_label = 'Статус не выбран'
        return form


def delete_deal(request, deal_id):
    """Delete employee"""
    Deal.objects.get(id=deal_id).delete()
    return HttpResponseRedirect("/deal/")


def print_deal(request, deal_id):
    """Delete employee"""
    d = Deal.objects.filter(id=deal_id).values('proposal__name', 'profit', 'proposal__price', 'proposal__employee',
                                               'proposal__contacts__name', 'proposal__contacts__post',
                                               'proposal__company__name', 'proposal__company__full_name', 'description',
                                               'proposal__company__address', 'proposal__company__ynp',
                                               'proposal__company__b_s', 'proposal__company__bank')
    print(d[0].get('proposal__name'))
    sys.path.append('D:\\Python\\crm\\crm\\media\\documents')
    os.chdir(sys.path[-1])
    a = datetime.now()
    doc = DocxTemplate('example.docx')
    context = {'name': d[0].get('proposal__company'), 'fio': d[0].get('proposal__contacts'),
               'post': d[0].get('proposal__contacts__post'), 'company': d[0].get('proposal__company__name'),
               'address': d[0].get('proposal__company__address'), 'price': d[0].get('proposal__price'),
               'full': d[0].get('proposal__company__full_name'), 'ynp': d[0].get('proposal__company__ynp'),
               'bs': d[0].get('proposal__company__b_s'), 'bank': d[0].get('proposal__company__bank')}
    doc.render(context)
    b = f'{a.date()}_{a.hour}-{a.minute}-{a.second}'
    doc.save(f'Договор{b}.docx')
    os.system(f'start D:\\Python\\crm\\crm\\media\\documents\\Договор{b}.docx')
    return HttpResponseRedirect(f"/deal/{deal_id}")
