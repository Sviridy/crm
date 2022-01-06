from django.urls import path
from .views import EmployeeHome

urlpatterns = [
    path('employee/', EmployeeHome.as_view(), name='employee'),
]
