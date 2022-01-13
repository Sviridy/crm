from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from crm_app.models import Contacts


class ContactsHome(ListView):
    model = Contacts
    template_name = 'contacts.html'
    context_object_name = 'contacts'


class AddContacts(CreateView):
    """Add specialization"""
    model = Contacts
    fields = ['name', 'post', 'phone_number', 'e_mail', 'company', 'status']
    template_name = 'add_contacts.html'
    context_object_name = 'contacts'
    success_url = reverse_lazy('contacts')

    def get_form(self, form_class=None):
        form = super(AddContacts, self).get_form(form_class)
        # form.fields['date_of_birth'].widget = forms.SplitDateTimeWidget(date_format='%Y-%m-%d')
        form.fields['company'].empty_label = 'Компания не выбран'
        return form


class EditContacts(UpdateView):
    """Edit employee"""
    model = Contacts
    fields = ['name', 'post', 'phone_number', 'e_mail', 'company', 'status']
    template_name = 'edit_contacts.html'
    pk_url_kwarg = 'contacts_id'
    context_object_name = 'contacts'
    success_url = reverse_lazy('contacts')

    def get_form(self, form_class=None):
        form = super(EditContacts, self).get_form(form_class)
        # form.fields['date_of_birth'].widget = forms.SplitDateTimeWidget(date_format='%Y-%m-%d')
        form.fields['company'].empty_label = 'Компания не выбран'
        return form


def delete_contacts(request, contacts_id):
    """Delete employee"""
    Contacts.objects.get(id=contacts_id).delete()
    return HttpResponseRedirect("/contacts/")
