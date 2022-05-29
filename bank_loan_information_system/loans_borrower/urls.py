from django.urls import path 
from . import views

urlpatterns = [
    path('view-loan-apps', views.viewLoanApps, name="view-loan-apps"),
    path('view-loan-apps-info/<str:pk>', views.viewLoanAppsInfo, name="view-loan-apps-info"),
    path('loan-apply', views.loanApply, name="loan-apply"),
]