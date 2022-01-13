from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from crm_app.models import Deal


class DealHome(ListView):
    model = Deal
    template_name = 'deal.html'
    context_object_name = 'deal'


class DealSearch(ListView):
    """Search employee"""
    model = Deal
    template_name = 'deal_search.html'
    context_object_name = 'deal'

    def get_queryset(self):
        query1 = self.request.GET.get('name')
        deal = Deal.objects.filter(
            Q(proposal__name__icontains=query1) | Q(status__name__icontains=query1) | Q(profit__icontains=query1) | Q(
                description__icontains=query1))
        return deal


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
