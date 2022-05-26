from django.urls import path 
from . import views

urlpatterns = [
    path('view-loan-apps',views.viewLoanApps,name="view-loan-apps"),
]