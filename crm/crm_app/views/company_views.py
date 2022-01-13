from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from crm_app.models import Company


class CompanyHome(ListView):
    model = Company
    template_name = 'company.html'
    context_object_name = 'company'


class CompanySearch(ListView):
    """Search employee"""
    model = Company
    template_name = 'company_search.html'
    context_object_name = 'company'

    def get_queryset(self):
        query1 = self.request.GET.get('name')
        company = Company.objects.filter(
            Q(name__icontains=query1) | Q(responsible__name__icontains=query1) | Q(
                phone_number_or_fax__icontains=query1) | Q(city__icontains=query1) | Q(e_mail__icontains=query1) | Q(
                bank__icontains=query1))
        return company


class AddCompany(CreateView):
    """Add specialization"""
    model = Company
    fields = ['full_name', 'name', 'responsible', 'type_of_activity', 'city', 'phone_number_or_fax', 'address',
              'e_mail', 'ynp', 'kpp', 'legal_address', 'b_s', 'bank']
    template_name = 'add_company.html'
    context_object_name = 'company'
    success_url = reverse_lazy('company')

    def get_form(self, form_class=None):
        form = super(AddCompany, self).get_form(form_class)
        # form.fields['date_of_birth'].widget = forms.SplitDateTimeWidget(date_format='%Y-%m-%d')
        form.fields['responsible'].empty_label = 'Ответственный не выбран'
        return form


class EditCompany(UpdateView):
    """Edit employee"""
    model = Company
    fields = ['full_name', 'name', 'responsible', 'type_of_activity', 'city', 'phone_number_or_fax', 'address',
              'e_mail', 'ynp', 'kpp', 'legal_address', 'b_s', 'bank']
    template_name = 'edit_company.html'
    pk_url_kwarg = 'company_id'
    context_object_name = 'company'
    success_url = reverse_lazy('company')

    def get_form(self, form_class=None):
        form = super(EditCompany, self).get_form(form_class)
        # form.fields['date_of_birth'].widget = forms.SplitDateTimeWidget(date_format='%Y-%m-%d')
        form.fields['responsible'].empty_label = 'Ответственный не выбран'
        return form


def delete_company(request, company_id):
    """Delete employee"""
    Company.objects.get(id=company_id).delete()
    return HttpResponseRedirect("/company/")
