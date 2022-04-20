from django.urls import path 
from . import views

urlpatterns = [
    path('loan-calculator',views.loan_calculator,name="loan-calculator"),
]