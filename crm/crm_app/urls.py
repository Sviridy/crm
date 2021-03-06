from django.urls import path
from .views import *

urlpatterns = [
    # path('', EmployeeHome.as_view(), name='home'),
    path('employee/', EmployeeHome.as_view(), name='employee'),
    path('employee/add_employee', AddEmployee.as_view(), name='add_employee'),
    path('employee/<int:employee_id>/', EditEmployee.as_view(), name='edit_employee'),
    path('employee/delete/<int:employee_id>/', delete_employee, name='delete_employee'),

    path('tasks/', TasksHome.as_view(), name='tasks'),
    path('tasks/add_tasks', AddTasks.as_view(), name='add_tasks'),
    path('tasks/<int:tasks_id>/', EditTasks.as_view(), name='edit_tasks'),
    path('tasks/delete/<int:tasks_id>/', delete_tasks, name='delete_tasks'),

    path('company/', CompanyHome.as_view(), name='company'),
    path('company/add_company', AddCompany.as_view(), name='add_company'),
    path('company/<int:company_id>/', EditCompany.as_view(), name='edit_company'),
    path('company/delete/<int:company_id>/', delete_company, name='delete_company'),

    path('contacts/', ContactsHome.as_view(), name='contacts'),
    path('contacts/add_contacts', AddContacts.as_view(), name='add_contacts'),
    path('contacts/<int:contacts_id>/', EditContacts.as_view(), name='edit_contacts'),
    path('contacts/delete/<int:contacts_id>/', delete_contacts, name='delete_contacts'),

    path('payment/', PaymentHome.as_view(), name='payment'),
    path('payment/add_payment', AddPayment.as_view(), name='add_payment'),
    path('payment/<int:payment_id>/', EditPayment.as_view(), name='edit_payment'),
    path('payment/delete/<int:payment_id>/', delete_payment, name='delete_payment'),

    path('proposal/', ProposalHome.as_view(), name='proposal'),
    path('proposal/add_proposal', AddProposal.as_view(), name='add_proposal'),
    path('proposal/<int:proposal_id>/', EditProposal.as_view(), name='edit_proposal'),
    path('proposal/delete/<int:proposal_id>/', delete_proposal, name='delete_proposal'),

    path('deal/', DealHome.as_view(), name='deal'),
    path('deal/add_deal', AddDeal.as_view(), name='add_deal'),
    path('deal/<int:deal_id>/', EditDeal.as_view(), name='edit_deal'),
    path('deal/delete/<int:deal_id>/', delete_deal, name='delete_deal'),
    path('deal/print/<int:deal_id>/', print_deal, name='print_deal'),

    path('chart/', dashboard, name='chart'),
]
