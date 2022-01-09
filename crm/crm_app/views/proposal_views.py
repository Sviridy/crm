from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from crm_app.models import Proposal


class ProposalHome(ListView):
    model = Proposal
    template_name = 'proposal.html'
    context_object_name = 'proposal'


class AddProposal(CreateView):
    """Add specialization"""
    model = Proposal
    fields = ['name', 'price', 'source', 'funnel', 'employee', 'contacts', 'tasks', 'company']
    template_name = 'add_proposal.html'
    context_object_name = 'proposal'
    success_url = reverse_lazy('proposal')

    def get_form(self, form_class=None):
        form = super(AddProposal, self).get_form(form_class)
        # form.fields['date_of_birth'].widget = forms.SplitDateTimeWidget(date_format='%Y-%m-%d')
        form.fields['funnel'].empty_label = 'Воронка не выбрана'
        form.fields['employee'].empty_label = 'Ответственный не выбран'
        form.fields['contacts'].empty_label = 'Контакт не выбран'
        form.fields['tasks'].empty_label = 'Задача не выбрана'
        form.fields['company'].empty_label = 'Компания не выбрана'
        return form


class EditProposal(UpdateView):
    """Edit employee"""
    model = Proposal
    fields = ['name', 'price', 'source', 'funnel', 'employee', 'contacts', 'tasks', 'company']
    template_name = 'edit_proposal.html'
    pk_url_kwarg = 'proposal_id'
    context_object_name = 'proposal'
    success_url = reverse_lazy('proposal')

    def get_form(self, form_class=None):
        form = super(EditProposal, self).get_form(form_class)
        # form.fields['date_of_birth'].widget = forms.SplitDateTimeWidget(date_format='%Y-%m-%d')
        form.fields['funnel'].empty_label = 'Воронка не выбрана'
        form.fields['employee'].empty_label = 'Ответственный не выбран'
        form.fields['contacts'].empty_label = 'Контакт не выбран'
        form.fields['tasks'].empty_label = 'Задача не выбрана'
        form.fields['company'].empty_label = 'Компания не выбрана'
        return form


def delete_proposal(request, proposal_id):
    """Delete employee"""
    Proposal.objects.get(id=proposal_id).delete()
    return HttpResponseRedirect("/proposal/")
