from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from crm_app.models import Payment


class PaymentHome(ListView):
    model = Payment
    template_name = 'payment.html'
    context_object_name = 'payment'


class AddPayment(CreateView):
    """Add specialization"""
    model = Payment
    fields = ['deal', 'date', 'price']
    template_name = 'add_payment.html'
    context_object_name = 'payment'
    success_url = reverse_lazy('payment')

    def get_form(self, form_class=None):
        form = super(AddPayment, self).get_form(form_class)
        # form.fields['date_of_birth'].widget = forms.SplitDateTimeWidget(date_format='%Y-%m-%d')
        form.fields['deal'].empty_label = 'Сделка не выбрана'
        return form


class EditPayment(UpdateView):
    """Edit employee"""
    model = Payment
    fields = ['deal', 'date', 'price']
    template_name = 'edit_payment.html'
    pk_url_kwarg = 'payment_id'
    context_object_name = 'payment'
    success_url = reverse_lazy('payment')

    def get_form(self, form_class=None):
        form = super(EditPayment, self).get_form(form_class)
        # form.fields['date_of_birth'].widget = forms.SplitDateTimeWidget(date_format='%Y-%m-%d')
        form.fields['deal'].empty_label = 'Сделка не выбрана'
        return form


def delete_payment(request, payment_id):
    """Delete employee"""
    Payment.objects.get(id=payment_id).delete()
    return HttpResponseRedirect("/payment/")
